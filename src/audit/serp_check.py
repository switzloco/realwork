import json
import os
import sys
import time

from dotenv import load_dotenv
load_dotenv()

from src.investigation.scraper_coordinator import _scrape_serp

def run_serp_checks():
    print("Loading audit results...")
    try:
        with open("data/audit_results.json", "r") as f:
            audit = json.load(f)
    except FileNotFoundError:
        print("data/audit_results.json not found! Run Task 1 first.")
        sys.exit(1)

    high_risk = audit.get("high_risk_private_null_disbursement", [])
    if not high_risk:
        print("No high risk entities found in audit results.")
        sys.exit(1)

    top_20 = high_risk[:20]
    print(f"Checking {len(top_20)} high-risk entities via Bright Data SERP...")

    results = []
    ghost_entities = []

    for i, entity in enumerate(top_20):
        name = entity.get("recipient", "Unknown")
        # clean location string
        loc = entity.get("location", "")
        # The location string from pandas might have newlines and garbage. Let's just use "California"
        # if it's messy, but we can try to extract the county.
        county = ""
        for line in loc.split('\n'):
            if "location" in line and "County" not in line and "NaN" not in line:
                val = line.replace("location", "").strip()
                if "Name:" not in val:
                    county = val

        query = f'"{name}" {county} California'.strip()
        print(f"[{i+1}/20] Query: {query}")
        
        try:
            raw_data, cost = _scrape_serp(query)
            
            is_ghost = False
            organic_count = 0
            
            if not raw_data:
                is_ghost = True
            else:
                try:
                    data = json.loads(raw_data)
                    if isinstance(data, list):
                        organic_count = len(data)
                        if organic_count == 0:
                            is_ghost = True
                    else:
                        organic_count = -1 # couldn't parse list
                except json.JSONDecodeError:
                    if "organic" not in raw_data.lower() and "http" not in raw_data:
                        is_ghost = True

            print(f"  -> Ghost? {is_ghost} (Organic results: {organic_count})")
            
            res = {
                "recipient": name,
                "award_amount": entity.get("award_amount"),
                "query": query,
                "is_ghost": is_ghost,
                "organic_results_count": organic_count
            }
            results.append(res)
            
            if is_ghost:
                ghost_entities.append(res)
                
            time.sleep(1) # Be nice
            
        except Exception as e:
            print(f"  -> Error: {e}")

    print("\n--- RESULTS ---")
    print(f"Found {len(ghost_entities)} potential ghost entities out of {len(top_20)} checked.")
    for ghost in ghost_entities:
        print(f"  - {ghost['recipient']} (${ghost['award_amount']:,.0f})")

    out_file = "data/serp_check_results.json"
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved full results to {out_file}")

if __name__ == "__main__":
    run_serp_checks()
