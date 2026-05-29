# Where Fraud Actually Hides
*Strategy note — 2026-05-28*

## The Question

Two rounds, two fiscal years, 27K records scanned, ~60 deeply investigated, $0
of confirmed fraud. The reasonable suspicion is: **we're looking in the wrong
place.** This note explains why that's almost certainly correct and where the
real fraud likely lives.

---

## Why the CA Grants Portal Is a Bad Hunting Ground

The Grants Portal is the *cleanest* slice of state spending by design:

1. **Awards, not payments.** The dataset records that a grant was awarded.
   It does not record what was paid, when, to whom, or for what milestones.
   The disbursement-tracking field is empty for ~100% of records — meaning
   fraud at the *spending* stage is invisible to anyone reading this data.

2. **High visibility = high gatekeeping.** Grant programs that show up here
   have application processes, scoring rubrics, eligibility reviews, and
   public award announcements. Easy to scrutinize. Hard to game without
   getting caught at the front door.

3. **Big dollar amounts = big audit attention.** A $1.5M NCMR award gets a
   compliance officer, possibly a CPA audit, possibly a site visit. The
   $5,000 sole-source consulting contract gets no one.

4. **"Recipient" is the prime, not the spender.** A grant to a fiscal
   agent or pass-through entity may funnel money to sub-recipients who
   never appear in this dataset. The Grants Portal can't see them.

In short: this dataset shows us *who got picked*, not *what happened with
the money*. Fraud lives in the second half.

---

## Where Fraud Actually Lives

Ranked roughly by "likely volume of real fraud per dollar searched":

### 1. Non-grant procurement — DGS purchase orders & CalProcure contracts
- **Dataset:** https://data.ca.gov/dataset/purchase-order-data , https://caleprocure.ca.gov/
- **Why it's the best target:** Sole-source contracts, no-bid awards, change
  orders, professional-services line items. The Caltrans bid-rigging case
  (Yong/Miller/Opp, $800K in bribes) lived here, not in a grants portal.
- **What to look for:**
  - Same vendor winning repeatedly from the same buyer
  - Change orders that 2-5x the original award
  - "Emergency" sole-source justifications
  - Vendors with addresses matching state employees
- **Why we haven't touched it:** We pivoted to the disbursement-gap story
  early. Worth a Round 3.

### 2. Non-profit overhead and exec-comp diversion (Track B from original plan)
- **Dataset:** ProPublica Nonprofit Explorer (free API, no Bright Data
  needed), IRS Form 990 filings
- **Why it's the best target:** State grants flow into non-profits, which
  then can re-route money to admin overhead, executive compensation, and
  related-party transactions. Reported, not audited.
- **What to look for:**
  - Non-profits whose admin expenses spike year-over-year when state
    funding increases
  - CEOs paid >$300K running orgs with <20 employees
  - Form 990 Schedule L (related-party transactions) entries
  - Homelessness/services nonprofits with low "program expense" ratios
- **Why we haven't touched it:** Antigravity's original plan listed this as
  Track B. We never built it. **This is the single highest-leverage move we
  haven't made.**

### 3. Federal pass-through to CA (USAspending)
- **Dataset:** USAspending.gov API (free)
- **Why it's the best target:** IIJA put ~$30B of federal infrastructure
  money through CA. Each pass-through layer (federal → state → sub-recipient
  → contractor) is a place to skim. State doesn't have to track money it's
  just forwarding.
- **What to look for:**
  - Sub-recipients with no SAM.gov registration
  - Recipients receiving from multiple federal programs simultaneously
  - DBE (Disadvantaged Business Enterprise) recipients whose actual work
    is performed by a non-DBE prime
- **Why we haven't touched it:** Our scope was CA-only. But CA *administers*
  these federal funds.

### 4. Open FI$Cal vendor transactions (we tried, hit a wall)
- **Dataset:** open.fiscal.ca.gov
- **Why it's the best target:** Actual cash flows out of the state. Vendor
  names, dollar amounts, account codes. The closest thing to ground truth
  for "did the money go somewhere real."
- **Why Round 2 couldn't run it:** The portal switched to a client-side
  rendered SPA. CKAN API endpoints don't return the data anymore. Web
  Unlocker would work but Antigravity didn't get the request format right.
- **The fix:** Use Bright Data Scraping Browser (full headless browser),
  drive the SPA, download the CSV. Or contact the State Controller and
  request the data feed directly — they're required to provide it.

### 5. Small-dollar repeating fraud
- **Where:** Anywhere $5K-$50K, especially consulting, training, "outreach"
- **Why:** It's beneath audit thresholds. A consultant billing $20K for
  "stakeholder engagement" with no deliverable is invisible to every
  oversight mechanism that exists.
- **Why we haven't touched it:** Our filter was $50K+. We *built* the
  bias toward big dollar amounts.

### 6. Sub-recipients and fiscal sponsors
- **Where:** Inside the larger nonprofit and JPA grants we cleared in
  Round 2
- **Why:** A clean JPA prime can have a dirty sub-recipient. We checked
  the JPAs at the top level and called them legitimate, but never asked
  who the actual money went to inside.

### 7. Form 990 + state grant flow correlation
- **Why:** A nonprofit's audited financials tell a different story than
  the state's award database. State says they got $5M. 990 says they
  spent $200K on programs and $3M on "consulting" — there's the story.

---

## What the Bright Data Budget Should Actually Buy

The $208 we have left is way better spent on the targets above than another
SERP sweep of high-dollar grant recipients. Concrete proposals:

### Proposal A: Non-profit overhead audit (Track B, finally)
- **Sources:** ProPublica Nonprofit Explorer for Form 990s, CA Grants
  Portal for state funding amounts
- **Method:**
  1. List every nonprofit recipient that got >$500K in state grants
     (~3,600 from the audit)
  2. Pull their Form 990 for the matching year
  3. Calculate: program expense ratio, exec comp ratio,
     admin-overhead-to-grant-revenue, related-party-transaction count
  4. Flag outliers (top 10% on admin ratio, top 5% on exec comp ratio)
- **Bright Data role:** ProPublica's API is free but heavily rate-limited.
  Web Unlocker fetches the 990 PDFs at scale. Estimated $30-50.
- **Why this is the big swing:** This is where Track B was always meant
  to live. Antigravity's original plan said it. We just never built it.

### Proposal B: DGS purchase order scan
- **Source:** https://data.ca.gov/dataset/purchase-order-data
- **Method:**
  1. Pull POs over $50K to non-government recipients
  2. Cluster by vendor: find vendors with 5+ POs from the same buyer
  3. Cluster by buyer: find buyers issuing 90%+ POs to a single vendor
  4. Cross-reference vendor addresses against state employee addresses
- **Bright Data role:** Mostly free state APIs. Bright Data only needed
  if portal blocks bulk access. Estimated $10-20.
- **Why it's promising:** This is where the only *successful* CA
  infrastructure fraud prosecution in the last decade lived (Caltrans).

### Proposal C: Open FI$Cal Scraping Browser
- **Source:** open.fiscal.ca.gov
- **Method:** Drive the SPA with Bright Data Scraping Browser, download
  every monthly CSV for FY 22-23, FY 23-24, FY 24-25 (account codes 5340*,
  5442*). That gives us actual cash flow out of the state.
- **Bright Data role:** Scraping Browser session, ~$5-15.
- **Why it's promising:** Once we have these CSVs, vendor_crossref.py can
  finally run. Recipients getting BOTH grants AND vendor payments for the
  same scope of work = strong signal.

---

## The Honest Hackathon Pivot

If we want to find something publishable in the time remaining, the play is
not another grants-portal sweep. It's:

1. **Pick Proposal A or B** (B is faster, A is bigger upside)
2. **Build it in the next 24 hours**
3. **Run it through the same flag → verify → publish-or-clear pipeline**

If A or B surfaces a real signal, that's the "fraud confirmed" story we've
been chasing. If they also clear everyone, that's three independent searches
of three different datasets and an even stronger systemic story:

> California publishes three separate datasets of state spending. We
> scanned all three. We found systemic accountability gaps in each. We
> found zero individual cases of confirmed fraud. The conclusion is not
> that California has no fraud — it's that California's data infrastructure
> cannot find it.

---

## Recommended Next Step

Pick one of the proposals and have Antigravity run it. **My vote: Proposal A.**
The nonprofit overhead angle is exactly the Track B that was in the original
spec and never built. It's also where the journalistic-impact stories tend
to land (homelessness contract scandals, exec comp at "charities," etc.).

The plumbing we need:
- ProPublica Nonprofit Explorer adapter (free API, no Bright Data dep)
- Form 990 PDF fetcher via Web Unlocker
- A 990 parser (these are structured PDFs — gettable with Gemini Flash)
- Overhead ratio calculator
- Cross-reference against the grants we already have in `data/grants_full.csv`

I can write all of that. Say the word and I'll build it as `src/track_b/`
in a way that doesn't touch any of the existing audit code.
