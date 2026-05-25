# Project RealWork: Ghost Infrastructure

**Mission:** Use AI-driven analysis and web scraping to identify potential fraud in California public infrastructure spending.
**Hackathon:** Lablab.ai "Web Data UNLOCKED" (May 25-31, 2026)
**Sponsor Integration:** Bright Data (web scraping infrastructure)

---

## The Approach

Instead of scraping everything and hoping to find fraud, we invert the process:
**AI picks the targets first, Bright Data gathers the evidence second.**

---

## Stage 1: Target Selection (AI-Driven Analysis)

**Goal:** Ingest California state grant/infrastructure spending data and use strong AI to rank projects by fraud likelihood. No scraping needed yet — this stage uses publicly available datasets and reasoning.

**Input:** California Open Data Portal (state grants, infrastructure projects, contract awards)

**Process:**
1. Pull and normalize state-level spending data for infrastructure, construction, environmental remediation, and transportation.
2. Feed project records through AI analysis to flag anomalies. Fraud indicators include:
   - Unusually high cost relative to project scope or comparable projects
   - Awardees with no prior public contract history
   - Projects with vague deliverables or missing milestones
   - Awards to entities in unrelated industries
   - Timing anomalies (rushed awards, end-of-fiscal-year dumps)
   - Geographic mismatches (awardee location vs. project location)
   - Sole-source contracts above typical thresholds
   - Repeated awards to the same entity or related entities
3. Output a ranked shortlist of 3-5 projects, scored by:
   - **Fraud probability** (how many red flags)
   - **Investigation feasibility** (can we actually find corroborating evidence online?)
   - **Dollar magnitude** (bigger = more impactful finding)

**AI Model for this stage:** Needs strong reasoning over tabular + unstructured data. Claude or GPT-4-class recommended. Gemini 1.5 Flash may be underpowered for the nuanced judgment calls here — consider using it for data extraction/parsing and a stronger model for the actual ranking.

---

## Stage 2: Evidence Gathering (Bright Data Scraping)

**Goal:** Starting with Project #1 from the ranked list, use Bright Data to scrape corroborating or exonerating evidence from across the web. If a project looks clean, document why and move to the next target.

**Process (per project):**
1. **Define the investigation plan** for this specific project based on its red flags.
2. **Deploy Bright Data scrapers** against relevant sources. These are NOT limited to official project sites — be creative:
   - **Official registries:** CSLB (contractor license status, employee count, workers' comp), Secretary of State (entity status, incorporation date, agent info)
   - **Permit systems:** County building/grading permit portals for the project address
   - **Corporate intelligence:** LinkedIn (does this company have real employees?), business review sites, BBB records
   - **Physical evidence:** Google Maps / Street View (is there actually construction at the stated location?), satellite imagery comparisons over time
   - **News & public records:** Local news archives, court records (PACER), campaign contribution databases, lobbying disclosures
   - **Subcontractor trails:** If the awardee claims subcontractors, do those subs exist? Do they have licenses?
   - **Financial signals:** SAM.gov registration status, DUNS lookups, any publicly filed financials
3. **Document everything.** For each project investigated:
   - If fraud indicators are confirmed: build the evidence package
   - If the project looks legitimate: record why (e.g., "permits confirmed, active license, Street View shows construction activity") and move to Project #2

**Key principle:** Each project investigation should be thorough before moving on. A well-documented "this one is clean" is valuable output too.

---

## Stage 3: Findings & Deliverables

**Goal:** Package all findings — both suspicious and cleared — into deliverables.

### For the Hackathon Submission
1. **Working demo:** A script/tool that runs the full pipeline end-to-end (Stage 1 targeting + Stage 2 scraping for at least one project)
2. **Findings report:** Structured output showing:
   - Projects investigated and their fraud risk scores
   - Evidence gathered per project
   - Conclusions (anomalous vs. legitimate) with supporting data
3. **3-minute video:** Show the pipeline running, explain the methodology, highlight the most interesting finding

### Beyond the Hackathon (if findings warrant it)
- Formal anomaly reports suitable for oversight bodies
- Anonymized/structured datasets of methodology + findings for public accountability
- Documentation of investigative methodology as a reusable framework

---

## Architecture

| Component | Tool | Role |
|-----------|------|------|
| Data Ingestion | CA Open Data Portal APIs / CSV | State spending data |
| Target Analysis | Strong LLM (TBD) | Rank projects by fraud likelihood |
| Web Scraping | Bright Data (Scraper API, proxies) | Gather evidence from hostile/protected sites |
| Data Extraction | Gemini 1.5 Flash | Parse unstructured scrape results (PDFs, HTML) into structured data |
| Storage | Firebase | Store project records, scrape results, investigation state |
| Orchestration | Python | Pipeline coordination |

---

## Investigation Log

Each project gets a log entry tracking:
- Initial red flags from Stage 1
- Evidence gathered in Stage 2
- Sources checked (with timestamps and scrape status)
- Conclusion: **FLAGGED** (anomalies confirmed), **CLEARED** (legitimate), or **INCONCLUSIVE** (insufficient data)
- Rationale for the conclusion

This log is a first-class deliverable, not just internal notes.
