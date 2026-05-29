# Round 4 Runbook — Validate the Findings
*Goal: turn Round 3 leads into defensible, publishable findings.*

We have three real signals from Round 3:
1. **DGS split-contract pattern** ($49,950 × 7 to one vendor) — needs cluster verification
2. **4 nonprofits with YoY exec comp spikes** — needs EIN match validation
3. **No SAM.gov debarment check has ever been run** — free smoking-gun lookup

This runbook turns each into something a journalist or auditor could act on.

---

## 1. DGS Split-Contract Deep Dive

For every just-under-threshold vendor in `data/dgs/po_anomalies.json`, pull
their full PO history and check the cluster structure:
- Same buyer issued all the suspect POs? (same decision-maker)
- Within a 7-day window? (one need split up, not ongoing relationship)
- Same description? (one job in pieces)
- Total lifetime value with that buyer?

Verdicts:
- `STRONG_SPLIT_CONTRACT_PATTERN` — meets ≥5 of the suspicion criteria
- `POSSIBLE_SPLIT_CONTRACT` — meets ≥3
- `INCONCLUSIVE_OR_LIKELY_BENIGN` — could be normal procurement

```bash
# Free (just hits CKAN)
python -m src.dgs.split_contract_deepdive --top 10

# With Bright Data enrichment (vendor existence/news/registry checks)
python -m src.dgs.split_contract_deepdive --top 10 --use-brightdata --budget 5
```

**Outputs:**
- `data/dgs/split_contract_dossiers/{vendor_slug}.json` — per-vendor full analysis
- `data/dgs/split_contract_report.md` — summary across all vendors

**What you're looking for:** any vendor with a `STRONG_SPLIT_CONTRACT_PATTERN`
verdict. That's the headline lead. The Local Food Vendor A case from Round 3
should land here.

---

## 2. Track B Flag Validation

Re-checks every Track B `FLAGGED` org and:
- Drops cases where the EIN match is bad (the MADD-at-$5K-revenue problem)
- Drops `STATE_FUNDING_EXCEEDS_REPORTED_REVENUE` flags where the ratio is
  >50x (almost certainly a wrong EIN)
- Surfaces the latest 990 PDF URL for manual review
- Re-classifies surviving cases as `VALIDATED` or `VALIDATED_HIGH_PRIORITY`

```bash
python -m src.track_b.validate_flags
# Or with Bright Data routing for ProPublica:
python -m src.track_b.validate_flags --use-brightdata --budget 3
```

**Outputs:**
- `data/track_b/validated_flags.json`
- `data/track_b/validated_report.md`

**What you're looking for:** the YoY exec comp spike orgs (Education/Science
Nonprofit F at +281%, Community Nonprofit E at +134%, Youth Nonprofit D,
Education Nonprofit G) should all survive validation. The MADD-style false
positives should drop out.

After validation, *manually open the 990 PDF URLs* for the survivors and
check Schedule J (compensation detail) and Schedule L (related-party
transactions). Schedule L hits are the gold standard for nonprofit fraud.

---

## 3. SAM.gov Debarment Scan

Cross-reference every CA grant recipient against the federal Excluded
Parties List. A hit means California is paying a contractor the federal
government has formally barred — that's an instantly publishable finding.

**Get a SAM.gov API key first** (free, 5 minutes):
1. Sign in at https://sam.gov
2. Account Details → API Keys → Generate
3. Add to `.env`: `SAM_GOV_API_KEY=xxxxx`

```bash
# With SAM.gov API (preferred — fast and free)
python -m src.sam_gov.debarment_check --top 1000

# Or via Bright Data (no key needed, slower)
python -m src.sam_gov.debarment_check --top 200 --use-brightdata --budget 5
```

**Outputs:**
- `data/sam_gov/debarment_results.json`

**What you're looking for:** any entity with `status: DEBARRED`. If even
one CA grant recipient is on the federal exclusion list, that's an
immediate publishable finding. The pipeline either confirms the headline
(zero hits = system clean) or surfaces a smoking gun.

---

## Suggested Order

```bash
# Fast and free, biggest payoff potential
python -m src.sam_gov.debarment_check --top 1000              # 5-10 min

# Validates the Track B claims so they're publishable
python -m src.track_b.validate_flags                          # 2-3 min

# Deep dive on the DGS lead
python -m src.dgs.split_contract_deepdive --top 10 --use-brightdata --budget 5  # 5-10 min
```

Total time: ~30 minutes. Total Bright Data spend: ~$5-8.

---

## After This

If any debarment hits land OR any `STRONG_SPLIT_CONTRACT_PATTERN` survives:
- That's the lead case for the submission
- Add it to `ROUND1_WRAPUP.md` under "What's Publishable"
- Update the UI to feature it (with the same legal framing — "anomaly
  warranting investigation," not "fraud")

If everything clears:
- The systemic story ($19.7B null disbursement) stays the headline
- The methodology arc ("we built it, ran 4 audits, cleared everyone except")
  is the supporting frame
- Either way, you've shipped a real working forensic pipeline
