"""
Vendor Cross-Reference — Match grant recipients against Open FISCal vendor payments.

This answers two critical questions:
1. Did a grant recipient ALSO receive direct vendor payments? (double-dipping)
2. Are there large vendor payments to entities with NO grant record? (off-books)

Data sources:
- Grant awards: data/grants_full.csv (from CA Grants Portal)
- Vendor transactions: data/vendor_transactions.csv (from Open FISCal)

To get vendor transaction data:
    1. Go to https://data.ca.gov/dataset/vendor-transactions
    2. Find the resource ID for the desired fiscal year
    3. Set VENDOR_TX_RESOURCE_ID in .env
    4. Run: python -m src.audit.vendor_crossref --fetch

Or download the CSV manually from data.ca.gov and save as data/vendor_transactions.csv.

Account code reference:
    5340xxx = Professional/consulting services
    5442xxx = Construction
    5301xxx = Travel
    5320xxx = Printing
    5540xxx = Equipment
"""

import json
import os
import re
import sys
from collections import defaultdict
from difflib import SequenceMatcher

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

VENDOR_TX_BASE_URL = "https://data.ca.gov/api/3/action/datastore_search"


def normalize_name(name: str) -> str:
    if not name or pd.isna(name):
        return ""
    name = name.lower().strip()
    name = re.sub(r"\b(inc|llc|corp|co|ltd|lp|lc|plc)\b\.?", "", name)
    name = re.sub(r"[^a-z0-9\s]", "", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def name_similarity(a: str, b: str) -> float:
    a_norm = normalize_name(a)
    b_norm = normalize_name(b)
    if not a_norm or not b_norm:
        return 0.0
    if a_norm == b_norm:
        return 1.0
    return SequenceMatcher(None, a_norm, b_norm).ratio()


def fetch_vendor_data(resource_id: str, account_codes: list[str] = None,
                      limit: int = 50000) -> pd.DataFrame:
    rows, offset = [], 0
    while True:
        params = {
            "resource_id": resource_id,
            "limit": 500,
            "offset": offset,
        }
        if account_codes:
            q = " OR ".join(account_codes)
            params["q"] = q

        r = requests.get(VENDOR_TX_BASE_URL, params=params, timeout=60)
        r.raise_for_status()
        records = r.json()["result"]["records"]
        if not records:
            break
        rows.extend(records)
        offset += 500
        if len(rows) >= limit:
            break
        if offset % 5000 == 0:
            print(f"  {len(rows)} vendor records...")

    return pd.DataFrame(rows)


def cross_reference(grants_df: pd.DataFrame, vendors_df: pd.DataFrame,
                    threshold: float = 0.85) -> dict:
    grant_names = {}
    if "recipient_name" in grants_df.columns:
        for _, row in grants_df.iterrows():
            name = str(row.get("recipient_name", ""))
            if name and name != "nan":
                norm = normalize_name(name)
                if norm not in grant_names:
                    grant_names[norm] = {
                        "original": name,
                        "total_grant_value": 0,
                        "grant_count": 0,
                        "grants": [],
                    }
                grant_names[norm]["total_grant_value"] += float(row.get("award_amount", 0) or 0)
                grant_names[norm]["grant_count"] += 1

    vendor_names = {}
    vendor_col = None
    for c in vendors_df.columns:
        if "vendor" in c.lower():
            vendor_col = c
            break
    if not vendor_col:
        return {"error": "No vendor_name column found in vendor data"}

    amount_col = None
    for c in vendors_df.columns:
        if "monetary" in c.lower() or "amount" in c.lower():
            amount_col = c
            break

    for _, row in vendors_df.iterrows():
        name = str(row.get(vendor_col, ""))
        if name and name != "nan":
            norm = normalize_name(name)
            amt = float(row.get(amount_col, 0) or 0) if amount_col else 0
            if norm not in vendor_names:
                vendor_names[norm] = {
                    "original": name,
                    "total_vendor_value": 0,
                    "tx_count": 0,
                }
            vendor_names[norm]["total_vendor_value"] += amt
            vendor_names[norm]["tx_count"] += 1

    matches = []
    for g_norm, g_info in grant_names.items():
        for v_norm, v_info in vendor_names.items():
            sim = name_similarity(g_info["original"], v_info["original"])
            if sim >= threshold:
                matches.append({
                    "grant_recipient": g_info["original"],
                    "vendor_name": v_info["original"],
                    "similarity": round(sim, 3),
                    "total_grant_value": g_info["total_grant_value"],
                    "grant_count": g_info["grant_count"],
                    "total_vendor_payments": v_info["total_vendor_value"],
                    "vendor_tx_count": v_info["tx_count"],
                    "combined_public_money": g_info["total_grant_value"] + v_info["total_vendor_value"],
                })

    matches.sort(key=lambda x: -x["combined_public_money"])

    vendors_only = []
    matched_vendor_norms = {normalize_name(m["vendor_name"]) for m in matches}
    for v_norm, v_info in sorted(vendor_names.items(), key=lambda x: -x[1]["total_vendor_value"]):
        if v_norm not in matched_vendor_norms and v_norm not in grant_names:
            if v_info["total_vendor_value"] >= 100000:
                vendors_only.append({
                    "vendor_name": v_info["original"],
                    "total_payments": v_info["total_vendor_value"],
                    "tx_count": v_info["tx_count"],
                })
                if len(vendors_only) >= 50:
                    break

    return {
        "matches": matches,
        "match_count": len(matches),
        "grant_recipients_checked": len(grant_names),
        "vendors_checked": len(vendor_names),
        "vendors_without_grants": vendors_only,
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Cross-reference grant recipients with vendor payments")
    parser.add_argument("--fetch", action="store_true", help="Fetch vendor data from API")
    parser.add_argument("--account", default="5340", help="Account code prefix (default: 5340 = professional services)")
    args = parser.parse_args()

    grants_path = "data/grants_full.csv"
    vendors_path = "data/vendor_transactions.csv"

    if not os.path.exists(grants_path):
        print(f"Need {grants_path} — run disbursement_audit.py first or download manually.")
        sys.exit(1)

    grants_df = pd.read_csv(grants_path, low_memory=False)
    col_map = {}
    for c in grants_df.columns:
        cl = c.lower().strip()
        if "recipientname" in cl or "primaryrecipient" in cl:
            col_map[c] = "recipient_name"
        elif "totalawardamount" in cl:
            col_map[c] = "award_amount"
    grants_df = grants_df.rename(columns=col_map)
    if "award_amount" in grants_df.columns:
        grants_df["award_amount"] = pd.to_numeric(
            grants_df["award_amount"].astype(str).str.replace(r"[^\d.]", "", regex=True),
            errors="coerce",
        )
    print(f"Loaded {len(grants_df)} grant records")

    if args.fetch:
        vendor_resource_id = os.getenv("VENDOR_TX_RESOURCE_ID", "")
        if not vendor_resource_id:
            print("Set VENDOR_TX_RESOURCE_ID in .env first.")
            print("Find it at: https://data.ca.gov/dataset/vendor-transactions")
            sys.exit(1)
        vendors_df = fetch_vendor_data(vendor_resource_id, account_codes=[args.account])
        if len(vendors_df):
            vendors_df.to_csv(vendors_path, index=False)
            print(f"Saved {len(vendors_df)} vendor records to {vendors_path}")
    elif os.path.exists(vendors_path):
        vendors_df = pd.read_csv(vendors_path, low_memory=False)
        print(f"Loaded {len(vendors_df)} vendor records")
    else:
        print(f"Need {vendors_path}. Use --fetch or download manually.")
        print("  https://data.ca.gov/dataset/vendor-transactions")
        sys.exit(1)

    results = cross_reference(grants_df, vendors_df)

    os.makedirs("data", exist_ok=True)
    with open("data/vendor_crossref_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'='*60}")
    print(f"VENDOR CROSS-REFERENCE RESULTS")
    print(f"  Grant recipients checked: {results['grant_recipients_checked']:,}")
    print(f"  Vendors checked: {results['vendors_checked']:,}")
    print(f"  Matches found: {results['match_count']}")
    if results["matches"]:
        print(f"\n  Top matches (grant recipient ↔ vendor):")
        for m in results["matches"][:15]:
            print(f"    {m['grant_recipient'][:35]:35s} | grants ${m['total_grant_value']:>12,.0f} | vendor ${m['total_vendor_payments']:>12,.0f}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
