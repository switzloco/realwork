"""
Deep dive on our best leads from the SERP blast.
1. Pinnpack Capital Holdings #2 — $3.5M GHOST
2. Coelho Dairy Biogas LLC — $1M LOW presence
3. Related entities check — are there more Pinnpack grants?
4. Individual recipients getting huge construction grants
"""

import json
import os
import time
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

from src.investigation.scraper_coordinator import _scrape_serp


def search_dataset_for(df, keyword):
    """Search the full dataset for a keyword in recipient name."""
    mask = df["RecipientName"].str.contains(keyword, case=False, na=False)
    matches = df[mask]
    print(f"\n--- Dataset search for '{keyword}' ---")
    print(f"Found {len(matches)} grants:")
    for _, row in matches.iterrows():
        name = row.get("RecipientName", "?")
        amount = row.get("TotalAwardAmount", "?")
        title = row.get("ProjectTitle", "?")
        agency = row.get("AgencyDept", "?")
        rtype = row.get("RecipientType", "?")
        abstract = str(row.get("ProjectAbstract", ""))[:150]
        county = row.get("CountiesServed", "?")
        safe_name = str(name).encode('ascii', 'replace').decode()
        safe_title = str(title).encode('ascii', 'replace').decode()
        safe_abstract = str(abstract).encode('ascii', 'replace').decode()
        print(f"  {safe_name} | {amount} | {safe_title}")
        print(f"    Agency: {agency} | Type: {rtype} | County: {county}")
        print(f"    Abstract: {safe_abstract}")
        print()
    return matches


def deep_serp(queries):
    """Run multiple SERP queries and return results."""
    results = []
    for q in queries:
        print(f"SERP: {q}")
        raw, cost = _scrape_serp(q)
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
            except:
                pass
        
        print(f"  Results: {organic_count}")
        for tr in top_results:
            title = tr['title'][:60].encode('ascii', 'replace').decode()
            link = tr['link'][:80].encode('ascii', 'replace').decode()
            snippet = tr['snippet'][:100].encode('ascii', 'replace').decode()
            print(f"    - {title}")
            print(f"      {link}")
            print(f"      {snippet}")
            print()
        
        results.append({
            "query": q,
            "organic_count": organic_count,
            "top_results": top_results,
            "raw_snippet": raw[:2000] if raw else "",
        })
        time.sleep(0.5)
    
    return results


def main():
    print("=" * 70)
    print("DEEP DIVE — HIGH-VALUE LEADS")
    print("=" * 70)
    
    # Load full dataset
    df = pd.read_csv("data/grants_full.csv", low_memory=False)
    
    all_findings = {}
    
    # ========================================
    # LEAD 1: Pinnpack Capital Holdings
    # ========================================
    print("\n" + "=" * 70)
    print("LEAD 1: PINNPACK CAPITAL HOLDINGS")
    print("=" * 70)
    
    search_dataset_for(df, "Pinnpack")
    search_dataset_for(df, "pinnpack")
    
    pinnpack_serps = deep_serp([
        '"Pinnpack Capital Holdings" California',
        '"Pinnpack Capital Holdings #2"',
        '"Pinnpack" recycling California',
        '"Pinnpack" LLC OR Inc OR Corp',
        'site:sos.ca.gov "Pinnpack"',
    ])
    all_findings["pinnpack"] = pinnpack_serps
    
    # ========================================
    # LEAD 2: Ivan's Recycling LLC
    # ========================================
    print("\n" + "=" * 70)
    print("LEAD 2: IVAN'S RECYCLING LLC")
    print("=" * 70)
    
    search_dataset_for(df, "Ivan's Recycling")
    
    ivans_serps = deep_serp([
        '"Ivan\'s Recycling, LLC" California',
        '"Ivan\'s Recycling" recycling grant',
        'site:sos.ca.gov "Ivan\'s Recycling"',
    ])
    all_findings["ivans_recycling"] = ivans_serps
    
    # ========================================
    # LEAD 3: Jose Perez — Individual, $2.19M
    # ========================================
    print("\n" + "=" * 70)
    print("LEAD 3: JOSE PEREZ — $2.19M INDIVIDUAL")
    print("=" * 70)
    
    search_dataset_for(df, "Jose Perez")
    search_dataset_for(df, "Perez MHP")
    
    perez_serps = deep_serp([
        '"Jose Perez" "Perez MHP" California',
        '"Perez MHP" mobile home park California',
        '"Jose Perez" "Department of Housing" California grant',
    ])
    all_findings["jose_perez"] = perez_serps
    
    # ========================================
    # LEAD 4: Luis Bojorquez — Individual, $1.43M
    # ========================================
    print("\n" + "=" * 70)
    print("LEAD 4: LUIS BOJORQUEZ — $1.43M INDIVIDUAL")
    print("=" * 70)
    
    search_dataset_for(df, "Bojorquez")
    
    bojorquez_serps = deep_serp([
        '"Luis Bojorquez" "Bojorquez MHP" California',
        '"Bojorquez MHP" mobile home park California',
        '"Luis Bojorquez" housing grant California',
    ])
    all_findings["bojorquez"] = bojorquez_serps
    
    # ========================================
    # LEAD 5: Skychargers LLC — $10.6M across 4 grants
    # ========================================
    print("\n" + "=" * 70)
    print("LEAD 5: SKYCHARGERS LLC — $10.6M")
    print("=" * 70)
    
    search_dataset_for(df, "Skycharger")
    
    sky_serps = deep_serp([
        '"Skychargers, LLC" California',
        '"Skychargers" EV charging California',
        'site:sos.ca.gov "Skychargers"',
    ])
    all_findings["skychargers"] = sky_serps
    
    # ========================================
    # LEAD 6: Table Rock LLC — 16 grants
    # ========================================
    print("\n" + "=" * 70)
    print("LEAD 6: TABLE ROCK LLC — 16 GRANTS")
    print("=" * 70)
    
    search_dataset_for(df, "Table Rock LLC")
    
    tr_serps = deep_serp([
        '"Table Rock LLC" California',
        '"Table Rock LLC" ranch livestock California',
        '"Table Rock LLC" "Department of Fish and Wildlife"',
    ])
    all_findings["table_rock"] = tr_serps
    
    # ========================================
    # LEAD 7: TOP ASSETS LLC — multiple grants, short name
    # ========================================
    print("\n" + "=" * 70)
    print("LEAD 7: TOP ASSETS LLC")
    print("=" * 70)
    
    search_dataset_for(df, "TOP ASSETS")
    
    ta_serps = deep_serp([
        '"TOP ASSETS LLC" California',
        '"TOP ASSETS" "service station" California',
    ])
    all_findings["top_assets"] = ta_serps
    
    # Save all findings
    with open("data/deep_dive_results.json", "w") as f:
        json.dump(all_findings, f, indent=2, default=str)
    print(f"\nAll findings saved to data/deep_dive_results.json")


if __name__ == "__main__":
    main()
