# Next Steps for Antigravity
*Written by Claude Code — 2026-05-26*

## Context

The individual fraud cases (Berkeley, Teknol) resolved as data quality issues, not fraud.
The bigger story is **systemic accountability**: how much of California's grant spending
has zero disbursement tracking?

We have $208 in Bright Data credits remaining and 3.5 days until the hackathon deadline.

---

## TASK 1: Run the Disbursement Audit (HIGHEST PRIORITY)

```bash
python -m src.audit.disbursement_audit --source api
```

This script:
1. Fetches the FULL FY 2022-2023 grants dataset from data.ca.gov (all ~11,698 records)
2. Analyzes how many grants have `TotalAwardUsed = null`
3. Breaks it down by size tier, recipient type, and funding source
4. Identifies high-risk records: private entities with null disbursement and awards > $50K
5. Outputs `accountability_audit.md` (the report) and `data/audit_results.json` (raw data)

If the API is slow, download the CSV manually from:
https://data.ca.gov/dataset/0ae62873-b7f0-498e-a595-476fa8478b0b/resource/86870d5c-e9fa-46f5-8f86-2a9893662ce1/download/grant-awards-fiscal-year-2022-2023.csv

Save it as `data/grants_full.csv` and run with `--source csv`.

**What we expect to find:** A large percentage of grants (possibly 50%+) have no
disbursement tracking whatsoever. This means the state has awarded billions with
no visibility into whether the money was actually spent as intended.

---

## TASK 2: Zero Web Presence Check (USE BRIGHT DATA)

From the high-risk list generated in Task 1, take the top 20 private entities
with null disbursement and run their names through Bright Data SERP API.

The question: does Google know this entity exists?

```python
# For each entity in the high-risk list:
# 1. Search: "{entity_name}" {location} California
# 2. If SERP returns zero organic results → GHOST ENTITY
# 3. If SERP returns results → extract and verify
```

A grant recipient that Google has never heard of is the strongest fraud signal
we've found so far. Combine null disbursement + zero web presence + private entity
= the shortlist worth investigating deeply.

Estimated cost: 20 entities × $0.50/SERP query = $10 in Bright Data credits.

---

## TASK 3: Run Additional Fiscal Years

The same audit should run on:
- FY 2023-2024: resource ID `018f3523-652d-4197-a4a8-a055bfd1544f`
- FY 2024-2025: find the resource ID on data.ca.gov

Set the resource ID in .env:
```
CA_GRANTS_RESOURCE_ID=018f3523-652d-4197-a4a8-a055bfd1544f
```

Cross-year comparison tells us if tracking is getting better or worse.

---

## TASK 4: Presentation Narrative (once Tasks 1-2 are done)

The hackathon story is now:

1. **We built an AI-powered grant fraud detection pipeline** (the tool)
2. **We investigated 22 projects, resolved them all** (the methodology works)
3. **But we discovered something bigger:** California's grant tracking is broken
   - X% of grants have zero disbursement data
   - $X billion in awards with no spend visibility
   - Among private entities specifically: X grants totaling $X with no tracking
   - Y entities receiving public money that don't exist on the public web
4. **This is the real finding:** You can't catch fraud if you can't even track
   whether the money was spent

This shifts from "we found one bad actor" to "we proved the system can't find bad actors."
That's a much stronger hackathon submission.

---

## What NOT to do

- Don't re-run Stage 1-3 on new data (we have enough individual cases)
- Don't spend Bright Data budget on more individual investigations
- Don't anonymize the audit findings — they're aggregate stats, not accusations
- Focus on the accountability audit numbers and the zero-web-presence check
