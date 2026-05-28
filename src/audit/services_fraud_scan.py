"""
Services Fraud Scanner — Find grants where services may never have been delivered.

Goes beyond construction to target the categories where fraud hides best:
- Professional services / consulting (no physical deliverable)
- Training / education / workforce (hard to verify attendance)
- Technical assistance (vague scope, easy to fabricate)
- "Pass-through" grants to intermediaries
- Grants to entities with suspicious characteristics

Also pulls Open FI$Cal vendor transactions (account code 5340xxx = professional services)
to cross-reference grant recipients against actual state expenditures.

Usage:
    python -m src.audit.services_fraud_scan --source api
    python -m src.audit.services_fraud_scan --source csv

Requires: data/grants_full.csv OR CA_GRANTS_RESOURCE_ID in .env
Optional: data/vendor_transactions.csv (from Open FISCal)
"""

import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

CA_GRANTS_BASE_URL = "https://data.ca.gov/api/3/action/datastore_search"
VENDOR_TX_BASE_URL = "https://data.ca.gov/api/3/action/datastore_search"

FISCAL_YEARS = {
    "FY2022-2023": "86870d5c-e9fa-46f5-8f86-2a9893662ce1",
    "FY2023-2024": "018f3523-652d-4197-a4a8-a055bfd1544f",
}

SERVICE_KEYWORDS = [
    "consulting", "consultant", "advisory", "technical assistance",
    "training", "education", "workforce", "professional development",
    "capacity building", "planning", "assessment", "evaluation",
    "outreach", "engagement", "marketing", "communications",
    "management", "administration", "program support",
    "research", "study", "analysis", "survey",
    "facilitation", "coordination", "staffing",
]

VAGUE_DESCRIPTION_PATTERNS = [
    r"provide\s+(services|support|assistance)",
    r"general\s+(services|support|operations)",
    r"program\s+(support|administration|management)",
    r"various\s+(services|activities|projects)",
    r"as\s+needed",
    r"on-call",
    r"miscellaneous",
]

SUSPICIOUS_ENTITY_PATTERNS = [
    r"\bllc\b",
    r"\binc\b",
    r"\bcorp\b",
    r"\benterprises?\b",
    r"\bholdings?\b",
    r"\bgroup\b",
    r"\bpartners?\b",
    r"\bassociates?\b",
    r"\bsolutions?\b",
    r"\bglobal\b",
    r"\bconsulting\b",
    r"\badvisory\b",
    r"\bservices\b",
]


def fetch_grants(source: str = "auto", resource_id: str = None) -> pd.DataFrame:
    csv_path = "data/grants_full.csv"
    if source == "csv" or (source == "auto" and os.path.exists(csv_path)):
        print(f"Loading from {csv_path}...")
        return pd.read_csv(csv_path, low_memory=False)

    rid = resource_id or os.getenv("CA_GRANTS_RESOURCE_ID", FISCAL_YEARS["FY2023-2024"])
    print(f"Fetching from data.ca.gov (resource: {rid})...")
    rows, offset = [], 0
    while True:
        r = requests.get(CA_GRANTS_BASE_URL, params={
            "resource_id": rid, "limit": 500, "offset": offset,
        }, timeout=60)
        r.raise_for_status()
        records = r.json()["result"]["records"]
        if not records:
            break
        rows.extend(records)
        offset += 500
        if offset % 2000 == 0:
            print(f"  {len(rows)} records...")
    print(f"  Total: {len(rows)}")
    return pd.DataFrame(rows)


def fetch_vendor_transactions(account_prefix: str = "5340") -> pd.DataFrame:
    """Fetch professional services vendor transactions from Open FISCal."""
    csv_path = "data/vendor_transactions.csv"
    if os.path.exists(csv_path):
        print(f"Loading vendor transactions from {csv_path}...")
        return pd.read_csv(csv_path, low_memory=False)

    vendor_resource_id = os.getenv("VENDOR_TX_RESOURCE_ID", "")
    if not vendor_resource_id:
        print("No VENDOR_TX_RESOURCE_ID set — skipping vendor transaction cross-reference.")
        print("  To enable: find the resource ID at https://data.ca.gov/dataset/vendor-transactions")
        print("  Then: export VENDOR_TX_RESOURCE_ID=<id>")
        return pd.DataFrame()

    print(f"Fetching vendor transactions (account {account_prefix}xxx)...")
    rows, offset = [], 0
    while True:
        r = requests.get(VENDOR_TX_BASE_URL, params={
            "resource_id": vendor_resource_id,
            "limit": 500,
            "offset": offset,
            "filters": json.dumps({"account": account_prefix}),
        }, timeout=60)
        r.raise_for_status()
        records = r.json()["result"]["records"]
        if not records:
            break
        rows.extend(records)
        offset += 500
        if len(rows) >= 50000:
            break
    print(f"  Total vendor transactions: {len(rows)}")
    df = pd.DataFrame(rows)
    if len(df):
        df.to_csv(csv_path, index=False)
    return df


def normalize(df: pd.DataFrame) -> pd.DataFrame:
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
        elif "grantnumber" in cl or "grantid" in cl:
            col_map[c] = "grant_id"

    df = df.rename(columns=col_map)
    for col in ["award_amount", "award_used", "matching_amount"]:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace(r"[^\d.]", "", regex=True),
                errors="coerce",
            )
    return df


def is_service_grant(row) -> bool:
    text = " ".join([
        str(row.get("grant_title", "")),
        str(row.get("description", "")),
        str(row.get("funding_source", "")),
    ]).lower()
    return any(kw in text for kw in SERVICE_KEYWORDS)


def has_vague_description(row) -> bool:
    desc = str(row.get("description", "")).lower()
    title = str(row.get("grant_title", "")).lower()
    text = f"{title} {desc}"
    if len(desc.strip()) < 20:
        return True
    return any(re.search(p, text) for p in VAGUE_DESCRIPTION_PATTERNS)


def score_entity_suspicion(name: str) -> int:
    """Higher score = more suspicious entity name patterns."""
    if not name or pd.isna(name):
        return 5
    name_lower = name.lower()
    score = 0
    word_count = len(name_lower.split())
    if word_count <= 2:
        score += 1
    matches = sum(1 for p in SUSPICIOUS_ENTITY_PATTERNS if re.search(p, name_lower))
    if matches >= 3:
        score += 2
    if re.search(r"\b(group|holdings?|enterprises?|global)\b", name_lower):
        score += 1
    return score


def find_duplicate_recipients(df: pd.DataFrame) -> dict:
    """Find recipients getting multiple grants — potential double-dipping."""
    if "recipient_name" not in df.columns:
        return {}
    counts = df.groupby("recipient_name").agg(
        grant_count=("award_amount", "count"),
        total_value=("award_amount", "sum"),
    ).sort_values("total_value", ascending=False)
    return counts[counts["grant_count"] >= 3].to_dict("index")


def find_max_award_grants(df: pd.DataFrame) -> pd.DataFrame:
    """Find grants at exactly the maximum allowed amount — a fraud signal."""
    if "funding_source" not in df.columns or "award_amount" not in df.columns:
        return pd.DataFrame()

    source_max = df.groupby("funding_source")["award_amount"].max().to_dict()
    source_counts = df.groupby("funding_source")["award_amount"].count().to_dict()

    at_max = []
    for idx, row in df.iterrows():
        src = row.get("funding_source", "")
        amt = row.get("award_amount", 0)
        if pd.isna(amt) or amt <= 0:
            continue
        max_for_src = source_max.get(src, 0)
        count_for_src = source_counts.get(src, 0)
        if amt == max_for_src and count_for_src >= 3 and amt >= 50000:
            at_max.append(idx)
    return df.loc[at_max] if at_max else pd.DataFrame()


def run_scan(df: pd.DataFrame) -> dict:
    results = {
        "scan_date": datetime.utcnow().isoformat(),
        "total_records": len(df),
        "total_value": float(df["award_amount"].sum()) if "award_amount" in df.columns else 0,
    }

    # 1. Service grants subset
    service_mask = df.apply(is_service_grant, axis=1)
    services_df = df[service_mask]
    results["service_grants"] = {
        "count": len(services_df),
        "value": float(services_df["award_amount"].sum()),
        "pct_of_total": round(len(services_df) / len(df) * 100, 1) if len(df) else 0,
    }

    # 2. Null disbursement in service grants
    if "award_used" in services_df.columns:
        null_used = services_df["award_used"].isna() | (services_df["award_used"] == 0)
    else:
        null_used = pd.Series([True] * len(services_df), index=services_df.index)

    services_null = services_df[null_used]
    results["service_grants_null_disbursement"] = {
        "count": len(services_null),
        "value": float(services_null["award_amount"].sum()),
        "pct": round(len(services_null) / len(services_df) * 100, 1) if len(services_df) else 0,
    }

    # 3. Vague descriptions
    vague_mask = services_df.apply(has_vague_description, axis=1)
    vague_df = services_df[vague_mask]
    results["vague_description_services"] = {
        "count": len(vague_df),
        "value": float(vague_df["award_amount"].sum()),
    }

    # 4. Private entities in service grants with null disbursement
    private_types = ["business", "individual", "llc", "corporation", "partnership",
                     "other legal entity"]
    if "recipient_type" in services_df.columns:
        is_private = services_df["recipient_type"].str.lower().isin(private_types)
        high_risk_services = services_df[null_used & is_private]
        high_risk_services = high_risk_services.sort_values("award_amount", ascending=False)

        risk_list = []
        for _, row in high_risk_services.head(100).iterrows():
            entity_score = score_entity_suspicion(row.get("recipient_name", ""))
            risk_list.append({
                "recipient": str(row.get("recipient_name", "Unknown")),
                "recipient_type": str(row.get("recipient_type", "Unknown")),
                "award_amount": float(row.get("award_amount", 0)),
                "grant_title": str(row.get("grant_title", "Unknown")),
                "description": str(row.get("description", ""))[:300],
                "location": str(row.get("location", "Unknown")),
                "funding_source": str(row.get("funding_source", "Unknown")),
                "entity_suspicion_score": entity_score,
                "vague_description": bool(has_vague_description(row)),
            })
        results["high_risk_service_grants"] = risk_list
        results["high_risk_service_count"] = len(high_risk_services)
        results["high_risk_service_value"] = float(high_risk_services["award_amount"].sum())

    # 5. Max-award grants (always asking for the maximum)
    max_award_df = find_max_award_grants(df)
    if len(max_award_df):
        max_list = []
        for _, row in max_award_df.head(50).iterrows():
            max_list.append({
                "recipient": str(row.get("recipient_name", "Unknown")),
                "award_amount": float(row.get("award_amount", 0)),
                "grant_title": str(row.get("grant_title", "Unknown")),
                "funding_source": str(row.get("funding_source", "Unknown")),
            })
        results["max_award_grants"] = max_list
        results["max_award_count"] = len(max_award_df)

    # 6. Multi-grant recipients
    multi = find_duplicate_recipients(df)
    multi_list = []
    for name, stats in list(multi.items())[:30]:
        multi_list.append({
            "recipient": str(name),
            "grant_count": int(stats["grant_count"]),
            "total_value": float(stats["total_value"]),
        })
    results["multi_grant_recipients"] = multi_list

    # 7. Grants to individuals (often least oversight)
    if "recipient_type" in df.columns:
        individuals = df[df["recipient_type"].str.lower() == "individual"]
        individuals = individuals.sort_values("award_amount", ascending=False)
        ind_list = []
        for _, row in individuals.head(30).iterrows():
            ind_list.append({
                "recipient": str(row.get("recipient_name", "Unknown")),
                "award_amount": float(row.get("award_amount", 0)),
                "grant_title": str(row.get("grant_title", "Unknown")),
                "funding_source": str(row.get("funding_source", "Unknown")),
                "description": str(row.get("description", ""))[:200],
            })
        results["largest_individual_grants"] = ind_list
        results["individual_grant_count"] = len(individuals)
        results["individual_grant_value"] = float(individuals["award_amount"].sum())

    # 8. Combined risk score for prioritization
    if "high_risk_service_grants" in results:
        for entry in results["high_risk_service_grants"]:
            score = 0
            if entry["vague_description"]:
                score += 3
            score += entry["entity_suspicion_score"]
            if entry["award_amount"] >= 500000:
                score += 2
            elif entry["award_amount"] >= 100000:
                score += 1
            entry["composite_risk_score"] = score

        results["high_risk_service_grants"].sort(
            key=lambda x: (-x["composite_risk_score"], -x["award_amount"])
        )

    return results


def print_report(results: dict) -> str:
    lines = []
    lines.append("# Services Fraud Scan — California Grants")
    lines.append(f"*Generated: {results['scan_date'][:16]} UTC*\n")

    lines.append("## Dataset Overview")
    lines.append(f"- **Total records:** {results['total_records']:,}")
    lines.append(f"- **Total value:** ${results['total_value']:,.0f}\n")

    sg = results["service_grants"]
    lines.append("## Service-Type Grants (consulting, training, TA, etc.)")
    lines.append(f"- **Count:** {sg['count']:,} ({sg['pct_of_total']}% of all grants)")
    lines.append(f"- **Value:** ${sg['value']:,.0f}\n")

    sn = results["service_grants_null_disbursement"]
    lines.append("## Service Grants with NO Disbursement Tracking")
    lines.append(f"- **Count:** {sn['count']:,} ({sn['pct']}% of service grants)")
    lines.append(f"- **Value:** ${sn['value']:,.0f}\n")

    vd = results["vague_description_services"]
    lines.append("## Service Grants with Vague Descriptions")
    lines.append(f"- **Count:** {vd['count']:,}")
    lines.append(f"- **Value:** ${vd['value']:,.0f}\n")

    if "high_risk_service_count" in results:
        lines.append(f"## HIGH RISK: Private Entity + Service Grant + No Tracking")
        lines.append(f"**{results['high_risk_service_count']:,} grants totaling ${results['high_risk_service_value']:,.0f}**\n")
        lines.append("Top entries by composite risk score:\n")
        lines.append("| Risk | Recipient | Amount | Program | Vague? |")
        lines.append("|------|-----------|--------|---------|--------|")
        for r in results.get("high_risk_service_grants", [])[:50]:
            vague = "YES" if r["vague_description"] else ""
            lines.append(f"| {r['composite_risk_score']} | {r['recipient'][:35]} | ${r['award_amount']:,.0f} | {r['grant_title'][:30]} | {vague} |")

    if "multi_grant_recipients" in results and results["multi_grant_recipients"]:
        lines.append(f"\n## Multi-Grant Recipients (3+ grants)")
        lines.append("| Recipient | Grants | Total Value |")
        lines.append("|-----------|--------|-------------|")
        for r in results["multi_grant_recipients"]:
            lines.append(f"| {r['recipient'][:40]} | {r['grant_count']} | ${r['total_value']:,.0f} |")

    if "largest_individual_grants" in results:
        lines.append(f"\n## Grants to Individuals ({results.get('individual_grant_count',0):,} grants, ${results.get('individual_grant_value',0):,.0f})")
        lines.append("| Recipient | Amount | Program |")
        lines.append("|-----------|--------|---------|")
        for r in results["largest_individual_grants"][:20]:
            lines.append(f"| {r['recipient'][:35]} | ${r['award_amount']:,.0f} | {r['grant_title'][:40]} |")

    if "max_award_grants" in results:
        lines.append(f"\n## Grants at Program Maximum ({results.get('max_award_count',0)} grants)")
        lines.append("*Recipients who received exactly the maximum allowed — asks for the ceiling.*\n")
        lines.append("| Recipient | Amount | Program | Source |")
        lines.append("|-----------|--------|---------|--------|")
        for r in results["max_award_grants"][:30]:
            lines.append(f"| {r['recipient'][:30]} | ${r['award_amount']:,.0f} | {r['grant_title'][:25]} | {r['funding_source'][:25]} |")

    return "\n".join(lines)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Scan CA grants for services fraud signals")
    parser.add_argument("--source", choices=["api", "csv", "auto"], default="auto")
    parser.add_argument("--fy", choices=list(FISCAL_YEARS.keys()), default=None,
                        help="Fiscal year to scan (default: all available)")
    args = parser.parse_args()

    all_dfs = []

    if args.fy:
        rid = FISCAL_YEARS[args.fy]
        df = fetch_grants(source=args.source, resource_id=rid)
        df["fiscal_year"] = args.fy
        all_dfs.append(df)
    elif args.source == "csv":
        df = fetch_grants(source="csv")
        all_dfs.append(df)
    else:
        for fy, rid in FISCAL_YEARS.items():
            print(f"\n--- {fy} ---")
            try:
                df = fetch_grants(source=args.source, resource_id=rid)
                df["fiscal_year"] = fy
                all_dfs.append(df)
            except Exception as e:
                print(f"  Failed: {e}")

    if not all_dfs:
        print("No data loaded. Use --source csv with data/grants_full.csv, or set CA_GRANTS_RESOURCE_ID.")
        sys.exit(1)

    combined = pd.concat(all_dfs, ignore_index=True)
    print(f"\nCombined dataset: {len(combined)} records")

    combined = normalize(combined)
    print(f"Normalized. Columns: {list(combined.columns)[:10]}...")

    results = run_scan(combined)

    report = print_report(results)
    os.makedirs("data", exist_ok=True)
    with open("services_fraud_scan.md", "w") as f:
        f.write(report)
    print(f"\nReport: services_fraud_scan.md")

    with open("data/services_fraud_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"Raw data: data/services_fraud_results.json")

    # Console summary
    print(f"\n{'='*60}")
    print("SERVICES FRAUD SCAN SUMMARY")
    sg = results["service_grants"]
    sn = results["service_grants_null_disbursement"]
    print(f"  Service-type grants: {sg['count']:,} worth ${sg['value']:,.0f}")
    print(f"  With NO spend tracking: {sn['count']:,} ({sn['pct']}%)")
    if "high_risk_service_count" in results:
        print(f"  HIGH RISK (private + service + untracked):")
        print(f"    {results['high_risk_service_count']:,} grants worth ${results['high_risk_service_value']:,.0f}")
    if "individual_grant_count" in results:
        print(f"  Grants to individuals: {results['individual_grant_count']:,} worth ${results['individual_grant_value']:,.0f}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
