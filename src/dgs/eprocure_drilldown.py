"""
Cal eProcure Drilldown — fetch line-item detail for specific PO IDs.

The DGS CKAN export gives us total price per PO. But the *actual* fraud
signal is per-line: how many sack lunches, at what unit price each? That
data lives in Cal eProcure (caleprocure.ca.gov), California's procurement
search portal.

Cal eProcure is a JavaScript-rendered SPA that blocks ordinary scrapers.
Bright Data Scraping Browser drives a real headless Chrome session
through their proxy network, so it sees the same data a human browser
would. This is the headline Bright Data product applied to the exact
data gap that turns "pattern" into "evidence."

For each PO ID:
  1. Navigate to Cal eProcure SCPRS search
  2. Search by PO number
  3. Open the PO detail page
  4. Extract line items: description, quantity, unit, unit price, total

Output: data/dgs/eprocure_drilldown/{po_id}.json with full line items.

Required env:
    BRIGHT_DATA_BROWSER_AUTH=brd-customer-XXX-zone-YYY:PASSWORD

Cost: ~$0.02-0.05 per PO drilldown (Scraping Browser session time).

Usage:
    # Drill into Panini Time's 12 just-under POs
    python -m src.dgs.eprocure_drilldown --vendor "Panini Time"

    # Drill into specific PO IDs
    python -m src.dgs.eprocure_drilldown --po-ids "PO12345,PO67890"
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = Path("data/dgs/eprocure_drilldown")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

BROWSER_AUTH = os.environ.get("BRIGHT_DATA_BROWSER_AUTH", "")
CKAN_BASE = "https://data.ca.gov/api/3/action/datastore_search"
RESOURCE_ID = os.environ.get("DGS_PO_RESOURCE_ID", "")

EPROCURE_SEARCH_URL = "https://caleprocure.ca.gov/pages/public-search.aspx"


def get_po_ids_for_vendor(vendor: str, threshold: int = 49999,
                           band: int = 100) -> list[dict]:
    """Pull the PO IDs from CKAN for a vendor at threshold edge."""
    if not RESOURCE_ID:
        print("DGS_PO_RESOURCE_ID not set")
        return []
    rows = []
    offset = 0
    while True:
        r = requests.get(CKAN_BASE, params={
            "resource_id": RESOURCE_ID, "limit": 500,
            "offset": offset, "q": vendor,
        }, timeout=60)
        r.raise_for_status()
        records = r.json()["result"]["records"]
        if not records:
            break
        for rec in records:
            v = None
            for k, val in rec.items():
                if "supplier" in k.lower() and "name" in k.lower():
                    v = str(val)
                    break
            if not v or vendor.lower() not in v.lower():
                continue
            amount = None
            po_id = None
            for k, val in rec.items():
                if "total" in k.lower() and "price" in k.lower():
                    try:
                        amount = float(str(val).replace("$", "").replace(",", ""))
                    except (ValueError, TypeError):
                        pass
                if "purchase order number" in k.lower():
                    po_id = str(val)
            if amount and po_id and threshold - band <= amount <= threshold:
                rows.append({"po_id": po_id, "amount": amount, "vendor": v,
                             "raw": rec})
        offset += 500
        if offset > 3000:
            break
    return rows


def drill_po(po_id: str, page) -> dict:
    """Drive Cal eProcure to fetch line-item detail for one PO."""
    print(f"    Navigating to eProcure search...")
    page.goto(EPROCURE_SEARCH_URL, timeout=60000, wait_until="domcontentloaded")
    page.wait_for_timeout(4000)

    # Try by ID, then by name — selectors vary by portal updates
    try:
        # eProcure uses ASP.NET-style form fields
        search_box = None
        for sel in ['input[name*="PONumber"]', 'input[id*="PONumber"]',
                    'input[name*="purchase"]', '#ctl00_MainContent_txtPONumber']:
            try:
                if page.locator(sel).count() > 0:
                    search_box = page.locator(sel).first
                    break
            except Exception:
                continue
        if search_box:
            search_box.fill(po_id)
            page.keyboard.press("Enter")
            page.wait_for_timeout(5000)
    except Exception as e:
        print(f"    Search step failed: {e}")

    # Try to find result row
    html = page.content()

    # Extract line items via DOM
    line_items = []
    try:
        rows = page.locator("table tbody tr, .line-item-row")
        cnt = rows.count()
        for i in range(min(cnt, 30)):
            row = rows.nth(i)
            text = (row.inner_text() or "").strip()
            if not text or len(text) < 5:
                continue
            line_items.append({
                "raw_text": text[:500],
            })
    except Exception:
        pass

    # Regex fallback on raw HTML for qty/unit/price triples
    qty_unit_price = re.findall(
        r"(\d{1,5}(?:\.\d{1,2})?)\s*(each|ea|case|cases|cs|box|boxes|lb|lbs|gal|gallon|cylinder|meal|lunch|hour|hr|month)[\s\S]{0,200}?\$\s*(\d{1,6}(?:\.\d{1,2})?)",
        html, re.I,
    )

    return {
        "po_id": po_id,
        "page_title": page.title(),
        "page_url": page.url,
        "line_items_dom": line_items,
        "qty_unit_price_extracted": [
            {"qty": float(q), "unit": u, "price": float(p)}
            for q, u, p in qty_unit_price[:20]
        ],
        "html_snippet": html[:5000] if not line_items and not qty_unit_price else None,
    }


def run_drilldown(po_records: list[dict]) -> list[dict]:
    """Drive Scraping Browser through every PO."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Need: pip install playwright && playwright install chromium")
        sys.exit(1)

    if not BROWSER_AUTH:
        print("BRIGHT_DATA_BROWSER_AUTH not set.")
        print("Get it from your Scraping Browser zone in brightdata.com/cp")
        sys.exit(1)

    ws_url = f"wss://{BROWSER_AUTH}@brd.superproxy.io:9222"
    results = []

    print(f"Connecting to Bright Data Scraping Browser...")
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(ws_url)
        try:
            context = browser.contexts[0] if browser.contexts else browser.new_context()
            page = context.new_page()

            for i, rec in enumerate(po_records, 1):
                po_id = rec["po_id"]
                print(f"\n[{i}/{len(po_records)}] PO {po_id} (${rec['amount']:,.0f})")
                try:
                    detail = drill_po(po_id, page)
                    detail["amount"] = rec["amount"]
                    detail["vendor"] = rec["vendor"]
                    results.append(detail)

                    # Save per-PO
                    safe_id = re.sub(r"[^a-zA-Z0-9_-]", "_", po_id)[:40]
                    with open(OUTPUT_DIR / f"{safe_id}.json", "w") as f:
                        json.dump(detail, f, indent=2, default=str)

                    n_extracted = len(detail.get("qty_unit_price_extracted", []))
                    n_dom = len(detail.get("line_items_dom", []))
                    print(f"  -> {n_dom} DOM rows, {n_extracted} qty/unit/price triples")

                    if detail.get("qty_unit_price_extracted"):
                        for ext in detail["qty_unit_price_extracted"][:3]:
                            implied = ext['price'] / ext['qty'] if ext['qty'] else 0
                            print(f"     {ext['qty']} {ext['unit']} @ ${ext['price']:.2f} "
                                  f"-> ${implied:.2f}/unit")
                except Exception as e:
                    print(f"  Error: {e}")
                    results.append({"po_id": po_id, "error": str(e)})
        finally:
            browser.close()

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vendor", default=None,
                        help="Vendor name to drill (uses CKAN to find PO IDs)")
    parser.add_argument("--threshold", type=int, default=49999)
    parser.add_argument("--po-ids", default=None,
                        help="Comma-separated PO IDs (overrides --vendor)")
    parser.add_argument("--limit", type=int, default=12,
                        help="Max POs to drill per run")
    args = parser.parse_args()

    if args.po_ids:
        po_records = [{"po_id": p.strip(), "amount": 0, "vendor": ""}
                      for p in args.po_ids.split(",")]
    elif args.vendor:
        print(f"Looking up PO IDs for {args.vendor} near ${args.threshold:,}...")
        po_records = get_po_ids_for_vendor(args.vendor, args.threshold)
        print(f"  Found {len(po_records)} threshold-edge POs")
        po_records = po_records[:args.limit]
    else:
        print("Need --vendor or --po-ids")
        sys.exit(1)

    if not po_records:
        print("No POs to drill.")
        return

    results = run_drilldown(po_records)

    summary_path = OUTPUT_DIR / "_summary.json"
    with open(summary_path, "w") as f:
        json.dump({"vendor": args.vendor, "drilled": len(results),
                   "results": results}, f, indent=2, default=str)

    print(f"\n{'='*60}")
    print(f"EPROCURE DRILLDOWN COMPLETE")
    print(f"  POs drilled: {len(results)}")

    # Aggregate unit prices
    all_units = []
    for r in results:
        for ext in r.get("qty_unit_price_extracted", []):
            if ext.get("qty"):
                implied = ext["price"] / ext["qty"] if ext["qty"] else 0
                all_units.append({"unit": ext["unit"], "implied": implied,
                                  "qty": ext["qty"], "po_id": r.get("po_id")})

    if all_units:
        print(f"\n  Aggregated unit prices found:")
        from collections import defaultdict
        by_unit = defaultdict(list)
        for u in all_units:
            by_unit[u["unit"].lower()].append(u["implied"])
        for unit, prices in by_unit.items():
            prices.sort()
            median = prices[len(prices) // 2]
            print(f"    {unit}: median ${median:.2f}/unit "
                  f"(range ${prices[0]:.2f} - ${prices[-1]:.2f}, "
                  f"n={len(prices)})")
    else:
        print(f"\n  No quantity/unit data extracted — check per-PO HTML snippets")
        print(f"  Cal eProcure selectors may need updating for current UI")
    print(f"\n  Per-PO outputs: data/dgs/eprocure_drilldown/")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
