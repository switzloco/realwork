# RealWork — Hackathon Submission

**Track:** Bright Data "Web Data UNLOCKED" Hackathon, May 2026
**Team:** RealWork (Nick Switzer + dual-AI agent build: Claude Code in cloud, Google Antigravity local)
**Repo:** https://github.com/switzloco/realwork

---

## What it is

A multi-stage autonomous forensic accountant for California public spending.
The pipeline scans state grant awards, IRS Form 990 filings, and DGS
purchase orders in parallel. It flags anomalies, verifies them against
external public records via Bright Data, and produces transparent audit
reports that frame every finding as "warrants investigation" — never as
fraud accusations.

## The findings

### 1. The $36 billion accountability gap

California's Grant Information Act (AB-132, Government Code §8333)
mandates that grantmakers track post-award disbursement of state grants.
We pulled both available fiscal years (FY 22-23 and FY 23-24) from
data.ca.gov's CKAN API: **26,907 grant records totaling $36.5 billion.**
**100% of those records have the `totalAwardUsed` disbursement field
empty.** Nobody — not the state, not federal regulators — has a
centralized record of whether any of that money was actually spent as
awarded.

This is the systemic story. It's the data, not an accusation. Anyone
can re-run our `disbursement_audit.py` script and reproduce the
finding. It would take the California State Auditor about ten minutes
to verify.

### 2. The lead case: Panini Time

Our DGS purchase order scan covered 50,000 records totaling $30.15
billion. One vendor surfaced as the textbook split-contract pattern:

- **Panini Time:** 12 purchase orders at *exactly* $49,950 each (the
  state's competitive-bidding threshold is $50,000)
- **100% single-buyer concentration** (Cal Fire / Department of
  Forestry and Fire Protection issued every one)
- **4 contracts in a single 7-day window**
- Total value of the just-under cluster: $599,300
- Total lifetime value of this vendor-buyer relationship: $2.88M

The factual pattern matches the 2019 federal prosecution of three
Caltrans procurement officials (USA v. Yong, Miller, Opp — 49-78 month
sentences, $3M restitution). California State Contracting Manual
explicitly prohibits "splitting purchases" to evade bidding thresholds.

The charitable explanation exists: emergency fire-response procurement
during the Robbers Fire (the actual PO description). Whether this is
benign emergency procurement or something else is a question for the
State Auditor — not a question we can answer from public records. **We
surface the pattern; oversight bodies determine intent.**

Five additional vendors exhibit similar but smaller versions of the
pattern: McKesson Medical (28 POs to Correctional Health Care), Falcon
Fuels (13 POs to Cal Fire), Progressive Medical (3 POs at exactly
$4,999 within 3 days), Airgas (6 POs to Air Resources Board), and
Prison Industry Authority.

### 3. The nonprofit overhead pattern

We pulled IRS Form 990 filings for 500 California nonprofit state-grant
recipients via the ProPublica Nonprofit Explorer API. After EIN-match
sanity validation (drops the wrong-EIN false positive where a tiny
local chapter gets matched against a national org's name), **36
organizations survived as HIGH PRIORITY anomalies.** Highlights:

- **Finish First Academy:** $4.75M in CA state grants. Form 990
  reports $556K in total revenue (an 8.5× gap). Officer comp grew 77%
  YoY, total expenses grew 190% YoY.
- **Land Together:** $338K officer compensation at a $1.34M-expense
  org (25% of expenses — sector median is 8-10%). Officer comp up 55%
  YoY. State grants 2.3× reported revenue.
- **Veterans Transition Center of California:** $722K officer
  compensation, $1.6M state grants.
- **Golden Gate National Parks Conservancy:** Officer compensation
  more than doubled YoY, from $900K to **$2.07 million** for a single
  officer.
- **Community Action Partnership of Kern:** Officer comp went from
  $451K to $2.05M YoY — a 355% jump.
- **CityServe Network:** Total expenses jumped 384% YoY ($6.7M → $32.5M).

Every number above comes from a publicly-filed Form 990. We are
calling out the numbers — not making accusations. Sector medians,
threshold comparisons, and YoY deltas are public-records analysis,
not legal conclusions.

## What we built (technical)

Six-stage pipeline:

1. **Multi-source ETL.** CA Grants Portal (26K records), DGS POs (50K),
   ProPublica 990s (500 nonprofits). Normalized into SQLite.

2. **Heuristic flagging.** Just-under-threshold PO clusters,
   repeating exact amounts, buyer-vendor concentration, nonprofit
   overhead ratios, exec-comp YoY spikes, state-grant-vs-reported-
   revenue gaps.

3. **Bright Data verification.** Web Unlocker for SPA-protected sites
   (bizfileonline.sos.ca.gov, ccld.dss.ca.gov, ProPublica, SAM.gov).
   SERP API for 5-variant queries on 1,751 entities. Scraping Browser
   available for client-rendered downloads. Hard budget cap at $250
   with JSONL cost ledger.

4. **LLM synthesis.** Gemini 2.5 Pro distinguishes real anomalies
   from data quality issues and DBA-trap false positives.

5. **Validation pass.** EIN-match sanity checking drops false positives
   (e.g., MADD flagged when our scanner matched a tiny local chapter
   against the national org's name). 102 of 104 nonprofit flags
   survived; 36 reached HIGH priority.

6. **Transparent reporting.** Auto-generated markdown reports per round.
   Every finding cites public records. Dead-end log documents what was
   cleared so future investigators don't repeat work. The audit trail
   is itself a deliverable.

## Bright Data integration

Bright Data is core to the project, not a bolt-on:

- **Web Unlocker** defeats anti-bot protection on the CA Secretary of
  State search (`bizfileonline.sos.ca.gov`), the CCLD childcare
  facility licensing search (`ccld.dss.ca.gov`), SAM.gov debarment
  search, ProPublica's PDF storage, and OpenCorporates.
- **SERP API** runs 5 variant queries per entity (existence,
  litigation, enforcement, LinkedIn, business directories) across the
  1,751-entity high-risk list. Would be impossible at this scale with
  direct Google requests.
- **Scraping Browser** for open.fiscal.ca.gov SPA downloads (script
  ready, awaiting browser-zone provisioning for full-run).

Total spend: well under the $250 budget with hard caps and audit
ledger. Auditable down to the cent.

## Why this matters

**For technical judges:** A real implementation of autonomous forensic
AI pipelines with budget controls, multi-stage verification, and honest
false-positive rejection. The pipeline cleared every individual Round 1
fraud hypothesis — that's the methodology working correctly, not
failing.

**For civic-tech judges:** California spent $36 billion in state grants
over two fiscal years with no centralized record of disbursement. We
proved that gap exists and surfaced specific cases that warrant
follow-up — without making accusations. This is the kind of tool a
State Auditor, an investigative journalist, or a qui tam attorney could
pick up tomorrow.

**For impact judges:** The 2019 Caltrans prosecution returned $3M in
restitution on a fact pattern very similar to what we surfaced in
current 2024-2025 DGS data. We didn't find that exact case again — we
found multiple new ones with the same signature, plus a separate
nonprofit overhead pattern across 36 organizations.

## What we explicitly don't claim

- We do not claim fraud has been proven
- We do not claim any individual entity has acted illegally
- We do not use "fraud" as a conclusion — only as a pattern label
- We do not name small businesses as fraud cases in the UI
- We do not bypass the qui tam process (file under seal first)

The path to actual recovery is the California False Claims Act qui tam
process. Our role is to surface candidates and reduce the cost of
investigation — not to make legal determinations.

## What's next

Three parallel tracks:

1. **Responsible disclosure** to the California State Auditor with the
   validated findings and the underlying data.
2. **Qui tam attorney consultation** on the strongest patterns (Panini
   Time, the multi-flag Track B cases). Attorneys work on contingency;
   the consultation is free.
3. **Open-source the pipeline** as a state-grant audit toolkit. The
   same code runs on Texas, Florida, New York with minor adaptations.

## Key files in the repo

| File | What it is |
|------|------------|
| `PITCH_PREP.md` | Single-doc team-leader briefing, NotebookLM-ready |
| `RESULTS_SO_FAR.md` | Current state of findings |
| `WHERE_FRAUD_HIDES.md` | Why we pivoted from grants-only to multi-source |
| `ROUND1_WRAPUP.md` | Honest accounting of what's publishable |
| `ROUND2_PLAN.md` | Strategic pivot plan |
| `ROUND3_RUNBOOK.md` | How to run the three new attack surfaces |
| `ROUND4_RUNBOOK.md` | How to validate the leads |
| `accountability_audit.md` | The $36B systemic finding |
| `data/dgs/po_anomalies.md` | The DGS scan output |
| `data/dgs/split_contract_report.md` | The Panini Time deep dive |
| `data/track_b/overhead_report.md` | The Track B scan output |
| `data/track_b/validated_report.md` | The 36 HIGH priority validated cases |
| `src/audit/disbursement_audit.py` | Reproduces the $36B finding |
| `src/dgs/purchase_orders.py` + `split_contract_deepdive.py` | DGS analysis |
| `src/track_b/overhead_audit.py` + `validate_flags.py` | Nonprofit analysis |
| `src/bright_data/*.py` | Bright Data integration layer |
| `ui/index.html` | Public-facing demo site |

---

**Built across two AI agents working from the same repo:** Claude Code
in the cloud for architecture, planning, and tool design. Google
Antigravity locally for execution against live APIs and Bright Data
calls. They synced via git on shared contracts. Two AI agents
collaborating on a forensic accountability project is itself part of
the story.

Real data. Real public records. Real accountability.
