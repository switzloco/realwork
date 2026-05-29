"""
Bulk SERP Scanner — runs multi-query Google searches on every high-risk entity.

For each entity in the high-risk list, runs 5 query variants:
  1. "name" California                       (general existence)
  2. "name" lawsuit OR settlement OR fraud   (prior litigation)
  3. "name" indicted OR convicted OR debarred (criminal/enforcement)
  4. "name" linkedin                         (employee presence)
  5. "name" site:bbb.org OR site:dnb.com     (business directories)

Classifies each entity:
  - GHOST: 0 organic results across all queries  → strongest signal
  - SHALLOW: <3 organic results total            → weak web presence
  - FLAGGED: any litigation/enforcement hit      → review priority
  - NORMAL: multiple organic results, no flags

Reads from data/audit_results.json (Antigravity may regenerate this — we
only READ it, never write).

Writes to data/bright_data/bulk_serp_results.json — exclusive to this script.

Usage:
    python -m src.bright_data.bulk_serp --budget 50 --top 200
    python -m src.bright_data.bulk_serp --resume     # skip entities already scanned
"""

import argparse
import json
import time
from pathlib import Path

from src.bright_data.client import BrightDataClient, BudgetExceeded, OUTPUT_DIR

LITIGATION_TERMS = ["lawsuit", "settlement", "fraud", "false claims"]
ENFORCEMENT_TERMS = ["indicted", "convicted", "debarred", "suspended", "investigation"]

QUERY_TEMPLATES = [
    ('existence', '"{name}" California'),
    ('litigation', '"{name}" (lawsuit OR settlement OR "false claims")'),
    ('enforcement', '"{name}" (indicted OR convicted OR debarred)'),
    ('linkedin', '"{name}" linkedin'),
    ('directory', '"{name}" (site:bbb.org OR site:dnb.com OR site:opencorporates.com)'),
]


def load_high_risk(top_n: int = 200) -> list[dict]:
    candidates = [
        "data/audit_results.json",
        "data/services_fraud_results.json",
    ]
    entities = []
    seen = set()

    for path in candidates:
        if not Path(path).exists():
            continue
        with open(path) as f:
            data = json.load(f)

        for key in ("high_risk_private_null_disbursement", "high_risk_service_grants"):
            for entry in data.get(key, []):
                name = entry.get("recipient", "").strip()
                if not name or name in seen or name.lower() == "unknown":
                    continue
                seen.add(name)
                entities.append({
                    "recipient": name,
                    "award_amount": entry.get("award_amount", 0),
                    "grant_title": entry.get("grant_title", ""),
                    "funding_source": entry.get("funding_source", ""),
                    "source_file": path,
                })

    entities.sort(key=lambda x: -x["award_amount"])
    return entities[:top_n]


def load_existing_results(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path) as f:
        return {e["recipient"]: e for e in json.load(f).get("entities", [])}


def classify(query_results: dict) -> dict:
    total_organic = sum(len(r.get("organic", [])) for r in query_results.values())
    litigation_hits = []
    enforcement_hits = []

    for query_type, result in query_results.items():
        for organic in result.get("organic", []):
            snippet = (organic.get("description", "") + " " + organic.get("title", "")).lower()
            if query_type == "litigation":
                hits = [t for t in LITIGATION_TERMS if t in snippet]
                if hits:
                    litigation_hits.append({"snippet": snippet[:200], "terms": hits,
                                            "url": organic.get("link", "")})
            if query_type == "enforcement":
                hits = [t for t in ENFORCEMENT_TERMS if t in snippet]
                if hits:
                    enforcement_hits.append({"snippet": snippet[:200], "terms": hits,
                                             "url": organic.get("link", "")})

    if total_organic == 0:
        classification = "GHOST"
    elif enforcement_hits:
        classification = "FLAGGED_ENFORCEMENT"
    elif litigation_hits:
        classification = "FLAGGED_LITIGATION"
    elif total_organic < 3:
        classification = "SHALLOW"
    else:
        classification = "NORMAL"

    return {
        "classification": classification,
        "total_organic": total_organic,
        "litigation_hits": litigation_hits,
        "enforcement_hits": enforcement_hits,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=float, default=50.0, help="Max spend in dollars")
    parser.add_argument("--top", type=int, default=200, help="Top N entities to scan")
    parser.add_argument("--resume", action="store_true", help="Skip entities already in results file")
    parser.add_argument("--delay", type=float, default=0.5, help="Seconds between requests")
    args = parser.parse_args()

    output_path = OUTPUT_DIR / "bulk_serp_results.json"
    existing = load_existing_results(output_path) if args.resume else {}

    entities = load_high_risk(top_n=args.top)
    print(f"Loaded {len(entities)} high-risk entities")
    if args.resume:
        entities = [e for e in entities if e["recipient"] not in existing]
        print(f"  Resume mode: {len(entities)} remaining ({len(existing)} already done)")

    client = BrightDataClient(budget_cap=args.budget, label="bulk_serp")
    results = list(existing.values())

    try:
        for i, entity in enumerate(entities, 1):
            name = entity["recipient"]
            query_results = {}
            for query_type, template in QUERY_TEMPLATES:
                query = template.format(name=name)
                query_results[query_type] = client.serp(query)
                time.sleep(args.delay)

            cls = classify(query_results)
            entry = {**entity, **cls, "queries": list(query_results.keys())}
            results.append(entry)

            tag = cls["classification"]
            print(f"[{i}/{len(entities)}] {name[:40]:40s} -> {tag} ({cls['total_organic']} hits) | {client.report()}")

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
    print(f"BULK SERP SCAN COMPLETE — {client.report()}")
    print(f"  Entities scanned: {len(results)}")
    counts = {}
    for r in results:
        c = r.get("classification", "UNKNOWN")
        counts[c] = counts.get(c, 0) + 1
    for cls, n in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {cls:25s} {n}")

    flagged = [r for r in results if r.get("classification", "").startswith("FLAGGED")]
    if flagged:
        print(f"\n  FLAGGED entities (litigation/enforcement hits):")
        for r in flagged[:20]:
            safe_name = r["recipient"].encode('ascii', 'ignore').decode('ascii')
            print(f"    {safe_name[:40]:40s} ${r['award_amount']:>12,.0f}  {r['classification']}")

    ghosts = [r for r in results if r.get("classification") == "GHOST"]
    if ghosts:
        print(f"\n  GHOST entities (zero web presence):")
        for r in ghosts[:20]:
            print(f"    {r['recipient'][:40]:40s} ${r['award_amount']:>12,.0f}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
