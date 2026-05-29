"""
Unit Price Analyzer — Detect overpricing in DGS purchase orders.

The DGS PO dataset gives us total price per PO. For commoditized goods
(industrial gas, fuel, medical supplies, catered meals), the actual fraud
risk is **markup fraud**: billing the state $500/lunch when commercial
caterers charge $15. The total price alone doesn't surface this — we need
quantity-per-PO to compute implied unit price.

Three-layer extraction:
  1. Column scan — does the CKAN record have quantity / unit fields?
  2. Description regex — pull quantities out of free-text descriptions
     ("100 each", "12 cases of bandages", "200 sack lunches")
  3. Market reference — Bright Data SERP for "{commodity} commercial price"
     and parse a representative dollar figure

For each vendor, compute:
  - Range of implied unit prices across POs
  - Median unit price
  - Estimated market unit price (from SERP)
  - Markup factor (implied / market)

Flag vendors with markup factor >= 3x as POSSIBLE_MARKUP_FRAUD.

Reads from data/dgs/split_contract_dossiers/ + live CKAN lookups.
Writes data/dgs/unit_price_analysis/{vendor}.json + summary.

Cost: ~$0.05 per vendor with Bright Data (3 SERP queries each).

Usage:
    # No Bright Data — just internal qty extraction
    python -m src.dgs.unit_price_analyzer

    # Full analysis with market price references
    python -m src.dgs.unit_price_analyzer --use-brightdata --budget 2
"""

import argparse
import json
import os
import re
from collections import defaultdict
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = Path("data/dgs/unit_price_analysis")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CKAN_BASE = "https://data.ca.gov/api/3/action/datastore_search"
RESOURCE_ID = os.environ.get("DGS_PO_RESOURCE_ID", "")

# Regex patterns to extract quantities from descriptions
QUANTITY_PATTERNS = [
    # "12 each", "12 ea", "12 ct"
    (re.compile(r"\b(\d+(?:,\d{3})*)\s*(?:each|ea|ct|count|pieces?|pcs?|units?)\b", re.I),
     "each"),
    # "5 cases", "10 box", "20 boxes"
    (re.compile(r"\b(\d+(?:,\d{3})*)\s*(?:cases?|boxes?|bx|cartons?|cases? of)\b", re.I),
     "case"),
    # "100 lunches", "200 meals"
    (re.compile(r"\b(\d+(?:,\d{3})*)\s*(?:lunches?|meals?|sack\s*lunches?)\b", re.I),
     "meal"),
    # "5 cylinders", "10 tanks"
    (re.compile(r"\b(\d+(?:,\d{3})*)\s*(?:cylinders?|tanks?|bottles?|drums?)\b", re.I),
     "cylinder"),
    # "100 gallons", "5000 gal"
    (re.compile(r"\b(\d+(?:,\d{3})*)\s*(?:gallons?|gal\b)", re.I), "gallon"),
    # "5 hours", "100 hrs"
    (re.compile(r"\b(\d+(?:,\d{3})*)\s*(?:hours?|hrs?)\b", re.I), "hour"),
    # "12 month rental", "annual rental"
    (re.compile(r"\b(\d+)\s*(?:months?\s*rental|month\s*rental)\b", re.I), "month"),
    # "qty: 100", "quantity: 50"
    (re.compile(r"qu?ant?(?:ity)?\s*[:=]\s*(\d+(?:,\d{3})*)\b", re.I), "qty"),
]

# Rough market reference prices (as fallback when SERP doesn't find one).
# These are conservative midpoints — used only when SERP fails.
MARKET_REFERENCE_FALLBACK = {
    "meal": 18.0,        # commercial catered sack lunch ~$15-20
    "cylinder": 25.0,    # industrial gas cylinder monthly rental
    "gallon": 4.5,       # diesel/gas wholesale ~$4-5
    "hour": 150.0,       # professional services hour
    "case": 75.0,        # generic case-priced supplies
    "month": 200.0,      # equipment rental month
    "each": 50.0,        # generic each-priced item
    "qty": 50.0,
}


def slug(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", s.lower()).strip("_")[:60]


def load_anchor_vendors() -> list[dict]:
    """Pull the STRONG_SPLIT_CONTRACT_PATTERN vendors from previous analysis."""
    dossier_dir = Path("data/dgs/split_contract_dossiers")
    if not dossier_dir.exists():
        return []
    out = []
    for p in dossier_dir.glob("*.json"):
        with open(p) as f:
            d = json.load(f)
        if d.get("analysis", {}).get("verdict") in (
            "STRONG_SPLIT_CONTRACT_PATTERN", "POSSIBLE_SPLIT_CONTRACT"
        ):
            top_desc = ""
            descs = d["analysis"].get("near_threshold_top_descriptions") or []
            if descs:
                top_desc = descs[0]["description"]
            out.append({
                "vendor": d["vendor"],
                "threshold": d["flagged_threshold"],
                "top_description": top_desc,
            })
    return out


def fetch_vendor_pos(vendor: str) -> pd.DataFrame:
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
        records = [
            rec for rec in records
            if any(vendor.lower() in str(v).lower()
                   for k, v in rec.items()
                   if "supplier" in k.lower() or "vendor" in k.lower())
        ]
        rows.extend(records)
        offset += 500
        if offset > 3000:
            break
    return pd.DataFrame(rows)


def extract_quantity(description: str) -> tuple[float | None, str | None]:
    """Try every regex pattern. Return (quantity, unit) or (None, None)."""
    if not description or not isinstance(description, str):
        return None, None
    for pattern, unit in QUANTITY_PATTERNS:
        m = pattern.search(description)
        if m:
            try:
                qty = float(m.group(1).replace(",", ""))
                if qty > 0:
                    return qty, unit
            except ValueError:
                continue
    return None, None


def find_columns(df: pd.DataFrame) -> dict:
    """Map known column names to our normalized names."""
    out = {}
    for c in df.columns:
        cl = c.lower().strip()
        if cl == "supplier name" or "supplier" in cl:
            out["vendor"] = c
        elif cl == "department name":
            out["buyer"] = c
        elif cl == "total price" or cl == "amount":
            out["amount"] = c
        elif cl == "item description" or "description" in cl:
            out.setdefault("description", c)
        elif cl == "quantity" or "qty" in cl:
            out["quantity_col"] = c
        elif "unit price" in cl or "unit cost" in cl:
            out["unit_price_col"] = c
        elif "unit of measure" in cl or cl == "uom":
            out["uom_col"] = c
        elif cl == "purchase date" or cl == "date":
            out.setdefault("date", c)
    return out


def get_market_reference(commodity: str, unit: str, bd_client) -> dict | None:
    """SERP for market prices on this commodity-unit."""
    if not bd_client:
        return None
    queries = {
        "meal": [f"commercial catered sack lunch price per meal California",
                 f"box lunch catering cost per person"],
        "cylinder": [f"industrial gas cylinder rental monthly price",
                     f"Airgas argon cylinder rental cost"],
        "gallon": [f"diesel fuel wholesale price gallon California",
                   f"gasoline commercial bulk price gallon"],
        "hour": [f"{commodity} consultant hourly rate California",
                 f"professional services hourly billing rate"],
        "case": [f"{commodity} bulk case price",
                 f"medical supplies case wholesale"],
    }
    qs = queries.get(unit, [f"{commodity} market price per {unit}"])

    prices_found = []
    for q in qs[:2]:
        r = bd_client.serp(q)
        for o in r.get("organic", [])[:5]:
            text = (o.get("title", "") + " " + o.get("description", "")).lower()
            # Naive $ extraction
            for m in re.finditer(r"\$\s*(\d{1,4}(?:\.\d{1,2})?)", text):
                try:
                    p = float(m.group(1))
                    if 1 <= p <= 1000:  # sanity range
                        prices_found.append(p)
                except ValueError:
                    continue

    if prices_found:
        prices_found.sort()
        median_price = prices_found[len(prices_found) // 2]
        return {
            "median_market_price": median_price,
            "sample_size": len(prices_found),
            "source": "serp",
        }
    return None


def analyze_vendor(vendor_name: str, anchor: dict, bd_client) -> dict:
    df = fetch_vendor_pos(vendor_name)
    if df.empty:
        return {"vendor": vendor_name, "status": "NO_POS_FOUND"}

    cols = find_columns(df)
    if "amount" not in cols:
        return {"vendor": vendor_name, "status": "NO_AMOUNT_COL"}

    amount_col = cols["amount"]
    df[amount_col] = pd.to_numeric(
        df[amount_col].astype(str).str.replace(r"[^\d.]", "", regex=True),
        errors="coerce",
    )

    desc_col = cols.get("description")
    qty_col = cols.get("quantity_col")
    unit_price_col = cols.get("unit_price_col")

    # Per-PO unit price extraction
    records = []
    for _, row in df.iterrows():
        amount = float(row.get(amount_col) or 0)
        if amount <= 0:
            continue
        desc = str(row.get(desc_col, "")) if desc_col else ""

        # Prefer explicit columns when present
        qty = None
        unit = None
        if qty_col:
            try:
                qty = float(str(row.get(qty_col, "")).replace(",", ""))
                unit = "explicit"
            except (ValueError, TypeError):
                pass
        if qty is None:
            qty, unit = extract_quantity(desc)

        if unit_price_col:
            try:
                up = float(str(row.get(unit_price_col, "0"))
                          .replace("$", "").replace(",", ""))
                records.append({
                    "amount": amount,
                    "qty": qty,
                    "unit": unit,
                    "implied_unit_price": up,
                    "source": "explicit_column",
                    "description": desc[:200],
                })
                continue
            except (ValueError, TypeError):
                pass

        if qty and qty > 0:
            implied = amount / qty
            records.append({
                "amount": amount,
                "qty": qty,
                "unit": unit,
                "implied_unit_price": implied,
                "source": "description_regex",
                "description": desc[:200],
            })
        else:
            records.append({
                "amount": amount,
                "qty": None,
                "unit": None,
                "implied_unit_price": None,
                "source": "no_qty",
                "description": desc[:200],
            })

    with_qty = [r for r in records if r["implied_unit_price"] is not None]
    if not with_qty:
        return {
            "vendor": vendor_name,
            "status": "NO_QTY_EXTRACTABLE",
            "total_pos": len(records),
            "sample_descriptions": [r["description"] for r in records[:5]],
        }

    # By unit
    by_unit = defaultdict(list)
    for r in with_qty:
        if r.get("unit"):
            by_unit[r["unit"]].append(r["implied_unit_price"])

    unit_analysis = {}
    flagged_unit_groups = []
    for unit, prices in by_unit.items():
        if not prices:
            continue
        prices.sort()
        median = prices[len(prices) // 2]
        unit_data = {
            "median_implied_unit_price": median,
            "min": prices[0],
            "max": prices[-1],
            "sample_size": len(prices),
        }

        # Market reference
        if bd_client:
            ref = get_market_reference(vendor_name, unit, bd_client)
            if ref:
                unit_data["market_reference"] = ref
                markup = median / ref["median_market_price"] if ref["median_market_price"] > 0 else None
                unit_data["markup_factor"] = round(markup, 2) if markup else None
        if "markup_factor" not in unit_data and unit in MARKET_REFERENCE_FALLBACK:
            ref_price = MARKET_REFERENCE_FALLBACK[unit]
            unit_data["market_reference"] = {
                "median_market_price": ref_price,
                "source": "fallback_estimate",
            }
            unit_data["markup_factor"] = round(median / ref_price, 2) if ref_price > 0 else None

        if unit_data.get("markup_factor", 0) and unit_data["markup_factor"] >= 3:
            flagged_unit_groups.append({"unit": unit, **unit_data})
        unit_analysis[unit] = unit_data

    verdict = ("POSSIBLE_MARKUP_FRAUD" if flagged_unit_groups else
               "WITHIN_REASONABLE_RANGE" if unit_analysis else
               "INCONCLUSIVE")

    return {
        "vendor": vendor_name,
        "anchor_threshold": anchor.get("threshold"),
        "anchor_description": anchor.get("top_description"),
        "verdict": verdict,
        "total_pos_analyzed": len(records),
        "pos_with_qty_extracted": len(with_qty),
        "by_unit": unit_analysis,
        "flagged_unit_groups": flagged_unit_groups,
        "sample_records": with_qty[:10],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--use-brightdata", action="store_true")
    parser.add_argument("--budget", type=float, default=2.0)
    args = parser.parse_args()

    anchors = load_anchor_vendors()
    if not anchors:
        print("No anchor vendors. Run split_contract_deepdive first.")
        return
    print(f"Analyzing unit pricing for {len(anchors)} vendors...")

    bd_client = None
    if args.use_brightdata:
        from src.bright_data.client import BrightDataClient
        bd_client = BrightDataClient(budget_cap=args.budget,
                                     label="unit_price")

    summary = []
    for i, a in enumerate(anchors, 1):
        v = a["vendor"]
        print(f"\n[{i}/{len(anchors)}] {v}")
        try:
            result = analyze_vendor(v, a, bd_client)
        except Exception as e:
            print(f"  ERROR: {e}")
            continue

        with open(OUTPUT_DIR / f"{slug(v)}.json", "w") as f:
            json.dump(result, f, indent=2, default=str)

        status = result.get("verdict") or result.get("status")
        print(f"  -> {status}")
        if result.get("verdict") == "POSSIBLE_MARKUP_FRAUD":
            for group in result.get("flagged_unit_groups", []):
                print(f"     ⚠️  {group['unit']}: "
                      f"${group['median_implied_unit_price']:.2f}/unit vs "
                      f"market ~${group['market_reference']['median_market_price']:.2f} "
                      f"= {group['markup_factor']}× markup")
        elif result.get("status") == "NO_QTY_EXTRACTABLE":
            print(f"     Sample descriptions:")
            for d in result.get("sample_descriptions", [])[:3]:
                print(f"       \"{d[:80]}\"")

        summary.append({
            "vendor": v,
            "verdict": result.get("verdict") or result.get("status"),
            "flagged_groups": len(result.get("flagged_unit_groups", [])),
            "pos_with_qty": result.get("pos_with_qty_extracted", 0),
        })

    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump({"vendors_analyzed": len(summary), "summary": summary},
                  f, indent=2)

    print(f"\n{'='*60}")
    print(f"UNIT PRICE ANALYSIS COMPLETE")
    flagged = [s for s in summary if s["verdict"] == "POSSIBLE_MARKUP_FRAUD"]
    if flagged:
        print(f"\n  🚨 POSSIBLE MARKUP FRAUD ({len(flagged)} vendors):")
        for s in flagged:
            print(f"    {s['vendor'][:35]:35s} "
                  f"({s['flagged_groups']} unit groups flagged)")
    if bd_client:
        print(f"\n  {bd_client.report()}")
    print(f"\n  Per-vendor dossiers: data/dgs/unit_price_analysis/*.json")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
