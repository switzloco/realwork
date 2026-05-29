"""
Vendor Cluster Expander — find connected DGS vendors via shared attributes.

For each STRONG_SPLIT_CONTRACT_PATTERN vendor from the deep-dive:
  1. Pull every PO from the same buyer (e.g. Cal Fire for Panini Time)
  2. Identify other vendors with similar near-threshold patterns to the
     same buyer
  3. Cross-reference vendor names via Bright Data SERP to find shared
     addresses, officers, or domain names (shell network signal)

A vendor cluster — multiple "different" vendors with the same address or
same officer all winning small contracts from the same buyer — is the
classic shell-network signal. One legitimate vendor splitting a contract
across thresholds is one pattern; three "competing" vendors that share
ownership winning the threshold-edge contracts is a stronger one.

Reads from data/dgs/split_contract_dossiers/ and data/dgs/po_anomalies.json.
Writes data/dgs/vendor_clusters/{buyer_slug}.json + summary.

Cost: ~$0.03 per buyer (SERP queries on 3-5 vendors).

Usage:
    # Free (just cluster analysis, no enrichment)
    python -m src.dgs.vendor_cluster_expand

    # With Bright Data enrichment
    python -m src.dgs.vendor_cluster_expand --use-brightdata --budget 3
"""

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()

OUTPUT_DIR = Path("data/dgs/vendor_clusters")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CKAN_BASE = "https://data.ca.gov/api/3/action/datastore_search"
RESOURCE_ID = os.environ.get("DGS_PO_RESOURCE_ID", "")


def slug(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", s.lower()).strip("_")[:60]


def load_strong_vendors() -> list[dict]:
    """Pull the STRONG_SPLIT_CONTRACT_PATTERN dossiers."""
    dossier_dir = Path("data/dgs/split_contract_dossiers")
    if not dossier_dir.exists():
        return []
    strong = []
    for p in dossier_dir.glob("*.json"):
        with open(p) as f:
            d = json.load(f)
        if d.get("analysis", {}).get("verdict") == "STRONG_SPLIT_CONTRACT_PATTERN":
            strong.append(d)
    return strong


def fetch_buyer_pos(buyer: str, limit: int = 5000) -> pd.DataFrame:
    if not RESOURCE_ID:
        return pd.DataFrame()
    rows, offset = [], 0
    while len(rows) < limit:
        r = requests.get(CKAN_BASE, params={
            "resource_id": RESOURCE_ID, "limit": 500,
            "offset": offset, "q": buyer,
        }, timeout=60)
        r.raise_for_status()
        records = r.json()["result"]["records"]
        if not records:
            break
        records = [
            rec for rec in records
            if any(buyer.lower() in str(v).lower()
                   for k, v in rec.items()
                   if "department" in k.lower() or "purchaser" in k.lower())
        ]
        rows.extend(records)
        offset += 500
        if not records and len(rows):
            break
    return pd.DataFrame(rows)


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    col_map = {}
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
        elif cl == "purchase date":
            col_map[c] = "date"
    df = df.rename(columns=col_map)
    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(
            df["amount"].astype(str).str.replace(r"[^\d.]", "", regex=True),
            errors="coerce",
        )
    return df


def find_co_vendors(df: pd.DataFrame, threshold: int,
                    band: int = 100) -> list[dict]:
    """Other vendors with similar near-threshold patterns to the same buyer."""
    if df.empty or "amount" not in df:
        return []
    near = df[(df["amount"] >= threshold - band) & (df["amount"] <= threshold)]
    if near.empty or "vendor" not in near.columns:
        return []
    vc = near["vendor"].value_counts()
    co_vendors = []
    for vendor, count in vc.items():
        if count >= 2:
            vendor_pos = near[near["vendor"] == vendor]
            co_vendors.append({
                "vendor": str(vendor),
                "po_count": int(count),
                "total_value": float(vendor_pos["amount"].sum()),
                "min_amount": float(vendor_pos["amount"].min()),
                "max_amount": float(vendor_pos["amount"].max()),
            })
    return co_vendors


def enrich_vendors(vendors: list[str], bd_client) -> dict:
    """SERP each vendor name to find address/officer overlaps."""
    if not bd_client:
        return {}
    out = {}
    for v in vendors[:10]:
        r = bd_client.serp(f'"{v}" address California')
        snippets = []
        for o in r.get("organic", [])[:3]:
            snippets.append({
                "title": o.get("title", "")[:120],
                "snippet": o.get("description", "")[:200],
                "url": o.get("link", ""),
            })
        out[v] = snippets
    return out


def detect_overlaps(enrichment: dict) -> list[dict]:
    """Naive overlap detection — same street address mentioned across vendors."""
    address_pattern = re.compile(
        r"\b\d{2,5}\s+[A-Z][a-zA-Z]+\s+(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Boulevard|Blvd|Way|Lane|Ln|Court|Ct|Place|Pl)\b",
        re.I,
    )
    vendor_addresses = {}
    for vendor, snippets in enrichment.items():
        addrs = set()
        for s in snippets:
            for txt in (s.get("title", ""), s.get("snippet", "")):
                for m in address_pattern.findall(txt):
                    addrs.add(m.lower())
        vendor_addresses[vendor] = addrs

    overlaps = []
    vendors = list(vendor_addresses.keys())
    for i in range(len(vendors)):
        for j in range(i + 1, len(vendors)):
            shared = vendor_addresses[vendors[i]] & vendor_addresses[vendors[j]]
            if shared:
                overlaps.append({
                    "vendor_a": vendors[i],
                    "vendor_b": vendors[j],
                    "shared_addresses": list(shared),
                })
    return overlaps


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--use-brightdata", action="store_true")
    parser.add_argument("--budget", type=float, default=3.0)
    args = parser.parse_args()

    strong = load_strong_vendors()
    if not strong:
        print("No STRONG_SPLIT_CONTRACT_PATTERN dossiers found. "
              "Run split_contract_deepdive first.")
        return

    print(f"Expanding clusters for {len(strong)} strong-pattern vendors...")

    bd_client = None
    if args.use_brightdata:
        from src.bright_data.client import BrightDataClient
        bd_client = BrightDataClient(budget_cap=args.budget,
                                     label="cluster_expand")

    cluster_summaries = []

    for i, dossier in enumerate(strong, 1):
        vendor = dossier["vendor"]
        threshold = dossier["flagged_threshold"]
        analysis = dossier["analysis"]
        top_buyer = None
        if analysis.get("near_threshold_buyer_breakdown"):
            top_buyer = analysis["near_threshold_buyer_breakdown"][0]["buyer"]

        if not top_buyer or top_buyer.lower() == "nan":
            continue

        print(f"\n[{i}/{len(strong)}] {vendor} via buyer: {top_buyer[:40]}")

        buyer_pos = fetch_buyer_pos(top_buyer)
        if buyer_pos.empty:
            print(f"  No POs returned for buyer")
            continue
        buyer_pos = normalize_columns(buyer_pos)
        print(f"  Buyer has {len(buyer_pos)} total POs")

        co_vendors = find_co_vendors(buyer_pos, threshold)
        # Drop the original vendor from co-vendors
        co_vendors = [c for c in co_vendors if c["vendor"] != vendor]
        co_vendors.sort(key=lambda x: -x["po_count"])
        print(f"  Found {len(co_vendors)} other vendors with same pattern")

        cluster = {
            "anchor_vendor": vendor,
            "buyer": top_buyer,
            "threshold": threshold,
            "co_vendors": co_vendors[:20],
        }

        if bd_client and co_vendors:
            names = [vendor] + [c["vendor"] for c in co_vendors[:5]]
            print(f"  Enriching {len(names)} vendor names via SERP...")
            try:
                enrichment = enrich_vendors(names, bd_client)
                cluster["enrichment"] = enrichment
                overlaps = detect_overlaps(enrichment)
                cluster["address_overlaps"] = overlaps
                if overlaps:
                    print(f"  ⚠️  {len(overlaps)} potential address overlaps:")
                    for o in overlaps:
                        print(f"     {o['vendor_a'][:25]} ↔ {o['vendor_b'][:25]} "
                              f": {o['shared_addresses']}")
            except Exception as e:
                print(f"  Enrichment failed: {e}")

        path = OUTPUT_DIR / f"{slug(vendor)}_{slug(top_buyer)}.json"
        with open(path, "w") as f:
            json.dump(cluster, f, indent=2, default=str)
        cluster_summaries.append({
            "anchor_vendor": vendor,
            "buyer": top_buyer,
            "co_vendor_count": len(co_vendors),
            "address_overlaps": len(cluster.get("address_overlaps", [])),
        })

    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump({"clusters": cluster_summaries}, f, indent=2, default=str)

    print(f"\n{'='*60}")
    print(f"VENDOR CLUSTER EXPANSION COMPLETE")
    print(f"  Clusters analyzed: {len(cluster_summaries)}")
    with_overlaps = [c for c in cluster_summaries if c["address_overlaps"] > 0]
    if with_overlaps:
        print(f"\n  🚨 Clusters with shared addresses (shell-network signal):")
        for c in with_overlaps:
            print(f"    {c['anchor_vendor'][:30]:30s} via {c['buyer'][:25]:25s} "
                  f"({c['address_overlaps']} overlaps)")
    if bd_client:
        print(f"\n  {bd_client.report()}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
