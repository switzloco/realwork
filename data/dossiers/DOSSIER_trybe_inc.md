# Investigation Dossier — Trybe Inc.
*A worked example of what a single-entity deep dossier looks like when the pipeline finds a HIGH PRIORITY anomaly. Every claim cites public records. This is the framing the State Auditor's office uses, not a fraud accusation.*

**Prepared:** May 2026, as a methodology demonstration for the RealWork hackathon submission.
**Subject:** Trybe, Inc. (a California nonprofit; the underlying IRS Form 990 is a public document)
**Status:** Anomaly warranting review by the California State Auditor.

---

## Executive summary

Trybe, Inc. — a California 501(c)(3) public charity — received $500,000 in California state grants in tax year 2023, per the California Grants Portal published on data.ca.gov. Trybe's publicly-filed IRS Form 990 for the same tax year reports **$834,009 in compensation to current officers, directors, and trustees**.

In other words: the organization's reported compensation to its officers exceeds the entire state grant award by approximately 67%. The officer-compensation ratio is also significantly above sector medians for small program-delivery nonprofits.

Three patterns combine in this filing:

1. **Officer compensation greater than state grant value.** Most nonprofits use state grants to fund program delivery. Trybe's 2023 990 reports compensating its leadership at $1.67 for every $1 of state grant received.
2. **Year-over-year compensation increase concurrent with state funding.** Officer compensation grew substantially YoY in the same fiscal year the organization received state grants.
3. **High officer-compensation ratio at a small organization.** Trybe is below the $5 million expense threshold our pipeline uses to flag organizations where executive compensation should be proportionate to total program scope.

We are not asserting fraud. We are surfacing a pattern present in public records that warrants review by an entity with subpoena authority.

---

## Public records cited

| Source | URL / Reference |
|--------|-----------------|
| IRS Form 990 (tax year 2023) | ProPublica Nonprofit Explorer (search by org name or EIN) |
| CA Grants Portal — FY 23-24 awards | https://data.ca.gov/dataset/california-grants-portal-grant-awards-2023-2024 |
| CA Secretary of State business registry | https://bizfileonline.sos.ca.gov |
| CA Attorney General Registry of Charitable Trusts | https://oag.ca.gov/charities |
| Methodology and source code | https://github.com/switzloco/realwork |

---

## The flags our pipeline raised

These flags survived our wrong-EIN sanity validation and our cross-model ensemble check via AI/ML API. Both Gemini 2.5 Pro (primary) and GPT-4o (second opinion) independently flagged the same pattern.

- **HIGH_OFFICER_COMP_SMALL_ORG**: $834,009 in officer compensation at an organization below the $5M expense threshold our pipeline uses for proportionality screening.
- **HIGH_OFFICER_COMP_RATIO**: Officer compensation represents a high percentage of total expenses, substantially above the CharityNavigator / GuideStar published sector median of approximately 8-10% for program-delivery nonprofits.
- **OFFICER_COMP_YOY_SPIKE**: Officer compensation increased materially from the prior fiscal year to the most recent reported year, during the same window the organization received state grants.

---

## Charitable explanations to rule out

A depth investigation must rule these out before treating the pattern as a finding:

1. **Multi-year grant amortization.** State grants are sometimes awarded in one year and disbursed/recognized over multiple years. The 990 may reflect partial recognition. **Status:** To be confirmed by reviewing the actual grant agreement and the org's audited financials, neither of which we have access to from public sources.
2. **Fiscal sponsorship arrangements.** The org may serve as a fiscal sponsor for other entities, in which case the headline numbers are misleading. **Status:** Reviewable on Schedule R of the 990. From our public-records review, Trybe does not appear to operate as a fiscal sponsor.
3. **Comparable-position salary justification.** Form 990 Schedule J requires the org to disclose how it justified high compensation against comparable positions. **Status:** The State Auditor's office can subpoena Schedule J supplemental documentation; we cannot from public records.
4. **Board-approved compensation process.** The org is required to document that compensation was approved by an independent board using comparable-salary data. **Status:** Reviewable on Form 990 Part VI. We have not yet examined the specific Part VI disclosures.

None of these have been ruled out. They are explicitly part of why this pattern warrants review by an entity with subpoena authority — public records alone cannot resolve them.

---

## What the State Auditor's investigators could do that we cannot

This is the core "why escalate" justification:

- Subpoena Schedule J supplemental compensation documentation, including comparable-salary justifications
- Subpoena the underlying state grant agreement and progress reports from the awarding agency
- Compare reported grant expenditures against the grant agreement's allowable-use clauses
- Interview the organization's auditor about the YoY compensation increase
- Review Part VI Section B for independence of the compensation-approval process
- Cross-reference Schedule R for related-party transactions not captured on Schedule L

---

## Recommended next step

We recommend submission of this dossier to the California State Auditor's confidential whistleblower hotline (auditor.ca.gov/hotline) using Template 1 in our `STATE_AUDITOR_TIP_TEMPLATES.md`. The pattern is consistent with the State Auditor's published I-series investigation criteria.

We do **not** recommend public publication of an unredacted version of this dossier (e.g., as a news story or open letter) prior to:

1. Qui tam attorney consultation, to evaluate whether the pattern is California False Claims Act-actionable. Public disclosure before qui tam filing under seal can affect standing.
2. The organization being given an opportunity to respond. Schedule J justifications and audited financial statements may resolve all three charitable explanations.

---

## Methodology

This dossier was produced by:

1. **Identifying** Trybe Inc as a HIGH PRIORITY anomaly in our Track B nonprofit overhead audit (`data/track_b/validated_report.md`). The org passed our wrong-EIN sanity validation (100% name overlap with the matched ProPublica record, CA state confirmed).
2. **Verifying** via cross-model ensemble: Gemini 2.5 Pro (primary) and GPT-4o (via AI/ML API) both independently flagged the same pattern when given the same facts.
3. **Cross-referencing** the org's Form 990 data (via ProPublica Nonprofit Explorer, accessed through Bright Data Web Unlocker) against the CA Grants Portal CKAN API.
4. **Writing** this dossier as a worked example of what the next step looks like when the pipeline surfaces an anomaly: name the entity, cite the records, list the charitable explanations that must be ruled out, recommend the specific oversight channel.

All steps are reproducible via the scripts in the linked repo.

---

## Disclaimer

This dossier is a methodology demonstration. It does not assert that Trybe Inc has engaged in fraud, illegal activity, or wrongdoing of any kind. The patterns described are present in publicly filed records. The charitable explanations may all hold and the matter may be entirely explained by documentation we do not have access to. We are surfacing a pattern for review by an entity with the authority and access to evaluate it definitively.

If Trybe Inc, its officers, board members, or representatives believe any factual statement in this dossier is incorrect, we will correct it. Contact the repository maintainer at the GitHub URL above.
