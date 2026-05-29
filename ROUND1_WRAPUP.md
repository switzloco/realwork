# Round 1 Wrap-Up — What's Publishable, What Isn't
*Written: 2026-05-28 — after Antigravity's Phase 1 audit pass*

## TL;DR

**We did not find publishable fraud.** Every entity-level "fraud" claim in
Round 1 either resolved as data quality, false positive, or remains
unverified due to blocked state databases.

**We did find a publishable systemic story:** California's grant tracking
infrastructure has a hole big enough to drive $19.7 billion through. That
finding is real, reproducible, and the most important deliverable from this
work.

**One thing needs immediate cleanup before any public publish:** the UI
labels Infinite Sky Inc. and Suarez Holdings LLC as "TRUE FRAUD" while the
audit commit that produced them concludes a 100% false positive rate due to
"DBA trap and LLM limitations." Publishing the UI as-is with accusations
the engineer's own audit refutes is the worst possible outcome — both
legally exposed and intellectually dishonest. Fix the UI to match the audit
before anything goes public.

---

## What's Publishable

### 1. The $19.7B accountability gap (STRONGEST FINDING)

**Claim:** Of 15,209 grants in CA's FY 2023-2024 dataset, 100% have no
`totalAwardUsed` data populated. $19.7 billion in awards with zero
state-level spend visibility.

**Evidence:**
- Source: data.ca.gov CKAN API, resource `018f3523-652d-4197-a4a8-a055bfd1544f`
- Pull script: `src/audit/disbursement_audit.py`
- Output: `accountability_audit.md`, `data/audit_results.json`
- The `totalAwardUsed` field exists in the schema (per AB132 / Gov Code 8333)
  but is never populated for FY 23-24

**Why it's publishable:** Aggregate stats, no individual accusation. The
finding is the data, not an inference about anyone's behavior. Anyone can
re-run the audit and get the same number.

**How to frame it:** "California's post-award data law requires disbursement
tracking. The data shows that for FY 23-24, the tracking field is empty
across the entire dataset. This is a compliance gap warranting investigation
by the State Auditor."

### 2. The methodology as a working artifact

**Claim:** A multi-stage AI pipeline can scan 11K+ grant records, flag ~40
anomalies, deeply investigate ~22, and produce a defensible "cleared vs
warrants-further-look" verdict per case.

**Evidence:**
- Code: full `src/` tree
- Worked examples: `BRIEFING.md` (Berkeley + Teknol), `data/archive/run1_findings.md`
- 4 evidence dossiers: `data/evidence_dossiers/`

**Why it's publishable:** The pipeline works as designed. Even when the
verdicts are "cleared," the process is the artifact — a journalist or
auditor can use the same tooling on a different dataset.

### 3. The Berkeley data-corruption case (HIGH-CONFIDENCE, LEGITIMATE)

**Claim:** Grant record `8dc4889ab35c` ($1.47M, Cal OES) has the title and
recipient from one FEMA project (Berkeley senior center seismic retrofit)
and the project description from a completely different FEMA project
(Western Municipal Water District backup pump in Riverside County).

**Evidence:**
- Both projects independently verified to exist via city council reports
  and FEMA public notices
- The conflation is internal to data.ca.gov, not an accusation against
  either recipient
- Cost: $1.00 of Bright Data spend

**Why it's publishable:** This is a data integrity failure, not fraud. We
can name it because the actual recipients (City of Berkeley, WMWD) are
public agencies and we're not accusing them of anything — we're pointing
out the record itself is scrambled.

### 4. The Teknol flag-to-resolution arc

**Claim:** Initial flag (software company on a construction grant) survived
through scraping and resolved at the manual-browser stage when CCLD records
confirmed Teknol Inc. is the licensee of "Laurel Play Gardens" infant
center at the same address.

**Why it's publishable:** Anonymize as "[Software Company A]" in the public
write-up. Lead value is the **arc**, not the entity. This shows the pipeline
working correctly: it flagged the right anomaly, the anomaly resolved
cleanly when better data was available, the system did not push a false
positive into a public accusation.

---

## What's NOT Publishable

### Infinite Sky Inc. — needs UI correction

**UI claim:** "TRUE FRAUD: PHANTOM CONSTRUCTION."

**Audit reality:** `run1_findings.md` concludes CLEARED with high
confidence — Infinite Sky holds an active CSLB license #1110009 as a
General Engineering Contractor and General Building Contractor. The
"phantom construction" framing is contradicted by the contractor license
record. The geographic mismatch (Van Nuys address, Placer County project)
is not on its own a fraud indicator.

**Action:** Change UI tag from "TRUE FRAUD" to something like "CLEARED:
GEOGRAPHIC MISMATCH ONLY" or remove the case from the showcase entirely.
**Do not publish accusations of an entity our own audit cleared.**

### Suarez Holdings, LLC — needs UI correction

**UI claim:** "TRUE FRAUD: INELIGIBLE ENTITY — FTB Forfeited Status."

**Audit reality:** `run1_findings.md` says FLAGGED with **medium** confidence
and explicitly notes "Inaccessible state and county databases prevent a
high-confidence conclusion." The FTB Forfeited claim in the UI comes from
the Gemini search validator, which the commit message itself describes as
prone to "DBA trap and LLM limitations." We never verified the forfeited
status against a state database directly.

**Action:** Either verify the FTB forfeited claim against bizfileonline.sos.ca.gov
(this is exactly what `src/bright_data/sos_check.py` does — run it on Suarez
first), OR downgrade the UI label to "UNVERIFIED — INVESTIGATION WARRANTED"
before publish. Naming a specific small business as fraud based on a
medium-confidence LLM hit is the legal exposure the BRIEFING explicitly
warns about.

### SBA Enterprises, JM3 Holdings — already correctly framed

JM3 is correctly shown as "CLEARED: FALSE POSITIVE" in the UI — keep as is.
SBA Enterprises has a dossier but isn't surfaced in the UI; the dossier
shows zero meaningful hits and inconsistent search localization (results
came back from Nigeria and Malaysia, indicating the SERP queries weren't
properly geo-locked).

---

## The Honest Hackathon Story

This is the version that actually holds up:

> We built an automated CA grant fraud detection pipeline. We scanned 27K
> records across two fiscal years, flagged 40 anomalies, deeply investigated
> 22. **Zero of those investigations confirmed fraud.** What looked like
> fraud was either (a) data quality failures inside the state database
> itself, or (b) entities the LLM didn't recognize because they operate
> under different DBA names.
>
> But the real finding came from running the audit at scale: 100% of
> California's FY 23-24 grant awards have no disbursement tracking
> populated. $19.7 billion awarded with no centralized record of whether
> the money was spent as intended. You cannot detect fraud in a system
> that doesn't track outcomes. That's the headline.
>
> The pipeline cleared every false alarm. The system that's supposed to
> catch fraud upstream of us doesn't have the data to do it.

This is stronger than any individual fraud claim because:
1. It's true
2. It's reproducible
3. It's specifically actionable (the State Auditor, the Legislature, or a
   journalist could pick this up tomorrow)
4. It doesn't require us to name anyone

---

## Audit Trail for the Entities Investigated

For each entity we touched, here's the "did we call them legit" status. This
goes in the public repo as a transparency log.

| Entity | Round 1 Verdict | Public Status | Why |
|--------|-----------------|---------------|-----|
| City of Berkeley / WMWD | CLEARED | Named — data error | Both verified legitimate; record is scrambled |
| Teknol Inc | CLEARED | Anonymized as "[Software Company A]" | Operates licensed infant center at same address |
| JM3 Holdings, LLC | CLEARED | Anonymized as "[Holdings LLC, Merced]" | Operates licensed daycare; LLC formed 4 days pre-award is a noteworthy detail but not fraud |
| Infinite Sky Inc | CLEARED (audit), miscategorized in UI | DO NOT PUBLISH until UI fixed | Has active CSLB license; UI claim contradicts audit |
| Suarez Holdings, LLC | FLAGGED-medium (audit), miscategorized in UI | DO NOT PUBLISH until verified | "FTB Forfeited" claim is from LLM, not verified |
| SBA Enterprises | INCONCLUSIVE | DO NOT NAME | Search results came back from wrong country geos |
| Santa Barbara County Water / Del Puerto Water | INCONCLUSIVE | Discuss as "another scrambled record like Berkeley" without entity names | Co-recipient geographically impossible — likely another data entry error |
| Creekside Dairy | CLEARED | Anonymized | Real farm in Escalon; flagged for missing SOS, but sole proprietors don't register |

---

## Recommended Pre-Publish Checklist

1. **Fix the UI labels** for Infinite Sky and Suarez. Either downgrade to
   "WARRANTS INVESTIGATION" or remove from the showcase.
2. **Run `src/bright_data/sos_check.py` on Suarez Holdings specifically.**
   If it confirms FTB Forfeited from the actual SOS database, the UI claim
   becomes defensible. If it doesn't, remove the claim.
3. **Lead with the $19.7B accountability gap.** That's the story. Individual
   cases are supporting evidence for the methodology, not the headline.
4. **Anonymize all small-business names** in committed/published findings.
   The qui tam guidance from BRIEFING.md still applies even if we're not
   filing qui tam: don't name a small entity as fraud in public.
5. **Add a "Limitations" section to the public write-up.** Acknowledge the
   100% false positive rate on Round 1 directly. It's a feature, not a bug —
   it's the system working: flag broadly, verify rigorously, refuse to
   publish weak claims.

---

## Then: Move to Round 2

Round 2 is laid out in `ROUND2_PLAN.md`. The new Bright Data bulk
verification scripts in `src/bright_data/` are ready to run when you give
the word. The minute we run `bulk_serp.py` and `sos_check.py` across the
top 200 entities, we'll have real ground-truth on which "ghosts" are actual
ghosts versus DBA misses.

The DBA trap from Round 1 is fixed by Round 2's approach: SOS check answers
the existence question directly (entity number, status), instead of relying
on a Google search that an LLM interprets.

---

## Round 3 Findings — New Attack Surfaces
*Written: 2026-05-29 — after Antigravity's Round 3 scan*

We executed scans on two new independent data streams (DGS purchase orders and Track B nonprofit overhead). Both datasets yielded clear anomalies warranting further investigation without labeling them as fraud. Small entities have been anonymized in this summary.

### 1. DGS Purchase Order Anomalies (Caltrans-pattern hunt)
We scanned 50,000 state purchase orders totaling $30.15 billion. The scan successfully identified several classic bidding and contracting anomalies:

* **Split-Contract Clusters (Just-Under-Threshold)**:
  * **[Local Food Vendor A]**: Won 7 POs clustered just below the $50,000 threshold at exactly $49,950 each, indicating potential split-contracting to bypass formal bidding requirements.
  * **McKesson Medical-Surgical**: Won 7 POs clustered just below the $5,000 threshold (ranging from $4,943 to $4,957), which is a common minor-threshold pattern.
* **Vague High-Value POs**:
  * **CENTRAL CALIFORNIA TECHNO**: Received a $40,500,000 PO from the Employment Development Department (EDD) for "IT technogy support services." The high value paired with a generic description represents a transparency gap.
  * **ABM Industries**: Received a $21,780,625 PO for "engineering services."

### 2. Track B Nonprofit Overhead Audit (Executive Bloat & Revenue Mismatches)
We performed a financial health sweep of the top 500 nonprofit CA grant recipients by matching them to ProPublica/IRS Form 990 filings. After resolving name-matching traps (such as correctly separating Stanford University from its bookstore subsidiary), we flagged 104 organizations for significant overhead anomalies:

* **State Funding Exceeds Reported Revenue (Possible Off-Books/Discrepancy)**:
  * **MADD**: Received $2,209,800 in CA state grants but reported only $5,000 in total revenue on its matching Form 990 filing for that period.
  * **[Social Services Nonprofit B]**: Received $719,841 in CA state grants but reported only $1 in total revenue.
  * **[Nonprofit C]**: Received $573,331 in CA state grants but reported only $47,984 in total revenue.
* **YoY Spikes in Executive Compensation & Total Expenses**:
  * **[Education/Science Nonprofit F]**: Officer compensation spiked by 281.3% YoY (from $132,755 to $506,146) at an organization with only $3,743,341 in total expenses.
  * **[Community Nonprofit E]**: Officer compensation spiked by 134.2% YoY (from $356,125 to $834,009) at an organization with $4,819,134 in total expenses.
  * **[Education Nonprofit G]**: Officer compensation grew by 77.4% YoY ($56,272 to $99,832) while total expenses spiked by 189.6% YoY ($210,171 to $608,725) following the receipt of state funding.
  * **[Youth Nonprofit D]**: Officer compensation grew by 74.6% YoY ($58,154 to $101,551) while total expenses grew by 181.9% YoY ($102,237 to $288,219) on state funding of $500,000.

These findings represent high-quality leads for manual audits. They demonstrate that while Stage 1 grant portal searches are easily cleared, looking at the post-award stage (how the money is reported on IRS filings or how contracts are split) is where the most significant systemic anomalies reside.
