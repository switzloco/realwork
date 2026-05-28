"""
Comprehensive fraud hunt — autonomous deep investigation.

Phase 1: Find ALL individual MHP grant recipients in the dataset
Phase 2: SERP-blast every MHP owner + their park for web presence
Phase 3: Search for physical addresses, Google Maps, property records
Phase 4: Check wolf claims for outlier analysis
Phase 5: Look for OTHER suspicious patterns (same address, same person, etc.)
"""

import json
import os
import re
import time
from collections import Counter, defaultdict

import pandas as pd
from dotenv import load_dotenv
load_dotenv()

from src.investigation.scraper_coordinator import _scrape_serp


def safe_print(s):
    print(str(s).encode('ascii', 'replace').decode())


def serp(query):
    """Single SERP query, returns (organic_count, top_results, raw_snippet)."""
    safe_print(f"  SERP: {query}")
    raw, cost = _scrape_serp(query)
    organic_count = 0
    top_results = []
    if raw:
        try:
            data = json.loads(raw)
            if isinstance(data, list):
                organic_count = len(data)
                for r in data[:5]:
                    if isinstance(r, dict):
                        top_results.append({
                            "title": r.get("title", ""),
                            "link": r.get("link", r.get("url", "")),
                            "snippet": r.get("description", r.get("snippet", ""))[:200],
                        })
            elif isinstance(data, dict) and "organic" in data:
                organic = data["organic"]
                if isinstance(organic, list):
                    organic_count = len(organic)
                    for r in organic[:5]:
                        if isinstance(r, dict):
                            top_results.append({
                                "title": r.get("title", ""),
                                "link": r.get("link", r.get("url", "")),
                                "snippet": r.get("description", r.get("snippet", ""))[:200],
                            })
        except:
            pass
    safe_print(f"    -> {organic_count} results")
    if top_results:
        safe_print(f"    Top: {top_results[0].get('title', '')[:70]}")
    time.sleep(0.3)
    return organic_count, top_results, raw[:3000] if raw else ""


def main():
    df = pd.read_csv("data/grants_full.csv", low_memory=False)
    # Normalize amount
    df["award_amount"] = pd.to_numeric(
        df["TotalAwardAmount"].astype(str).str.replace(r"[^\d.]", "", regex=True),
        errors="coerce"
    )
    
    findings = {
        "mhp_analysis": {},
        "wolf_analysis": {},
        "more_program_deep_dive": [],
        "new_suspects": [],
    }

    # ================================================================
    # PHASE 1: Find ALL MHP / MORE program recipients
    # ================================================================
    print("=" * 70)
    print("PHASE 1: ALL MHP / MORE PROGRAM RECIPIENTS")
    print("=" * 70)
    
    # Search for MORE program grants and MHP grants
    mhp_mask = (
        df["ProjectTitle"].str.contains("MHP", case=False, na=False) |
        df["ProjectAbstract"].str.contains("mobilehome|mobile home|manufactured housing", case=False, na=False, regex=True) |
        df["ProjectTitle"].str.contains("MORE", case=False, na=False)
    )
    mhp_df = df[mhp_mask].copy()
    print(f"Found {len(mhp_df)} MHP/MORE-related grants")
    
    # Also look for individual recipients with large grants across ALL programs
    individual_mask = df["RecipientType"].str.lower() == "individual"
    individual_large = df[individual_mask & (df["award_amount"] >= 100_000)]
    print(f"Found {len(individual_large)} individual recipients with grants >= $100K")
    
    # Show all MHP grants
    mhp_summary = []
    for _, row in mhp_df.iterrows():
        name = str(row.get("RecipientName", ""))
        amount = row.get("award_amount", 0)
        title = str(row.get("ProjectTitle", ""))
        agency = str(row.get("AgencyDept", ""))
        rtype = str(row.get("RecipientType", ""))
        county = str(row.get("CountiesServed", ""))
        abstract = str(row.get("ProjectAbstract", ""))[:200]
        location = str(row.get("GeographicLocationServed", ""))
        
        entry = {
            "recipient": name,
            "award_amount": float(amount) if pd.notna(amount) else 0,
            "title": title,
            "agency": agency,
            "type": rtype,
            "county": county,
            "location": location,
            "abstract": abstract,
        }
        mhp_summary.append(entry)
        safe_print(f"  {name} | ${amount:,.0f} | {title} | {rtype} | {county}")
    
    findings["mhp_analysis"]["all_grants"] = mhp_summary
    
    # ================================================================
    # PHASE 2: Deep SERP on Individual MHP owners
    # ================================================================
    print("\n" + "=" * 70)
    print("PHASE 2: SERP BLAST ON INDIVIDUAL MHP OWNERS")
    print("=" * 70)
    
    # Get unique individual MHP recipients
    individual_mhp = [m for m in mhp_summary if m["type"] == "Individual" and m["award_amount"] >= 50000]
    # Also deduplicate
    seen_names = set()
    unique_individual_mhp = []
    for m in individual_mhp:
        if m["recipient"] not in seen_names:
            seen_names.add(m["recipient"])
            unique_individual_mhp.append(m)
    
    print(f"Unique individual MHP recipients (>=$50K): {len(unique_individual_mhp)}")
    
    mhp_investigations = []
    
    for m in unique_individual_mhp:
        name = m["recipient"]
        title = m["title"]
        county = m["county"]
        amount = m["award_amount"]
        location = m["location"]
        
        print(f"\n--- Investigating: {name} ({title}) ${amount:,.0f} ---")
        
        investigation = {
            "recipient": name,
            "title": title,
            "amount": amount,
            "county": county,
            "location": location,
            "serp_results": {},
            "verdict": "PENDING",
        }
        
        # Query 1: Owner + park name
        q1_count, q1_results, _ = serp(f'"{name}" "{title}" California')
        investigation["serp_results"]["owner_and_park"] = {
            "count": q1_count, "results": q1_results
        }
        
        # Query 2: Park name + location
        q2_count, q2_results, _ = serp(f'"{title}" mobile home park {county} California')
        investigation["serp_results"]["park_location"] = {
            "count": q2_count, "results": q2_results
        }
        
        # Query 3: Owner name + property
        q3_count, q3_results, _ = serp(f'"{name}" property owner {county} California')
        investigation["serp_results"]["owner_property"] = {
            "count": q3_count, "results": q3_results
        }
        
        # Query 4: Google Maps / address search  
        q4_count, q4_results, _ = serp(f'"{title}" address Thermal OR Coachella OR "Riverside County" California')
        investigation["serp_results"]["address_search"] = {
            "count": q4_count, "results": q4_results
        }
        
        # Query 5: Any violations or complaints
        q5_count, q5_results, _ = serp(f'"{title}" violation OR complaint OR inspection')
        investigation["serp_results"]["violations"] = {
            "count": q5_count, "results": q5_results
        }
        
        # Determine web presence score
        total_organic = q1_count + q2_count + q3_count + q4_count + q5_count
        # Count how many are just grant docs (hcd.ca.gov)
        grant_doc_count = 0
        for qr in [q1_results, q2_results, q3_results, q4_results, q5_results]:
            for r in qr:
                if "hcd.ca.gov" in r.get("link", "") or "grants.ca.gov" in r.get("link", ""):
                    grant_doc_count += 1
        
        investigation["total_organic"] = total_organic
        investigation["grant_doc_only_count"] = grant_doc_count
        investigation["non_grant_results"] = total_organic - grant_doc_count
        
        # Cost per unit
        if "unit" in m["abstract"].lower() or "spaces" in m["abstract"].lower():
            # Try to extract unit count from abstract
            unit_match = re.search(r'(\d+)\s*(unit|space|lot)', m["abstract"].lower())
            if unit_match:
                units = int(unit_match.group(1))
                investigation["units"] = units
                investigation["cost_per_unit"] = amount / units if units > 0 else 0
        
        if investigation.get("non_grant_results", 0) <= 2:
            investigation["verdict"] = "GHOST - No web presence outside grant docs"
            investigation["fraud_probability"] = "HIGH"
        elif investigation.get("non_grant_results", 0) <= 5:
            investigation["verdict"] = "LOW PRESENCE - Minimal web footprint"
            investigation["fraud_probability"] = "MEDIUM"
        else:
            investigation["verdict"] = "HAS PRESENCE - Web footprint exists"
            investigation["fraud_probability"] = "LOW"
        
        safe_print(f"  VERDICT: {investigation['verdict']}")
        safe_print(f"  Total organic: {total_organic} (grant docs: {grant_doc_count}, non-grant: {investigation['non_grant_results']})")
        
        mhp_investigations.append(investigation)
    
    findings["more_program_deep_dive"] = mhp_investigations
    
    # ================================================================
    # PHASE 3: Broader MORE program analysis
    # ================================================================
    print("\n" + "=" * 70)
    print("PHASE 3: MORE PROGRAM ANALYSIS")
    print("=" * 70)
    
    # Search for MORE program info
    more_count, more_results, _ = serp("California MORE program mobilehome park grants audit fraud")
    findings["more_program_context"] = {"count": more_count, "results": more_results}
    
    # Search for cost benchmarks
    bench_count, bench_results, _ = serp("mobile home park remediation cost per unit California average")
    findings["cost_benchmark"] = {"count": bench_count, "results": bench_results}
    
    # Search for Thermal CA mobile home parks specifically
    thermal_count, thermal_results, _ = serp("Thermal California mobile home parks violations conditions")
    findings["thermal_context"] = {"count": thermal_count, "results": thermal_results}
    
    # ================================================================
    # PHASE 4: Wolf depredation outlier analysis
    # ================================================================
    print("\n" + "=" * 70)
    print("PHASE 4: WOLF DEPREDATION OUTLIER ANALYSIS")
    print("=" * 70)
    
    wolf_mask = df["ProjectTitle"].str.contains("Wolf-", case=False, na=False)
    wolf_df = df[wolf_mask].copy()
    print(f"Total wolf depredation grants: {len(wolf_df)}")
    
    # Group by recipient
    wolf_by_recipient = wolf_df.groupby("RecipientName").agg(
        grant_count=("award_amount", "count"),
        total_value=("award_amount", "sum"),
    ).sort_values("total_value", ascending=False)
    
    print("\nTop wolf claim recipients:")
    wolf_ranking = []
    for name, row in wolf_by_recipient.head(15).iterrows():
        safe_print(f"  {name}: {int(row['grant_count'])} grants, ${row['total_value']:,.0f}")
        wolf_ranking.append({
            "recipient": name,
            "grant_count": int(row["grant_count"]),
            "total_value": float(row["total_value"]),
        })
    
    findings["wolf_analysis"] = {
        "total_grants": len(wolf_df),
        "total_value": float(wolf_df["award_amount"].sum()),
        "unique_recipients": len(wolf_by_recipient),
        "top_recipients": wolf_ranking,
    }
    
    # Is Table Rock an outlier?
    if len(wolf_ranking) > 1:
        top_value = wolf_ranking[0]["total_value"]
        second_value = wolf_ranking[1]["total_value"]
        ratio = top_value / second_value if second_value > 0 else float("inf")
        findings["wolf_analysis"]["top_vs_second_ratio"] = ratio
        print(f"\nTop recipient vs #2 ratio: {ratio:.1f}x")
    
    # ================================================================
    # PHASE 5: Search for duplicate/related entities
    # ================================================================
    print("\n" + "=" * 70)
    print("PHASE 5: DUPLICATE AND RELATED ENTITY SEARCH")
    print("=" * 70)
    
    # Find all Business recipients in Thermal/Coachella/Riverside with construction grants
    thermal_mask = (
        df["GeographicLocationServed"].str.contains("Thermal|Coachella", case=False, na=False) |
        df["CountiesServed"].str.contains("Riverside", case=False, na=False)
    )
    hcd_mask = df["AgencyDept"].str.contains("Housing", case=False, na=False)
    thermal_hcd = df[thermal_mask & hcd_mask]
    
    print(f"HCD grants in Riverside County: {len(thermal_hcd)}")
    thermal_hcd_list = []
    for _, row in thermal_hcd.iterrows():
        name = str(row.get("RecipientName", ""))
        amount = row.get("award_amount", 0)
        title = str(row.get("ProjectTitle", ""))
        rtype = str(row.get("RecipientType", ""))
        location = str(row.get("GeographicLocationServed", ""))
        
        entry = {
            "recipient": name,
            "amount": float(amount) if pd.notna(amount) else 0,
            "title": title,
            "type": rtype,
            "location": location,
        }
        thermal_hcd_list.append(entry)
        safe_print(f"  {name} | ${amount:,.0f} | {title} | {rtype}")
    
    findings["riverside_hcd_grants"] = thermal_hcd_list
    
    # ================================================================
    # PHASE 6: Deep dive on any HIGH fraud probability findings
    # ================================================================
    print("\n" + "=" * 70)
    print("PHASE 6: DEEP DIVE ON HIGH-PROBABILITY TARGETS")
    print("=" * 70)
    
    high_prob = [m for m in mhp_investigations if m.get("fraud_probability") == "HIGH"]
    print(f"High-probability targets: {len(high_prob)}")
    
    for target in high_prob:
        name = target["recipient"]
        title = target["title"]
        print(f"\n--- DEEP DIVE: {name} ({title}) ---")
        
        # Try to find ANY evidence this park exists
        deep_results = {}
        
        # Google Maps search
        c1, r1, _ = serp(f'{title} mobile home park Google Maps')
        deep_results["google_maps"] = {"count": c1, "results": r1}
        
        # Riverside County assessor
        c2, r2, _ = serp(f'"{name}" Riverside County assessor property records')
        deep_results["assessor"] = {"count": c2, "results": r2}
        
        # HCD license/registration
        c3, r3, _ = serp(f'"{title}" HCD mobilehome park registration license California')
        deep_results["hcd_license"] = {"count": c3, "results": r3}
        
        # Building permits
        c4, r4, _ = serp(f'"{name}" OR "{title}" building permit Riverside County')
        deep_results["permits"] = {"count": c4, "results": r4}
        
        # Yelp / tenant reviews
        c5, r5, _ = serp(f'"{title}" review OR tenant OR resident')
        deep_results["reviews"] = {"count": c5, "results": r5}
        
        # Code enforcement / violations history
        c6, r6, _ = serp(f'"{title}" code enforcement violation Riverside')
        deep_results["code_enforcement"] = {"count": c6, "results": r6}
        
        target["deep_dive"] = deep_results
        
        total_deep = c1 + c2 + c3 + c4 + c5 + c6
        # Filter out grant doc results
        non_grant_deep = 0
        for qr_list in [r1, r2, r3, r4, r5, r6]:
            for r in qr_list:
                link = r.get("link", "")
                if "hcd.ca.gov" not in link and "grants.ca.gov" not in link:
                    non_grant_deep += 1
        
        target["deep_total_organic"] = total_deep
        target["deep_non_grant"] = non_grant_deep
        
        safe_print(f"  Deep dive total: {total_deep} results ({non_grant_deep} non-grant)")
        
        if non_grant_deep <= 3:
            target["final_verdict"] = "CONFIRMED GHOST - Extremely high fraud probability"
            target["final_fraud_probability"] = "VERY HIGH (>90%)"
        elif non_grant_deep <= 8:
            target["final_verdict"] = "SUSPICIOUS - Low web presence for a funded entity"
            target["final_fraud_probability"] = "HIGH (70-90%)"
        else:
            target["final_verdict"] = "INCONCLUSIVE - Some web presence found"
            target["final_fraud_probability"] = "MEDIUM (40-70%)"
        
        safe_print(f"  FINAL VERDICT: {target['final_verdict']}")
        safe_print(f"  FRAUD PROBABILITY: {target['final_fraud_probability']}")
    
    # Save everything
    with open("data/comprehensive_hunt.json", "w") as f:
        json.dump(findings, f, indent=2, default=str)
    
    # Print final summary
    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    
    for target in mhp_investigations:
        prob = target.get("final_fraud_probability", target.get("fraud_probability", "UNKNOWN"))
        verdict = target.get("final_verdict", target.get("verdict", "UNKNOWN"))
        safe_print(f"  {target['recipient']} | ${target['amount']:,.0f} | {prob} | {verdict}")
    
    print(f"\nResults saved to data/comprehensive_hunt.json")


if __name__ == "__main__":
    main()
