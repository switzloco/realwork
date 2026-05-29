"""
DGS Split-Contract Deep Dive — verify whether just-under-threshold clusters
are the textbook split-contract pattern or just coincidence.

For each vendor flagged in data/dgs/po_anomalies.json under
'just_under_threshold', we pull every PO they got and check:

  1. Same-buyer cluster: how many of the just-under POs went to ONE buyer?
     (Same-buyer = same decision-maker = stronger intent signal)
  2. Same-week cluster: were the POs issued close in time?
     (Splitting one need = same week; ongoing relationship = spread out)
  3. Same-description: do the descriptions suggest related scope?
     (Same job split = same description; different jobs = different descriptions)
  4. Total dollars at risk: vendor's lifetime total from the buyer

Then enriches with Bright Data SERP + Web Unlocker on the vendor name to
answer: does this vendor exist? News mentions? Other state contracts?
Officers? Address (residential vs commercial)?

Output: data/dgs/split_contract_dossiers/{slug}.json + a summary markdown.

Cost: ~$0.05 per vendor dossier with Bright Data (3 SERP queries + 1 unlock).

Usage:
    python -m src.dgs.split_contract_deepdive --top 10
    python -m src.dgs.split_contract_deepdive --top 10 --use-brightdata --budget 5
"""

import argparse
import json
import os
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

CKAN_BASE = "https://data.ca.gov/api/3/action/datastore_search"
RESOURCE_ID = os.environ.get("DGS_PO_RESOURCE_ID", "")

OUTPUT_DIR = Path("data/dgs/split_contract_dossiers")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def slug(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", s.lower()).strip("_")[:60]


def load_flagged_vendors() -> list[dict]:
    path = Path("data/dgs/po_anomalies.json")
    if not path.exists():
        print(f"Need {path} — run src.dgs.purchase_orders first")
        return []
    with open(path) as f:
        data = json.load(f)
    return data.get("just_under_threshold", [])


def fetch_vendor_pos(vendor: str, fields_only: bool = False) -> pd.DataFrame:
    """Pull every PO record matching the vendor name from CKAN."""
    if not RESOURCE_ID:
        return pd.DataFrame()
    rows, offset = [], 0
    while True:
        r = requests.get(CKAN_BASE, params={
            "resource_id": RESOURCE_ID,
            "limit": 500,
            "offset": offset,
            "q": vendor,
        }, timeout=60)
        r.raise_for_status()
        records = r.json()["result"]["records"]
        if not records:
            break
        # CKAN q-search is fuzzy; filter to exact vendor name match
        records = [
            r for r in records
            if any(vendor.lower() in str(v).lower()
                   for k, v in r.items() if "supplier" in k.lower() or "vendor" in k.lower())
        ]
        rows.extend(records)
        offset += 500
        if offset > 5000:
            break
    return pd.DataFrame(rows)


def normalize_po_df(df: pd.DataFrame) -> pd.DataFrame:
    col_map = {}
    for c in df.columns:
        cl = c.lower().strip()
        if cl == "supplier name" or ("supplier" in cl and "name" in cl):
            col_map[c] = "vendor"
        elif cl == "department name" or "department" in cl:
            col_map[c] = "buyer"
        elif cl == "total price" or cl == "amount" or "total" in cl:
            if "amount" not in col_map.values():
                col_map[c] = "amount"
        elif cl == "item description" or "description" in cl:
            if "description" not in col_map.values():
                col_map[c] = "description"
        elif "purchase order number" in cl:
            col_map[c] = "po_id"
        elif "purchase date" in cl or (cl == "date"):
            if "date" not in col_map.values():
                col_map[c] = "date"
        elif "fiscal year" in cl:
            col_map[c] = "fiscal_year"
    df = df.rename(columns=col_map)
    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(
            df["amount"].astype(str).str.replace(r"[^\d.]", "", regex=True),
            errors="coerce",
        )
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df


def analyze_cluster(df: pd.DataFrame, threshold: int, band: int = 100) -> dict:
    """Cluster analysis: same-buyer, same-week, same-scope?"""
    if df.empty:
        return {"po_count": 0}

    band_lo, band_hi = threshold - band, threshold
    near = df[(df["amount"] >= band_lo) & (df["amount"] <= band_hi)] if "amount" in df else df

    result = {
        "total_pos_in_dataset": len(df),
        "near_threshold_count": len(near),
        "threshold": threshold,
        "total_lifetime_value": float(df["amount"].sum()) if "amount" in df else 0,
        "near_threshold_value": float(near["amount"].sum()) if "amount" in near else 0,
    }

    if near.empty:
        return result

    # Buyer concentration in the near-threshold set
    if "buyer" in near.columns:
        buyer_counts = near["buyer"].value_counts()
        result["near_threshold_buyer_breakdown"] = [
            {"buyer": str(b), "count": int(c),
             "share": round(c / len(near), 3)}
            for b, c in buyer_counts.head(5).items()
        ]
        top_buyer_share = buyer_counts.iloc[0] / len(near) if len(buyer_counts) else 0
        result["single_buyer_concentration"] = round(float(top_buyer_share), 3)

    # Date clustering
    if "date" in near.columns and near["date"].notna().any():
        dates = near["date"].dropna().sort_values()
        if len(dates) >= 2:
            span_days = (dates.iloc[-1] - dates.iloc[0]).days
            result["date_span_days"] = int(span_days)
            result["first_po_date"] = str(dates.iloc[0].date())
            result["last_po_date"] = str(dates.iloc[-1].date())
            # Count within any 7-day window
            same_week = 0
            for d in dates:
                window = dates[(dates >= d) & (dates <= d + pd.Timedelta(days=7))]
                same_week = max(same_week, len(window))
            result["max_same_week_count"] = int(same_week)

    # Description similarity
    if "description" in near.columns:
        descs = near["description"].dropna().astype(str).str.lower().str.strip()
        if len(descs):
            most_common = Counter(descs).most_common(3)
            result["near_threshold_top_descriptions"] = [
                {"description": d[:200], "count": c} for d, c in most_common
            ]

    # PO IDs for paper-trail
    if "po_id" in near.columns:
        result["near_threshold_po_ids"] = [
            str(p) for p in near["po_id"].dropna().head(20).tolist()
        ]

    # Suspicion score
    score = 0
    factors = []
    if result.get("single_buyer_concentration", 0) >= 0.75:
        score += 3
        factors.append("single buyer issued >=75% of near-threshold POs")
    if result.get("max_same_week_count", 0) >= 3:
        score += 2
        factors.append(f"{result['max_same_week_count']} POs in a single 7-day window")
    top_desc = result.get("near_threshold_top_descriptions", [])
    if top_desc and top_desc[0]["count"] >= 3:
        score += 2
        factors.append(f"same description used {top_desc[0]['count']}+ times")
    if result["near_threshold_count"] >= 5:
        score += 1
        factors.append(f"{result['near_threshold_count']} POs in the just-under band")

    result["suspicion_score"] = score
    result["suspicion_factors"] = factors
    if score >= 5:
        result["verdict"] = "STRONG_SPLIT_CONTRACT_PATTERN"
    elif score >= 3:
        result["verdict"] = "POSSIBLE_SPLIT_CONTRACT"
    else:
        result["verdict"] = "INCONCLUSIVE_OR_LIKELY_BENIGN"

    return result


def enrich_via_brightdata(vendor: str, client) -> dict:
    """SERP + Web Unlocker pass on the vendor name. Optional."""
    enrichment = {"vendor": vendor}
    queries = [
        f'"{vendor}" California',
        f'"{vendor}" lawsuit OR settlement OR debarred',
        f'"{vendor}" linkedin OR opencorporates',
    ]
    serp_summary = []
    for q in queries:
        r = client.serp(q)
        organics = r.get("organic", [])[:3]
        serp_summary.append({
            "query": q,
            "result_count": len(r.get("organic", [])),
            "top_results": [
                {"title": o.get("title", ""), "link": o.get("link", "")}
                for o in organics
            ],
        })
    enrichment["serp"] = serp_summary
    return enrichment


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=10,
                        help="How many flagged vendors to deep-dive")
    parser.add_argument("--use-brightdata", action="store_true")
    parser.add_argument("--budget", type=float, default=5.0)
    args = parser.parse_args()

    flagged = load_flagged_vendors()
    if not flagged:
        return

    flagged = flagged[:args.top]
    print(f"Deep-diving {len(flagged)} just-under-threshold vendors...")

    bd_client = None
    if args.use_brightdata:
        from src.bright_data.client import BrightDataClient
        bd_client = BrightDataClient(budget_cap=args.budget, label="split_deepdive")

    dossiers = []
    for i, flag in enumerate(flagged, 1):
        vendor = flag["vendor"]
        threshold = flag["threshold"]
        print(f"\n[{i}/{len(flagged)}] {vendor} (threshold ${threshold:,})")

        po_df = fetch_vendor_pos(vendor)
        if po_df.empty:
            print(f"  No POs returned from CKAN — skipping")
            continue
        po_df = normalize_po_df(po_df)
        print(f"  Pulled {len(po_df)} POs total")

        analysis = analyze_cluster(po_df, threshold)
        print(f"  Verdict: {analysis.get('verdict', '?')} "
              f"(score {analysis.get('suspicion_score', 0)})")
        for f in analysis.get("suspicion_factors", []):
            print(f"    - {f}")

        dossier = {
            "vendor": vendor,
            "flagged_threshold": threshold,
            "analysis": analysis,
        }

        if bd_client:
            try:
                dossier["enrichment"] = enrich_via_brightdata(vendor, bd_client)
                print(f"  {bd_client.report()}")
            except Exception as e:
                print(f"  Bright Data enrichment failed: {e}")

        with open(OUTPUT_DIR / f"{slug(vendor)}.json", "w") as f:
            json.dump(dossier, f, indent=2, default=str)
        dossiers.append(dossier)

    # Summary report
    strong = [d for d in dossiers
              if d["analysis"].get("verdict") == "STRONG_SPLIT_CONTRACT_PATTERN"]
    possible = [d for d in dossiers
                if d["analysis"].get("verdict") == "POSSIBLE_SPLIT_CONTRACT"]

    lines = ["# DGS Split-Contract Deep Dive\n",
             f"Generated: {datetime.utcnow().isoformat()} UTC\n",
             f"Vendors analyzed: **{len(dossiers)}**",
             f"- Strong split-contract pattern: **{len(strong)}**",
             f"- Possible split-contract: **{len(possible)}**\n"]

    if strong:
        lines.append("## Strong Pattern (highest priority)\n")
        for d in strong:
            a = d["analysis"]
            lines.append(f"### {d['vendor']}")
            lines.append(f"- Threshold: ${d['flagged_threshold']:,}")
            lines.append(f"- POs just under threshold: {a['near_threshold_count']} "
                         f"(value ${a['near_threshold_value']:,.0f})")
            lines.append(f"- Lifetime PO value: ${a['total_lifetime_value']:,.0f}")
            lines.append(f"- Single-buyer concentration: "
                         f"{a.get('single_buyer_concentration', 0)*100:.0f}%")
            lines.append(f"- Date span: {a.get('date_span_days', '?')} days, "
                         f"max same-week count: {a.get('max_same_week_count', '?')}")
            lines.append(f"- Suspicion factors:")
            for f in a.get("suspicion_factors", []):
                lines.append(f"  - {f}")
            buyers = a.get("near_threshold_buyer_breakdown", [])
            if buyers:
                lines.append(f"- Top buyer: {buyers[0]['buyer']} "
                             f"({buyers[0]['count']} POs)")
            descs = a.get("near_threshold_top_descriptions", [])
            if descs:
                lines.append(f"- Most common description: \"{descs[0]['description'][:80]}\" "
                             f"({descs[0]['count']}x)")
            lines.append("")

    if possible:
        lines.append("\n## Possible Pattern (review)\n")
        for d in possible:
            a = d["analysis"]
            lines.append(f"- **{d['vendor']}** — {a['near_threshold_count']} POs at "
                         f"~${d['flagged_threshold']:,}, "
                         f"buyer concentration "
                         f"{a.get('single_buyer_concentration', 0)*100:.0f}%")

    with open(OUTPUT_DIR.parent / "split_contract_report.md", "w") as f:
        f.write("\n".join(lines))

    print(f"\n{'='*60}")
    print(f"SPLIT-CONTRACT DEEP DIVE COMPLETE")
    print(f"  Strong pattern: {len(strong)}")
    print(f"  Possible: {len(possible)}")
    print(f"  Report: data/dgs/split_contract_report.md")
    if bd_client:
        print(f"  {bd_client.report()}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
