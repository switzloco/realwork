# RealWork — AI-Driven Public Spending Anomaly Detection

**Mission:** Identify likely fraud in California public spending by inverting the normal approach — AI picks the targets first, web scraping gathers the corroborating evidence second.

**Hackathon:** Lablab.ai "Web Data UNLOCKED" (May 25–31, 2026) — submitted ✓  
**Bright Data Budget:** $250 hard cap (actual spend tracked in `data/ledger.jsonl`)  
**Live demo:** [switzloco.github.io/realwork](https://switzloco.github.io/realwork)

---

## What We Actually Built

The original plan was a generic state infrastructure grants scanner ("Ghost Infrastructure"). That pivot happened fast once we hit real data. Two concrete investigations shipped:

### 1. DGS Procurement Threshold Analysis

California's Department of General Services publishes all state purchase orders. Filtering for amounts clustered just below competitive-bidding thresholds surfaces a classic fraud pattern: **12 purchase orders to a single vendor at exactly $49,950** (the CA threshold is $50,000), all to Cal Fire, all signed by one procurement officer within a 17-day window during active wildfire operations.

**Code:** `src/dgs/` — threshold clustering, OSINT sweep, Panini Time vendor investigation  
**Bright Data usage:** SERP API (10 queries, vendor discovery) + Web Unlocker (LinkedIn, SAM.gov, OpenCorporates follow-ups)

### 2. LA Alliance PDF Black Hole

LA County publishes 1,652 invoices from homeless-service providers as raw scanned PDFs. No CSV, no API — the billing detail is locked inside files no auditor can query. We turned them into a structured dataset.

**Pipeline:** Bright Data Web Unlocker (binary PDF fetch) → Gemini 2.5 Flash (native PDF vision, no OCR) → Pydantic normalization → public ledger  
**Result:** 123 invoices extracted, $22.8M structured, 70 providers identified  
**Bonus:** Gemini 2.5 Pro with Google Search grounding decoded billing codes (D7, PHK, SAM), looked up contracted MOU rates, and flagged billing patterns consistent with known Medi-Cal violations. Those findings are under private review.

**Code:** `src/la_alliance/` — discovery, fetch, extraction, risk analysis  
**Bright Data usage:** Web Unlocker (binary PDF fetch), SERP (Algolia index discovery)

---

## Architecture

```
                     Public Data Sources
                    (CA Open Data, Socrata,
                     DGS PO export, LA Algolia)
                              │
                              ▼
                    ┌─────────────────┐
                    │   ETL / Ingest  │   No Bright Data spend here
                    │  (src/etl/)     │
                    └────────┬────────┘
                             │  clean structured records
                             ▼
                    ┌─────────────────┐
                    │  Red Flag       │   Gemini 2.5 Pro
                    │  Analyst        │   + Google Search grounding
                    │  (Stage 1)      │   — zero scraping cost
                    └────────┬────────┘
                             │  ranked targets with evidence brief
                             ▼
                    ┌─────────────────┐
                    │  Evidence       │   Bright Data:
                    │  Gathering      │   SERP API + Web Unlocker
                    │  (Stage 2)      │   + fetch_bytes (PDFs)
                    └────────┬────────┘
                             │
                    ┌────────┘
                    │  Budget Controller gates every API call
                    │  (src/bright_data/client.py)
                    ▼
                    ┌─────────────────┐
                    │  Risk Analysis  │   Gemini 2.5 Pro + grounding
                    │  + Synthesis    │   decodes billing codes,
                    │  (Stage 3)      │   finds contracted rates
                    └────────┬────────┘
                             │
                             ▼
                    ledger.json → GitHub Pages live site
```

---

## Key Components

### `src/bright_data/client.py`
Single Bright Data client used by the whole pipeline. Every call is budget-tracked and written to a JSONL ledger.

```python
client = BrightDataClient(budget_cap=50.0, label="la_alliance")
client.serp(query)          # SERP API
client.unlock(url)          # Web Unlocker (HTML)
client.fetch_bytes(url)     # Web Unlocker (binary — PDFs, images)
client.report()             # "spent $X.XX of $Y.YY"
```

`BudgetExceeded` is raised (not swallowed) when the cap is hit — callers can break cleanly.

### `src/la_alliance/invoice_extractor.py`
Three discovery modes → unified pipeline:

```bash
# local PDFs already downloaded
python -m src.la_alliance.invoice_extractor --pdf-dir data/la_alliance/raw --limit 50

# JSON manifest of {title, url} pairs
python -m src.la_alliance.invoice_extractor --manifest data/la_alliance/manifest.json

# Socrata catalog (SF, Santa Clara, etc. — same Socrata API)
python -m src.la_alliance.invoice_extractor --dataset https://data.sfgov.org/resource/XXXX.json
```

Output: `data/la_alliance/ledger.json` (machine-readable) + `before_after.md` (demo-ready).

### `src/la_alliance/risk_analyst.py`
Gemini 2.5 Pro with Google Search grounding. For each invoice vendor, it looks up contracted rates from public MOU documents, decodes billing codes, and flags anomalies — without hallucinating baselines, because it searches for the actual numbers.

```bash
python -m src.la_alliance.risk_analyst --loop   # continuous post-submission mode
```

Resumable via `risk_done.txt` checkpoint. Rate-limited to 6s/request (grounding quota).

### `src/dgs/panini_osint.py`
10-query SERP sweep + targeted Web Unlocker fetches for a suspicious vendor. Writes a redacted `digest.md` (safe to commit) and a full `raw_results.json` (gitignored).

```bash
python -m src.dgs.panini_osint --budget 10
```

---

## What's Blocked (and Why)

Two planned Phase 3 routes were closed and documented in `PHASE3_BLOCKED.md`:

- **CA Secretary of State** — Bright Data policy classifies it as a government domain; returns 502 with `x-brd-error: Access denied`. No workaround within Bright Data's terms.
- **OpenCorporates** — HAProxy CAPTCHA returns 200 OK with 0-byte body even at 180s timeout. Parsers exist in `src/graph/sos_parser.py` but can't be fed real data through Web Unlocker. Future path: bulk data license or local Playwright stealth browser.

---

## Live Site

`docs/index.html` + `docs/script.js` — GitHub Pages site that fetches `ledger.json` from GitHub raw every 60s and renders live stats and a table of the latest 12 invoices.

Key hardcoded fallbacks in the HTML (123 docs / $22.8M / 70 providers) ensure the counter is never zero while the fetch is in-flight.

---

## Legal & Safety Rules

- **Language:** Never say "fraud" as a conclusion. Use "anomaly," "warrants investigation," "discrepancy." The tool identifies candidates for investigation — not legal determinations.
- **Public repos:** Real entity names in findings are redacted or omitted from commits. Raw results stay gitignored. Live demos and private reports may show real names.
- **Qui tam findings:** The billing anomalies flagged by the risk analyst (duplicate billing, prospective billing patterns) are held privately. The California False Claims Act (qui tam) rewards filing under seal *before* public disclosure. Contact a qui tam attorney (contingency, 15–30% of recovery) before any public disclosure.
- **No contact:** Do not contact any flagged entity, the awarding agency, or the press.

---

## Tech Stack

| Component | Tool |
|-----------|------|
| Pipeline orchestration | Python |
| ETL | Python (pandas, requests, Socrata API) |
| Web scraping | Bright Data Web Unlocker + SERP API |
| PDF ingestion | Gemini 2.5 Flash (native vision, no OCR) |
| Red flag analysis | Gemini 2.5 Pro + Google Search grounding |
| Budget controller | `BrightDataClient` (Python, JSONL ledger) |
| Storage | JSON/JSONL files (SQLite planned for scale) |
| Frontend | Vanilla JS, GitHub Pages |

---

## Expansion: SF + Santa Clara

Both counties use Socrata open data portals — the existing `--dataset` flag in `invoice_extractor.py` connects directly. Tabular contract/payment data needs no Bright Data at all (direct Socrata API). PDF invoice batches would use the same Web Unlocker + Gemini path as LA.

Estimated Bright Data spend for a 200-vendor sweep of both counties: **$5–15**.

Top California counties by homeless services spend (expansion priority order):

| County | Est. annual spend | Portal |
|--------|-------------------|--------|
| Los Angeles | ~$3B+ | `data.lacounty.gov` ✓ done |
| San Francisco | ~$800M–$1.2B | `data.sfgov.org` |
| Santa Clara | ~$400–600M | `data.sccgov.org` |
| Alameda | ~$300–400M | `data.acgov.org` |
| San Diego | ~$250–350M | `data.sandiegocounty.gov` |
