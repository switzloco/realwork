"""
ETL Agent — Stage 1
Pulls CA state grant/spending data, normalizes it, writes to SQLite.

Primary source: CA State Grants Portal via data.ca.gov CKAN API
Fallback: local CSV (place in data/grants.csv)

To find the right dataset:
  1. Browse data.ca.gov/dataset
  2. Search "grants" or "infrastructure"
  3. Copy the resource ID from the URL into CA_GRANTS_RESOURCE_ID below
"""

import hashlib
import json
import os
import re

import pandas as pd
import requests

from src.db import get_conn, init_db

# data.ca.gov CKAN API — update this resource ID as needed
CA_GRANTS_BASE_URL  = "https://data.ca.gov/api/3/action/datastore_search"
CA_GRANTS_RESOURCE_ID = os.getenv("CA_GRANTS_RESOURCE_ID", "")

TARGET_CATEGORIES = {
    "infrastructure", "construction", "environmental",
    "transportation", "remediation", "water", "road", "bridge",
}

FIELD_MAP = {
    # Maps possible source column names → our normalized field names
    # Add mappings here as you discover the actual CA dataset schema
    "project_name":    ["project_name", "project title", "projecttitle", "grant name", "award name"],
    "recipient_name":  ["applicant_name", "recipient", "recipientname", "grantee", "organization"],
    "recipient_type":  ["entity_type", "applicant type", "recipienttype", "org type"],
    "award_amount":    ["award_amount", "amount", "total award", "totalawardamount", "grant amount", "funding amount"],
    "award_date":      ["award_date", "date awarded", "projectstartdate", "approval date"],
    "category":        ["category", "program area", "fund type", "project type"],
    "description":     ["project_description", "description", "projectabstract", "project summary", "abstract"],
    "location":        ["project_location", "county", "countiesserved", "geographiclocationserved", "city", "address", "location"],
    "funding_source":  ["funding_source", "fund source", "agencydept", "program", "agency"],
    "contract_type":   ["contract_type", "award type", "procurement type"],
}


def _project_id(row: dict) -> str:
    key = f"{row.get('recipient_name','')}-{row.get('award_amount','')}-{row.get('award_date','')}"
    return hashlib.md5(key.encode()).hexdigest()[:12]


def _map_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Remap whatever column names exist in source data to our normalized names."""
    col_lower = {c.lower().strip(): c for c in df.columns}
    rename = {}
    for target_field, candidates in FIELD_MAP.items():
        for candidate in candidates:
            if candidate in col_lower:
                rename[col_lower[candidate]] = target_field
                break
    return df.rename(columns=rename)


def _is_target_category(row: dict) -> bool:
    text = " ".join([
        str(row.get("category", "")),
        str(row.get("description", "")),
        str(row.get("funding_source", "")),
    ]).lower()
    return any(kw in text for kw in TARGET_CATEGORIES)


def _clean_amount(val) -> float:
    if pd.isna(val):
        return 0.0
    return float(re.sub(r"[^\d.]", "", str(val)) or 0)


def fetch_from_api(limit: int = 5000) -> pd.DataFrame:
    if not CA_GRANTS_RESOURCE_ID:
        raise ValueError("CA_GRANTS_RESOURCE_ID not set. Add it to .env or use a local CSV.")

    rows, offset = [], 0
    while True:
        r = requests.get(CA_GRANTS_BASE_URL, params={
            "resource_id": CA_GRANTS_RESOURCE_ID,
            "limit": 100,
            "offset": offset,
        }, timeout=30)
        r.raise_for_status()
        records = r.json()["result"]["records"]
        if not records:
            break
        rows.extend(records)
        offset += 100
        if len(rows) >= limit:
            break

    return pd.DataFrame(rows)


def fetch_from_csv(path: str = "data/grants.csv") -> pd.DataFrame:
    return pd.read_csv(path, low_memory=False)


def run(source: str = "auto") -> list[dict]:
    """
    Load, normalize, filter, and persist CA grants data.
    source: "api" | "csv" | "auto" (tries API, falls back to CSV)
    Returns list of normalized project dicts.
    """
    init_db()

    print("Loading grant data...")
    if source == "api" or (source == "auto" and CA_GRANTS_RESOURCE_ID):
        df = fetch_from_api()
    else:
        df = fetch_from_csv()

    print(f"  Loaded {len(df)} raw records")

    df = _map_columns(df)
    df["award_amount"] = df.get("award_amount", pd.Series(dtype=float)).apply(_clean_amount)

    # Filter to target categories and private recipients only (not gov-to-gov grants)
    records = df.to_dict("records")
    records = [r for r in records if _is_target_category(r)]
    records = [r for r in records if 100_000 <= r.get("award_amount", 0) <= 1_500_000]

    # Sort by award amount descending, keep up to 40 records to avoid API limits
    records.sort(key=lambda r: r.get("award_amount", 0), reverse=True)
    top_n = min(40, len(records))
    records = records[:top_n]

    print(f"  Filtered to {len(records)} target records ($100k-$1.5M tier, max 40)")

    projects = []
    with get_conn() as conn:
        for r in records:
            project_id = _project_id(r)
            p = {
                "project_id":    project_id,
                "project_name":  str(r.get("project_name", ""))[:500],
                "recipient_name": str(r.get("recipient_name", ""))[:500],
                "recipient_type": str(r.get("recipient_type", ""))[:100],
                "award_amount":  r.get("award_amount", 0),
                "award_date":    str(r.get("award_date", ""))[:50],
                "category":      str(r.get("category", ""))[:200],
                "description":   str(r.get("description", ""))[:2000],
                "location":      str(r.get("location", ""))[:500],
                "funding_source": str(r.get("funding_source", ""))[:200],
                "contract_type": str(r.get("contract_type", ""))[:100],
                "raw_record":    json.dumps(r),
            }
            conn.execute("""
                INSERT OR REPLACE INTO projects VALUES
                (:project_id,:project_name,:recipient_name,:recipient_type,
                 :award_amount,:award_date,:category,:description,
                 :location,:funding_source,:contract_type,:raw_record)
            """, p)
            projects.append(p)

    print(f"  Wrote {len(projects)} projects to DB")
    return projects
