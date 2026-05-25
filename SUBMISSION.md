# Hackathon Submission Copy
## Web Data UNLOCKED — lablab.ai (May 25-30, 2026)

---

## Project Title
**RealWork: AI-Driven Ghost Infrastructure Detection**

---

## Short Description (tweet-length)
A multi-agent AI pipeline that analyzes California state grant data to identify likely fraud, then deploys Bright Data to gather corroborating evidence — surfacing ghost projects where public money was awarded but no real work exists.

---

## Long Description

Every year, billions in public infrastructure funds are awarded to companies that do little or no actual work. The fraud is hiding in plain sight — in public grant databases, business registries, contractor license records, and permit portals — but connecting those dots across hostile, fragmented government websites has been technically impossible. Until now.

**RealWork** is a multi-agent AI pipeline that inverts the traditional approach to fraud detection: instead of scraping everything and hoping to find something, the AI picks the targets first, then Bright Data gathers the evidence.

### How It Works

**Stage 1: AI-Driven Target Selection (no scraping)**
We ingest California state infrastructure grant data from the CA Open Data Portal and run it through a multi-agent analysis pipeline powered by Gemini 2.5 Pro. The Red Flag Analyst agent scores each project against a battery of fraud indicators — unusually high costs relative to scope, sole-source awards, vague deliverables, timing anomalies, geographic mismatches, and entities with no prior public contract history. A Ranking Agent then produces a prioritized shortlist of 3-5 projects most worth investigating, scored on fraud probability, investigation feasibility, and dollar magnitude.

**Stage 2: Evidence Gathering with Bright Data**
For each target project, an Investigation Planner agent designs a custom scraping strategy based on that project's specific red flags. A central Budget Controller (deterministic Python, not AI) gates every Bright Data API call and enforces a hard spend cap. The Scraper Coordinator then deploys Bright Data across a creative range of sources:

- **CA Secretary of State** — is the entity active? When did it incorporate? (Web Scraper API)
- **CA Contractors State License Board** — valid license? Claimed employees? Workers' comp? (Web Scraper API)
- **SAM.gov** — federal registration status (Web Unlocker)
- **LinkedIn** — does this company actually have employees? (Web Scraper API)
- **Google Maps / Street View** — is there actual construction at the stated project address? (Scraping Browser)
- **County permit portals** — did anyone pull a permit for a multi-million dollar project? (Scraping Browser)
- **SERP API** — news, lawsuits, complaints about the entity (SERP API)
- **Court records, campaign finance databases, subcontractor trails** — the paper trail (Web Unlocker)

Every API call is logged with source, cost, and finding. Investigations are sequential: finish Project #1 before starting #2. If a project comes up clean, we document why and move on — a well-evidenced clearance is valuable output too.

**Stage 3: Structured Findings**
A Synthesis agent produces a forensic report for each project: evidence summary, conclusion (FLAGGED / CLEARED / INCONCLUSIVE), confidence level, and supporting sources. The final output is a complete investigation log — suitable for submission to a government oversight body, a journalist, or a qui tam attorney.

### Why This Matters

The California False Claims Act allows private citizens to file fraud claims on behalf of the state and receive a portion of recovered funds. Our pipeline is designed to surface the cases most worth pursuing — and to do it at a scale no human investigator could match. One well-documented ghost project at $5M+ is worth far more than a thousand weak signals.

### Why Bright Data

The hardest part of this investigation isn't analysis — it's data access. California's county permit portals, contractor license databases, and business registries are fragmented, JavaScript-heavy, and actively hostile to scrapers. Without Bright Data's proxy infrastructure and Scraping Browser, most of these sources are effectively inaccessible to an automated agent. Bright Data is what makes the "reality check" layer of this pipeline possible.

### Tracks
- **Track 2: Finance & Market Intelligence** — alternative data pipeline identifying financial anomalies in public contract awards
- **Track 3: Security & Compliance** — AI agents that investigate risk indicators and return structured compliance assessments autonomously

---

## Technology Tags
`Gemini 2.5 Pro` `Bright Data` `Web Scraper API` `Scraping Browser` `SERP API` `Web Unlocker` `Python` `SQLite` `Multi-Agent` `Civic Tech` `Fraud Detection` `Public Accountability`

---

## Judging Criteria Notes (internal — do not submit)

**Application of Technology:** Multi-agent pipeline with 8 specialized agents. Bright Data's full stack — Web Scraper API, Scraping Browser, SERP API, Web Unlocker — each matched to the right source type. Budget Controller enforces responsible spend.

**Presentation:** The investigation log IS the demo. Show the pipeline running against a real grant record. The "FLAGGED / CLEARED" output is compelling and easy to understand. Lean into the civic narrative.

**Business Value:** Government oversight bodies, inspector generals, investigative journalism organizations, qui tam attorneys, and civic tech nonprofits are all real potential customers. Scales to any state's grant data.

**Originality:** Nobody is doing AI-driven civic fraud detection with Bright Data. The AI-first-then-scrape inversion is novel. The budget controller as a first-class component shows production maturity.

---

## What to Have Ready for Submission

- [ ] Public GitHub repo (clean README, clear setup instructions)
- [ ] Demo video (3 min): show the pipeline running, highlight the agent architecture, show a real finding
- [ ] Slide deck: problem → approach → agent architecture → demo → business case
- [ ] Cover image: something that visually conveys "finding the ghost in the machine"
- [ ] Application URL: even a simple hosted output or Streamlit dashboard counts
