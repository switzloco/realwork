"""
SAM.gov Debarment Check — federal exclusion list lookup for CA grant recipients.

SAM.gov publishes the Excluded Parties List System (EPLS) — every entity
debarred, suspended, or otherwise excluded from receiving federal funds.

If a CA grant recipient appears on this list, that's a smoking gun:
California is paying public money to an entity the federal government has
formally barred from receiving federal money. Whether that's allowed
state-by-state varies, but it's at minimum a finding worth surfacing.

Data sources (in preference order):
  1. SAM.gov Exclusions API — requires free API key (SAM_GOV_API_KEY)
     https://open.gsa.gov/api/exclusions-api/
  2. Bright Data Web Unlocker on the public SAM.gov search UI (fallback)

Reads from data/audit_results.json (READ ONLY).
Writes to data/sam_gov/debarment_results.json.

Usage:
    # With SAM.gov API key (recommended)
    SAM_GOV_API_KEY=xxx python -m src.sam_gov.debarment_check --top 1000

    # Via Bright Data (no SAM key needed)
    python -m src.sam_gov.debarment_check --top 200 --use-brightdata --budget 5
"""

import argparse
import json
import os
import re
import time
from pathlib import Path
from urllib.parse import quote_plus

import requests
from dotenv import load_dotenv

load_dotenv()

SAM_API_BASE = "https://api.sam.gov/entity-information/v3/exclusions"
SAM_PUBLIC_SEARCH = "https://sam.gov/search/?index=ex&keywords="
SAM_API_KEY = os.environ.get("SAM_GOV_API_KEY", "")

OUTPUT_DIR = Path("data/sam_gov")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_PATH = OUTPUT_DIR / "debarment_results.json"


def normalize_name(name: str) -> str:
    n = name.lower().strip()
    n = re.sub(r"\b(inc|llc|corp|co|ltd|lp|lc|plc)\b\.?", "", n)
    n = re.sub(r"[^a-z0-9\s]", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def load_entities(top_n: int = 1000) -> list[dict]:
    entities = []
    seen = set()
    for path in ["data/audit_results.json", "data/services_fraud_results.json",
                 "data/track_b/overhead_results.json"]:
        if not Path(path).exists():
            continue
        with open(path) as f:
            data = json.load(f)
        for key in ("high_risk_private_null_disbursement",
                    "high_risk_service_grants", "entities"):
            for e in data.get(key, []):
                name = (e.get("recipient") or e.get("name") or "").strip()
                if not name or name in seen or name.lower() == "unknown":
                    continue
                seen.add(name)
                entities.append({
                    "name": name,
                    "amount": float(e.get("award_amount", 0) or
                                    e.get("total_state_grants", 0) or 0),
                    "recipient_type": e.get("recipient_type", ""),
                })

    entities.sort(key=lambda x: -x["amount"])
    return entities[:top_n]


def check_via_sam_api(name: str) -> dict:
    """Query SAM.gov exclusions API directly. Requires SAM_GOV_API_KEY."""
    try:
        r = requests.get(SAM_API_BASE, params={
            "api_key": SAM_API_KEY,
            "exclusionName": name,
        }, timeout=30)
        if r.status_code == 401:
            return {"status": "AUTH_ERROR",
                    "error": "SAM_GOV_API_KEY rejected"}
        if not r.ok:
            return {"status": "API_ERROR",
                    "error": f"HTTP {r.status_code}"}
        data = r.json()
        # SAM API response shape:
        # { excludedEntity: [...], totalRecords: N }
        records = data.get("excludedEntity") or data.get("exclusions") or []
        total = data.get("totalRecords", len(records))
        if total == 0:
            return {"status": "CLEAR", "match_count": 0}

        # Filter to exact-ish name matches
        nn = normalize_name(name)
        matches = []
        for r_ in records[:20]:
            cand = r_.get("name") or r_.get("entityName") or ""
            if normalize_name(cand) == nn:
                matches.append({
                    "name": cand,
                    "exclusion_type": r_.get("exclusionType"),
                    "exclusion_program": r_.get("exclusionProgram"),
                    "active_date": r_.get("activeDate"),
                    "termination_date": r_.get("terminationDate"),
                    "excluding_agency": r_.get("excludingAgencyName"),
                    "cause": r_.get("causeAndTreatment"),
                })

        if matches:
            return {"status": "DEBARRED", "matches": matches,
                    "total_records_returned": total}
        return {"status": "NAME_OVERLAP_NO_EXACT_MATCH",
                "total_records_returned": total,
                "candidates": [
                    r_.get("name") or r_.get("entityName") or ""
                    for r_ in records[:5]
                ]}

    except Exception as e:
        return {"status": "EXCEPTION", "error": str(e)}


def check_via_brightdata(name: str, bd_client) -> dict:
    """Fallback: Web Unlocker on SAM.gov public search UI."""
    url = SAM_PUBLIC_SEARCH + quote_plus(name)
    resp = bd_client.unlock(url, render_js=True)
    if not resp.get("html"):
        return {"status": "NO_RESPONSE"}

    html = resp["html"].lower()
    # Look for "no results" patterns
    if any(phrase in html for phrase in
           ["no results", "0 results", "did not match", "no records"]):
        return {"status": "CLEAR"}

    # Look for exclusion-indicator patterns
    debarment_terms = ["excluded", "debarred", "suspended",
                       "active exclusion", "ineligible"]
    found_terms = [t for t in debarment_terms if t in html]

    nn = normalize_name(name)
    name_in_results = nn in normalize_name(html[:5000])

    if name_in_results and found_terms:
        return {"status": "POSSIBLE_DEBARMENT",
                "matched_terms": found_terms,
                "note": "Web Unlocker found exclusion-indicator terms near the "
                        "entity name. Manual SAM.gov check recommended."}
    return {"status": "UNCLEAR"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=500)
    parser.add_argument("--use-brightdata", action="store_true",
                        help="Use Bright Data fallback (no SAM API key needed)")
    parser.add_argument("--budget", type=float, default=5.0)
    parser.add_argument("--delay", type=float, default=0.3)
    args = parser.parse_args()

    entities = load_entities(top_n=args.top)
    if not entities:
        print("No entities to check.")
        return
    print(f"Checking SAM.gov debarment status for {len(entities)} entities...")

    use_api = bool(SAM_API_KEY) and not args.use_brightdata
    if use_api:
        print("Using SAM.gov API (free, requires SAM_GOV_API_KEY)")
    elif args.use_brightdata:
        print("Using Bright Data Web Unlocker fallback")
    else:
        print("No SAM_GOV_API_KEY set and --use-brightdata not specified.")
        print("Get a free key at https://sam.gov (under Account Details > API Keys)")
        print("Or run with --use-brightdata to scrape the public search UI.")
        return

    bd_client = None
    if args.use_brightdata:
        from src.bright_data.client import BrightDataClient
        bd_client = BrightDataClient(budget_cap=args.budget, label="sam_gov")

    results = []
    debarred_count = 0

    try:
        for i, entity in enumerate(entities, 1):
            name = entity["name"]
            if use_api:
                check = check_via_sam_api(name)
            else:
                check = check_via_brightdata(name, bd_client)

            entry = {**entity, **check}
            results.append(entry)
            status = check.get("status", "UNKNOWN")
            if status in ("DEBARRED", "POSSIBLE_DEBARMENT"):
                debarred_count += 1
            alert = "  🚨" if status == "DEBARRED" else (
                "  ⚠️" if status == "POSSIBLE_DEBARMENT" else "")
            safe = name.encode("ascii", "ignore").decode("ascii")
            print(f"[{i}/{len(entities)}] {safe[:40]:40s} -> {status}{alert}")

            time.sleep(args.delay)
            if i % 25 == 0:
                _write(results)

    except KeyboardInterrupt:
        print("\n⚠️  Interrupted — saving partial results")
    finally:
        _write(results)

    print(f"\n{'='*60}")
    print(f"SAM.GOV DEBARMENT CHECK COMPLETE")
    print(f"  Entities checked: {len(results)}")
    print(f"  Debarred / possible-debarment: {debarred_count}")

    debarred = [r for r in results if r.get("status") == "DEBARRED"]
    possible = [r for r in results if r.get("status") == "POSSIBLE_DEBARMENT"]

    if debarred:
        print(f"\n  🚨 CONFIRMED DEBARRED entities receiving CA grants:")
        for r in debarred:
            print(f"    {r['name'][:40]:40s} ${r['amount']:>12,.0f}")
            for m in r.get("matches", [])[:1]:
                print(f"      {m.get('exclusion_type')} by "
                      f"{m.get('excluding_agency')} on {m.get('active_date')}")

    if possible:
        print(f"\n  ⚠️  POSSIBLE debarment (manual verification needed):")
        for r in possible:
            print(f"    {r['name'][:40]:40s} ${r['amount']:>12,.0f}")

    if bd_client:
        print(f"  {bd_client.report()}")
    print(f"{'='*60}")


def _write(results: list):
    debarred = [r for r in results if r.get("status") == "DEBARRED"]
    possible = [r for r in results if r.get("status") == "POSSIBLE_DEBARMENT"]
    with open(RESULTS_PATH, "w") as f:
        json.dump({
            "checked": len(results),
            "debarred_count": len(debarred),
            "possible_count": len(possible),
            "debarred": debarred,
            "possible_debarment": possible,
            "all_results": results,
        }, f, indent=2, default=str)


if __name__ == "__main__":
    main()
