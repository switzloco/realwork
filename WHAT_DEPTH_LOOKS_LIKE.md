# What Depth Would Look Like
*Appendix to the hackathon submission. An honest answer to "what would you do with three more weeks and no time constraint?"*

The hackathon work went **wide**: three data streams, ~14 scripts, 1,751 entities pattern-scanned, 500 nonprofits cross-referenced. A real investigation would go **deep**: pick 1-3 of the strongest leads and pursue each to a State Auditor-ready dossier or a qui tam consultation. This appendix sketches what that depth-first version looks like.

## Step 1 — Pick the targets, not the dataset

A depth-first investigation starts by picking the entity, not by scanning a database. With what we have today, the three best targets would be:

1. **Trybe Inc.** (EIN [REDACTED IN PUBLIC DOC]) — $834K officer compensation at an organization receiving $500K in CA state grants. The officer comp alone exceeds the entire state grant. That's the single most extreme officer-comp-to-state-grant ratio in our dataset.
2. **Kounkuey Design Initiative** — $892K officer comp at a $473K-state-grant org. Similar pattern.
3. **Veterans Transition Center of California** — $722K officer comp, $1.6M state grants, YoY spike. Larger dollar volume than the first two; possibly easier to investigate because of size.

Pick ONE. Go deep.

## Step 2 — Read the rules cold

Before touching the data, learn the actual rules that govern the entity:

- The specific state grant program(s) the org received money from. Pull the **Notice of Funding Availability (NOFA)**, the **grant agreement template**, the **monitoring requirements**, and the **closeout requirements**.
- The nonprofit's classification and the rules that apply to it. 501(c)(3) public charity vs. private foundation, churches, etc. — different sets of governing rules.
- The state's grant accountability framework. AB-132. Government Code §§ 8333-8334.1. The State Administrative Manual (SAM) sections on grants.
- The IRS rules on related-party transactions. Form 990 Schedule J and Schedule L disclosure thresholds and definitions.

For Trybe Inc specifically: pull the state grant agreement from the awarding agency (CA Department of [whichever], FOIA if needed). Compare reported expenditures against the agreement's allowable-use clauses.

## Step 3 — Build the entity map

For the chosen target, build a complete map of:

- **Legal entities.** SOS registration, related LLCs/corporations under same officer(s), parent/subsidiary structure.
- **Officers and directors.** Names, LinkedIn profiles, prior nonprofit boards, professional licenses, criminal/civil court history.
- **Addresses.** Registered, mailing, operational. Cross-reference against personal residences of officers (red flag if the org's "office" is the executive director's home).
- **Bank relationships and major vendors.** Reported on Form 990 Schedule R and other schedules.
- **Auditor.** Who audited the org's financials. If a small CPA firm with no other nonprofit clients, that's a flag.

Bright Data tools we'd use for this:
- Web Unlocker on CA Secretary of State business registry for the entity number, status, and officer list
- SERP API for officer LinkedIn profiles and any news coverage
- OpenCorporates via Web Unlocker for related entities under the same officers
- Property records via county assessor sites (each county has its own portal)

## Step 4 — Read the 990s in full

The aggregate metrics our pipeline computes are screening signals, not findings. A depth investigation reads the actual filings:

- **Form 990 main filing.** Lines 1-22 (revenue/expense lines). Look at the *categories* of revenue and expense, not just the totals. Where is the money coming from? Where is it going?
- **Schedule A.** Public support test. Is the org actually public-supported or is it functionally a private foundation?
- **Schedule J.** Detailed compensation. Is the high officer comp justified by hours worked, comparable salary data, and board approval?
- **Schedule L.** Related-party transactions. Even an answer of "No" matters — if the org has obvious related parties (officer's spouse, officer's other business) and Schedule L shows "No," that's a disclosure failure worth flagging.
- **Schedule O.** Supplemental narrative. The org's own explanation of unusual items. Often where the actual story is told.
- **Schedule R.** Related organizations. Sister nonprofits, controlled entities, partnerships. The fraud often lives here.
- **Independent auditor's report.** Attached to larger 990s. Read the management letter if available.

For Trybe Inc: pull the actual 990 PDF, read every page, flag every unusual item with a specific question for the State Auditor or qui tam attorney.

## Step 5 — Pull the underlying grant agreement

The state grant award database tells you that money was awarded. The grant agreement tells you what the money was supposed to be spent on. This is the document a fraud investigation hinges on.

- File a Public Records Act request with the awarding agency for the grant agreement, the budget justification, the progress reports, the final closeout report, and any monitoring documentation.
- Pull the agency's published audit reports for the program.
- If the program was federally pass-through funded, pull the federal award terms via USAspending.gov.

Most fraud is found by comparing **what the grant agreement allowed** against **what the 990 says the money was spent on**. The agreement says "youth services in San Bernardino County." The 990 says "consulting services to [related entity]." That's the case.

## Step 6 — Run the entity name through the regulatory grid

For the chosen target, cross-check against every regulatory dataset that might surface a flag:

- **SAM.gov debarment list.** Federally excluded entities.
- **CA Franchise Tax Board.** Status — Active / Suspended / Forfeited.
- **CA Attorney General Registry of Charitable Trusts.** Form RRF-1 filings, registration status.
- **CA Department of Justice (DOJ) charity registration.**
- **State Auditor's published I-series reports.** Has this entity been investigated before?
- **PACER federal court records.** Civil and criminal litigation.
- **CA Superior Court records.** State litigation, county-by-county.
- **News archive search.** Local press coverage, especially.

Most of these can be partially automated via Bright Data Web Unlocker on the relevant search portals. A depth investigation does each one manually for the chosen target.

## Step 7 — Write the dossier

A State Auditor-ready dossier is approximately:

- **1 page summary** — what the entity is, what the pattern is, why it warrants review
- **2-3 pages of evidence** — every claim cited to a public document, with stable URLs
- **1 page of "charitable explanations considered and not yet ruled out"** — the honest other-side-of-the-argument analysis
- **1 page of recommended next steps** — specific questions the State Auditor's subpoena power could answer that public records cannot

The dossier is the deliverable. It is the document that converts "anomaly in public data" into "investigation lead."

## Step 8 — Consult a qui tam attorney before public disclosure

If the pattern looks False Claims Act-actionable (state grants spent on non-allowed uses, false certification of compliance, etc.):

- Find a CA qui tam attorney. The CA Bar Lawyer Referral or organizations like Taxpayers Against Fraud Education Fund are starting points.
- Initial consultations are typically free and confidential under attorney-client privilege.
- The attorney evaluates standing, suggests jurisdiction (state CFCA vs. federal FCA), and may file under seal.
- Public disclosure (e.g., posting the dossier on a public repo) **before** filing can affect qui tam standing. Hold the public version until the attorney confirms.

## Step 9 — Submit the State Auditor tip (or the qui tam filing)

If qui tam is not the right path, submit a citizen tip to the State Auditor using one of the templates in `STATE_AUDITOR_TIP_TEMPLATES.md`. Link the repo for methodology. Cite the public records.

If qui tam IS the right path, the attorney handles filing under seal. You do not publish the dossier until the case is unsealed by the court (months to years).

---

## How much of this could we do in five hackathon days?

We did Steps 1, 2 (partially), and 4 (partially) for the 36 HIGH PRIORITY Track B entities at the aggregate-pattern level. We did NOT do Steps 3, 5, 6, 7, 8, or 9 for any single entity to depth.

**Estimated time for a single complete dossier:** 8-12 hours of focused human work, or 2-3 hours of focused AI-assisted work with subpoena-substitute access to FOIA-able documents. We could fit one Trybe Inc dossier in a long evening if we focused.

This appendix is the answer to "what would you do with more time." It is also the recommended next step after submission.

---

## Why we didn't do this for the hackathon

Two reasons, honestly:

1. **Hackathon optimization.** Breadth makes for a stronger judge demo than depth. A pipeline that scans 1,751 entities looks more impressive than a 5-page memo on one entity. The judging criteria reward what we did. They would not reward a single deep dossier the same way.

2. **Risk surface.** Naming a single specific entity in detail as a public hackathon deliverable creates legal exposure (defamation risk) that the aggregate pattern framing avoids. The dossier is the right artifact for the State Auditor's confidential channel — not the right artifact for a public lablab.ai submission.

If you are reading this appendix as part of the hackathon judging: the depth-first version of this project exists in plan, and we are equipped to ship it after the submission window. The State Auditor receives our tips; the qui tam attorneys evaluate our strongest candidates; the depth dossiers ship through the right channels, not through GitHub.

If you are reading this appendix as a future investigator: clone the repo, pick a HIGH PRIORITY entity, follow Steps 1-9. The tool gets you to Step 2. The rest is the human work that the tool cannot do.
