"""
DGS Purchase Order Scanner — Looking for non-grant procurement fraud.

The CA Department of General Services publishes purchase order data on
data.ca.gov. This is sole-source contracts, no-bid awards, and professional
services — where the Caltrans bid-rigging case actually lived.

Patterns we look for:
  1. Buyer concentration — buyer issuing >75% of POs to a single vendor
  2. Vendor concentration — vendor winning 5+ POs from the same buyer
  3. Repeating-amount fraud — exact same dollar amount across many POs
     (often indicates split contracts to dodge approval thresholds)
  4. Just-under-threshold clustering — POs at $4,999 / $9,999 / $49,999
     (the $5K and $50K marks are common DGS approval thresholds)
  5. Generic descriptions — "services," "miscellaneous," "as needed"
     (no real deliverable to verify against)

Data source: https://data.ca.gov/dataset/purchase-order-data
Resource IDs vary by fiscal year — set DGS_PO_RESOURCE_ID in .env.

Usage:
    python -m src.dgs.purchase_orders --source api          # via CKAN
    python -m src.dgs.purchase_orders --source csv          # from data/dgs_po.csv

Writes:
    data/dgs/po_anomalies.json
    data/dgs/po_anomalies.md
"""

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = Path("data/dgs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CKAN_BASE = "https://data.ca.gov/api/3/action/datastore_search"
RESOURCE_ID = os.environ.get("DGS_PO_RESOURCE_ID", "")

DGS_THRESHOLDS = [4999, 9999, 24999, 49999, 99999]
NEAR_THRESHOLD_BAND = 100  # within $100 of threshold = "just under"

VAGUE_DESCRIPTION_TERMS = [
    "services", "miscellaneous", "as needed", "on-call", "various",
    "general", "professional services", "consulting services",
]


def fetch_from_api(limit: int = 50000) -> pd.DataFrame:
    if not RESOURCE_ID:
        print("DGS_PO_RESOURCE_ID not set in .env")
        sys.exit(1)
    rows, offset = [], 0
    while len(rows) < limit:
        r = requests.get(CKAN_BASE, params={
            "resource_id": RESOURCE_ID, "limit": 500, "offset": offset,
        }, timeout=60)
        r.raise_for_status()
        records = r.json()["result"]["records"]
        if not records:
            break
        rows.extend(records)
        offset += 500
        if offset % 5000 == 0:
            print(f"  {len(rows)} POs...")
    return pd.DataFrame(rows)


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    col_map = {}
    # First pass: try to get exact/best matches
    for c in df.columns:
        cl = c.lower().strip()
        if cl == "supplier name":
            col_map[c] = "vendor"
        elif cl == "department name":
            col_map[c] = "buyer"
        elif cl == "total price":
            col_map[c] = "amount"
        elif cl == "item description":
            col_map[c] = "description"
        elif cl == "purchase order number":
            col_map[c] = "po_id"
        elif cl == "purchase date":
            col_map[c] = "date"

    # Second pass: fallback fuzzy matching, ensuring uniqueness
    for c in df.columns:
        if c in col_map:
            continue
        cl = c.lower().strip()
        if "supplier" in cl or "vendor" in cl or "payee" in cl:
            if "vendor" not in col_map.values():
                col_map[c] = "vendor"
        elif "purchaser" in cl or "buyer" in cl or "department" in cl:
            if "buyer" not in col_map.values():
                col_map[c] = "buyer"
        elif "amount" in cl or "total" in cl:
            if "amount" not in col_map.values():
                col_map[c] = "amount"
        elif "description" in cl or "item" in cl or "purpose" in cl:
            if "description" not in col_map.values():
                col_map[c] = "description"
        elif "po" in cl and ("number" in cl or "id" in cl):
            if "po_id" not in col_map.values():
                col_map[c] = "po_id"
        elif "date" in cl:
            if "date" not in col_map.values():
                col_map[c] = "date"

    df = df.rename(columns=col_map)
    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(
            df["amount"].astype(str).str.replace(r"[^\d.]", "", regex=True),
            errors="coerce",
        )
    return df


def find_anomalies(df: pd.DataFrame) -> dict:
    results = {
        "total_records": len(df),
        "total_value": float(df["amount"].sum()) if "amount" in df.columns else 0,
    }

    # 1. Buyer-vendor concentration
    if "buyer" in df.columns and "vendor" in df.columns:
        bv = df.groupby(["buyer", "vendor"]).agg(
            po_count=("amount", "count"),
            total_value=("amount", "sum"),
        ).reset_index()
        buyer_totals = df.groupby("buyer")["amount"].sum().to_dict()
        bv["buyer_total"] = bv["buyer"].map(buyer_totals)
        bv["share_of_buyer"] = bv["total_value"] / bv["buyer_total"]

        concentrated = bv[(bv["share_of_buyer"] >= 0.75) &
                          (bv["po_count"] >= 3) &
                          (bv["total_value"] >= 50_000)]
        concentrated = concentrated.sort_values("total_value", ascending=False)

        results["buyer_vendor_concentration"] = [
            {
                "buyer": str(r["buyer"]),
                "vendor": str(r["vendor"]),
                "po_count": int(r["po_count"]),
                "total_value": float(r["total_value"]),
                "share_of_buyer_spend": round(float(r["share_of_buyer"]), 3),
            }
            for _, r in concentrated.head(50).iterrows()
        ]

        # Repeat winners — vendors getting 10+ POs from any one buyer
        repeats = bv[bv["po_count"] >= 10].sort_values("total_value", ascending=False)
        results["repeat_winners"] = [
            {"buyer": str(r["buyer"]), "vendor": str(r["vendor"]),
             "po_count": int(r["po_count"]), "total_value": float(r["total_value"])}
            for _, r in repeats.head(50).iterrows()
        ]

    # 2. Just-under-threshold POs
    if "amount" in df.columns:
        near_threshold = []
        for t in DGS_THRESHOLDS:
            band = df[(df["amount"] >= t - NEAR_THRESHOLD_BAND) &
                      (df["amount"] <= t)]
            if len(band) >= 3:
                # Group by vendor to find serial dodgers
                by_vendor = band.groupby("vendor").size().sort_values(ascending=False)
                serial = by_vendor[by_vendor >= 2]
                for vendor, count in serial.items():
                    near_threshold.append({
                        "vendor": str(vendor),
                        "threshold": t,
                        "po_count_in_band": int(count),
                        "example_amounts": [
                            float(a) for a in
                            band[band["vendor"] == vendor]["amount"].tolist()[:5]
                        ],
                    })
        results["just_under_threshold"] = sorted(
            near_threshold, key=lambda x: -x["po_count_in_band"]
        )[:50]

    # 3. Repeating exact amounts
    if "amount" in df.columns and "vendor" in df.columns:
        repeating = []
        for vendor, group in df.groupby("vendor"):
            if len(group) < 3:
                continue
            amt_counts = group["amount"].value_counts()
            for amt, count in amt_counts.items():
                if count >= 3 and amt >= 5000:
                    repeating.append({
                        "vendor": str(vendor),
                        "exact_amount": float(amt),
                        "po_count": int(count),
                        "total": float(amt * count),
                    })
        repeating.sort(key=lambda x: -x["total"])
        results["repeating_amounts"] = repeating[:50]

    # 4. Vague descriptions
    if "description" in df.columns:
        df["desc_lower"] = df["description"].astype(str).str.lower()
        vague = df[df["desc_lower"].apply(
            lambda d: isinstance(d, str) and any(t in d for t in VAGUE_DESCRIPTION_TERMS) and len(d) < 60
        )]
        if "amount" in vague.columns:
            vague = vague[vague["amount"] >= 25_000]
            top_vague = vague.sort_values("amount", ascending=False).head(50)
            results["vague_high_value_pos"] = [
                {
                    "vendor": str(r.get("vendor", "")),
                    "buyer": str(r.get("buyer", "")),
                    "amount": float(r.get("amount", 0)),
                    "description": str(r.get("description", ""))[:200],
                }
                for _, r in top_vague.iterrows()
            ]

    return results


def write_report(results: dict):
    lines = ["# DGS Purchase Order Anomalies\n"]
    lines.append(f"- Records analyzed: {results['total_records']:,}")
    lines.append(f"- Total value: ${results['total_value']:,.0f}\n")

    if results.get("buyer_vendor_concentration"):
        lines.append("## Buyer-Vendor Concentration (>=75% of buyer's spend)\n")
        lines.append("| Buyer | Vendor | POs | Total | Share |")
        lines.append("|-------|--------|-----|-------|-------|")
        for r in results["buyer_vendor_concentration"][:30]:
            lines.append(f"| {r['buyer'][:30]} | {r['vendor'][:30]} | {r['po_count']} "
                         f"| ${r['total_value']:,.0f} | {r['share_of_buyer_spend']*100:.0f}% |")

    if results.get("just_under_threshold"):
        lines.append("\n## Just-Under-Threshold Clusters (split-contract pattern)\n")
        lines.append("| Vendor | Threshold | Count | Example amounts |")
        lines.append("|--------|-----------|-------|-----------------|")
        for r in results["just_under_threshold"][:30]:
            amts = ", ".join(f"${a:,.0f}" for a in r["example_amounts"][:3])
            lines.append(f"| {r['vendor'][:35]} | ${r['threshold']:,} "
                         f"| {r['po_count_in_band']} | {amts} |")

    if results.get("repeating_amounts"):
        lines.append("\n## Repeating Exact-Amount POs (round-tripping pattern)\n")
        lines.append("| Vendor | Amount | Count | Total |")
        lines.append("|--------|--------|-------|-------|")
        for r in results["repeating_amounts"][:30]:
            lines.append(f"| {r['vendor'][:35]} | ${r['exact_amount']:,.0f} "
                         f"| {r['po_count']} | ${r['total']:,.0f} |")

    if results.get("vague_high_value_pos"):
        lines.append("\n## Vague High-Value POs (no real deliverable)\n")
        lines.append("| Vendor | Buyer | Amount | Description |")
        lines.append("|--------|-------|--------|-------------|")
        for r in results["vague_high_value_pos"][:30]:
            lines.append(f"| {r['vendor'][:25]} | {r['buyer'][:25]} "
                         f"| ${r['amount']:,.0f} | {r['description'][:50]} |")

    with open(OUTPUT_DIR / "po_anomalies.md", "w") as f:
        f.write("\n".join(lines))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", choices=["api", "csv"], default="api")
    parser.add_argument("--csv-path", default="data/dgs_po.csv")
    args = parser.parse_args()

    if args.source == "csv":
        df = pd.read_csv(args.csv_path, low_memory=False)
    else:
        df = fetch_from_api()
    print(f"Loaded {len(df)} POs, {len(df.columns)} columns")

    df = normalize(df)
    print(f"Normalized. Has columns: {sorted(set(df.columns))[:15]}...")

    results = find_anomalies(df)
    with open(OUTPUT_DIR / "po_anomalies.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    write_report(results)

    print(f"\n{'='*60}")
    print(f"DGS PO SCAN COMPLETE")
    print(f"  Buyer-vendor concentration: "
          f"{len(results.get('buyer_vendor_concentration', []))}")
    print(f"  Just-under-threshold clusters: "
          f"{len(results.get('just_under_threshold', []))}")
    print(f"  Repeating-amount patterns: "
          f"{len(results.get('repeating_amounts', []))}")
    print(f"  Vague high-value POs: "
          f"{len(results.get('vague_high_value_pos', []))}")
    print(f"  Reports: data/dgs/po_anomalies.{{json,md}}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
