# Round 2 Investigation Plan
*Drafted: 2026-05-28 — to execute after Antigravity completes the current audit run*

## Premise

Round 1 found systemic accountability gaps (100% null disbursement on FY 23-24)
and resolved two construction-grant cases as non-fraud. The construction angle
is exhausted: physical projects are too verifiable to hide theft inside.

Round 2 pivots to where money disappears with no trail:
**service grants to private entities with no disbursement tracking.**

We also commit to leaving a public, reproducible audit trail so anyone — a
journalist, an auditor, a future grad student — can pick up where we stopped.

---

## What "Better Than Round 1" Means

Round 1 was:
- 11,698 records → 40 flagged → 22 investigated → 0 confirmed fraud
- All targets were construction/infrastructure (physical, verifiable)
- Bright Data used on ~22 entity verifications

Round 2 should be:
- Combined FY 22-23 + FY 23-24 dataset (~27K records)
- Filter to service-type grants only (~estimated 30-40% of dataset)
- Apply composite risk score (entity suspicion + vague description + null disbursement + max award + private recipient)
- Take top 50 by score → Bright Data verification on each
- Target: surface at least one case that is **NOT** a data-quality issue

The bar to clear isn't "find fraud." It's "find an anomaly that survives
verification" — something where the obvious-but-charitable explanation doesn't
hold up.

---

## Execution Sequence

### Step 0 — Wait for Antigravity audit to finish

Don't start work that touches the same files (data/grants_full.csv,
data/audit_results.json). Let Antigravity's run land cleanly.

### Step 1 — Run the services fraud scan
```bash
python -m src.audit.services_fraud_scan --source csv
```
Output: `services_fraud_scan.md` + `data/services_fraud_results.json`

Look for the top 50 by composite_risk_score. Expected distribution: heavy
weighting toward consulting LLCs, "training" providers, "outreach" grants.

### Step 2 — Pull Open FI$Cal vendor transactions
```bash
# Find resource ID at https://data.ca.gov/dataset/vendor-transactions
export VENDOR_TX_RESOURCE_ID=<id>
python -m src.audit.vendor_crossref --fetch --account 5340
```
This gives us the *actual* payment side. Critical questions:
- Do any high-risk-score grant recipients show up as 5340xxx vendors too?
- Are there 5340xxx vendors receiving >$1M who have no grant record? (off-books contracting)

### Step 3 — Bright Data verification on top 50
Three checks per entity, prioritized by cost:

1. **SERP check** (cheap, ~$0.50/query) — does Google know this entity exists?
   Reuse `src/audit/zero_web_presence.py`, point at the new high-risk list.
2. **CA SOS business registry** — is the entity in good standing? Forfeited
   or suspended status = immediate escalation.
3. **Web Unlocker on entity website** (if found) — does the site describe
   work that matches the grant scope, or is it a parked domain / boilerplate?

Budget: 50 entities × ~$3 average = $150. Fits within remaining $208.

### Step 4 — Investigate the top 5 survivors

After SERP + SOS filtering, manually investigate the 5 strongest signals:
- News search for the entity name + "settlement" / "investigation" / "audit"
- Look up the funding source's grant program rules — does the recipient
  even qualify?
- Check if the entity's address is residential, a virtual office, or shared
  with other suspicious recipients
- For training/workforce grants: is there any public record of trainees,
  curriculum, or outcomes?

### Step 5 — Cross-fiscal-year pattern hunt

The same recipient receiving similar-size grants across FY 22-23 AND
FY 23-24 with null disbursement on both years is a stronger signal than
either alone. The vendor_crossref tool has the fuzzy-matching primitives;
extend it with a `--cross-year` mode if Step 4 doesn't surface enough.

---

## Leaving a Trail

### Public artifacts to commit
Everything below goes in the repo. Anonymize entity names only where we'd
otherwise be naming specific individuals or small businesses without
corroboration. Aggregate stats and entity names of large LLCs/corporations
are fair game.

- `services_fraud_scan.md` — the full ranked list with methodology
- `data/services_fraud_results.json` — raw data for reproducibility
- `data/vendor_crossref_results.json` — recipient ↔ vendor matches
- `data/ghost_entities_round2.json` — SERP results from Step 3
- `ROUND2_FINDINGS.md` — narrative report:
  - What we looked at
  - What we found (positive: anomalies; negative: dead ends)
  - What we couldn't verify with our tools
  - What a follow-up investigator should do next

### Reproducibility checklist for `ROUND2_FINDINGS.md`
Each finding must include:
1. Source dataset + resource ID + fetch date
2. Exact filter criteria that surfaced it
3. The Bright Data checks performed + results
4. The verification chain (what we confirmed vs. what we assumed)
5. The charitable explanation we considered + why it held or didn't
6. A "to verify this yourself" section with exact commands

This is the difference between "Claude found fraud" and "here is a public
methodology anyone can run." The second is what makes the work durable.

### Dead-ends log
Maintain `data/dead_ends.md` — entities we investigated and cleared, with
the reason. This is unsexy but it's the most valuable thing for future
investigators: it tells them where NOT to spend their budget.

### Methodology doc
Promote the audit pipeline into a standalone reusable doc:
`METHODOLOGY.md` describing the full chain (categories → scoring →
SERP filter → SOS check → manual investigation) so it can be re-run on
FY 24-25 when that dataset lands, or adapted for other states.

---

## What NOT to Do

- **Don't burn budget on individual SERP checks before scoring.** Always
  score first, verify second.
- **Don't keep investigating construction.** The pipeline already proved
  it; pivot is the point.
- **Don't publish accusations.** Every finding is framed as "warrants
  investigation by [appropriate body]." We are surfacing anomalies, not
  pronouncing guilt.
- **Don't lose data.** The grants_full.csv that Antigravity is generating
  is irreplaceable from this sandbox (data.ca.gov is blocked). Commit it
  or back it up before re-running anything that overwrites it.
- **Don't skip the dead-ends log.** "We checked X and it was fine" is part
  of the trail.

---

## Success Criteria

Round 2 succeeds if any of these is true:

1. We surface at least one service-grant anomaly that survives SERP + SOS
   verification and is NOT a data-quality issue
2. The vendor cross-reference reveals a previously-undisclosed dual-payment
   pattern (same entity, grant + vendor, both significant)
3. We publish a methodology doc that a third party could re-run end-to-end
   on a different fiscal year

If none of those land, Round 2 still produced a public, reproducible audit
trail — which is the more important deliverable than any individual finding.

---

## Budget at Round 2 Start (estimated)

- Bright Data: $208 remaining
- Allocate: $150 for Step 3 (top 50 SERP+SOS), $50 reserve for Step 4 deep dives, $8 buffer
- Gemini: estimated $5-10 for any LLM-assisted entity classification
- Total cost ceiling: ~$170

If Step 3 surfaces more than 5 strong candidates, raise the question of
extending the budget before continuing — don't silently overrun.
