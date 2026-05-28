"""
Targeted SERP Blast — Run Bright Data SERP checks on the most suspicious entities
from the smart hunt results. Focus on entities that are actually worth investigating,
not Fortune 500 companies.

Estimated cost: ~$0.0015 per SERP query (SERP API is $1.50/1k requests)
"""

import json
import os
import sys
import time

from dotenv import load_dotenv
load_dotenv()

from src.investigation.scraper_coordinator import _scrape_serp


def deduplicate_suspects(suspects: list) -> list:
    """Deduplicate by recipient name, keeping highest-scoring entry."""
    seen = {}
    for s in suspects:
        name = s["recipient"]
        if name not in seen or s["suspicion_score"] > seen[name]["suspicion_score"]:
            seen[name] = s
    return sorted(seen.values(), key=lambda x: int(x["suspicion_score"]), reverse=True)


def run_targeted_serp(suspects: list):
    results = []
    ghosts = []
    low_presence = []

    for i, suspect in enumerate(suspects):
        name = suspect["recipient"]
        county = suspect.get("county", "")
        # Clean up county field
        if "NaN" in county or "location" in county:
            county = ""
        
        # Build a clean query
        query = f'"{name}" California'
        
        print(f"[{i+1}/{len(suspects)}] SERP: {query}")
        print(f"  Score: {suspect['suspicion_score']} | ${suspect['award_amount']:,.0f} | {suspect['grant_title'][:50]}")
        
        try:
            raw_data, cost = _scrape_serp(query)
            
            organic_count = 0
            top_results = []
            
            if not raw_data:
                organic_count = 0
            else:
                try:
                    data = json.loads(raw_data)
                    if isinstance(data, list):
                        organic_count = len(data)
                        # Extract top 3 result titles and URLs for context
                        for r in data[:3]:
                            if isinstance(r, dict):
                                top_results.append({
                                    "title": r.get("title", ""),
                                    "link": r.get("link", r.get("url", "")),
                                    "description": r.get("description", r.get("snippet", ""))[:150],
                                })
                    elif isinstance(data, dict):
                        organic = data.get("organic", [])
                        if isinstance(organic, list):
                            organic_count = len(organic)
                            for r in organic[:3]:
                                if isinstance(r, dict):
                                    top_results.append({
                                        "title": r.get("title", ""),
                                        "link": r.get("link", r.get("url", "")),
                                        "description": r.get("description", r.get("snippet", ""))[:150],
                                    })
                except json.JSONDecodeError:
                    organic_count = -1
            
            is_ghost = organic_count == 0
            is_low_presence = 0 < organic_count <= 2
            
            res = {
                "recipient": name,
                "recipient_type": suspect["recipient_type"],
                "award_amount": suspect["award_amount"],
                "grant_title": suspect["grant_title"],
                "agency": suspect["agency"],
                "suspicion_score": suspect["suspicion_score"],
                "flags": suspect["flags"],
                "grant_count": suspect.get("grant_count", 1),
                "query": query,
                "is_ghost": is_ghost,
                "is_low_presence": is_low_presence,
                "organic_results_count": organic_count,
                "top_results": top_results,
            }
            results.append(res)
            
            status = "GHOST!" if is_ghost else ("LOW" if is_low_presence else f"OK ({organic_count})")
            print(f"  -> {status}")
            if top_results:
                print(f"     Top result: {top_results[0].get('title', 'N/A')[:60]}")
            
            if is_ghost:
                ghosts.append(res)
            elif is_low_presence:
                low_presence.append(res)
            
            time.sleep(0.5)
            
        except Exception as e:
            print(f"  -> ERROR: {e}")
    
    return results, ghosts, low_presence


def main():
    print("=" * 60)
    print("TARGETED SERP BLAST")
    print("=" * 60)
    
    with open("data/smart_hunt_results.json") as f:
        all_suspects = json.load(f)
    
    # Deduplicate
    unique = deduplicate_suspects(all_suspects)
    print(f"Total unique suspects: {len(unique)}")
    
    # Take top 50 unique entities by score
    targets = unique[:50]
    print(f"Targeting top {len(targets)} unique entities")
    print(f"Estimated cost: {len(targets)} * $0.0015 = ${len(targets) * 0.0015:.2f}")
    print()
    
    results, ghosts, low_presence = run_targeted_serp(targets)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"RESULTS SUMMARY")
    print(f"{'='*60}")
    print(f"Total checked: {len(results)}")
    print(f"GHOST entities (0 results): {len(ghosts)}")
    print(f"LOW presence (1-2 results): {len(low_presence)}")
    print(f"Normal presence (3+): {len(results) - len(ghosts) - len(low_presence)}")
    
    if ghosts:
        print(f"\n--- GHOST ENTITIES ---")
        ghost_value = sum(g["award_amount"] for g in ghosts)
        print(f"Total ghost value: ${ghost_value:,.0f}")
        for g in ghosts:
            print(f"  {g['recipient']} — ${g['award_amount']:,.0f} — {g['grant_title'][:40]}")
            print(f"    Flags: {', '.join(g['flags'][:3])}")
    
    if low_presence:
        print(f"\n--- LOW PRESENCE ENTITIES ---")
        lp_value = sum(lp["award_amount"] for lp in low_presence)
        print(f"Total low-presence value: ${lp_value:,.0f}")
        for lp in low_presence:
            print(f"  {lp['recipient']} — ${lp['award_amount']:,.0f} — {lp['grant_title'][:40]} ({lp['organic_results_count']} results)")
            if lp["top_results"]:
                print(f"    Top: {lp['top_results'][0].get('title', 'N/A')[:60]}")
    
    # Save
    output = {
        "total_checked": len(results),
        "ghost_count": len(ghosts),
        "low_presence_count": len(low_presence),
        "ghosts": ghosts,
        "low_presence": low_presence,
        "all_results": results,
    }
    
    with open("data/targeted_serp_results.json", "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nSaved to data/targeted_serp_results.json")


if __name__ == "__main__":
    main()
