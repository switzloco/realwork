"""
Smart Hunt — Find actually suspicious grant recipients.

The previous SERP check failed because it checked the top 20 by dollar amount,
which are all Fortune 500 companies. This script uses smarter heuristics:

1. Filter to Business/Individual only (not Public Agency or Nonprofit)
2. Focus on $100K-$5M range (fraud sweet spot — too small for Fortune 500s, too big to ignore)
3. Look for LLC/Holdings/Corp/Inc patterns that suggest shell entities
4. Find entities receiving MULTIPLE grants (double-dipping)
5. Find grants in high-risk categories (construction, equipment, services)
6. Run SERP checks ONLY on the most suspicious subset
"""

import json
import os
import re
import sys
import time
from collections import Counter, defaultdict

import pandas as pd
from dotenv import load_dotenv

load_dotenv()


# Known legitimate large companies to exclude
KNOWN_LEGIT = {
    "applied materials", "northrop grumman", "pratt & whitney", "snapchat",
    "intuitive surgical", "calstart", "aptera motors", "enovix",
    "affirmed housing", "palm communities", "related companies",
    "amcal multi-housing", "hitzke development", "republic services",
    "wattev", "humane, inc", "infinera", "tynergy", "aibot",
    "berkshire hathaway", "bhe renewables", "wm renewable",
}

# Suspicious name patterns (shell company indicators)
SHELL_PATTERNS = [
    r'\b(holdings?)\b',
    r'\b(enterprises?)\b', 
    r'\b(ventures?)\b',
    r'\b(group)\b',
    r'\b(partners?)\b',
    r'\b(associates?)\b',
    r'\b(solutions?)\b',
    r'\b(services?)\b',
    r'\b(consulting)\b',
    r'\b(management)\b',
    r'\b(international)\b',
    r'\b(global)\b',
    r'\b(properties)\b',
    r'\b(investments?)\b',
    r'\b(capital)\b',
]

# High-risk grant program keywords
HIGH_RISK_PROGRAMS = [
    "construction", "renovation", "equipment", "infrastructure",
    "facility", "building", "improvement", "capital",
]


def load_data():
    df = pd.read_csv("data/grants_full.csv", low_memory=False)
    
    # Normalize amount
    for col in ["TotalAwardAmount"]:
        if col in df.columns:
            df["award_amount"] = pd.to_numeric(
                df[col].astype(str).str.replace(r"[^\d.]", "", regex=True),
                errors="coerce"
            )
    
    return df


def is_known_legit(name: str) -> bool:
    name_lower = name.lower()
    return any(k in name_lower for k in KNOWN_LEGIT)


def shell_score(name: str) -> int:
    """Count how many shell-company name patterns match."""
    score = 0
    name_lower = name.lower()
    for pat in SHELL_PATTERNS:
        if re.search(pat, name_lower):
            score += 1
    # Extra points for very short names + LLC
    if "llc" in name_lower and len(name) < 25:
        score += 2
    if "inc" in name_lower and len(name) < 20:
        score += 1
    return score


def is_high_risk_program(title: str, abstract: str) -> bool:
    combined = f"{title} {abstract}".lower()
    return any(kw in combined for kw in HIGH_RISK_PROGRAMS)


def find_multi_grant_recipients(df: pd.DataFrame) -> dict:
    """Find entities receiving more than one grant."""
    counts = df["RecipientName"].value_counts()
    multi = counts[counts > 1]
    return dict(multi)


def run_hunt(df: pd.DataFrame) -> list:
    """Main analysis: score every Business/Individual grant recipient."""
    
    # Filter to Business and Individual only
    biz_mask = df["RecipientType"].str.lower().isin(["business", "individual"])
    biz_df = df[biz_mask].copy()
    print(f"Business/Individual grants: {len(biz_df)}")
    
    # Filter to $50K - $5M (fraud sweet spot)
    range_mask = (biz_df["award_amount"] >= 50_000) & (biz_df["award_amount"] <= 5_000_000)
    target_df = biz_df[range_mask].copy()
    print(f"In $50K-$5M range: {len(target_df)}")
    
    # Remove known legitimate companies
    target_df = target_df[~target_df["RecipientName"].apply(is_known_legit)]
    print(f"After removing known legit: {len(target_df)}")
    
    # Find multi-grant recipients across FULL dataset
    multi_grants = find_multi_grant_recipients(df)
    
    # Score each grant
    scored = []
    for _, row in target_df.iterrows():
        name = str(row.get("RecipientName", ""))
        amount = float(row.get("award_amount", 0))
        title = str(row.get("ProjectTitle", ""))
        abstract = str(row.get("ProjectAbstract", ""))
        rtype = str(row.get("RecipientType", ""))
        agency = str(row.get("AgencyDept", ""))
        location = str(row.get("GeographicLocationServed", ""))
        county = str(row.get("CountiesServed", ""))
        
        score = 0
        flags = []
        
        # Shell company name patterns
        s = shell_score(name)
        if s >= 2:
            score += s * 3
            flags.append(f"Shell-like name (score={s})")
        elif s == 1:
            score += 2
            flags.append(f"Mildly suspicious name")
        
        # High risk program
        if is_high_risk_program(title, abstract):
            score += 5
            flags.append("High-risk program (construction/equipment)")
        
        # Multi-grant recipient
        grant_count = multi_grants.get(name, 1)
        if grant_count > 1:
            score += grant_count * 2
            flags.append(f"Multiple grants ({grant_count})")
        
        # Amount in the suspicious sweet spot ($500K-$2M)
        if 500_000 <= amount <= 2_000_000:
            score += 3
            flags.append("Sweet-spot amount ($500K-$2M)")
        elif amount >= 2_000_000:
            score += 2
            flags.append("Large amount (>$2M)")
        
        # Individual recipient with large amount
        if rtype.lower() == "individual" and amount >= 100_000:
            score += 5
            flags.append(f"Individual receiving ${amount:,.0f}")
        
        # Very vague/short name
        if len(name) < 15 and ("llc" in name.lower() or "inc" in name.lower()):
            score += 3
            flags.append("Very short entity name")
        
        # Name contains a person's name pattern (first last format) for a business
        if rtype.lower() == "business":
            words = name.split()
            if len(words) == 2 and all(w[0].isupper() and w[1:].islower() for w in words if len(w) > 1):
                score += 2
                flags.append("Person-name as business name")
        
        if score >= 5:  # Only keep entities with meaningful suspicion
            scored.append({
                "recipient": name,
                "recipient_type": rtype,
                "award_amount": amount,
                "grant_title": title,
                "agency": agency,
                "location": location,
                "county": county,
                "abstract": abstract[:200],
                "suspicion_score": score,
                "flags": flags,
                "grant_count": grant_count,
            })
    
    # Sort by suspicion score descending
    scored.sort(key=lambda x: x["suspicion_score"], reverse=True)
    return scored


def main():
    print("=" * 60)
    print("SMART HUNT — Finding Actually Suspicious Entities")
    print("=" * 60)
    
    df = load_data()
    print(f"Total records: {len(df)}")
    
    suspects = run_hunt(df)
    print(f"\nFound {len(suspects)} suspicious entities (score >= 5)")
    
    # Show top 40
    print(f"\n{'='*60}")
    print("TOP 40 MOST SUSPICIOUS GRANT RECIPIENTS")
    print(f"{'='*60}\n")
    
    for i, s in enumerate(suspects[:40]):
        print(f"#{i+1} — Score: {s['suspicion_score']}")
        print(f"   Recipient: {s['recipient']}")
        print(f"   Type: {s['recipient_type']} | Amount: ${s['award_amount']:,.0f}")
        print(f"   Program: {s['grant_title']}")
        print(f"   Agency: {s['agency']}")
        print(f"   Flags: {', '.join(s['flags'])}")
        print()
    
    # Save full list
    with open("data/smart_hunt_results.json", "w") as f:
        json.dump(suspects, f, indent=2, default=str)
    print(f"Saved {len(suspects)} suspects to data/smart_hunt_results.json")
    
    # Summary stats
    total_suspicious_value = sum(s["award_amount"] for s in suspects)
    print(f"\nTotal suspicious value: ${total_suspicious_value:,.0f}")
    print(f"Average suspicion score: {sum(s['suspicion_score'] for s in suspects) / len(suspects):.1f}")
    
    # Group by agency
    agency_counts = Counter(s["agency"] for s in suspects)
    print(f"\nTop agencies with suspicious grants:")
    for agency, count in agency_counts.most_common(10):
        agency_value = sum(s["award_amount"] for s in suspects if s["agency"] == agency)
        print(f"  {agency}: {count} grants (${agency_value:,.0f})")


if __name__ == "__main__":
    main()
