import os
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from src.investigation.scraper_coordinator import _scrape_serp
from src.budget import BudgetController

budget = BudgetController()

TARGETS = [
    {"name": "JM3 Holdings, LLC", "city": "Merced"},
    {"name": "Suarez Holdings, LLC", "city": "Sacramento"},
    {"name": "SBA Enterprises", "city": "Sacramento"},
    {"name": "Infinite Sky Inc.", "city": "Roseville"}
]

EVIDENCE_DIR = Path("data/evidence_dossiers")
EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

def safe_filename(name):
    return "".join([c if c.isalnum() else "_" for c in name]).lower()

def run_query(entity_name, query, description):
    print(f"\n--- Gathering: {description} ---")
    res = budget.reserve(0.50, description, entity_name)
    if not res["approved"]:
        print(f"Denied: {res['reason']}")
        return None
    
    data, cost = _scrape_serp(query)
    
    budget.record(
        project_id=entity_name,
        source="Google SERP",
        product="serp_api",
        estimated_cost=0.50,
        actual_cost=cost,
        description=description
    )
    
    try:
        parsed = json.loads(data)
        return parsed
    except:
        return data

def investigate_entity(target):
    name = target["name"]
    city = target["city"]
    print(f"\n\n================ INVESTIGATING {name} ================")
    
    dossier = {}
    
    # 1. CA SoS
    q_sos = f'"{name}" site:bizfileonline.sos.ca.gov'
    dossier["sos"] = run_query(name, q_sos, f"SoS Check - {name}")
    
    # 2. CSLB
    q_cslb = f'"{name}" site:cslb.ca.gov'
    dossier["cslb"] = run_query(name, q_cslb, f"CSLB Check - {name}")
    
    # 3. Permits
    q_permit = f'"{name}" "permit" {city} California'
    dossier["permit"] = run_query(name, q_permit, f"Permit Check - {name}")
    
    # 4. OpenCorporates
    q_opencorp = f'"{name}" California site:opencorporates.com'
    dossier["opencorporates"] = run_query(name, q_opencorp, f"OpenCorp Check - {name}")
    
    # 5. General Web Presence / Operations
    q_general = f'"{name}" {city} California (daycare OR childcare OR janitorial OR construction)'
    dossier["general"] = run_query(name, q_general, f"General Ops - {name}")
    
    # Save dossier
    fname = safe_filename(name)
    with open(EVIDENCE_DIR / f"{fname}.json", "w") as f:
        json.dump(dossier, f, indent=2)
    print(f"\nSaved dossier to {EVIDENCE_DIR}/{fname}.json")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    for target in TARGETS:
        investigate_entity(target)
    
    budget.status()
