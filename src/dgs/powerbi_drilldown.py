"""
Power BI DGS Report Drilldown — Scraping Browser into the actual state dashboard.

California publishes DGS PO line-item detail in a Power BI public-embed
report. The CKAN export is a summary view; the Power BI report has the
underlying line items (quantity, unit, item description per line).

This was discovered manually — a user looked up "Panini Time" in the
Power BI search and saw the per-PO breakdown.

Strategy: drive the Power BI iframe via Bright Data Scraping Browser,
search by vendor, screenshot + DOM-extract the visible table data.

Power BI publish-to-web iframes use opaque embed tokens and render data
client-side after multiple round-trips. Direct HTTP scraping fails; you
need a real browser session. Bright Data Scraping Browser is precisely
designed for this.

Required env:
    BRIGHT_DATA_BROWSER_AUTH=brd-customer-XXX-zone-YYY:PASSWORD

Cost: ~$0.05-0.15 per vendor drilldown (session time).

Usage:
    # Drill Panini Time via the known public Power BI URL
    python -m src.dgs.powerbi_drilldown \\
        --url "https://app.powerbigov.us/view?r=eyJrIjoi..." \\
        --vendor "Panini Time"

    # Just navigate + screenshot + extract everything visible
    python -m src.dgs.powerbi_drilldown --url "<URL>"
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = Path("data/dgs/powerbi")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

BROWSER_AUTH = os.environ.get("BRIGHT_DATA_BROWSER_AUTH", "")


def slug(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", s.lower()).strip("_")[:60]


def drill(report_url: str, vendor: str | None) -> dict:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Need: pip install playwright && playwright install chromium")
        sys.exit(1)

    if not BROWSER_AUTH:
        print("BRIGHT_DATA_BROWSER_AUTH not set in .env")
        print("Get it from your Scraping Browser zone in brightdata.com/cp")
        sys.exit(1)

    ws_url = f"wss://{BROWSER_AUTH}@brd.superproxy.io:9222"
    out = {"report_url": report_url, "vendor": vendor}

    print("Connecting to Scraping Browser...")
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(ws_url)
        try:
            ctx = browser.contexts[0] if browser.contexts else browser.new_context()
            page = ctx.new_page()
            page.set_viewport_size({"width": 1600, "height": 1000})

            print(f"  Navigating to {report_url[:80]}...")
            page.goto(report_url, timeout=90000, wait_until="domcontentloaded")
            print("  Waiting for Power BI to render (15s)...")
            page.wait_for_timeout(15000)

            # Find Power BI iframe
            print("  Locating Power BI iframe...")
            try:
                page.wait_for_selector("iframe", timeout=20000)
            except Exception:
                pass

            iframe_handle = None
            for fr in page.frames:
                if "powerbi" in (fr.url or "").lower() or "powerbi" in (fr.name or ""):
                    iframe_handle = fr
                    break
            if iframe_handle is None and len(page.frames) > 1:
                iframe_handle = page.frames[1]

            target = iframe_handle or page

            # Screenshot the rendered state
            shot_path = OUTPUT_DIR / f"{slug(vendor or 'report')}_initial.png"
            page.screenshot(path=str(shot_path), full_page=True)
            out["initial_screenshot"] = str(shot_path)
            print(f"  Saved screenshot: {shot_path}")

            # If a vendor name given, try to type it into the search box
            if vendor:
                # Power BI search boxes are typically textboxes inside a slicer
                print(f"  Searching for vendor: {vendor}")
                try:
                    # Try common search box selectors inside the iframe
                    selectors = [
                        '[role="searchbox"]',
                        'input[type="text"]',
                        '[aria-label*="search" i]',
                        '[placeholder*="search" i]',
                        '.searchInput',
                    ]
                    found = False
                    for sel in selectors:
                        try:
                            els = target.locator(sel)
                            if els.count() > 0:
                                els.first.click(timeout=3000)
                                els.first.fill(vendor)
                                page.keyboard.press("Enter")
                                page.wait_for_timeout(8000)
                                found = True
                                print(f"    used selector {sel}")
                                break
                        except Exception:
                            continue
                    if not found:
                        print("    no search box found — trying keyboard search")
                        page.keyboard.press("Control+F")
                        page.wait_for_timeout(500)
                        page.keyboard.type(vendor)
                        page.wait_for_timeout(2000)
                except Exception as e:
                    print(f"    search attempt failed: {e}")

                shot_path2 = OUTPUT_DIR / f"{slug(vendor)}_searched.png"
                page.screenshot(path=str(shot_path2), full_page=True)
                out["search_screenshot"] = str(shot_path2)
                print(f"  Saved search screenshot: {shot_path2}")

            # Extract all visible text from the iframe
            print("  Extracting visible text...")
            try:
                full_text = target.locator("body").inner_text(timeout=20000)
            except Exception:
                full_text = ""
            out["extracted_text_length"] = len(full_text)

            text_path = OUTPUT_DIR / f"{slug(vendor or 'report')}_text.txt"
            with open(text_path, "w") as f:
                f.write(full_text)
            out["text_dump"] = str(text_path)

            # Try to pull table rows specifically (Power BI uses divs with role=row)
            print("  Extracting table rows...")
            rows = []
            try:
                row_locator = target.locator('[role="row"]')
                cnt = row_locator.count()
                for i in range(min(cnt, 200)):
                    rows.append(row_locator.nth(i).inner_text().strip())
            except Exception:
                pass
            out["table_rows_count"] = len(rows)
            out["table_rows"] = rows[:200]

            # Heuristic: parse qty / amount patterns from text
            qty_amt = re.findall(
                r"(\d{1,5}(?:\.\d{1,2})?)\s*(each|ea|lunches?|meals?|cylinders?|gallons?|cases?|hours?)\b[\s\S]{0,300}?\$\s*(\d{1,7}(?:,\d{3})*(?:\.\d{1,2})?)",
                full_text, re.I,
            )
            qty_unit_amts = [
                {"qty": float(q.replace(",", "")), "unit": u,
                 "amount": float(a.replace(",", ""))}
                for q, u, a in qty_amt
            ]
            out["qty_unit_amount_triples"] = qty_unit_amts[:50]

            # Implied unit prices
            if qty_unit_amts:
                from collections import defaultdict
                by_unit = defaultdict(list)
                for ext in qty_unit_amts:
                    if ext["qty"] > 0:
                        by_unit[ext["unit"].lower()].append(
                            ext["amount"] / ext["qty"])
                unit_summary = {}
                for unit, prices in by_unit.items():
                    prices.sort()
                    unit_summary[unit] = {
                        "median_implied_unit_price": prices[len(prices)//2],
                        "min": prices[0], "max": prices[-1], "n": len(prices),
                    }
                out["implied_unit_prices"] = unit_summary

            # PO number pattern (Cal eProcure-style)
            po_ids = list(set(re.findall(r"\b(?:PO|P\.O\.|Purchase Order)\s*[#:]?\s*([A-Z0-9-]{6,20})\b", full_text)))
            out["po_ids_found"] = po_ids[:50]

        finally:
            browser.close()

    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True,
                        help="Power BI public-embed URL (app.powerbigov.us/view?r=...)")
    parser.add_argument("--vendor", default=None,
                        help="Vendor name to search inside the report")
    args = parser.parse_args()

    print(f"Power BI drilldown — vendor: {args.vendor or 'no search'}")
    result = drill(args.url, args.vendor)

    out_path = OUTPUT_DIR / f"{slug(args.vendor or 'report')}.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2, default=str)

    print(f"\n{'='*60}")
    print(f"POWER BI DRILLDOWN COMPLETE")
    print(f"  Extracted text: {result.get('extracted_text_length', 0)} chars")
    print(f"  Table rows: {result.get('table_rows_count', 0)}")
    print(f"  PO IDs found: {len(result.get('po_ids_found', []))}")
    triples = result.get("qty_unit_amount_triples", [])
    print(f"  qty/unit/amount triples extracted: {len(triples)}")

    if result.get("implied_unit_prices"):
        print(f"\n  💰 IMPLIED UNIT PRICES:")
        for unit, stats in result["implied_unit_prices"].items():
            print(f"    {unit:15s} median ${stats['median_implied_unit_price']:.2f} "
                  f"(range ${stats['min']:.2f}-${stats['max']:.2f}, "
                  f"n={stats['n']})")
        # Compare to market for meals
        if "meal" in result["implied_unit_prices"] or "lunch" in result["implied_unit_prices"]:
            unit = "meal" if "meal" in result["implied_unit_prices"] else "lunch"
            implied = result["implied_unit_prices"][unit]["median_implied_unit_price"]
            market_ref = 18.0  # commercial catered lunch ~$15-20
            markup = implied / market_ref
            print(f"\n  📊 SACK LUNCH UNIT PRICE: ${implied:.2f} vs commercial market ~${market_ref:.2f}")
            print(f"     Markup factor: {markup:.1f}×")
            if markup >= 3:
                print(f"     🚨 POSSIBLE MARKUP FRAUD")

    print(f"\n  Output: {out_path}")
    print(f"  Screenshots: {OUTPUT_DIR}/*.png")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
