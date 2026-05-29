"""
Lead News Check — quick SERP sweep for press coverage of our top patterns.

We want to know if our DGS lead vendors (especially Panini Time) have
prior press coverage. If yes, we either cite it (strengthens finding) or
back off (someone already explained the pattern).

Reads from data/dgs/split_contract_dossiers/ — pulls every STRONG vendor.
Writes data/dgs/news_check_results.json + a tight summary in stdout.

Cost: ~$0.02 per vendor (3-4 SERP queries each).

Usage:
    python -m src.dgs.lead_news_check --budget 1
"""

import argparse
import json
from pathlib import Path

from src.bright_data.client import BrightDataClient

QUERY_TEMPLATES = [
    '"{vendor}" California state contract',
    '"{vendor}" {buyer} investigation OR audit',
    '"{vendor}" California Cal Fire procurement',
    '"{vendor}" lawsuit OR settlement OR debarred',
]

OUTPUT_DIR = Path("data/dgs")
RESULTS_PATH = OUTPUT_DIR / "news_check_results.json"


def load_strong_vendors() -> list[dict]:
    dossier_dir = Path("data/dgs/split_contract_dossiers")
    if not dossier_dir.exists():
        return []
    out = []
    for p in dossier_dir.glob("*.json"):
        with open(p) as f:
            d = json.load(f)
        if d.get("analysis", {}).get("verdict") == "STRONG_SPLIT_CONTRACT_PATTERN":
            top_buyer = ""
            buyers = d["analysis"].get("near_threshold_buyer_breakdown") or []
            if buyers:
                top_buyer = buyers[0]["buyer"]
            out.append({"vendor": d["vendor"], "buyer": top_buyer})
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=float, default=1.0)
    args = parser.parse_args()

    vendors = load_strong_vendors()
    if not vendors:
        print("No STRONG_SPLIT_CONTRACT_PATTERN dossiers. "
              "Run split_contract_deepdive first.")
        return

    print(f"Checking news coverage for {len(vendors)} lead vendors...")
    client = BrightDataClient(budget_cap=args.budget, label="lead_news_check")

    results = []
    for i, v in enumerate(vendors, 1):
        vendor = v["vendor"]
        buyer = v["buyer"]
        print(f"\n[{i}/{len(vendors)}] {vendor}")
        queries = []
        for template in QUERY_TEMPLATES:
            q = template.format(vendor=vendor, buyer=buyer)
            r = client.serp(q)
            organic = r.get("organic", [])
            top_results = [
                {"title": o.get("title", "")[:120],
                 "snippet": o.get("description", "")[:200],
                 "url": o.get("link", "")}
                for o in organic[:3]
            ]
            queries.append({
                "query": q,
                "result_count": len(organic),
                "top_results": top_results,
            })
            print(f"  {q[:60]:60s} -> {len(organic)} results")

        results.append({
            "vendor": vendor,
            "buyer": buyer,
            "queries": queries,
            "total_results": sum(q["result_count"] for q in queries),
        })

    with open(RESULTS_PATH, "w") as f:
        json.dump({"vendors_checked": len(results), "results": results,
                   "spent": client.spent}, f, indent=2)

    print(f"\n{'='*60}")
    print(f"LEAD NEWS CHECK COMPLETE — {client.report()}")
    for r in results:
        verdict = ("NO COVERAGE" if r["total_results"] == 0 else
                   "COVERAGE FOUND" if r["total_results"] >= 5 else
                   "LOW COVERAGE")
        print(f"  {r['vendor'][:35]:35s} -> {verdict} ({r['total_results']} hits)")
    print(f"\n  Detailed: {RESULTS_PATH}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
