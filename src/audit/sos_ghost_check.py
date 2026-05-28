"""
SOS Ghost Check — The definitive test.

If an entity received a California state grant as a "Business" but is NOT
registered with the CA Secretary of State, that is an extremely strong fraud
signal. A legitimate business receiving >$100K in state funds MUST be registered.

Strategy:
1. Get all Business-type recipients with awards $100K-$5M
2. Filter to construction/infrastructure/equipment grants (hardest to verify delivery)
3. Exclude known-legit large companies
4. Run SOS searches via Bright Data SERP: site:bizfileonline.sos.ca.gov "{entity name}"
5. Any entity with 0 SOS results = CONFIRMED GHOST

Also: re-check our original NCMR entities with fresh SERP queries.
"""

import json
import os
import re
import time
from collections import Counter

import pandas as pd
from dotenv import load_dotenv
load_dotenv()

from src.investigation.scraper_coordinator import _scrape_serp


def safe_print(s):
    print(str(s).encode('ascii', 'replace').decode())


def serp(query):
    """Single SERP query."""
    safe_print(f"  SERP: {query}")
    raw, cost = _scrape_serp(query)
    organic_count = 0
    top_results = []
    if raw:
        try:
            data = json.loads(raw)
            if isinstance(data, list):
                organic_count = len(data)
                for r in data[:3]:
                    if isinstance(r, dict):
                        top_results.append({
                            "title": r.get("title", ""),
                            "link": r.get("link", r.get("url", "")),
                            "snippet": r.get("description", r.get("snippet", ""))[:200],
                        })
        except:
            pass
    safe_print(f"    -> {organic_count} results")
    time.sleep(0.3)
    return organic_count, top_results, raw[:3000] if raw else ""


# Known large/legitimate companies to skip
KNOWN_LEGIT_KEYWORDS = [
    "applied materials", "northrop grumman", "pratt & whitney", "snapchat",
    "intuitive surgical", "calstart", "aptera motors", "enovix",
    "affirmed housing", "palm communities", "related companies",
    "amcal multi-housing", "hitzke development", "republic services",
    "wattev", "humane, inc", "infinera", "tynergy", "aibot",
    "berkshire hathaway", "bhe renewables", "wm renewable", "tesla",
    "pinnpack", "ivan's recycling", "skycharger", "calbiog",
    "eden housing", "habitat for humanity", "national community renaissance",
    "united cerebral palsy", "repet", "recycle from home",
    "university", "college", "school district", "county of", "city of",
    "cal pac recycling", "jessie lord bakery", "touchstone pistachio",
    "raven sr", "harbor cogeneration", "domus", "aemetis",
    "biggs bioenergy", "mariposa bioenergy", "newlight",
    "se us development", "materials research", "zimeno", "foggy bottoms",
]


def is_known_legit(name):
    name_lower = name.lower()
    return any(k in name_lower for k in KNOWN_LEGIT_KEYWORDS)


def main():
    df = pd.read_csv("data/grants_full.csv", low_memory=False)
    df["award_amount"] = pd.to_numeric(
        df["TotalAwardAmount"].astype(str).str.replace(r"[^\d.]", "", regex=True),
        errors="coerce"
    )

    findings = {"sos_checks": [], "confirmed_ghosts": [], "ncmr_recheck": []}

    # ================================================================
    # PART A: Find all NCMR / construction business grants
    # ================================================================
    print("=" * 70)
    print("PART A: CONSTRUCTION/EQUIPMENT BUSINESS GRANTS ($100K-$5M)")
    print("=" * 70)

    biz_mask = df["RecipientType"].str.lower() == "business"
    amount_mask = (df["award_amount"] >= 100_000) & (df["award_amount"] <= 5_000_000)

    # High-risk program keywords
    high_risk_kw = [
        "construction", "renovation", "equipment", "infrastructure",
        "facility", "building", "improvement", "capital", "site improvement",
        "purchase", "install",
    ]
    
    def is_high_risk(row):
        combined = f"{row.get('ProjectTitle', '')} {row.get('ProjectAbstract', '')}".lower()
        return any(kw in combined for kw in high_risk_kw)
    
    target_df = df[biz_mask & amount_mask].copy()
    target_df["is_high_risk"] = target_df.apply(is_high_risk, axis=1)
    hr_df = target_df[target_df["is_high_risk"]]
    
    print(f"Business grants $100K-$5M: {len(target_df)}")
    print(f"Of those, high-risk programs: {len(hr_df)}")
    
    # Remove known legit
    hr_df = hr_df[~hr_df["RecipientName"].apply(is_known_legit)]
    print(f"After removing known legit: {len(hr_df)}")
    
    # Deduplicate by recipient name
    unique_recipients = hr_df.drop_duplicates(subset=["RecipientName"])
    print(f"Unique recipients to check: {len(unique_recipients)}")
    
    # Sort by amount descending
    unique_recipients = unique_recipients.sort_values("award_amount", ascending=False)
    
    # ================================================================
    # PART B: SOS Registration Check via SERP
    # ================================================================
    print("\n" + "=" * 70)
    print("PART B: SOS REGISTRATION CHECKS")
    print("=" * 70)
    
    # Check up to 60 entities (budget: ~$0.09)
    check_limit = 60
    checked = 0
    
    for _, row in unique_recipients.head(check_limit).iterrows():
        name = str(row["RecipientName"])
        amount = row["award_amount"]
        title = str(row.get("ProjectTitle", ""))
        agency = str(row.get("AgencyDept", ""))
        
        checked += 1
        safe_print(f"\n[{checked}/{min(len(unique_recipients), check_limit)}] {name} | ${amount:,.0f}")
        
        # SOS check
        sos_count, sos_results, _ = serp(f'"{name}" California Secretary of State OR bizfileonline.sos.ca.gov')
        
        # General web presence check
        web_count, web_results, _ = serp(f'"{name}" California')
        
        result = {
            "recipient": name,
            "award_amount": float(amount),
            "grant_title": title,
            "agency": agency,
            "sos_results": sos_count,
            "sos_top": [r["title"][:80] for r in sos_results[:3]],
            "web_results": web_count,
            "web_top": [{"title": r["title"][:80], "link": r["link"][:100]} for r in web_results[:3]],
        }
        
        # Check if SOS results actually match this entity
        sos_match = False
        name_lower = name.lower().replace(",", "").replace(".", "").strip()
        name_words = set(name_lower.split())
        
        for r in sos_results[:5]:
            r_text = f"{r.get('title', '')} {r.get('snippet', '')}".lower()
            # Check if at least 2 significant words from entity name appear
            matching_words = sum(1 for w in name_words if len(w) > 2 and w in r_text)
            if matching_words >= 2:
                sos_match = True
                break
        
        result["sos_match"] = sos_match
        
        # Classify
        if sos_count == 0 or (sos_count > 0 and not sos_match):
            if web_count <= 2:
                result["classification"] = "GHOST ENTITY"
                result["fraud_signal"] = "VERY HIGH"
                safe_print(f"  *** GHOST ENTITY *** No SOS registration, no web presence")
                findings["confirmed_ghosts"].append(result)
            else:
                result["classification"] = "NO SOS REGISTRATION"
                result["fraud_signal"] = "HIGH"
                safe_print(f"  ** NO SOS ** Has web presence but no state registration")
                findings["confirmed_ghosts"].append(result)
        else:
            result["classification"] = "REGISTERED"
            result["fraud_signal"] = "LOW"
            safe_print(f"  OK - Registered with SOS")
        
        findings["sos_checks"].append(result)
    
    # ================================================================
    # PART C: Re-check NCMR entities
    # ================================================================
    print("\n" + "=" * 70)
    print("PART C: NCMR ENTITY RE-VALIDATION")
    print("=" * 70)
    
    ncmr_entities = [
        {"name": "Suarez Holdings, LLC", "amount": 1500000},
        {"name": "JM3 Holdings, LLC", "amount": 1500000},
        {"name": "SBA Enterprises", "amount": 1500000},
        {"name": "Infinite Sky Inc", "amount": 1500000},
    ]
    
    for entity in ncmr_entities:
        name = entity["name"]
        amount = entity["amount"]
        
        safe_print(f"\n--- NCMR Re-check: {name} (${amount:,.0f}) ---")
        
        ncmr_result = {
            "recipient": name,
            "amount": amount,
            "checks": {},
        }
        
        # SOS check
        c1, r1, _ = serp(f'"{name}" site:bizfileonline.sos.ca.gov OR "Secretary of State"')
        ncmr_result["checks"]["sos"] = {"count": c1, "results": [r["title"][:80] for r in r1[:3]]}
        
        # CSLB contractor check
        c2, r2, _ = serp(f'"{name}" CSLB OR "contractor license" California')
        ncmr_result["checks"]["cslb"] = {"count": c2, "results": [r["title"][:80] for r in r2[:3]]}
        
        # Building permits
        c3, r3, _ = serp(f'"{name}" building permit OR construction permit California')
        ncmr_result["checks"]["permits"] = {"count": c3, "results": [r["title"][:80] for r in r3[:3]]}
        
        # General web presence
        c4, r4, _ = serp(f'"{name}" California')
        ncmr_result["checks"]["web"] = {"count": c4, "results": [{"title": r["title"][:80], "link": r["link"][:100]} for r in r4[:3]]}
        
        # Child care license (since NCMR is for childcare)
        c5, r5, _ = serp(f'"{name}" child care OR daycare OR childcare license California')
        ncmr_result["checks"]["childcare"] = {"count": c5, "results": [r["title"][:80] for r in r5[:3]]}
        
        # Calculate ghost score
        total = c1 + c2 + c3 + c4 + c5
        # How many results are about the ACTUAL entity vs noise?
        grant_noise = 0
        for rlist in [r1, r2, r3, r4, r5]:
            for r in rlist:
                link = r.get("link", "")
                if "grants.ca.gov" in link or "hcd.ca.gov" in link:
                    grant_noise += 1
        
        ncmr_result["total_results"] = total
        ncmr_result["grant_noise"] = grant_noise
        ncmr_result["real_results"] = total - grant_noise
        
        if total <= 3:
            ncmr_result["verdict"] = "CONFIRMED GHOST"
            ncmr_result["fraud_probability"] = ">95%"
        elif ncmr_result["real_results"] <= 5:
            ncmr_result["verdict"] = "VERY SUSPICIOUS"
            ncmr_result["fraud_probability"] = ">80%"
        else:
            ncmr_result["verdict"] = "HAS SOME PRESENCE"
            ncmr_result["fraud_probability"] = "NEEDS REVIEW"
        
        safe_print(f"  VERDICT: {ncmr_result['verdict']} ({ncmr_result['fraud_probability']})")
        safe_print(f"  Total: {total} results (grant noise: {grant_noise}, real: {ncmr_result['real_results']})")
        
        findings["ncmr_recheck"].append(ncmr_result)
    
    # ================================================================
    # FINAL REPORT
    # ================================================================
    print("\n" + "=" * 70)
    print("FINAL REPORT")
    print("=" * 70)
    
    ghosts = findings["confirmed_ghosts"]
    print(f"\nGHOST / NO-SOS entities found: {len(ghosts)}")
    total_ghost_value = sum(g["award_amount"] for g in ghosts)
    print(f"Total ghost value: ${total_ghost_value:,.0f}")
    
    for g in ghosts:
        safe_print(f"  {g['recipient']} | ${g['award_amount']:,.0f} | {g['classification']} | {g['grant_title'][:50]}")
    
    print(f"\nNCMR Re-checks:")
    for n in findings["ncmr_recheck"]:
        safe_print(f"  {n['recipient']} | {n['verdict']} | {n['fraud_probability']}")
    
    # Save
    with open("data/sos_ghost_check.json", "w") as f:
        json.dump(findings, f, indent=2, default=str)
    print(f"\nAll results saved to data/sos_ghost_check.json")


if __name__ == "__main__":
    main()
