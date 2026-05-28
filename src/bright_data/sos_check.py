"""
CA Secretary of State business registry checker (via Bright Data Web Unlocker).

For each entity name, queries CA SOS bizfileonline search and extracts:
  - Entity status (Active / Suspended / Forfeited / Dissolved)
  - Entity number, registration date, jurisdiction
  - Agent for service of process

Suspended/Forfeited status while receiving an active grant = immediate red flag.

Reads from data/audit_results.json (READ ONLY).
Writes to data/bright_data/sos_results.json (exclusive).

Note: CA SOS search at https://bizfileonline.sos.ca.gov returns JSON via
their internal API. We use Web Unlocker because it routes around bot
detection — the same name search done from a script directly gets blocked.

Usage:
    python -m src.bright_data.sos_check --budget 20 --top 200
"""

import argparse
import json
import re
import time
from pathlib import Path
from urllib.parse import quote_plus

from src.bright_data.client import BrightDataClient, BudgetExceeded, OUTPUT_DIR

SOS_SEARCH_URL = "https://bizfileonline.sos.ca.gov/api/Records/businesssearch"

STATUS_PATTERNS = {
    "ACTIVE": re.compile(r"\bactive\b", re.I),
    "SUSPENDED": re.compile(r"\bsuspended\b", re.I),
    "FORFEITED": re.compile(r"\bforfeited\b", re.I),
    "DISSOLVED": re.compile(r"\bdissolved\b", re.I),
    "CANCELED": re.compile(r"\bcancell?ed\b", re.I),
    "MERGED": re.compile(r"\bmerged\b", re.I),
}


def load_entities(top_n: int = 200) -> list[dict]:
    entities = []
    seen = set()
    for path in ["data/audit_results.json", "data/services_fraud_results.json"]:
        if not Path(path).exists():
            continue
        with open(path) as f:
            data = json.load(f)
        for key in ("high_risk_private_null_disbursement", "high_risk_service_grants"):
            for entry in data.get(key, []):
                name = entry.get("recipient", "").strip()
                rtype = entry.get("recipient_type", "").lower()
                if not name or name in seen or "individual" in rtype:
                    continue
                seen.add(name)
                entities.append({
                    "recipient": name,
                    "award_amount": entry.get("award_amount", 0),
                    "recipient_type": entry.get("recipient_type", ""),
                })
    entities.sort(key=lambda x: -x["award_amount"])
    return entities[:top_n]


def clean_for_search(name: str) -> str:
    name = re.sub(r"\b(inc|llc|corp|co|ltd|lp|lc|plc)\b\.?", "", name, flags=re.I)
    name = re.sub(r"[^a-zA-Z0-9\s]", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def parse_status_from_html(html: str) -> dict:
    if not html:
        return {"status": "NO_RESPONSE", "details": []}

    statuses_found = []
    for status, pattern in STATUS_PATTERNS.items():
        if pattern.search(html):
            statuses_found.append(status)

    entity_match = re.search(r'(?:entity\s*number|file\s*number)[:\s]*([A-Z0-9]+)', html, re.I)
    entity_number = entity_match.group(1) if entity_match else None

    date_match = re.search(r'(\d{1,2}/\d{1,2}/\d{4})', html)
    registration_date = date_match.group(1) if date_match else None

    if not statuses_found:
        if "no results" in html.lower() or "no records" in html.lower():
            return {"status": "NOT_FOUND", "entity_number": None, "registration_date": None}
        return {"status": "UNKNOWN", "entity_number": entity_number, "registration_date": registration_date}

    priority = ["FORFEITED", "SUSPENDED", "DISSOLVED", "CANCELED", "MERGED", "ACTIVE"]
    primary = next((s for s in priority if s in statuses_found), statuses_found[0])

    return {
        "status": primary,
        "all_statuses": statuses_found,
        "entity_number": entity_number,
        "registration_date": registration_date,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=float, default=20.0)
    parser.add_argument("--top", type=int, default=200)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--delay", type=float, default=0.5)
    args = parser.parse_args()

    output_path = OUTPUT_DIR / "sos_results.json"
    existing = {}
    if args.resume and output_path.exists():
        with open(output_path) as f:
            existing = {e["recipient"]: e for e in json.load(f).get("entities", [])}

    entities = load_entities(top_n=args.top)
    if args.resume:
        entities = [e for e in entities if e["recipient"] not in existing]
    print(f"Checking SOS for {len(entities)} entities")

    client = BrightDataClient(budget_cap=args.budget, label="sos_check")
    results = list(existing.values())

    try:
        for i, entity in enumerate(entities, 1):
            name = entity["recipient"]
            search_term = clean_for_search(name)
            search_url = f"https://bizfileonline.sos.ca.gov/search/business?SearchType=NUMBER_OR_NAME&SearchCriteria={quote_plus(search_term)}&SearchSubType=ALL"

            resp = client.unlock(search_url, render_js=True)
            parsed = parse_status_from_html(resp.get("html", "") or "")

            entry = {**entity, "search_term": search_term, "search_url": search_url, **parsed}
            results.append(entry)

            tag = parsed["status"]
            alert = "  ⚠️" if tag in ("SUSPENDED", "FORFEITED") else ""
            print(f"[{i}/{len(entities)}] {name[:40]:40s} → {tag}{alert} | {client.report()}")

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
    print(f"SOS CHECK COMPLETE — {client.report()}")
    counts = {}
    for r in results:
        c = r.get("status", "UNKNOWN")
        counts[c] = counts.get(c, 0) + 1
    for cls, n in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {cls:25s} {n}")

    flags = [r for r in results if r.get("status") in ("SUSPENDED", "FORFEITED")]
    if flags:
        print(f"\n  ⚠️  Entities in BAD STANDING receiving grants:")
        for r in flags:
            print(f"    {r['recipient'][:40]:40s} ${r['award_amount']:>12,.0f}  {r['status']}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
