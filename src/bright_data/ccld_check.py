"""
CCLD (Community Care Licensing Division) facility verifier.

CA Department of Social Services publishes licensed childcare facilities.
NCMR grants ($1.5M max) require recipients to operate a licensed facility.
The CCLD search site (ccld.dss.ca.gov) blocks automated access — Web Unlocker
routes around that.

For each NCMR grant recipient:
  1. Search facility by licensee name
  2. Search facility by address
  3. Extract license number, facility type, capacity, status

Recipients with NO licensed facility = anomaly. NCMR is for building/
renovating *licensed* childcare facilities; if there's no license, ask
how the grant was used.

Reads from data/audit_results.json (READ ONLY) — pulls NCMR grants only.
Writes to data/bright_data/ccld_results.json.

Usage:
    python -m src.bright_data.ccld_check --budget 20
"""

import argparse
import json
import re
import time
from pathlib import Path
from urllib.parse import quote_plus

from src.bright_data.client import BrightDataClient, BudgetExceeded, OUTPUT_DIR

CCLD_SEARCH_URL = "https://www.ccld.dss.ca.gov/carefacilitysearch/"


def load_ncmr_grants(top_n: int = 100) -> list[dict]:
    candidates = []
    for path in ["data/audit_results.json", "data/services_fraud_results.json"]:
        if not Path(path).exists():
            continue
        with open(path) as f:
            data = json.load(f)
        for key in ("high_risk_private_null_disbursement", "high_risk_service_grants"):
            for entry in data.get(key, []):
                title = entry.get("grant_title", "").lower()
                desc = entry.get("description", "").lower()
                source = entry.get("funding_source", "").lower()
                if any(kw in title + desc + source for kw in
                       ["ncmr", "child care", "childcare", "new construction and major"]):
                    candidates.append(entry)

    seen = set()
    unique = []
    for c in candidates:
        n = c.get("recipient", "").strip()
        if n and n not in seen:
            seen.add(n)
            unique.append(c)
    unique.sort(key=lambda x: -x.get("award_amount", 0))
    return unique[:top_n]


def parse_ccld_html(html: str) -> dict:
    if not html:
        return {"facilities": [], "match_count": 0}

    facility_rows = re.findall(
        r'(?:Facility|License)\s*(?:Number|#)[:\s]*(\d{6,10})',
        html, re.I,
    )
    capacity = re.findall(r'capacity[:\s]*(\d+)', html, re.I)
    facility_types = re.findall(
        r'(infant\s*center|family\s*child\s*care|day\s*care|preschool|center)',
        html, re.I,
    )

    has_no_results = bool(
        re.search(r"no\s+(results|records|facilities)\s+(found|match)", html, re.I)
    )

    return {
        "facilities": [
            {"license_number": ln,
             "capacity": capacity[i] if i < len(capacity) else None,
             "type": facility_types[i].title() if i < len(facility_types) else None}
            for i, ln in enumerate(facility_rows)
        ],
        "match_count": len(facility_rows),
        "no_results_message": has_no_results,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=float, default=20.0)
    parser.add_argument("--top", type=int, default=100)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--delay", type=float, default=0.5)
    args = parser.parse_args()

    output_path = OUTPUT_DIR / "ccld_results.json"
    existing = {}
    if args.resume and output_path.exists():
        with open(output_path) as f:
            existing = {e["recipient"]: e for e in json.load(f).get("entities", [])}

    grants = load_ncmr_grants(top_n=args.top)
    if args.resume:
        grants = [g for g in grants if g["recipient"] not in existing]

    if not grants:
        print("No NCMR-style grants found in audit results.")
        print("  (Looking for grants with 'child care' / 'NCMR' / 'New Construction and Major' in title/description)")
        return

    print(f"Checking CCLD for {len(grants)} childcare grant recipients")
    client = BrightDataClient(budget_cap=args.budget, label="ccld_check")
    results = list(existing.values())

    try:
        for i, grant in enumerate(grants, 1):
            name = grant["recipient"]
            search_term = re.sub(r"[^a-zA-Z0-9\s]", " ", name).strip()
            url = f"{CCLD_SEARCH_URL}?searchType=name&searchName={quote_plus(search_term)}"

            resp = client.unlock(url, render_js=True)
            parsed = parse_ccld_html(resp.get("html", "") or "")
            verdict = "LICENSED" if parsed["match_count"] > 0 else "NO_LICENSE_FOUND"

            entry = {**grant, "search_url": url, "verdict": verdict, **parsed}
            results.append(entry)

            alert = "  ⚠️" if verdict == "NO_LICENSE_FOUND" else ""
            print(f"[{i}/{len(grants)}] {name[:40]:40s} -> {verdict}{alert} | {client.report()}")

            time.sleep(args.delay)
            if i % 10 == 0:
                _write(output_path, results, client)

    except BudgetExceeded as e:
        print(f"\n⚠️  {e}")
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted — saving partial results")
    finally:
        _write(output_path, results, client)
        _print_summary(results, client)


def _write(path: Path, results: list, client):
    with open(path, "w") as f:
        json.dump({
            "spent_usd": round(client.spent, 4),
            "budget_cap": client.budget_cap,
            "entities": results,
        }, f, indent=2)


def _print_summary(results: list, client):
    print(f"\n{'='*60}")
    print(f"CCLD CHECK COMPLETE — {client.report()}")
    licensed = [r for r in results if r.get("verdict") == "LICENSED"]
    unlicensed = [r for r in results if r.get("verdict") == "NO_LICENSE_FOUND"]
    print(f"  Licensed facilities found: {len(licensed)}")
    print(f"  No license found: {len(unlicensed)}")

    if unlicensed:
        total = sum(r.get("award_amount", 0) for r in unlicensed)
        print(f"\n  ⚠️  Childcare grants where no CCLD license found:")
        print(f"     ({len(unlicensed)} entities, ${total:,.0f} in grants)")
        for r in unlicensed[:30]:
            print(f"    {r['recipient'][:40]:40s} ${r['award_amount']:>12,.0f}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
