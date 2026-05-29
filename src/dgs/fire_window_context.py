"""
Fire Window Context — what was Cal Fire procurement doing Aug 14 - Sep 9, 2025?

The Panini Time pattern coincides with two real wildfires (King Fire Aug 14-18,
Dillon Fire Aug 28+). To honestly evaluate whether Panini Time is anomalous
WITHIN that emergency context, we need to know what *everyone else* was getting
in Cal Fire POs during the same window.

Questions answered:
  1. How many POs did Cal Fire issue in Aug 14 - Sep 9 2025?
  2. How many vendors? What size distribution?
  3. How many vendors got >=3 POs in that window? (recurring emergency vendors)
  4. Were other vendors also clustered at $49,950?
  5. Where does Panini Time rank by PO count and by total value?

If Panini Time is one of 50 catering vendors all averaging 5-10 POs at varied
amounts during the fire emergency, the pattern is normal. If they're the only
vendor with 5+ POs at *exactly* $49,950, the pattern persists.

Reads from CKAN live (no caching by design — re-run gets fresh data).
Writes data/dgs/fire_window_context.json + a markdown summary.

Usage:
    python -m src.dgs.fire_window_context
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

CKAN_BASE = "https://data.ca.gov/api/3/action/datastore_search_sql"
CKAN_SEARCH = "https://data.ca.gov/api/3/action/datastore_search"
RESOURCE_ID = os.environ.get("DGS_PO_RESOURCE_ID", "")

# Fire window: Aug 14 - Sep 9 2025 (covers both King and Dillon fire start)
WINDOW_START = "2025-08-14"
WINDOW_END = "2025-09-09"

CAL_FIRE_NAMES = [
    "Forestry and Fire Protection",
    "Forestry & Fire Protection",
    "CAL FIRE",
    "3540-CAL FIRE",
]


def fetch_cal_fire_window() -> pd.DataFrame:
    """Pull every Cal Fire PO in the fire window."""
    if not RESOURCE_ID:
        print("DGS_PO_RESOURCE_ID not set")
        sys.exit(1)

    rows = []
    offset = 0
    print(f"Fetching Cal Fire POs from CKAN (this may take a minute)...")
    while True:
        r = requests.get(CKAN_SEARCH, params={
            "resource_id": RESOURCE_ID,
            "limit": 500,
            "offset": offset,
            "q": "CAL FIRE",
        }, timeout=60)
        r.raise_for_status()
        records = r.json()["result"]["records"]
        if not records:
            break
        rows.extend(records)
        offset += 500
        if offset % 5000 == 0:
            print(f"  {len(rows)} records...")
        if offset > 50000:
            break

    df = pd.DataFrame(rows)
    if df.empty:
        return df

    # Normalize columns
    col_map = {}
    for c in df.columns:
        cl = c.lower().strip()
        if cl == "supplier name":
            col_map[c] = "vendor"
        elif cl == "department name":
            col_map[c] = "buyer"
        elif cl == "total price":
            col_map[c] = "amount"
        elif cl == "purchase date":
            col_map[c] = "date"
        elif cl == "purchase order number":
            col_map[c] = "po_id"
        elif cl == "item description":
            col_map[c] = "description"
        elif cl == "buyer name":
            col_map[c] = "buyer_name"
        elif cl == "buyer email":
            col_map[c] = "buyer_email"
    df = df.rename(columns=col_map)

    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(
            df["amount"].astype(str).str.replace(r"[^\d.]", "", regex=True),
            errors="coerce",
        )
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Filter to Cal Fire buyer
    if "buyer" in df.columns:
        mask = df["buyer"].astype(str).str.upper().str.contains(
            "FIRE|FORESTRY", regex=True, na=False
        )
        df = df[mask]

    # Filter to fire window
    if "date" in df.columns:
        df = df[
            (df["date"] >= pd.Timestamp(WINDOW_START))
            & (df["date"] <= pd.Timestamp(WINDOW_END))
        ]

    return df.reset_index(drop=True)


def analyze(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"error": "no Cal Fire POs in window — check date range and RESOURCE_ID"}

    total_pos = len(df)
    total_value = float(df["amount"].sum())
    n_vendors = int(df["vendor"].nunique()) if "vendor" in df.columns else 0
    n_buyers = int(df["buyer_name"].nunique()) if "buyer_name" in df.columns else 0

    # Vendor-level rollup
    if "vendor" in df.columns:
        by_vendor = df.groupby("vendor").agg(
            po_count=("amount", "count"),
            total_value=("amount", "sum"),
            median_amount=("amount", "median"),
        ).sort_values("po_count", ascending=False)
        top_vendors = [
            {
                "vendor": str(v),
                "po_count": int(r["po_count"]),
                "total_value": float(r["total_value"]),
                "median_amount": float(r["median_amount"]),
            }
            for v, r in by_vendor.head(30).iterrows()
        ]
    else:
        top_vendors = []
        by_vendor = pd.DataFrame()

    # How many vendors got >=3 POs?
    multi_po_vendors = int((by_vendor["po_count"] >= 3).sum()) if not by_vendor.empty else 0
    multi_po_vendor_list = [
        {"vendor": str(v), "po_count": int(r["po_count"]),
         "total_value": float(r["total_value"])}
        for v, r in by_vendor[by_vendor["po_count"] >= 3].iterrows()
    ]

    # Were other vendors clustered at $49,950?
    near_50k = df[(df["amount"] >= 49_900) & (df["amount"] <= 49_950)]
    exactly_49950 = df[df["amount"] == 49_950]
    near_50k_vendors = []
    if not near_50k.empty and "vendor" in near_50k.columns:
        for v, group in near_50k.groupby("vendor"):
            near_50k_vendors.append({
                "vendor": str(v),
                "po_count_near_49950": int(len(group)),
                "po_count_exact_49950": int((group["amount"] == 49_950).sum()),
            })
        near_50k_vendors.sort(key=lambda x: -x["po_count_exact_49950"])

    # Buyer-level rollup (named procurement officers)
    if "buyer_name" in df.columns:
        by_buyer = df.groupby("buyer_name").agg(
            po_count=("amount", "count"),
            total_value=("amount", "sum"),
            distinct_vendors=("vendor", "nunique") if "vendor" in df.columns else ("amount", "count"),
        ).sort_values("po_count", ascending=False)
        top_buyers = [
            {
                "buyer": str(b),
                "po_count": int(r["po_count"]),
                "total_value": float(r["total_value"]),
                "distinct_vendors": int(r["distinct_vendors"]),
            }
            for b, r in by_buyer.head(20).iterrows()
        ]
    else:
        top_buyers = []

    # Panini Time specific
    panini_rows = df[df["vendor"].astype(str).str.upper().str.contains(
        "PANINI", na=False
    )] if "vendor" in df.columns else pd.DataFrame()
    panini_stats = {
        "po_count": int(len(panini_rows)),
        "total_value": float(panini_rows["amount"].sum()) if not panini_rows.empty else 0,
    }
    if not panini_rows.empty:
        panini_stats["amounts"] = [float(a) for a in panini_rows["amount"].tolist()]

    return {
        "window": f"{WINDOW_START} to {WINDOW_END}",
        "summary": {
            "total_pos": total_pos,
            "total_value": total_value,
            "n_unique_vendors": n_vendors,
            "n_unique_buyers": n_buyers,
            "vendors_with_3plus_pos": multi_po_vendors,
            "pos_at_exactly_49950": int(len(exactly_49950)),
            "pos_near_49950": int(len(near_50k)),
        },
        "top_vendors_by_po_count": top_vendors,
        "vendors_with_3plus_pos": multi_po_vendor_list[:30],
        "vendors_with_49950_clusters": near_50k_vendors[:15],
        "top_buyers_by_po_count": top_buyers,
        "panini_time_in_context": panini_stats,
    }


def write_markdown(result: dict):
    s = result["summary"]
    lines = [
        f"# Cal Fire Fire-Window Context Report",
        f"*Window: {result['window']} (covers King Fire start through Dillon Fire ramp)*\n",
        f"## Headline Numbers",
        f"- Total Cal Fire POs in window: **{s['total_pos']:,}**",
        f"- Total value: **${s['total_value']:,.0f}**",
        f"- Unique vendors: **{s['n_unique_vendors']:,}**",
        f"- Unique procurement officers: **{s['n_unique_buyers']:,}**",
        f"- Vendors with 3+ POs in window: **{s['vendors_with_3plus_pos']}**",
        f"- POs at exactly $49,950: **{s['pos_at_exactly_49950']}**",
        f"- POs in $49,900-$49,950 band: **{s['pos_near_49950']}**\n",
        f"## Panini Time in Context",
    ]
    p = result["panini_time_in_context"]
    lines.append(f"- POs in window: **{p['po_count']}**")
    lines.append(f"- Total value: **${p['total_value']:,.0f}**")
    if p.get("amounts"):
        unique_amounts = sorted(set(p["amounts"]))
        lines.append(f"- Distinct PO amounts: {', '.join(f'${a:,.0f}' for a in unique_amounts)}")
    lines.append("")

    lines.append("## Vendors with $49,950 Clusters (the threshold-edge pattern)")
    if result["vendors_with_49950_clusters"]:
        lines.append("| Vendor | POs near $49,950 | POs at exactly $49,950 |")
        lines.append("|--------|------------------|------------------------|")
        for v in result["vendors_with_49950_clusters"]:
            lines.append(f"| {v['vendor'][:40]} | {v['po_count_near_49950']} | "
                         f"{v['po_count_exact_49950']} |")
    else:
        lines.append("*No vendors had multi-PO $49,950 clusters in this window.*\n")
        lines.append("This would strengthen the Panini Time signal — they would be unique.")
    lines.append("")

    lines.append("## Top Vendors by PO Count (in window)")
    lines.append("| Vendor | POs | Total Value | Median Amount |")
    lines.append("|--------|-----|-------------|---------------|")
    for v in result["top_vendors_by_po_count"][:20]:
        lines.append(f"| {v['vendor'][:40]} | {v['po_count']} | "
                     f"${v['total_value']:,.0f} | ${v['median_amount']:,.0f} |")
    lines.append("")

    lines.append("## Top Procurement Officers by PO Count")
    lines.append("| Officer | POs | Total Value | Distinct Vendors |")
    lines.append("|---------|-----|-------------|------------------|")
    for b in result["top_buyers_by_po_count"][:15]:
        lines.append(f"| {b['buyer']} | {b['po_count']} | "
                     f"${b['total_value']:,.0f} | {b['distinct_vendors']} |")

    with open(OUTPUT_DIR / "fire_window_context.md", "w") as f:
        f.write("\n".join(lines))


def main():
    df = fetch_cal_fire_window()
    print(f"\nFetched {len(df)} Cal Fire POs in fire window")

    if df.empty:
        print("No data — check DGS_PO_RESOURCE_ID covers FY 25 / Aug-Sep 2025")
        return

    result = analyze(df)
    with open(OUTPUT_DIR / "fire_window_context.json", "w") as f:
        json.dump(result, f, indent=2, default=str)
    write_markdown(result)

    print(f"\n{'='*60}")
    print(f"FIRE WINDOW CONTEXT")
    s = result["summary"]
    print(f"  Cal Fire POs in window: {s['total_pos']:,}")
    print(f"  Unique vendors: {s['n_unique_vendors']:,}")
    print(f"  Vendors with 3+ POs in window: {s['vendors_with_3plus_pos']}")
    print(f"  POs at exactly $49,950: {s['pos_at_exactly_49950']}")
    print(f"\n  Panini Time: {result['panini_time_in_context']['po_count']} POs, "
          f"${result['panini_time_in_context']['total_value']:,.0f}")
    print(f"\n  $49,950 clusters across vendors:")
    for v in result["vendors_with_49950_clusters"][:10]:
        print(f"    {v['vendor'][:40]:40s} {v['po_count_exact_49950']} POs at exactly $49,950")
    print(f"\n  Report: data/dgs/fire_window_context.md")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
