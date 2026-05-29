"""
CA Secretary of State business registry checker (via Bright Data Web Unlocker).

Strategy: hit bizfileonline.sos.ca.gov's internal JSON API directly. That endpoint
returns structured records with status, entity number, and registration date —
much more reliable than scraping the SPA's rendered HTML or relying on Google
SERP guesses.

Falls back to OpenCorporates if the SOS endpoint doesn't return a match.

Reads from data/audit_results.json (READ ONLY).
Writes to data/bright_data/sos_results.json (exclusive).
Also writes data/bright_data/sos_raw/{slug}.json with the raw response per entity
for debugging and audit trail.

Usage:
    # Single-entity sanity check (e.g. settle the Suarez claim)
    python -m src.bright_data.sos_check --only "Suarez Holdings"

    # Full sweep
    python -m src.bright_data.sos_check --budget 20 --top 200
"""

import argparse
import json
import re
import time
from pathlib import Path
from urllib.parse import quote_plus

from src.bright_data.client import BrightDataClient, BudgetExceeded, OUTPUT_DIR

SOS_API_URL = "https://bizfileonline.sos.ca.gov/api/Records/businesssearch"
OPENCORP_URL = "https://opencorporates.com/companies/us_ca"

STATUS_NORMALIZE = {
    "active": "ACTIVE",
    "good standing": "ACTIVE",
    "forfeited": "FORFEITED",
    "ftb forfeited": "FORFEITED",
    "sos/ftb forfeited": "FORFEITED",
    "ftb suspended": "SUSPENDED",
    "sos suspended": "SUSPENDED",
    "suspended": "SUSPENDED",
    "dissolved": "DISSOLVED",
    "cancelled": "CANCELED",
    "canceled": "CANCELED",
    "merged out": "MERGED",
    "surrender": "SURRENDERED",
    "surrendered": "SURRENDERED",
    "terminated": "TERMINATED",
}

RAW_DIR = OUTPUT_DIR / "sos_raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def slug(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", name.lower()).strip("_")
    return s[:80]


def load_entities(top_n: int = 200, only: str = None) -> list[dict]:
    entities = []
    seen = set()
    sources = [
        "data/audit_results.json",
        "data/services_fraud_results.json",
    ]
    for path in sources:
        if not Path(path).exists():
            continue
        with open(path) as f:
            data = json.load(f)
        for key in ("high_risk_private_null_disbursement", "high_risk_service_grants"):
            for entry in data.get(key, []):
                name = entry.get("recipient", "").strip()
                rtype = entry.get("recipient_type", "").lower()
                if not name or name in seen:
                    continue
                if "individual" in rtype and not only:
                    continue
                seen.add(name)
                entities.append({
                    "recipient": name,
                    "award_amount": entry.get("award_amount", 0),
                    "recipient_type": entry.get("recipient_type", ""),
                })

    if only:
        needle = only.lower()
        entities = [e for e in entities if needle in e["recipient"].lower()]
        if not entities:
            entities = [{
                "recipient": only,
                "award_amount": 0,
                "recipient_type": "Manual",
            }]
        return entities

    entities.sort(key=lambda x: -x["award_amount"])
    return entities[:top_n]


def clean_for_search(name: str) -> str:
    n = re.sub(r"\b(inc|llc|corp|co|ltd|lp|lc|plc)\b\.?", "", name, flags=re.I)
    n = re.sub(r"[^a-zA-Z0-9\s&]", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def normalize_status(text: str) -> str:
    if not text:
        return ""
    t = text.lower().strip()
    for k, v in STATUS_NORMALIZE.items():
        if k in t:
            return v
    return t.upper()


def query_sos_api(client: BrightDataClient, name: str) -> dict:
    """Hit bizfileonline's POST API via Web Unlocker. Returns parsed JSON or None."""
    payload_inner = {
        "SEARCH_VALUE": name,
        "SEARCH_FILTER_TYPE_ID": "0",
        "SEARCH_TYPE_ID": "1",
        "FILING_TYPE_ID": "",
        "STATUS_ID": "",
        "FILING_DATE": {"start": None, "end": None},
        "OFFICER_SEARCH_TYPE_ID": None,
        "NUMBER_OF_FILINGS_TO_FETCH": "50",
        "SORT_TYPE_ID": None,
        "SORT_ORDER": None,
        "FETCH_INACTIVE": True,
        "STAKEHOLDER_TYPES": ["INDIVIDUAL", "BUSINESS_ENTITY"],
        "BankruptcyJudgmentSearch": None,
    }
    request_payload = {
        "zone": client.session.headers.get("X-Unlocker-Zone", "realwork_unlocker"),
        "url": SOS_API_URL,
        "method": "POST",
        "format": "raw",
        "data": json.dumps(payload_inner),
        "headers": [
            {"name": "Content-Type", "value": "application/json"},
            {"name": "Accept", "value": "application/json"},
        ],
    }
    # We use unlock() so cost tracking works; pass override via the session
    from src.bright_data.client import ENDPOINT, UNLOCKER_ZONE
    request_payload["zone"] = UNLOCKER_ZONE

    try:
        client._check_budget(client.UNLOCKER_COST)
        r = client.session.post(ENDPOINT, json=request_payload, timeout=60)
        client.spent += client.UNLOCKER_COST
        client._log({"type": "sos_api", "name": name, "status": r.status_code,
                     "size": len(r.content), "cost": client.UNLOCKER_COST})
        if r.ok:
            try:
                return r.json()
            except Exception:
                return {"_raw_text": r.text[:5000]}
        return {"_error": f"http {r.status_code}", "_body": r.text[:500]}
    except Exception as e:
        client._log({"type": "sos_api", "name": name, "error": str(e), "cost": 0})
        return {"_error": str(e)}


def parse_sos_response(resp: dict, target_name: str) -> dict:
    """The SOS API returns a list of matching records under 'rows'."""
    if not resp or "_error" in resp:
        return {"status": "NO_RESPONSE", "error": resp.get("_error") if resp else "no resp"}

    rows = resp.get("rows") or resp.get("Rows") or []
    if not rows and "businessEntities" in resp:
        rows = resp["businessEntities"]

    if not rows:
        return {"status": "NOT_FOUND", "matches": 0}

    target_clean = clean_for_search(target_name).lower()
    best = None
    best_score = 0.0
    for row in rows:
        title = (row.get("TITLE") or row.get("Title") or
                 row.get("entityName") or row.get("title") or "")
        if not title:
            continue
        title_clean = clean_for_search(title).lower()
        if title_clean == target_clean:
            score = 1.0
        elif target_clean in title_clean or title_clean in target_clean:
            score = 0.8
        else:
            overlap = set(target_clean.split()) & set(title_clean.split())
            score = len(overlap) / max(len(target_clean.split()), 1)
        if score > best_score:
            best_score = score
            best = row

    if not best or best_score < 0.5:
        return {"status": "NO_GOOD_MATCH", "matches": len(rows),
                "candidates": [(r.get("TITLE") or r.get("Title") or "")[:60] for r in rows[:5]]}

    raw_status = (best.get("STATUS") or best.get("Status") or
                  best.get("entityStatus") or "")
    entity_num = (best.get("ENTITY_NUM") or best.get("EntityNumber") or
                  best.get("entityNumber") or best.get("FILE_NUMBER") or "")
    reg_date = (best.get("FILING_DATE") or best.get("FilingDate") or
                best.get("filingDate") or "")
    entity_type = (best.get("ENTITY_TYPE") or best.get("EntityType") or "")

    return {
        "status": normalize_status(raw_status) or "UNKNOWN",
        "raw_status": raw_status,
        "entity_number": entity_num,
        "registration_date": reg_date,
        "entity_type": entity_type,
        "matched_title": (best.get("TITLE") or best.get("Title") or
                          best.get("entityName") or ""),
        "match_score": round(best_score, 2),
        "total_matches": len(rows),
    }


def query_opencorporates(client: BrightDataClient, name: str) -> dict:
    """Fallback when SOS API misses — OpenCorporates often has the same data."""
    search = clean_for_search(name)
    url = f"{OPENCORP_URL}?q={quote_plus(search)}"
    resp = client.unlock(url, render_js=False)
    if not resp.get("html"):
        return {"status": "OPENCORP_NO_RESPONSE"}

    html = resp["html"].lower()
    if "no companies found" in html or "0 companies" in html:
        return {"status": "OPENCORP_NOT_FOUND"}

    for key in ["dissolved", "forfeited", "suspended", "cancelled",
                "canceled", "inactive", "active"]:
        if key in html:
            return {"status": normalize_status(key), "source": "opencorporates"}
    return {"status": "OPENCORP_INCONCLUSIVE", "source": "opencorporates"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=float, default=20.0)
    parser.add_argument("--top", type=int, default=200)
    parser.add_argument("--only", default=None,
                        help="Substring match — check just one entity (e.g. 'Suarez')")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--delay", type=float, default=0.5)
    parser.add_argument("--fallback-opencorp", action="store_true",
                        help="Also try OpenCorporates if SOS API doesn't match")
    args = parser.parse_args()

    output_path = OUTPUT_DIR / "sos_results.json"
    existing = {}
    if args.resume and output_path.exists():
        with open(output_path) as f:
            existing = {e["recipient"]: e for e in json.load(f).get("entities", [])}

    entities = load_entities(top_n=args.top, only=args.only)
    if args.resume:
        entities = [e for e in entities if e["recipient"] not in existing]

    if not entities:
        print("No entities to check.")
        return

    print(f"Checking SOS for {len(entities)} entities")
    client = BrightDataClient(budget_cap=args.budget, label="sos_check")
    results = list(existing.values())

    try:
        for i, entity in enumerate(entities, 1):
            name = entity["recipient"]
            search_term = clean_for_search(name)

            raw = query_sos_api(client, search_term)
            parsed = parse_sos_response(raw, name)
            source = "sos_api"

            if (args.fallback_opencorp and
                parsed["status"] in ("NOT_FOUND", "NO_GOOD_MATCH", "NO_RESPONSE")):
                fb = query_opencorporates(client, name)
                if fb.get("status") not in ("OPENCORP_NO_RESPONSE", "OPENCORP_NOT_FOUND",
                                            "OPENCORP_INCONCLUSIVE"):
                    parsed = fb
                    source = "opencorporates"

            raw_path = RAW_DIR / f"{slug(name)}.json"
            with open(raw_path, "w") as f:
                json.dump({"query": search_term, "response": raw}, f, indent=2)

            entry = {**entity, "search_term": search_term, "source": source, **parsed}
            results.append(entry)

            tag = parsed["status"]
            alert = "  ⚠️" if tag in ("SUSPENDED", "FORFEITED", "DISSOLVED") else ""
            safe_name = name.encode("ascii", "ignore").decode("ascii")
            print(f"[{i}/{len(entities)}] {safe_name[:40]:40s} -> {tag}{alert} | {client.report()}")

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

    flags = [r for r in results if r.get("status") in ("SUSPENDED", "FORFEITED", "DISSOLVED")]
    if flags:
        print(f"\n  ⚠️  Entities in BAD STANDING receiving grants:")
        for r in flags:
            print(f"    {r['recipient'][:40]:40s} ${r['award_amount']:>12,.0f}  {r['status']}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
