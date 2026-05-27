import json
import os
import requests
import time
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("BRIGHT_DATA_API_KEY")
ZONE = os.environ.get("BRIGHT_DATA_SERP_ZONE", "realwork_serp")

def run():
    print("Loading high-risk entities from data/audit_results.json...")
    with open("data/audit_results.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Sort high-risk by award amount descending
    high_risk = sorted(data["high_risk_private_null_disbursement"], key=lambda x: x["award_amount"], reverse=True)
    top_20 = high_risk[:20]

    print(f"Searching top {len(top_20)} entities using Bright Data SERP API...")
    results = []

    for i, rec in enumerate(top_20, 1):
        entity_name = rec["recipient"]
        query = f'"{entity_name}" California'
        url = "https://api.brightdata.com/request"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "zone": ZONE,
            "url": f"https://www.google.com/search?q={quote_plus(query)}&brd_json=1",
            "format": "json",
        }
        
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=30)
            has_results = False
            organic_count = 0
            if r.status_code == 200:
                try:
                    resp_data = r.json()
                    
                    # Try unwrapping body if needed
                    if "body" in resp_data and isinstance(resp_data["body"], str):
                        try:
                            body_data = json.loads(resp_data["body"])
                            if "organic" in body_data:
                                organic_count = len(body_data["organic"])
                                has_results = organic_count > 0
                        except Exception:
                            pass
                    
                    if not has_results and "organic" in resp_data:
                        organic_count = len(resp_data["organic"])
                        has_results = organic_count > 0
                except Exception:
                    has_results = True # If not JSON but 200, assume some HTML came back
            
            status = "FOUND" if has_results else "GHOST ENTITY"
            print(f"[{i}/20] {query}")
            print(f"  -> {status} ({organic_count} organic results)")
            
            results.append({
                "entity": entity_name,
                "award": rec["award_amount"],
                "query": query,
                "status": status,
                "organic_count": organic_count
            })
        except Exception as e:
            print(f"Error on {entity_name}: {e}")
        time.sleep(1)

    with open("data/ghost_entities.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    ghosts = [r for r in results if r["status"] == "GHOST ENTITY"]
    print(f"\n============================================================")
    print(f"ZERO WEB PRESENCE AUDIT COMPLETE")
    print(f"Found {len(ghosts)} ghost entities out of {len(top_20)} searched.")
    for g in ghosts:
        print(f"  - {g['entity']} (${g['award']:,.2f})")
    print(f"============================================================")

if __name__ == "__main__":
    run()
