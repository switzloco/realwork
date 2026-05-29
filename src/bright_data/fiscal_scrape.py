"""
Open FI$Cal Vendor Transactions scraper — via Bright Data Scraping Browser.

The open.fiscal.ca.gov portal is a client-side rendered SPA. Web Unlocker
can fetch HTML but the data lives behind JS-rendered tables and download
buttons. Scraping Browser gives us a full headless Chrome session that
clicks through to the CSV download.

We pull two streams:
  1. Vendor Transactions (account codes 5340xxx = professional services)
  2. Vendor Transactions (account codes 5442xxx = construction)

The script saves the raw CSVs and then runs a vendor-name cross-reference
against grant recipients (reads data/grants_full.csv) to surface entities
receiving both grants AND vendor payments — a strong double-dipping signal.

Bright Data Scraping Browser is priced at ~$5/GB or ~$0.001/s of session.
This whole script should cost $1-3.

Required env var:
  BRIGHT_DATA_BROWSER_AUTH (format: brd-customer-XXX-zone-YYY:PASSWORD)
  See: https://docs.brightdata.com/scraping-automation/scraping-browser

Usage:
    python -m src.bright_data.fiscal_scrape --account 5340 --year 2024
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = Path("data/bright_data/fiscal")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

BROWSER_AUTH = os.environ.get("BRIGHT_DATA_BROWSER_AUTH", "")
PORTAL_URL = "https://open.fiscal.ca.gov/expenditures/"


def fetch_via_scraping_browser(account_prefix: str, fiscal_year: int) -> Path:
    """
    Drive open.fiscal.ca.gov with Bright Data Scraping Browser.

    Returns the path to the downloaded CSV.

    The portal has filter controls for fiscal year and account code. We
    use Playwright (connected to Bright Data's remote browser via CDP) to:
      1. Open the expenditures page
      2. Wait for the SPA to hydrate
      3. Apply filters
      4. Click the CSV export button
      5. Capture the downloaded file
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Need playwright: pip install playwright")
        sys.exit(1)

    if not BROWSER_AUTH:
        print("BRIGHT_DATA_BROWSER_AUTH not set in env.")
        print("Get from https://brightdata.com/cp/zones (Scraping Browser zone)")
        sys.exit(1)

    ws_url = f"wss://{BROWSER_AUTH}@brd.superproxy.io:9222"
    print(f"Connecting to Scraping Browser...")
    out_path = OUTPUT_DIR / f"vendor_tx_{account_prefix}_FY{fiscal_year}.csv"

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(ws_url)
        context = browser.contexts[0]
        page = context.new_page()
        try:
            page.goto(PORTAL_URL, timeout=60000, wait_until="domcontentloaded")
            print("  Page loaded — waiting for SPA hydration...")
            page.wait_for_timeout(8000)  # SPA boot

            # The portal's exact selectors change; these are best-effort.
            # Tune by visiting the live portal and copying selectors.
            try:
                page.get_by_role("combobox", name="Fiscal Year").select_option(str(fiscal_year))
            except Exception:
                pass
            try:
                page.get_by_label("Account").fill(account_prefix)
            except Exception:
                pass
            page.wait_for_timeout(3000)

            with page.expect_download(timeout=120000) as dl_info:
                page.get_by_role("button", name="Export CSV").click()
            download = dl_info.value
            download.save_as(out_path)
            print(f"  Saved: {out_path}")
        finally:
            browser.close()

    return out_path


def cross_reference_grants(csv_path: Path) -> dict:
    """Match vendor names against grant recipients. Surface dual-payment entities."""
    import pandas as pd
    from difflib import SequenceMatcher
    import re

    grants_path = Path("data/grants_full.csv")
    if not grants_path.exists():
        return {"error": "data/grants_full.csv not found"}

    grants = pd.read_csv(grants_path, low_memory=False)
    vendors = pd.read_csv(csv_path, low_memory=False)

    # Locate columns flexibly
    g_name_col = next((c for c in grants.columns
                       if "recipient" in c.lower() and "name" in c.lower()), None)
    g_amt_col = next((c for c in grants.columns
                      if "totalawardamount" in c.lower().replace(" ", "")), None)
    v_name_col = next((c for c in vendors.columns if "vendor" in c.lower()), None)
    v_amt_col = next((c for c in vendors.columns
                      if "amount" in c.lower() or "monetary" in c.lower()), None)

    if not (g_name_col and v_name_col):
        return {"error": "couldn't locate name columns",
                "grant_cols": list(grants.columns),
                "vendor_cols": list(vendors.columns)}

    def norm(n):
        n = str(n).lower().strip()
        n = re.sub(r"\b(inc|llc|corp|co|ltd|lp|lc|plc)\b\.?", "", n)
        n = re.sub(r"[^a-z0-9\s]", " ", n)
        return re.sub(r"\s+", " ", n).strip()

    grant_lookup = {}
    for _, r in grants.iterrows():
        nm = norm(r[g_name_col])
        if nm:
            amt = float(r.get(g_amt_col, 0) or 0) if g_amt_col else 0
            grant_lookup.setdefault(nm, {"name": str(r[g_name_col]), "total": 0,
                                        "count": 0})
            grant_lookup[nm]["total"] += amt
            grant_lookup[nm]["count"] += 1

    vendor_lookup = {}
    for _, r in vendors.iterrows():
        nm = norm(r[v_name_col])
        if nm:
            amt = float(r.get(v_amt_col, 0) or 0) if v_amt_col else 0
            vendor_lookup.setdefault(nm, {"name": str(r[v_name_col]), "total": 0,
                                         "count": 0})
            vendor_lookup[nm]["total"] += amt
            vendor_lookup[nm]["count"] += 1

    matches = []
    for g_norm, g in grant_lookup.items():
        if g_norm in vendor_lookup:
            v = vendor_lookup[g_norm]
            matches.append({
                "name": g["name"],
                "grant_total": g["total"],
                "grant_count": g["count"],
                "vendor_total": v["total"],
                "vendor_tx_count": v["count"],
                "combined": g["total"] + v["total"],
            })
    matches.sort(key=lambda x: -x["combined"])

    return {
        "match_count": len(matches),
        "matches": matches,
        "grant_recipients_checked": len(grant_lookup),
        "vendors_checked": len(vendor_lookup),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--account", default="5340",
                        help="Account code prefix (5340=prof services, 5442=construction)")
    parser.add_argument("--year", type=int, default=2024,
                        help="Fiscal year")
    parser.add_argument("--skip-scrape", action="store_true",
                        help="Skip scraping; just run cross-reference on existing CSV")
    args = parser.parse_args()

    csv_path = OUTPUT_DIR / f"vendor_tx_{args.account}_FY{args.year}.csv"

    if not args.skip_scrape:
        csv_path = fetch_via_scraping_browser(args.account, args.year)

    if not csv_path.exists():
        print(f"No CSV at {csv_path} — cannot cross-reference")
        return

    print("\nCross-referencing against grant recipients...")
    result = cross_reference_grants(csv_path)
    out_json = OUTPUT_DIR / f"crossref_{args.account}_FY{args.year}.json"
    with open(out_json, "w") as f:
        json.dump(result, f, indent=2, default=str)

    if "error" in result:
        print(f"Error: {result['error']}")
        return

    print(f"\n{'='*60}")
    print(f"FI$CAL VENDOR CROSS-REFERENCE")
    print(f"  Grant recipients: {result['grant_recipients_checked']:,}")
    print(f"  Vendors: {result['vendors_checked']:,}")
    print(f"  Dual-payment matches: {result['match_count']}")
    if result["matches"]:
        print(f"\n  Top matches (grants + vendor payments):")
        for m in result["matches"][:20]:
            print(f"    {m['name'][:40]:40s} grants ${m['grant_total']:>12,.0f} "
                  f"vendor ${m['vendor_total']:>12,.0f}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
