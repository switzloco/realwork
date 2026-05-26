# RealWork Investigation Briefing
*For: Nick Switzer | Date: 2026-05-26*

---

## What is this?

You built a tool that scans California's public grant database for anomalies. It found two genuinely interesting cases. This document explains what was found, what it means, and what to do next.

---

## Case 1: The Scrambled Grant Record (Berkeley / Water District)

### What the database says
A single grant record in data.ca.gov shows:
- **Project name:** South Berkeley Senior Center Seismic Retrofit
- **Recipient:** City of Berkeley
- **Amount:** $1,470,000
- **Funder:** Governor's Office of Emergency Services
- **BUT the project description says:** "The Western Municipal Water District will install a permanent backup diesel engine-driven self-primed pump at the WRCRWA Treatment Plant's South Regional Pump Station"

Berkeley is in Alameda County. The water district is in Riverside County. These are 400 miles apart.

### What we verified
Both projects are real:
- **Berkeley** really did get ~$1.2-1.5M from FEMA's Hazard Mitigation Grant Program for a seismic retrofit of the South Berkeley Senior Center. City council reports confirm this.
- **Western Municipal Water District** really does operate the South Regional Pump Station serving the WRCRWA (Western Riverside County Regional Wastewater Authority) treatment plant. FEMA issued a public notice for an HMGP grant to them under disaster declaration DR-4558-CA for a backup generator.

### What it means
Someone at Cal OES (or whoever enters data into the state grants portal) copy-pasted the wrong project description into this record. Two completely unrelated FEMA grants — one in Berkeley, one in Riverside — got merged into a single database row.

**This is not fraud. It's a data integrity failure.** But it's still significant:
- $1.47M in public money has a corrupted audit trail
- If an auditor tried to verify this grant, they'd be chasing a water pump in Riverside when the money actually went to a senior center in Berkeley
- It raises the question: how many other records in this database have scrambled fields?

### Hackathon value
HIGH. This is a perfect demo case — your tool caught a real, verifiable anomaly in a real government database. It's not fraud, but it's exactly the kind of thing oversight tools should find. Lead with this in the video.

---

## Case 2: The Tech Company Getting Construction Grants (Teknol Inc)

### What the database says
- **Recipient:** Teknol Inc
- **Amount:** $1,500,000 (the maximum allowed)
- **Funder:** CA Department of Social Services
- **Category:** New Construction and Major Renovation (NCMR)
- **Location:** Santa Clara County

### What we verified

**About the NCMR program:**
- NCMR grants are specifically for **building or renovating licensed child care facilities**
- Run by CA Department of Social Services, Child Care and Development Division
- $150 million total program
- Licensed child care centers can receive up to exactly **$1,500,000** (the max — which is what Teknol got)
- Recipients must be childcare providers undertaking physical construction

**About Teknol Inc:**
- Real company, incorporated in CA ~October 2015
- Headquartered at 1050 Park Ave, San Jose, CA 95126
- Founded by **Rahul Beri** (CEO since 2015)
- **Teknol is a digital marketing agency and software company.** It builds websites, does SEO, runs ad campaigns
- It has a childcare technology vertical: products include **PREto3** (childcare management software), **Avo Kids** (daycare marketplace for parents), **Circle Time Jobs** (childcare staffing)
- BBB classifies it as an "Educational Consultant"
- 11-50 employees
- **No contractor's license. No construction capabilities. No evidence it operates a physical childcare facility.**
- Website is teknol.xyz

**About JM3 Holdings LLC (another NCMR recipient, same date field):**
- Registered in Merced, CA
- Evidence links it to operating a day care center — which would make it a legitimate NCMR recipient
- Has the same "2021-08-01" date in the award_date field (see below)

**Critical update — the "2021-08-01" date is NOT an award date:**
- The NCMR program requires applicants to have "at least one child care facility in operation **on or before August 01, 2021**"
- The program was enacted July 23, 2021. Applications were due January 31, 2023. Awardees notified September 2022.
- The date "2021-08-01" in the grant database is almost certainly the **eligibility cutoff date** stored in the award_date field, not the date money was awarded
- This means the "multiple grants on the same day" pattern is a data quality issue, not evidence of suspicious batch processing

**Child care facility license search:**
- No license found for "Teknol Inc," "Rahul Beri," or address "1050 Park Ave, San Jose" via web searches of the CA CCLD facility database
- The CCLD search tool (ccld.dss.ca.gov) blocks automated access — **a manual browser search is needed to confirm**
- Rahul Beri does have childcare sector involvement: board member at Silicon Valley 4 Kids (youth programs nonprofit), founded PREto3 (childcare SaaS)

**The grants dataset HAS a disbursement field:**
- Field called `totalAwardUsed` — the amount actually spent/disbursed
- It exists alongside `totalAwardAmount` in the data.ca.gov schema
- Our ETL doesn't capture it yet — we could query the API to check if Teknol's $1.5M was actually disbursed

### What it means (updated assessment)

There are a few possibilities, ranked by likelihood:

### RESOLVED — Teknol operates a real childcare facility

**Manual CCLD search confirmed:** Teknol Inc is the licensee of **"Laurel Play Gardens"**, an infant center at 1050 Park Ave, San Jose, CA 95126.
- Licensed 12/1/2023, capacity 14, facility type: Infant Center
- Owners: **Aakriti Beri and Rahul Beri** (Rahul is Teknol's CEO)
- 8 state visits since October 2023, most recent 05/20/2026
- One complaint investigated (child left unattended allegation) — **unsubstantiated** after video review showed proper supervision
- Staff on site during inspection: site supervisor + 2 teacher assistants + 7 infants

**Timeline makes sense:** Grant awarded ~2022 → construction/renovation → facility licensed December 2023 → operating since.

**However — the disbursement data is still anomalous:**
- `TotalAwardAmount`: $1,500,000
- `MatchingFundingAmount`: $150,000
- `TotalAwardUsed`: **null**

After nearly 5 years and a facility that's been open since 2023, the state's database has zero visibility into how much of the $1.5M was actually spent. Either the money was never disbursed, or the tracking is completely broken. Both are concerning — not about Teknol specifically, but about systemic accountability.

### Final assessment
**Teknol is NOT a fraud case.** The initial flags were reasonable (software company + construction grant), the investigation was thorough, and the resolution is clean. This is the pipeline working exactly as designed: flag → investigate → resolve.

### Hackathon value
VERY HIGH — not as a fraud finding, but as a complete investigation arc. Flag, investigate, resolve. Plus the `TotalAwardUsed: null` discovery points to a systemic accountability gap that may be the bigger story.

---

## What To Do Next

### For the hackathon (by May 30):

1. **Lead with the investigation arc**, not "we found fraud." The story is: 11,698 records → AI flags 40 → investigate 22 → clear 15 → 1 confirmed data integrity failure (Berkeley) → 1 complete flag-to-resolution cycle (Teknol) → systemic accountability gap discovered (null disbursements)
2. **The `TotalAwardUsed: null` finding may be the biggest story.** Query the ENTIRE dataset for how many grants have null disbursement tracking. If it's thousands of records and billions of dollars with no spend visibility, that's a headline.
3. **Anonymize in the GitHub repo.** Use "[Entity A]" and "[Entity B]" in any findings pushed publicly. Show real names only in the live demo.

### For finding real fraud — strategic pivot:

4. **We may be looking in the wrong category.** Infrastructure/construction grants to cities and known entities are heavily monitored. The fraud is more likely in:
   - **Grants to private entities** (LLCs, sole proprietors) with weak oversight
   - **Smaller, less-monitored programs** where nobody's watching
   - **Entities that don't exist at all** — not "software company doing construction" but "company that literally has no presence anywhere"
   - **Grants where TotalAwardUsed is null AND the recipient has no web/registry footprint** — that's the intersection of "money untracked" and "entity unverifiable"

5. **The systemic angle might be worth more than any single case.** If you can show that X% of California grants have zero disbursement tracking, that's a finding that affects billions, not millions. The tool becomes "we audited California's grant accountability and found a black hole."

6. **Bright Data + CCLD:** Yes, Web Unlocker or Scraping Browser could automate the CCLD facility search. That would let you batch-verify whether NCMR recipients actually have licensed facilities — a much more powerful check than doing it one at a time in a browser.

### Next investigation moves:

7. **[HIGH PRIORITY] Query the full dataset for TotalAwardUsed = null.** How many grants? What's the total dollar value? This is free (just API calls to data.ca.gov).
8. **[HIGH PRIORITY] Look for grants to entities with ZERO web presence.** Run SERP searches for the recipient names of flagged projects. If Google returns nothing — no website, no business listing, no LinkedIn, no news — that's a much stronger fraud signal than "wrong industry."
9. **[MEDIUM] Cross-reference recipients against SoS business registry.** Grants to entities with "Suspended" or "Forfeited" status = immediate red flag.
10. **[MEDIUM] Automate CCLD checks via Bright Data** for all NCMR recipients — verify they have actual licensed facilities.

### Legal guidance (unchanged):
- If you find something real: qui tam attorney first, no public disclosure
- Frame everything as "anomalies warranting investigation"
- Keep your name clean — you built a tool, you didn't make accusations

---

## Budget Status
- **Bright Data spent:** $41.50 of $250 (GREEN zone) — **$208 remaining**
- **Projects investigated:** 22
- **Gemini API cost:** estimated $5-15 total
- **Total project cost so far:** ~$50-60
- **Plenty of budget for a strategic pivot**
