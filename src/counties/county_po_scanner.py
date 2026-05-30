"""
County / Local Government Purchase Order Scanner.

The state grants portal is the most-audited slice of CA public spending.
Local government procurement (county + city) is where less-audited fraud
actually lives. Each jurisdiction publishes its own data — SF, LA, San
Diego, San Jose all have open data portals. The same threshold-edge,
repeating-amount, and buyer-concentration heuristics that we ran against
DGS data apply directly.

This scanner is the "the tool generalizes" demonstration. It's the same
analysis logic as src/dgs/purchase_orders.py but with per-jurisdiction
adapters for the local portals.

Supported sources (extend by adding to LOCAL_SOURCES):
  - SF Open Data (SF Controller spending) — Socrata API
  - LA County Open Data — Socrata API
  - LA City Open Data — Socrata API
  - Sacramento Open Data — Socrata API
  - San Jose Open Data — Socrata API

Reads from per-source open data APIs (no auth required for public datasets).
Writes data/counties/{source}/po_anomalies.{json,md}.

Usage:
    # Scan SF county procurement
    python -m src.counties.county_po_scanner --source sf

    # Scan all configured sources
    python -m src.counties.county_po_scanner --source all
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()


# Each entry: (display_name, Socrata endpoint, $limit per request, field map)
# Field map keys map our normalized names to the source's column names.
# If you don't know the schema yet, leave fields empty and the scanner
# will auto-detect via find_columns().
LOCAL_SOURCES = {
    "sf": {
        "display": "San Francisco — Vendor Payments",
        "url": "https://data.sfgov.org/resource/g5ai-z4az.json",  # vendor payments
        "limit_per_request": 1000,
        "max_records": 50000,
    },
    "la_county": {
        "display": "Los Angeles County — Open Checkbook (spending)",
        "url": "https://data.lacounty.gov/resource/wymi-pnxc.json",  # placeholder; update for current resource
        "limit_per_request": 1000,
        "max_records": 50000,
    },
    "sac": {
        "display": "Sacramento — Vendor Payments",
        "url": "https://data.cityofsacramento.org/resource/q49g-2u6n.json",  # placeholder
        "limit_per_request": 1000,
        "max_records": 50000,
    },
    "sj": {
        "display": "San José — City Payments",
        "url": "https://data.sanjoseca.gov/resource/5z82-9pbk.json",  # placeholder
        "limit_per_request": 1000,
        "max_records": 50000,
    },
}

# Same thresholds as DGS scanner. Local thresholds vary slightly
# (often $3,500 / $25,000 / $100,000) but the heuristic is the same.
THRESHOLDS = [4999, 9999, 24999, 49999, 99999, 249999]
NEAR_THRESHOLD_BAND = 100


def fetch_source(source_key: str) -> pd.DataFrame:
    if source_key not in LOCAL_SOURCES:
        print(f"Unknown source: {source_key}. Options: {list(LOCAL_SOURCES.keys())}")
        sys.exit(1)
    src = LOCAL_SOURCES[source_key]
    print(f"Fetching {src['display']}...")
    rows = []
    offset = 0
    while offset < src["max_records"]:
        try:
            r = requests.get(src["url"], params={
                "$limit": src["limit_per_request"],
                "$offset": offset,
            }, timeout=60)
            if not r.ok:
                print(f"  HTTP {r.status_code} — endpoint may be stale. "
                      f"Update LOCAL_SOURCES[{source_key!r}]['url']")
                break
            batch = r.json()
            if not batch:
                break
            rows.extend(batch)
            offset += src["limit_per_request"]
            if offset % 5000 == 0:
                print(f"  {len(rows)} records...")
        except Exception as e:
            print(f"  Fetch error: {e}")
            break
    return pd.DataFrame(rows)


def find_columns(df: pd.DataFrame) -> dict:
    out = {}
    for c in df.columns:
        cl = c.lower().strip()
        if any(k in cl for k in ("vendor", "supplier", "payee")) and "name" not in out.values():
            out.setdefault("vendor", c)
        if any(k in cl for k in ("dept", "department", "agency", "buyer", "purchaser")):
            out.setdefault("buyer", c)
        if any(k in cl for k in ("amount", "total", "paid", "price")) and "amount" not in out:
            out.setdefault("amount", c)
        if any(k in cl for k in ("description", "item", "purpose", "object")):
            out.setdefault("description", c)
        if "date" in cl and "date" not in out:
            out.setdefault("date", c)
        if ("po" in cl or "voucher" in cl or "warrant" in cl or "check" in cl) and "id" in cl:
            out.setdefault("po_id", c)
    return out


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    cols = find_columns(df)
    rename = {v: k for k, v in cols.items()}
    df = df.rename(columns=rename)
    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(
            df["amount"].astype(str).str.replace(r"[^\d.]", "", regex=True),
            errors="coerce",
        )
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df, cols


def find_anomalies(df: pd.DataFrame) -> dict:
    results = {"total_records": len(df)}
    if "amount" in df.columns:
        results["total_value"] = float(df["amount"].sum())

    # Just-under-threshold clusters
    if "amount" in df.columns and "vendor" in df.columns:
        near = []
        for t in THRESHOLDS:
            band = df[(df["amount"] >= t - NEAR_THRESHOLD_BAND) &
                      (df["amount"] <= t)]
            if len(band) >= 3:
                by_vendor = band.groupby("vendor").size().sort_values(ascending=False)
                for vendor, count in by_vendor.items():
                    if count >= 2:
                        amounts = band[band["vendor"] == vendor]["amount"].tolist()
                        near.append({
                            "vendor": str(vendor),
                            "threshold": t,
                            "po_count_in_band": int(count),
                            "example_amounts": [float(a) for a in amounts[:5]],
                        })
        results["just_under_threshold"] = sorted(near, key=lambda x: -x["po_count_in_band"])[:30]

    # Repeating exact amounts
    if "amount" in df.columns and "vendor" in df.columns:
        repeating = []
        for vendor, group in df.groupby("vendor"):
            if len(group) < 3:
                continue
            for amt, count in group["amount"].value_counts().items():
                if count >= 3 and amt >= 5000:
                    repeating.append({
                        "vendor": str(vendor),
                        "exact_amount": float(amt),
                        "po_count": int(count),
                        "total": float(amt * count),
                    })
        repeating.sort(key=lambda x: -x["total"])
        results["repeating_amounts"] = repeating[:30]

    # Buyer-vendor concentration
    if "buyer" in df.columns and "vendor" in df.columns:
        bv = df.groupby(["buyer", "vendor"]).agg(
            po_count=("amount", "count"),
            total_value=("amount", "sum"),
        ).reset_index()
        buyer_totals = df.groupby("buyer")["amount"].sum().to_dict()
        bv["buyer_total"] = bv["buyer"].map(buyer_totals)
        bv["share"] = bv["total_value"] / bv["buyer_total"]
        concentrated = bv[(bv["share"] >= 0.75) & (bv["po_count"] >= 3) &
                          (bv["total_value"] >= 25_000)]
        concentrated = concentrated.sort_values("total_value", ascending=False)
        results["buyer_vendor_concentration"] = [
            {"buyer": str(r["buyer"]), "vendor": str(r["vendor"]),
             "po_count": int(r["po_count"]), "total_value": float(r["total_value"]),
             "share": round(float(r["share"]), 3)}
            for _, r in concentrated.head(30).iterrows()
        ]
    return results


def write_report(source_key: str, results: dict, output_dir: Path):
    lines = [f"# Local Government PO Anomalies — {LOCAL_SOURCES[source_key]['display']}\n"]
    lines.append(f"- Records analyzed: {results.get('total_records', 0):,}")
    if "total_value" in results:
        lines.append(f"- Total value: ${results['total_value']:,.0f}\n")

    if results.get("just_under_threshold"):
        lines.append("## Just-Under-Threshold Clusters\n")
        lines.append("| Vendor | Threshold | POs | Example Amounts |")
        lines.append("|--------|-----------|-----|-----------------|")
        for r in results["just_under_threshold"][:20]:
            amts = ", ".join(f"${a:,.0f}" for a in r["example_amounts"][:3])
            lines.append(f"| {r['vendor'][:35]} | ${r['threshold']:,} | "
                         f"{r['po_count_in_band']} | {amts} |")

    if results.get("repeating_amounts"):
        lines.append("\n## Repeating Exact-Amount Payments\n")
        lines.append("| Vendor | Amount | Count | Total |")
        lines.append("|--------|--------|-------|-------|")
        for r in results["repeating_amounts"][:20]:
            lines.append(f"| {r['vendor'][:35]} | ${r['exact_amount']:,.0f} | "
                         f"{r['po_count']} | ${r['total']:,.0f} |")

    if results.get("buyer_vendor_concentration"):
        lines.append("\n## Buyer-Vendor Concentration\n")
        lines.append("| Buyer | Vendor | POs | Total | Share |")
        lines.append("|-------|--------|-----|-------|-------|")
        for r in results["buyer_vendor_concentration"][:20]:
            lines.append(f"| {r['buyer'][:30]} | {r['vendor'][:30]} | {r['po_count']} | "
                         f"${r['total_value']:,.0f} | {r['share']*100:.0f}% |")

    with open(output_dir / "po_anomalies.md", "w") as f:
        f.write("\n".join(lines))


def scan_one(source_key: str):
    output_dir = Path(f"data/counties/{source_key}")
    output_dir.mkdir(parents=True, exist_ok=True)

    df = fetch_source(source_key)
    if df.empty:
        print(f"  No records — skipping")
        return
    df, cols = normalize(df)
    print(f"  Detected columns: {cols}")
    results = find_anomalies(df)

    with open(output_dir / "po_anomalies.json", "w") as f:
        json.dump({"source": source_key, "detected_columns": cols,
                   "results": results}, f, indent=2, default=str)
    write_report(source_key, results, output_dir)

    print(f"\n  Output: {output_dir}/po_anomalies.{{json,md}}")
    print(f"  Just-under-threshold clusters: "
          f"{len(results.get('just_under_threshold', []))}")
    print(f"  Repeating-amount patterns: "
          f"{len(results.get('repeating_amounts', []))}")
    print(f"  Buyer-vendor concentration: "
          f"{len(results.get('buyer_vendor_concentration', []))}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="sf",
                        choices=list(LOCAL_SOURCES.keys()) + ["all"])
    args = parser.parse_args()

    if args.source == "all":
        for key in LOCAL_SOURCES:
            print(f"\n{'='*60}\n{key.upper()}\n{'='*60}")
            try:
                scan_one(key)
            except Exception as e:
                print(f"  Failed: {e}")
    else:
        scan_one(args.source)

    print(f"\n{'='*60}")
    print("LOCAL GOVERNMENT PO SCAN COMPLETE")
    print("This demonstrates the tool generalizes beyond state data.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
