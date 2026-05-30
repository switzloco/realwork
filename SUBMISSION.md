# RealWork — Hackathon Submission

**Track:** Bright Data "Web Data UNLOCKED" Hackathon, May 2026
**Team:** RealWork (Nick Switzer)
**Repo:** https://github.com/switzloco/realwork

---

## The pitch in one line

**The grant accountability audit tool California doesn't have — built in five days, methodology documented, pipeline open-source.**

## The problem

California publishes its grant award database under the Grant Information Act (AB-132, Gov Code §8333). The law mandates that grantmakers track post-award disbursement — whether the money was actually spent as awarded.

We pulled both available fiscal years from data.ca.gov's CKAN API:

- 26,907 grant records across FY 22-23 and FY 23-24
- **$36.5 billion in total awards**
- **100% of those records have the `totalAwardUsed` disbursement field empty**

Nobody — not the state, not federal regulators, not journalists — has a centralized record of whether any of that money was spent as awarded. The state mandates the data. The data is not populated. That's a $36.5B accountability gap. Not an accusation. Not an inference. Just what the public records say.

## What we built

A multi-stage forensic audit pipeline that does the work the state's existing systems are not doing. It pulls three data streams in parallel — state grants, DGS purchase orders, IRS Form 990 nonprofit filings — and cross-references them against external verification sources via Bright Data.

For each anomaly the pipeline surfaces, it:

1. **Validates** against documented fraud patterns (split contracts, related-party transactions, ghost recipients, executive comp spikes correlated with new funding, just-under-threshold purchasing)
2. **Cross-checks** via Bright Data Web Unlocker against state databases that block ordinary scrapers — CA Secretary of State, CCLD childcare licensing, ProPublica's 990 archive, SAM.gov debarments
3. **Re-validates** via a second AI model (AI/ML API ensemble) — cross-model agreement reduces single-model hallucination risk
4. **Drops false positives** through EIN-match sanity checking and a wrong-EIN-signature detector that catches "we matched a dormant local chapter, not the real org"
5. **Produces transparent reports** — every finding cites public records, no claims of fraud, only "warrants investigation"

The dead-end log is itself a deliverable: it documents which entities the pipeline cleared and why, so future investigators don't repeat the work.

## What the tool surfaced

Note the framing: these are demonstrations of what the pipeline finds, not accusations. Every finding is positioned for State Auditor review.

### Track B: Nonprofit overhead patterns

We scanned IRS Form 990 filings for 500 California nonprofit grant recipients via the ProPublica Nonprofit Explorer API. After EIN-match sanity validation, **36 organizations surfaced as HIGH PRIORITY anomalies**. Public-records examples:

The pipeline flags two distinct patterns — not just "comp went up when grants came in," which has innocent explanations:

**Pattern 1: Compensation disproportionate to program scale.** If a grant funds expanded programs, officer comp should scale with program delivery — total expenses, headcount, beneficiaries served. When compensation consumes an outsized share of the organization's total budget, and that share grows when new funding arrives, the anomaly is the ratio, not the raw number.

- **Finish First Academy:** $4.75M in CA state grants. Form 990 reports $556K total revenue — less than the state grants alone. Officer comp up 77% YoY, total expenses up 190% YoY. The revenue figure implies the 990 does not reflect the full grant inflow, which itself is a reporting anomaly.
- **Land Together:** $338K officer compensation at a $1.34M-expense org — 25% of all expenses going to officer comp, against a sector median of 8-10%. Officer comp up 55% YoY while reported program delivery did not scale proportionally.

**Pattern 2: Compensation spike without matching program delivery evidence.**

- **Veterans Transition Center of California:** $722K officer compensation, $1.6M state grants — officer comp alone consumes nearly half of total state funding received.
- **Golden Gate National Parks Conservancy:** Officer compensation more than doubled YoY, from $900K to **$2.07 million** for a single officer — a $1.17M increase in one year.
- **Community Action Partnership of Kern:** Officer comp went from $451K to $2.05M YoY — a 355% jump in a single fiscal year coinciding with a $2.7M state grant award.
- **CityServe Network:** Total expenses jumped 384% YoY ($6.7M → $32.5M) — a scale of growth that would require extraordinary operational expansion to justify.

Every number above comes from a publicly-filed Form 990. The tool surfaced the ratios; the State Auditor decides if they warrant follow-up.

### DGS: Threshold-edge purchase order patterns

We scanned 50,000 purchase orders totaling $30.15 billion. The pipeline surfaced six vendors with statistically anomalous threshold-edge concentration. The strongest:

**Panini Time:** 12 purchase orders at exactly $49,950 — $50 below the state's $50,000 competitive-bidding threshold. 100% concentrated to Cal Fire. A manual Power BI drilldown surfaced that 5 of 6 most recent contracts were signed by a single procurement officer within a 17-day window in August 2025.

**Context that matters:** That window coincides with two real wildfires (King Fire Aug 14-18, Dillon Fire Aug 28+). Cal Fire was actively battling fires that scaled from 256 personnel to 1,760. Emergency procurement is a plausible explanation for the timing and same-buyer concentration. **What it does not explain:** why every PO rounded to exactly $49,950 across a window where actual crew size varied 7×.

The pipeline reframes this from "Caltrans-style bid splitting" (which the fire context partly debunks) to a **threshold-ceiling pattern**: a procurement officer defaulting to the just-under-threshold dollar amount regardless of actual need. That's a softer finding, more defensible, and exactly the kind of pattern the State Auditor's office should periodically scan for.

This is the pipeline working correctly: surface a pattern, validate it, honestly weaken the finding when contextual evidence emerges, ship the calibrated verdict to oversight.

## Why this is the tool California needs

The State Auditor's office runs investigations on tips and on selected programs. It does not have the engineering capacity to continuously cross-reference state grants against Form 990s against purchase orders against external verification sources. No state does.

We built the tool that performs that cross-reference in hours, not months. It runs on commodity infrastructure ($250 of Bright Data credits, $10 of AI/ML API credits, an OpenAI-compatible model layer, Gemini for primary reasoning). It is open-source. The methodology is documented. The patterns it flags are the patterns the State Auditor's published risk frameworks already describe — we operationalized them.

A state-level deployment would:
- Run continuously against fresh CKAN data
- Maintain a per-fiscal-year flagged-anomaly queue for human review
- Maintain a transparent dead-end log of cleared anomalies
- Output reports the Auditor's office can act on without engineering effort

The Caltrans bid-rigging case (USA v. Yong, Miller, Opp, 2019 — 49-78 month sentences, $3M restitution) was caught by a whistleblower, not by data analysis. There was no continuous data-analysis pipeline that would have caught it. We built one.

## The honest disappointment

We want to say this directly: **we did not find smoking-gun fraud, and that's frustrating to us.** We spent five days, $50 of Bright Data credits, and most of a week of intense AI-assisted investigation, and we cleared 100% of our Round 1 individual fraud hypotheses. Our strongest single lead — the Panini Time threshold-edge pattern — substantially weakened when wildfire context emerged. Our 36 nonprofit anomalies are all defensible as worth investigating, but every single one has a plausible non-fraud explanation that we could not rule out from public records alone.

This is either:

- **The methodology working correctly.** The easy fraud doesn't survive cross-source validation. Pattern matching plus charitable explanations equals "warrants investigation," not "confirmed fraud." That's what an honest pipeline should output.
- **The dataset is wrong.** The state's grant-award database is the most-audited slice of state spending. Real fraud lives downstream — in disbursement, in local-government procurement, in behavioral health billing, in federal pass-through funds the state forwarded without auditing. We didn't scan those.
- **Both.** Most likely both.

A more experienced investigator with subpoena power, three more weeks, and access to the State Auditor's confidential tip line would probably take one or two of our HIGH PRIORITY findings and convert them to actual cases. We can't do that in a hackathon. We're saying so plainly because the project is more credible if we name the gap than if we paper over it.

## The Bright Data integration

Bright Data is the foundation, not a bolt-on. Without it the pipeline does not work, because the state's own databases block ordinary scrapers.

- **Web Unlocker** routes around anti-bot on `bizfileonline.sos.ca.gov` (CA Secretary of State), `ccld.dss.ca.gov` (CCLD childcare licensing), SAM.gov, and ProPublica's 990 PDF archive. These are the authoritative verification sources for "does this entity exist, is it in good standing, does it hold required licenses, is it federally debarred."
- **SERP API** runs five variant queries per entity (existence, litigation, enforcement, LinkedIn, business directories) across our 1,751-entity high-risk list. Manual Google requests at that scale would be CAPTCHA-blocked within minutes.
- **Scraping Browser** drives the state's public Power BI procurement dashboard — a JavaScript-rendered single-page application that exposes per-PO buyer and date detail not available in the CKAN summary export. This is how we surfaced the named procurement officer behind the Panini Time pattern.

Hard budget cap at $250 with a JSONL cost ledger auditable down to the cent. Total spend: well under budget.

## The AI/ML API integration

Every HIGH PRIORITY anomaly the primary pipeline surfaces is sent to a second model (AI/ML API → GPT-4o) for independent review. The second model is given the same facts and asked the same question. If both models agree, the verdict is upgraded to `ENSEMBLE_CONFIRMED`. If they disagree, the finding moves to `NEEDS_HUMAN_REVIEW`.

Cross-model agreement is a published calibration technique. It also reduces the "what if the LLM hallucinated" objection that civic-tech work routinely faces.

Qualifies for the AI/ML API partner prize: $1,000 cash + $1,000 in credits.

## Dual-use disclosure

This tool documents patterns that fraud detection systems flag. Those patterns are derived from publicly available sources: the California State Contracting Manual, the published filings of the 2019 Caltrans prosecution, the State Auditor's risk frameworks, and academic fraud-detection literature. They are well-known to fraud examiners. Publishing detection methodology supports oversight; it does not create new evasion opportunities. The defender's advantage is that detection systems cross-reference many signals simultaneously — evading all of them is harder than evading any one.

This tool is intended for use by oversight bodies (State Auditor, DOJ Procurement Collusion Strike Force, qui tam attorneys), accountability journalists, and other entities whose mandate is public integrity. It is not intended for use by parties who would game procurement.

## What we explicitly don't claim

- We do not claim fraud has been proven against any entity
- We do not claim any individual entity has acted illegally
- We do not use "fraud" as a conclusion — only as a pattern label
- We do not name small businesses or individual procurement officers as fraud cases in public-facing artifacts
- We do not bypass the qui tam process; recovery candidates would be filed under seal before public disclosure

The path from "anomaly warranting investigation" to "confirmed fraud" runs through the State Auditor's office, the DOJ, and the courts — not through a hackathon submission.

## What's next

Three parallel tracks:

1. **Responsible disclosure** to the California State Auditor with the validated findings and the underlying data
2. **Qui tam attorney consultation** on the strongest patterns
3. **Open-source the pipeline** as a state-grant audit toolkit — the same code runs on Texas, Florida, New York with minor adaptations

## Key files

| File | What it is |
|------|------------|
| `ZOOM_OUT.md` | Honest inventory: what survived scrutiny, what didn't |
| `PITCH_PREP.md` | Single-doc team briefing, NotebookLM-ready |
| `WHAT_DEPTH_LOOKS_LIKE.md` | 9-step methodology for the depth-first version of this work |
| `STATE_AUDITOR_TIP_TEMPLATES.md` | Three pre-drafted tip letter templates for the State Auditor |
| `accountability_audit.md` | The $36.5B systemic finding output |
| `data/track_b/validated_report.md` | The 36 HIGH PRIORITY validated nonprofit cases |
| `data/dgs/split_contract_report.md` | The DGS threshold-edge analysis |
| `data/dgs/fire_window_context.md` | Honest re-evaluation of the Panini Time pattern under wildfire context |
| `data/dossiers/DOSSIER_trybe_inc.md` | A worked example of a State Auditor-ready single-entity dossier |
| `src/audit/disbursement_audit.py` | Reproduces the $36.5B finding |
| `src/dgs/*.py` | DGS analysis pipeline |
| `src/track_b/*.py` | Nonprofit analysis pipeline |
| `src/counties/county_po_scanner.py` | Generalization to local-government data (SF, LA County, Sacramento, San Jose) |
| `src/bright_data/*.py` | Bright Data integration layer |
| `src/ensemble/second_opinion.py` | AI/ML API cross-model validator |
| `ui/index.html` | Public-facing demo site |
| `ui/submit-a-tip.html` | Pre-drafted State Auditor tip templates for the public |

---

Real data. Real public records. Real reproducibility.

The tool is the deliverable. California can deploy it on Monday.
