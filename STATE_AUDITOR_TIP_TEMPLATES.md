# State Auditor Tip Letter — Templates
*Pre-filled drafts ready for submission to the California State Auditor's confidential whistleblower hotline (auditor.ca.gov). Replace bracketed fields and review before sending. Not legal advice.*

## Where to submit

**California State Auditor**
Whistleblower Hotline: **800-952-5665**
Web form: https://www.auditor.ca.gov/hotline
Email: hotline@auditor.ca.gov
Mail: California State Auditor, Investigations, 621 Capitol Mall, Suite 1200, Sacramento, CA 95814

Submissions are confidential under California Government Code § 8547.5. Whistleblower retaliation protections apply.

**Note:** For potential California False Claims Act qui tam, consult a qui tam attorney *before* sending the tip to the State Auditor — public disclosure can affect qui tam standing.

---

## Template 1 — Nonprofit financial pattern (Track B-style)

> Re: Form 990 anomalies — [ORGANIZATION NAME], EIN [XX-XXXXXXX]
>
> To the State Auditor:
>
> I am submitting public-records analysis suggesting that [ORGANIZATION NAME] (EIN [XX-XXXXXXX], based in [CITY, CA]) warrants review by your office. The organization received approximately **$[STATE GRANT TOTAL]** in California state grants during fiscal year [YEAR] from [STATE AGENCY OR PROGRAM]. Public IRS Form 990 filings for the same period show patterns that, in my analysis, warrant follow-up:
>
> 1. **Officer compensation:** $[OFFICER COMP TOTAL] paid to one officer at an organization reporting total expenses of $[TOTAL EXPENSES]. That ratio ([X]% of expenses to one officer) is substantially above the sector median of 8-10% reported by CharityNavigator and GuideStar.
>
> 2. **Year-over-year change:** Officer compensation grew [X]% from the prior fiscal year ($[PRIOR] → $[CURRENT]) during the same period the organization received state grants of $[STATE GRANT TOTAL].
>
> 3. **State funding vs. reported revenue:** The state's published grant award database shows the organization received $[STATE GRANT TOTAL] in CA grants during a year for which the organization reports total revenue of $[REPORTED REVENUE] on Form 990. The discrepancy may be explained by multi-year disbursement, fiscal sponsorship, or restricted-grant accounting — but it warrants confirmation.
>
> **Public records cited:**
> - Form 990 (Tax Year [YEAR]): https://projects.propublica.org/nonprofits/organizations/[EIN]
> - CA Grants Portal: https://data.ca.gov/dataset/california-grants-portal-grant-awards-[FY]
> - Methodology and data: https://github.com/switzloco/realwork
>
> I am not making a legal determination of fraud. I am surfacing a pattern present in public records that I believe warrants review by an entity with subpoena authority. I am happy to provide additional underlying data on request.
>
> Sincerely,
> [YOUR NAME]
> [CONTACT]

---

## Template 2 — Procurement threshold-edge pattern (DGS-style)

> Re: Repeated threshold-edge purchase orders — [VENDOR NAME] / [STATE AGENCY]
>
> To the State Auditor:
>
> I am submitting public-records analysis suggesting that a pattern of state purchase orders to [VENDOR NAME] from the [STATE AGENCY] warrants review. The pattern was identified through automated analysis of the DGS Purchase Order public dataset (data.ca.gov, fiscal years [Y]–[Y+2]).
>
> **The pattern:**
>
> - [N] purchase orders to [VENDOR NAME] at amounts of exactly $[THRESHOLD-1] each (totaling $[TOTAL])
> - [N] of those POs were issued by a single procurement officer at [STATE AGENCY] within a [N]-day window
> - The amount $[THRESHOLD-1] is exactly $[GAP] below the [STATE AGENCY]'s competitive-bidding threshold of $[THRESHOLD], above which formal bid solicitation is required under Public Contract Code §§ 10301-10340 and the State Contracting Manual
> - No subcontractors are disclosed on any PO
>
> **Charitable explanations to rule out:**
>
> - **Emergency procurement.** [If applicable: "The window coincides with [EVENT, e.g., wildfire response]. Expedited procurement rules may apply. However, emergency procurement is expected to produce variable PO amounts sized to actual operational need, not identical-amount POs across a window when underlying need varied substantially."]
> - **Recurring supply relationship.** A single ongoing vendor relationship typically produces POs at varied amounts reflecting actual purchase quantities, not identical sums repeating across multiple separate POs.
>
> **The factual pattern matches** the bid-splitting signature documented in the 2019 federal prosecution of three Caltrans procurement officials (USA v. Yong, Miller, Opp — 49 to 78 month sentences, $3M restitution).
>
> **Public records cited:**
> - DGS Purchase Order data: https://data.ca.gov/dataset/purchase-order-data
> - Specific PO numbers: [LIST]
> - Methodology: https://github.com/switzloco/realwork
>
> I am not alleging fraud. I am identifying a procurement pattern matching documented fraud signatures and asking that your office determine whether the underlying decisions complied with State Contracting Manual provisions on threshold-edge purchasing.
>
> Sincerely,
> [YOUR NAME]
> [CONTACT]

---

## Template 3 — Systemic data integrity / disbursement gap

> Re: Systemic compliance gap — AB-132 post-award disbursement tracking
>
> To the State Auditor:
>
> I am writing to report a systemic data-integrity issue, not a specific entity finding. The Grant Information Act of 2018 (AB-2252, codified at Government Code §§ 8333-8334.1) and AB-132 require grantmaking state agencies to track post-award disbursement of state grants. This data is required to be published on the California Open Data Portal.
>
> **The finding:** We pulled both available fiscal years (FY 2022-23 and FY 2023-24) from data.ca.gov's CKAN API. Of **26,907 grant records totaling $36,585,412,711 in awards**, the `totalAwardUsed` field is empty on **100%** of records. No grantmaker has reported post-award disbursement under the statutorily-required schema.
>
> The implication is that the state currently has no centralized record of whether any of $36.5 billion in awarded grants was actually spent as awarded. This affects oversight at every level — your office, the legislature, journalists, and any qui tam attorney evaluating cases under the California False Claims Act.
>
> **Public records / reproduction:**
> - CKAN resource (FY 22-23): `86870d5c-e9fa-46f5-8f86-2a9893662ce1`
> - CKAN resource (FY 23-24): `018f3523-652d-4197-a4a8-a055bfd1544f`
> - Pull script (reproduces the finding in approximately 10 minutes): https://github.com/switzloco/realwork/blob/main/src/audit/disbursement_audit.py
>
> I would welcome any guidance on whether this gap is known to your office, whether the responsible agencies have been issued findings, and whether AB-132 compliance is on your current high-risk audit list.
>
> Sincerely,
> [YOUR NAME]
> [CONTACT]

---

## Use checklist before submitting

- [ ] **Read the qui tam guidance.** If you think the pattern might be False Claims Act-actionable, consult a qui tam attorney first. Public disclosure can affect standing.
- [ ] **Anonymize sources you don't want disclosed.** State Auditor submissions can be subject to public records requests in some cases.
- [ ] **Cite public records only.** Do not include anything you obtained through non-public channels.
- [ ] **Frame as "warrants investigation," not "is fraud."** Let the State Auditor make the legal determination.
- [ ] **Provide reproducible methodology.** Link the repo and the specific scripts. The State Auditor's investigators can re-run your analysis.
- [ ] **Save a copy.** Keep a timestamped copy of what you sent.

---

## What happens after you submit

- The State Auditor's office acknowledges receipt within ~5 business days (auto-generated for the web form).
- Investigations of Improper Activities (I-series reports) typically take 3-12 months when accepted.
- The State Auditor publishes findings in their semi-annual I-series reports. Look at past reports for what accepted-and-investigated cases look like: https://www.auditor.ca.gov/reports
- Some tips are referred to other agencies (DOJ, CHP, the Fair Political Practices Commission, etc.) depending on jurisdiction.
- You will generally not be told the disposition of your specific tip beyond receipt confirmation.

---

*Last updated: May 2026. Templates derived from public sources including California Government Code, State Contracting Manual, and prior State Auditor I-series reports. Not legal advice. Consult a qui tam attorney before submitting tips that may be False Claims Act-actionable.*
