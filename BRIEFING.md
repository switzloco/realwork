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

1. **Teknol is legitimately building or renovating a child care facility** and we haven't found evidence yet. Rahul Beri has real childcare sector ties (nonprofit board, childcare software). It's plausible he's opening a physical facility with Teknol as the entity. NCMR eligibility requires having an operating facility before Aug 2021, but we can't search CCLD automatically to verify. **This is now a stronger possibility than initially assessed.**

2. **Teknol applied based on childcare software credentials, not a physical facility.** If they don't operate a licensed facility, they wouldn't meet NCMR eligibility requirements. The grant is explicitly for physical construction of childcare facilities.

3. **The grant was awarded but never disbursed.** Checking `totalAwardUsed` in the dataset would resolve this quickly.

### What makes this interesting
- A digital marketing/software company receiving the maximum possible grant ($1.5M) for physical childcare facility construction
- No contractor's license, no CSLB record, no evidence of construction capability
- But real childcare sector connections through software and nonprofits
- **Still no evidence of a licensed childcare facility** — the critical piece

### What we still don't know
- Does the CCLD database have a facility licensed to Teknol or Beri? (requires manual browser search)
- Was the $1.5M actually disbursed? (requires querying `totalAwardUsed` from data.ca.gov API)
- What did Teknol's NCMR application say they'd build? (requires public records request to DSS)

### Hackathon value
HIGH — but frame carefully. The anomaly is real (software company + construction grant), the investigation process is compelling, but the explanation may be innocent. This is actually a *better* demo than "we found fraud" because it shows the tool's nuance: flag, investigate, and present the evidence for humans to decide.

### Honest assessment
The Teknol case got weaker with the date correction. It's still an anomaly worth investigating, but "multiple $1.5M grants on the same suspicious day" was a data artifact, not a fraud pattern. The core question — does a software company have a licensed childcare facility? — is still unanswered and still worth asking.

---

## What To Do Next

### For the hackathon (by May 30):

1. **Don't change the evidence.** What you have is already strong. Both cases are verified with real sources.
2. **Record the demo video** showing the pipeline finding these anomalies. The narrative arc is: "We fed in 11,698 grant records, the AI flagged 40, we investigated 22, cleared 14, and found 2 that are genuinely concerning."
3. **Use the Berkeley case** to show the tool catches data integrity failures.
4. **Use the Teknol case** to show the tool catches potential misuse of grant programs.
5. **Anonymize in the GitHub repo.** Use "[Entity A]" and "[Entity B]" in any findings pushed publicly. Show real names only in the live demo.

### For real life (after the hackathon):

6. **Do NOT contact Teknol, Rahul Beri, DSS, or any press.** If this is a real misuse of funds, the California False Claims Act (qui tam) lets you file a claim under seal and receive 15-30% of any recovered funds. Public disclosure before filing forfeits that position.

7. **Next investigation steps** (if you want to pursue this):
   - **[DO THIS FIRST — 2 minutes]** Manually search https://www.ccld.dss.ca.gov/carefacilitysearch/ for "Teknol" and "Beri" — this tells you whether they operate a licensed facility. If yes, the case is probably clean. If no, it gets very interesting.
   - **[DO THIS SECOND — 5 minutes]** Have Antigravity query the data.ca.gov API for Teknol's record and check the `totalAwardUsed` field. If it's $0 or empty, the grant may never have been disbursed.
   - Pull the actual NCMR grant application (public records request to DSS) to see what Teknol claimed they'd build
   - The "same date" pattern is likely just the eligibility cutoff date (2021-08-01) stored in the wrong field — not suspicious

8. **Talk to a qui tam attorney** if step 7 turns up more smoke. They work on contingency (you pay nothing upfront). Google "California qui tam attorney" or "False Claims Act whistleblower lawyer." Initial consultations are typically free. The attorney will tell you whether there's enough for a case and handle the filing.

9. **Keep your name clean.** Your tool identifies anomalies. You are not accusing anyone of fraud. You are flagging discrepancies that warrant investigation by qualified authorities. This framing protects you legally and is also just accurate — you don't know the full story yet.

---

## Budget Status
- **Bright Data spent:** $41.50 of $250 (GREEN zone)
- **Projects investigated:** 22
- **Gemini API cost:** estimated $5-15 total
- **Total project cost so far:** ~$50-60
