# Round 3 Runbook
*Three new attack surfaces, each independent. Run in any order.*

## Track B — Nonprofit Overhead Audit (highest upside)

Pulls Form 990s from ProPublica for every nonprofit grant recipient. Computes
overhead ratios, exec comp ratios, YoY mgmt-overhead spikes. Flags orgs where
program expense ratio < 65%, exec comp > $300K at a small org, or state
funding exceeds reported total revenue.

**Cost:** Free (ProPublica is free) up to ~5 req/sec. Add `--use-brightdata`
to route through Web Unlocker — cost ~$0.001 per request → ~$5-10 for 500 orgs.

```bash
# Smoke test (no Bright Data, 10 orgs)
python -m src.track_b.overhead_audit --top 10

# Full sweep with Bright Data routing
python -m src.track_b.overhead_audit --top 500 --use-brightdata --budget 30
```

**Outputs:**
- `data/track_b/overhead_results.json`
- `data/track_b/overhead_report.md`
- `data/track_b/org_index.json` (name→EIN cache)
- `data/track_b/filings/{ein}.json` (per-org cache)

**What to look for in output:**
- `verdict: FLAGGED_HIGH` orgs — start there
- `STATE_FUNDING_EXCEEDS_REPORTED_REVENUE` flag — the strongest signal
- `MGMT_OVERHEAD_YOY_SPIKE` flag — admin costs grew >50% YoY

---

## FI$Cal Vendor Scrape (best Bright Data showcase)

Drives open.fiscal.ca.gov with **Bright Data Scraping Browser** (the full
headless Chrome) to download actual state cash flow CSVs. Then matches vendor
names against grant recipients to find dual-payment patterns.

**Required env var:**
```
BRIGHT_DATA_BROWSER_AUTH=brd-customer-XXX-zone-YOUR_BROWSER_ZONE:PASSWORD
```
Get from https://brightdata.com/cp/zones (create a "Scraping Browser" zone).

**Cost:** ~$1-3 per fiscal year × account code.

```bash
# Need playwright once:
pip install playwright && playwright install chromium

# Pull professional services for FY 2024
python -m src.bright_data.fiscal_scrape --account 5340 --year 2024

# Pull construction for FY 2024
python -m src.bright_data.fiscal_scrape --account 5442 --year 2024

# If portal selectors don't match (they change), download CSV manually
# and place in data/bright_data/fiscal/, then:
python -m src.bright_data.fiscal_scrape --account 5340 --year 2024 --skip-scrape
```

**Outputs:**
- `data/bright_data/fiscal/vendor_tx_{account}_FY{year}.csv` (raw)
- `data/bright_data/fiscal/crossref_{account}_FY{year}.json` (matches)

**What to look for:** any entity in `matches[]` with significant amounts on
**both** sides (grant_total AND vendor_total) — that's a recipient who's
getting both grant money AND vendor payments from the state for the same
period. Strong double-dipping or sub-contracting signal.

---

## DGS Purchase Order Anomalies (Caltrans-pattern hunt)

Scans DGS purchase order data for the patterns that surfaced in the only
successful CA infrastructure fraud prosecution of the last decade.

**Set env var:**
```
DGS_PO_RESOURCE_ID=<resource_id_from_data.ca.gov>
```
Find at https://data.ca.gov/dataset/purchase-order-data — copy the latest
fiscal year's resource ID.

**Cost:** Free. CKAN API only.

```bash
python -m src.dgs.purchase_orders --source api
```

**Outputs:**
- `data/dgs/po_anomalies.json`
- `data/dgs/po_anomalies.md`

**Four patterns flagged:**
1. **Buyer-vendor concentration** — one buyer issuing 75%+ of spend to one vendor
2. **Repeat winners** — vendor winning 10+ POs from same buyer
3. **Just-under-threshold** — POs at $4,999 / $9,999 / $49,999 (split contracts)
4. **Repeating exact amounts** — same dollar amount across 3+ POs to same vendor
5. **Vague high-value POs** — "services", "miscellaneous", >$25K, short description

---

## Suggested Order

1. **DGS POs first** (5 min, free, no setup) — see if the historical fraud
   pattern shows up at all in current data.
2. **Track B with `--top 50` then `--use-brightdata`** (10-15 min) — this is
   the biggest fraud-finding bet. Smoke test free first to confirm the
   ProPublica matches look reasonable.
3. **FI$Cal scrape** (15-30 min once Scraping Browser is set up) — the
   biggest hackathon-optics piece because it uses the headline Bright Data
   product.

If any of these surface real signal, the wrap-up note in `ROUND1_WRAPUP.md`
can be expanded with a "Round 3 Findings" section.
