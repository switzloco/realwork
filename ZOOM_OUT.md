# Zoom-Out: What We Actually Have
*Honest inventory after the Panini Time / fire-context check. Pre-submission.*

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
  - Golden Gate National Parks Conservancy — officer comp $900K → $2.07M YoY
  - Community Action Partnership of Kern — officer comp +355% YoY
  - CityServe Network — expenses +384% YoY ($6.7M → $32.5M)
  - Land Together — $338K officer comp at $1.34M-expense org (25% ratio)
  - Veterans Transition Center of CA — $722K officer comp
  - Finish First Academy — $4.75M state / $556K revenue

### Softer (publish with context)
- **The $49,950 / Panini Time pattern** — explained partly by the King Fire
  + Dillon Fire emergency window, but the *identical amounts* across varying
  crew sizes still points to "threshold-ceiling abuse" (not the stronger
  bid-splitting fraud framing). Worth surfacing with the fire context
  acknowledged.
- **The other DGS threshold-edge patterns** (McKesson, Falcon Fuels, Progressive
  Medical) — same pattern at smaller dollar amounts, mostly to Correctional
  Health Care. Mention as supporting examples.

### Dead ends (worth saying we cleared them)
- Round 1 individual fraud cases (Berkeley, Teknol, Infinite Sky, Suarez,
  JM3, Creekside) — all CLEARED or unverified, none survived as fraud
- Schedule L analysis — analyzer worked, all 3 sampled orgs answered "No" to
  Schedule L questions, which is expected (orgs don't self-incriminate)
- Vendor cluster expansion — Panini Time is the ONLY vendor at $49,950
  going to Cal Fire (no shell network), McKesson/Airgas have many co-vendors
  at $4,999 which is normal commerce

### Inconclusive (acknowledge)
- SAM.gov debarment scan — script written, not run
- Press coverage check (lead_news_check.py) — script written, not run
- Cal eProcure / Power BI line-item drilldown — written, partially executed
  manually (yielded the named procurement officer finding)
- Unit price markup analysis — script written, results inconclusive without
  line-item data from Cal eProcure

## What the Panini Time deep-dive actually showed (combined)

Layer by layer:

1. **Aggregate pattern** (split_contract_deepdive): 12 POs at exactly $49,950,
   100% to Cal Fire, span 719 days, max 4 in any week. Looked suspicious.

2. **Cluster expansion** (vendor_cluster_expand): 0 co-vendors at $49,950
   going to Cal Fire. So it's not a shell network — Panini Time is alone in
   this exact pattern. Could still be either fraud or a single legit recurring
   vendor.

3. **Power BI drilldown** (manual): 5 of the 6 most recent POs (Aug 14 - Sep 9,
   2025) were signed by ONE procurement officer at Cal Fire. Tighter pattern
   than the 719-day span suggested.

4. **Fire context check** (manual + Wikipedia): Those exact dates coincide with
   the King Fire (Aug 14-18, peaked 256 personnel) and the Dillon Fire
   (Aug 28+, peaked 1,760 personnel on Sep 5). Active emergency response.

5. **Honest synthesis:** The fire context plausibly explains the TIMING and
   the same-buyer concentration. It does NOT explain the IDENTICAL $49,950
   amounts across a period when crew sizes varied 7×. Real emergencies
   produce variable-amount POs sized to actual need.

**Final framing:** Threshold-ceiling pattern warranting State Auditor review,
not bid-splitting fraud. Softer finding, more defensible.

## The other Cal Fire vendors (still on the list)

Falcon Fuels — 13 POs at ~$4,999 to Cal Fire. Same fire context applies.
Same threshold-ceiling question: did fuel orders genuinely all round to $4,999?

If the fire-window context script (just shipped) shows that *no other vendor*
had a $49,950 cluster, Panini Time's pattern is unique. If many vendors did,
it's standard Cal Fire emergency procurement habit. **That's the next data point
worth getting.**

## What's the strongest publishable story right now

In order of strength:

1. **The $36B systemic gap.** Period. Lead with this everywhere.
2. **The methodology** — a working forensic pipeline that surfaces
   anomalies AND honestly debunks itself when context emerges.
3. **The Track B findings** — 36 nonprofit anomalies, named with public 990s.
4. **The Panini Time threshold-ceiling case** — as a worked methodology
   example, with the fire context openly acknowledged.

The submission claim is no longer "we found fraud." It's:

> We built a tool that scans California's state spending data, surfaces
> anomalies, and validates them honestly — including dropping initial leads
> when contextual evidence weakens them. We proved a $36B systemic
> accountability gap and surfaced 36+ specific anomalies for State Auditor
> follow-up. Our tool cleared everything it couldn't substantiate.

That's a stronger position than overclaiming on the catering pattern.

## What's left to do before submit

| Task | Time | Value |
|------|------|-------|
| Run `fire_window_context.py` | 5 min | Quantifies whether Panini Time is unique |
| Run `lead_news_check.py` | 5 min | Confirms no prior press coverage |
| Run `second_opinion.py` (AI/ML API) | 10 min | Cross-model validation + partner prize |
| Re-run `schedule_l_analyzer.py` (PDF fix) | 5 min | Schedule L was a dead end but confirm |
| Drop `PITCH_PREP.md` in NotebookLM | 0 work | Audio briefing for the walk |
| Submit | — | — |

Total time to a complete submission: under an hour of Antigravity execution.

## What to NOT do

- Don't keep looking for more vendors. Diminishing returns.
- Don't try to definitively prove Panini Time is fraud. It's not our job.
- Don't burn more Bright Data credits on grants — we've covered that surface.
- Don't lengthen the UI further. It's tight and honest.

Ship it.
