# Zoom-Out: What We Actually Have
*Honest inventory of what survived scrutiny.*

## The headline (unchanged)

**$36.5 billion in California state grants across FY 22-23 and FY 23-24 with
100% null disbursement tracking.** This is the systemic story. It's the data,
not an inference. It's the strongest single finding.

## What survived honest scrutiny

### Strong (publish as-is)
- **The $36B systemic gap** — irrefutable, just reads the data
- **The pipeline itself** — multi-source ETL, multi-stage verification,
  budget controls, dead-end log, audit trail. The methodology IS the deliverable.
- **The Track B nonprofit overhead pattern** — 36 HIGH PRIORITY orgs from 500
  scanned, every flag backed by a public 990. Notable named cases:
  - NP-39 — officer comp $900K → $2.07M YoY
  - NP-44 — officer comp +355% YoY
  - NP-45 — expenses +384% YoY ($6.7M → $32.5M)
  - NP-03 — $338K officer comp at $1.34M-expense org (25% ratio)
  - NP-08 — $722K officer comp
  - NP-01 — $4.75M state / $556K revenue

### Dead ends (worth saying we cleared them)
- **The DGS threshold-edge / $49,950 vendor pattern — CLEARED.** The lead
  vendor's purchase orders all fell during active wildfire emergency response
  (King Fire + Dillon Fire). Feeding/supplying fire crews during a crisis is
  the obvious non-fraud explanation. Dropped as a finding.
- Round 1 individual fraud cases (Berkeley, Teknol, Infinite Sky, Suarez,
  JM3, Creekside) — all CLEARED or unverified, none survived as fraud
- Schedule L analysis — analyzer worked, all 3 sampled orgs answered "No" to
  Schedule L questions, which is expected (orgs don't self-incriminate)

### Inconclusive (acknowledge)
- SAM.gov debarment scan — script written, not run
- Press coverage check (lead_news_check.py) — script written, not run
- Cal eProcure / Power BI line-item drilldown — written, partially executed
  manually (yielded the named procurement officer finding)
- Unit price markup analysis — script written, results inconclusive without
  line-item data from Cal eProcure

## What's the strongest publishable story right now

In order of strength:

1. **The $36B systemic gap.** Period. Lead with this everywhere.
2. **The methodology** — a working forensic pipeline that surfaces
   anomalies AND honestly debunks itself when context emerges.
3. **The Track B findings** — 36 nonprofit anomalies, each backed by a public 990.

The claim is no longer "we found fraud." It's:

> We built a tool that scans California's state spending data, surfaces
> anomalies, and validates them honestly — including dropping initial leads
> when contextual evidence weakens them. We proved a $36B systemic
> accountability gap and surfaced 36+ specific anomalies for State Auditor
> follow-up. Our tool cleared everything it couldn't substantiate.

That's a stronger position than overclaiming on the catering pattern.

## What's left to do before submit

| Task | Time | Value |
|------|------|-------|
| Run `lead_news_check.py` | 5 min | Confirms no prior press coverage |
| Run `second_opinion.py` (AI/ML API) | 10 min | Cross-model validation + partner prize |
| Re-run `schedule_l_analyzer.py` (PDF fix) | 5 min | Schedule L was a dead end but confirm |
| Drop `PITCH_PREP.md` in NotebookLM | 0 work | Audio briefing for the walk |
| Submit | — | — |

Total time to a complete submission: under an hour of Antigravity execution.

## What to NOT do

- Don't keep looking for more vendors. Diminishing returns.
- Don't burn more Bright Data credits on grants — we've covered that surface.
- Don't lengthen the UI further. It's tight and honest.

Ship it.
