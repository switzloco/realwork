"""
Accountability Audit — Dataset-wide analysis of grant disbursement tracking.

Run this script to analyze the full CA grants dataset for systemic issues:
- How many grants have null/empty TotalAwardUsed?
- What's the total dollar value of untracked grants?
- Break down by category, size tier, and age
- Identify grants to entities with no web presence (for Bright Data follow-up)

Usage:
    python -m src.audit.disbursement_audit

Requires: data/grants_full.csv (the COMPLETE dataset, not the filtered one)
    Download from: https://data.ca.gov/dataset/california-grants-portal-grant-awards-2022-2023/resource/86870d5c-e9fa-46f5-8f86-2a9893662ce1

Or set CA_GRANTS_RESOURCE_ID in .env and use --source api to pull via CKAN API.
"""

import json
import os
import sys
from datetime import datetime

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

from src.db import get_conn, init_db

CA_GRANTS_BASE_URL = "https://data.ca.gov/api/3/action/datastore_search"
CA_GRANTS_RESOURCE_ID = os.getenv("CA_GRANTS_RESOURCE_ID", "86870d5c-e9fa-46f5-8f86-2a9893662ce1")

SIZE_TIERS = [
    ("Under $50K", 0, 50_000),
    ("$50K-$100K", 50_000, 100_000),
    ("$100K-$500K", 100_000, 500_000),
    ("$500K-$1M", 500_000, 1_000_000),
    ("$1M-$5M", 1_000_000, 5_000_000),
    ("Over $5M", 5_000_000, float("inf")),
]


def fetch_full_dataset(source: str = "auto") -> pd.DataFrame:
    if source == "csv" or (source == "auto" and os.path.exists("data/grants_full.csv")):
        print("Loading from data/grants_full.csv...")
        return pd.read_csv("data/grants_full.csv", low_memory=False)

    print(f"Fetching full dataset from data.ca.gov (resource: {CA_GRANTS_RESOURCE_ID})...")
    rows, offset = [], 0
    while True:
        r = requests.get(CA_GRANTS_BASE_URL, params={
            "resource_id": CA_GRANTS_RESOURCE_ID,
            "limit": 500,
            "offset": offset,
        }, timeout=60)
        r.raise_for_status()
        result = r.json()["result"]
        records = result["records"]
        if not records:
            break
        rows.extend(records)
        offset += 500
        if offset % 2000 == 0:
            print(f"  Fetched {len(rows)} records...")

    print(f"  Total: {len(rows)} records")
    df = pd.DataFrame(rows)
    df.to_csv("data/grants_full.csv", index=False)
    print("  Saved to data/grants_full.csv")
    return df


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    col_map = {}
    for c in df.columns:
        cl = c.lower().strip()
        if "totalawardamount" in cl or cl == "total award amount":
            col_map[c] = "award_amount"
        elif "totalawardused" in cl or cl == "total award used":
            col_map[c] = "award_used"
        elif "matchingfundingamount" in cl:
            col_map[c] = "matching_amount"
        elif "recipientname" in cl or cl == "recipient" or "primaryrecipient" in cl:
            col_map[c] = "recipient_name"
        elif "recipienttype" in cl:
            col_map[c] = "recipient_type"
        elif "geographiclocation" in cl or cl == "county" or "countiesserved" in cl:
            col_map[c] = "location"
        elif "agencydept" in cl or "fundingsource" in cl or cl == "agency":
            col_map[c] = "funding_source"
        elif "projectabstract" in cl or cl == "description":
            col_map[c] = "description"
        elif "projectstartdate" in cl or cl == "award_date":
            col_map[c] = "start_date"
        elif "granttitle" in cl or "projecttitle" in cl:
            col_map[c] = "grant_title"

    df = df.rename(columns=col_map)

    for col in ["award_amount", "award_used", "matching_amount"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(r"[^\d.]", "", regex=True), errors="coerce")

    return df


def classify_tier(amount):
    if pd.isna(amount):
        return "Unknown"
    for label, lo, hi in SIZE_TIERS:
        if lo <= amount < hi:
            return label
    return "Unknown"


def run_audit(df: pd.DataFrame) -> dict:
    total_records = len(df)
    total_award_value = df["award_amount"].sum()

    has_used = df["award_used"].notna() & (df["award_used"] > 0) if "award_used" in df.columns else pd.Series([False] * len(df))
    null_used = ~has_used

    null_count = null_used.sum()
    null_value = df.loc[null_used, "award_amount"].sum()
    tracked_count = has_used.sum()
    tracked_value = df.loc[has_used, "award_amount"].sum()

    results = {
        "total_records": int(total_records),
        "total_award_value": float(total_award_value),
        "disbursement_tracked": {
            "count": int(tracked_count),
            "value": float(tracked_value),
            "pct_records": round(tracked_count / total_records * 100, 1) if total_records else 0,
            "pct_value": round(tracked_value / total_award_value * 100, 1) if total_award_value else 0,
        },
        "disbursement_null": {
            "count": int(null_count),
            "value": float(null_value),
            "pct_records": round(null_count / total_records * 100, 1) if total_records else 0,
            "pct_value": round(null_value / total_award_value * 100, 1) if total_award_value else 0,
        },
    }

    # By size tier
    df["tier"] = df["award_amount"].apply(classify_tier)
    tier_analysis = []
    for label, _, _ in SIZE_TIERS:
        tier_df = df[df["tier"] == label]
        tier_null = tier_df[null_used.loc[tier_df.index]] if len(tier_df) > 0 else tier_df.iloc[0:0]
        tier_analysis.append({
            "tier": label,
            "total_grants": len(tier_df),
            "total_value": float(tier_df["award_amount"].sum()),
            "null_count": len(tier_null),
            "null_value": float(tier_null["award_amount"].sum()),
            "null_pct": round(len(tier_null) / len(tier_df) * 100, 1) if len(tier_df) else 0,
        })
    results["by_tier"] = tier_analysis

    # By funding source (top 20)
    if "funding_source" in df.columns:
        source_groups = df.groupby("funding_source").agg(
            total_grants=("award_amount", "count"),
            total_value=("award_amount", "sum"),
        ).sort_values("total_value", ascending=False).head(20)

        source_analysis = []
        for src, row in source_groups.iterrows():
            src_mask = df["funding_source"] == src
            src_null = df[src_mask & null_used]
            source_analysis.append({
                "source": str(src),
                "total_grants": int(row["total_grants"]),
                "total_value": float(row["total_value"]),
                "null_count": len(src_null),
                "null_value": float(src_null["award_amount"].sum()),
                "null_pct": round(len(src_null) / int(row["total_grants"]) * 100, 1) if row["total_grants"] else 0,
            })
        results["by_source_top20"] = source_analysis

    # By recipient type
    if "recipient_type" in df.columns:
        type_groups = df.groupby("recipient_type").agg(
            total_grants=("award_amount", "count"),
            total_value=("award_amount", "sum"),
        ).sort_values("total_value", ascending=False)

        type_analysis = []
        for rtype, row in type_groups.iterrows():
            type_mask = df["recipient_type"] == rtype
            type_null = df[type_mask & null_used]
            type_analysis.append({
                "type": str(rtype),
                "total_grants": int(row["total_grants"]),
                "total_value": float(row["total_value"]),
                "null_count": len(type_null),
                "null_value": float(type_null["award_amount"].sum()),
                "null_pct": round(len(type_null) / int(row["total_grants"]) * 100, 1) if row["total_grants"] else 0,
            })
        results["by_recipient_type"] = type_analysis

    # High-risk list: private entities with null disbursement and award > $50K
    if "recipient_type" in df.columns:
        private_types = ["Business", "Individual", "LLC", "Corporation", "Partnership"]
        is_private = df["recipient_type"].str.lower().isin([t.lower() for t in private_types])
        high_risk = df[null_used & is_private & (df["award_amount"] >= 50_000)]
        high_risk = high_risk.sort_values("award_amount", ascending=False)

        risk_list = []
        for _, row in high_risk.head(50).iterrows():
            risk_list.append({
                "recipient": str(row.get("recipient_name", "Unknown")),
                "recipient_type": str(row.get("recipient_type", "Unknown")),
                "award_amount": float(row.get("award_amount", 0)),
                "grant_title": str(row.get("grant_title", "Unknown")),
                "location": str(row.get("location", "Unknown")),
                "funding_source": str(row.get("funding_source", "Unknown")),
                "description": str(row.get("description", ""))[:200],
            })
        results["high_risk_private_null_disbursement"] = risk_list
        results["high_risk_count"] = len(high_risk)
        results["high_risk_total_value"] = float(high_risk["award_amount"].sum())

    return results


def print_report(results: dict) -> str:
    lines = []
    lines.append("# California Grants Accountability Audit")
    lines.append(f"*Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC*\n")

    lines.append("## Dataset Summary")
    lines.append(f"- **Total grant records:** {results['total_records']:,}")
    lines.append(f"- **Total award value:** ${results['total_award_value']:,.0f}\n")

    d = results["disbursement_null"]
    t = results["disbursement_tracked"]
    lines.append("## Disbursement Tracking Gap")
    lines.append(f"- **Grants with NO disbursement data:** {d['count']:,} ({d['pct_records']}% of all grants)")
    lines.append(f"- **Value with NO disbursement data:** ${d['value']:,.0f} ({d['pct_value']}% of all dollars)")
    lines.append(f"- **Grants WITH disbursement data:** {t['count']:,} ({t['pct_records']}%)")
    lines.append(f"- **Value WITH disbursement data:** ${t['value']:,.0f} ({t['pct_value']}%)\n")

    lines.append("## Breakdown by Grant Size")
    lines.append("| Tier | Grants | Total Value | Null Tracking | Null Value | Null % |")
    lines.append("|------|--------|-------------|---------------|------------|--------|")
    for tier in results.get("by_tier", []):
        lines.append(f"| {tier['tier']} | {tier['total_grants']:,} | ${tier['total_value']:,.0f} | {tier['null_count']:,} | ${tier['null_value']:,.0f} | {tier['null_pct']}% |")

    if "by_recipient_type" in results:
        lines.append("\n## Breakdown by Recipient Type")
        lines.append("| Type | Grants | Total Value | Null Tracking | Null Value | Null % |")
        lines.append("|------|--------|-------------|---------------|------------|--------|")
        for rt in results["by_recipient_type"]:
            lines.append(f"| {rt['type']} | {rt['total_grants']:,} | ${rt['total_value']:,.0f} | {rt['null_count']:,} | ${rt['null_value']:,.0f} | {rt['null_pct']}% |")

    if "by_source_top20" in results:
        lines.append("\n## Top 20 Funding Sources by Value")
        lines.append("| Source | Grants | Total Value | Null % |")
        lines.append("|--------|--------|-------------|--------|")
        for src in results["by_source_top20"]:
            lines.append(f"| {src['source'][:50]} | {src['total_grants']:,} | ${src['total_value']:,.0f} | {src['null_pct']}% |")

    if "high_risk_private_null_disbursement" in results:
        lines.append(f"\n## High-Risk: Private Entities with Null Disbursement (>$50K)")
        lines.append(f"**{results['high_risk_count']:,} grants totaling ${results['high_risk_total_value']:,.0f}**\n")
        lines.append("Top 50 by award amount:\n")
        lines.append("| Recipient | Type | Amount | Program | Location |")
        lines.append("|-----------|------|--------|---------|----------|")
        for r in results["high_risk_private_null_disbursement"]:
            lines.append(f"| {r['recipient'][:30]} | {r['recipient_type']} | ${r['award_amount']:,.0f} | {r['grant_title'][:30]} | {r['location'][:20]} |")

    return "\n".join(lines)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Audit CA grants for disbursement tracking gaps")
    parser.add_argument("--source", choices=["api", "csv", "auto"], default="auto")
    args = parser.parse_args()

    init_db()
    df = fetch_full_dataset(source=args.source)
    print(f"Loaded {len(df)} records, {len(df.columns)} columns")
    print(f"Columns: {list(df.columns)}")

    df = normalize_columns(df)
    print(f"Normalized. award_amount non-null: {df['award_amount'].notna().sum()}")
    if "award_used" in df.columns:
        print(f"award_used non-null: {df['award_used'].notna().sum()}")
    else:
        print("WARNING: No award_used / TotalAwardUsed column found in dataset")

    results = run_audit(df)

    report = print_report(results)
    with open("accountability_audit.md", "w") as f:
        f.write(report)
    print(f"\nReport written to accountability_audit.md")

    with open("data/audit_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"Raw data written to data/audit_results.json")

    # Print summary to console
    d = results["disbursement_null"]
    print(f"\n{'='*60}")
    print(f"DISBURSEMENT TRACKING GAP")
    print(f"  {d['count']:,} grants ({d['pct_records']}%) have NO spend tracking")
    print(f"  ${d['value']:,.0f} ({d['pct_value']}%) in untracked dollars")
    if "high_risk_count" in results:
        print(f"\nHIGH-RISK (private entities, null disbursement, >$50K):")
        print(f"  {results['high_risk_count']:,} grants worth ${results['high_risk_total_value']:,.0f}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
