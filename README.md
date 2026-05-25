# Project RealWork: Ghost Infrastructure

**Mission:** Use AI-driven analysis and web scraping to identify potential fraud in California public infrastructure spending.
**Hackathon:** Lablab.ai "Web Data UNLOCKED" (May 25-31, 2026)
**Sponsor Integration:** Bright Data (web scraping infrastructure)
**Bright Data Budget:** $250 hard cap

---

## The Approach

Instead of scraping everything and hoping to find fraud, we invert the process:
**AI picks the targets first, Bright Data gathers the evidence second.**

The system is built as a set of cooperating agents, each with a clear role. A central Budget Controller gates all Bright Data spend.

---

## Agent Architecture

```
                    ┌─────────────────────┐
                    │   ORCHESTRATOR      │
                    │   (Pipeline Control) │
                    └─────────┬───────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
     ┌────────▼──────┐ ┌─────▼──────┐ ┌──────▼───────┐
     │  STAGE 1      │ │  STAGE 2   │ │  STAGE 3     │
     │  Target       │ │  Evidence  │ │  Synthesis   │
     │  Selection    │ │  Gathering │ │  & Reporting │
     └───────┬───────┘ └─────┬──────┘ └──────────────┘
             │               │
    ┌────────┼────┐    ┌─────┼──────────┐
    │        │    │    │     │          │
  ┌─▼─┐  ┌──▼┐ ┌─▼┐ ┌▼─┐ ┌─▼──┐  ┌───▼────┐
  │ETL│  │RA │ │RK│ │IP│ │SC  │  │  BD    │
  └───┘  └───┘ └──┘ └──┘ └─┬──┘  │Budget  │
                            │     │Control │
                     ┌──────┼──┐  └───┬────┘
                     │      │  │      │
                    ┌▼┐   ┌─▼┐▌▼┐    ▌│
                    │S│   │S ││S│  (gates every
                    │1│   │2 ││3│   API call)
                    └─┘   └──┘└─┘
```

### The Agents

#### 1. Orchestrator
The top-level controller. Runs the pipeline sequentially (Stage 1 → 2 → 3), passes outputs between stages, and enforces the overall investigation flow: investigate Project #1 thoroughly before moving to #2.

#### 2. ETL Agent (Stage 1)
**Role:** Data janitor. Pulls raw grant/spending data from CA Open Data Portal, normalizes it, enriches it with basic lookups.
- Pulls CSV/API data from CA state sources
- Normalizes fields: recipient name, amount, date, category, location, project description
- Deduplicates and cross-references (same recipient across multiple grants)
- Outputs a clean project table for analysis
- **No LLM needed** — this is pure data engineering (Python/pandas)

#### 3. Red Flag Analyst Agent (Stage 1)
**Role:** The detective brain. Takes the clean project table and reasons about each project's fraud likelihood.
- **Model: Gemini 2.5 Pro** — strong reasoning over mixed structured/unstructured data, low cost
- Analyzes each project against fraud indicators:
  - Unusually high cost relative to project scope or comparable projects
  - Awardees with no prior public contract history
  - Projects with vague deliverables or missing milestones
  - Awards to entities in unrelated industries
  - Timing anomalies (rushed awards, end-of-fiscal-year dumps)
  - Geographic mismatches (awardee location vs. project location)
  - Sole-source contracts above typical thresholds
  - Repeated awards to the same entity or related entities
  - Recipient appears in multiple grants with different entity names but same address/agent
- Outputs a fraud risk assessment per project with reasoning
- **Key design choice:** Feed projects in batches with context about what "normal" looks like (median grant sizes by category, typical timelines). The model needs a baseline to spot outliers.

#### 4. Ranking Agent (Stage 1)
**Role:** Prioritizer. Takes all the Red Flag Analyst's assessments and produces the final ranked shortlist.
- Scores each project on three axes:
  - **Fraud probability** (density and severity of red flags)
  - **Investigation feasibility** (can we find corroborating evidence online? Is the recipient a searchable entity?)
  - **Dollar magnitude** (bigger = more impactful finding, more hackathon points)
- Produces a ranked list of 3-5 projects with a 1-paragraph investigation brief per project
- **Model: Gemini 2.5 Pro** — highest-leverage reasoning in the pipeline, keeps costs in Google ecosystem.

#### 5. Investigation Planner Agent (Stage 2)
**Role:** For each target project, plans the specific scraping strategy based on its unique red flags.
- Reads the project brief from the Ranking Agent
- Decides which evidence sources to hit and in what order (cheapest/fastest first)
- Produces a structured investigation plan:
  ```
  Project: "Highway 99 Overpass Remediation - Acme LLC"
  Red flags: [no prior history, sole-source, vague deliverables]
  Investigation plan:
    1. Secretary of State lookup (entity status, incorporation date) — est. $0.50
    2. CSLB license check (active? employees?) — est. $0.50
    3. LinkedIn scrape (does this company exist? employees?) — est. $2.00
    4. Google Maps/Street View at project address — est. $1.00
    5. County permit portal for project address — est. $3.00
    Estimated total: $7.00
    Budget remaining: $243.00
  ```
- **Must get cost estimate approved by Budget Controller before proceeding**

#### 6. Scraper Coordinator Agent (Stage 2)
**Role:** Executes the investigation plan by dispatching Bright Data API calls.
- Takes the approved investigation plan and executes scrapes in order
- For each scrape target, selects the right Bright Data product:
  - **Web Scraper API** for structured sites (SoS, CSLB, SAM.gov)
  - **Scraping Browser** for JS-heavy sites (county permit portals, Google Maps)
  - **SERP API** for news/public records searches about the entity
- Parses raw results into structured evidence records
- Uses Gemini 2.5 Flash for cheap extraction from messy HTML/PDFs
- **Every API call goes through the Budget Controller** — no exceptions
- Spawns sub-scrapers for parallel evidence gathering when budget allows

#### 7. Budget Controller (Shared Service — NOT an LLM agent)
**Role:** Hard gate on all Bright Data spend. This is code, not AI.
- Maintains a running ledger of all Bright Data API costs
- **$250 hard cap, with warning thresholds:**
  - Green: $0-150 (proceed freely)
  - Yellow: $150-200 (Investigation Planner must justify each new scrape)
  - Red: $200-240 (only high-confidence, high-value scrapes approved)
  - Hard stop: $240 ($10 reserve for retries/errors)
- Logs every API call with: timestamp, target URL, Bright Data product used, cost, project being investigated
- Exposes current spend to all agents via a simple API:
  ```python
  budget.check()       # returns {spent, remaining, zone}
  budget.reserve(amt)  # reserves amount, returns approval/denial
  budget.record(call)  # logs completed API call with actual cost
  ```
- **Implementation:** Simple Python class backed by SQLite. No LLM needed — this is deterministic logic.
- **Cost estimation:** Bright Data pricing varies by product:
  - Web Scraper API: ~$0.50-2.00 per page
  - Scraping Browser: ~$2.00-5.00 per session
  - SERP API: ~$0.50-1.00 per query
  - Proxy bandwidth: ~$0.10-0.50 per request
  These are estimates — the Budget Controller logs actuals and adjusts remaining budget in real time.

#### 8. Synthesis Agent (Stage 3)
**Role:** Reads all investigation logs and evidence, produces final deliverables.
- For each investigated project, writes a structured finding:
  - Evidence summary (what we found, source by source)
  - Conclusion: FLAGGED / CLEARED / INCONCLUSIVE
  - Confidence level and reasoning
  - For FLAGGED projects: the specific fraud indicators confirmed
  - For CLEARED projects: the specific evidence that exonerates
- Produces the final report with all projects, budget spent, methodology description
- **Model: Gemini 2.5 Pro** (default) or **Claude via personal Max account** (optional, for higher-quality prose)

---

## Stage 1: Target Selection (Detail)

**No Bright Data spend in this stage.** All data comes from public APIs/CSVs.

```
CA Open Data Portal → ETL Agent → Clean Project Table → Red Flag Analyst → Scored Projects → Ranking Agent → Top 3-5 Targets
```

The Red Flag Analyst processes projects in batches. For a dataset of, say, 500 infrastructure grants, we'd batch them ~50 at a time with category-level context ("the median construction grant in 2024 was $X, typical duration is Y months"). This gives the model a baseline for spotting statistical outliers without having to hold the entire dataset in context.

**Critical output:** Each target project gets a brief that the Investigation Planner can act on:
```
PROJECT BRIEF #1
Name: [Project Name]
Recipient: [Entity Name]
Amount: $X,XXX,XXX
Category: [Infrastructure/Construction/etc.]
Red Flags:
  - [Flag 1 with reasoning]
  - [Flag 2 with reasoning]
Fraud Probability: HIGH/MEDIUM
Investigation Feasibility: HIGH/MEDIUM/LOW
Suggested Evidence Sources: [list]
```

---

## Stage 2: Evidence Gathering (Detail)

**This is where Bright Data budget gets spent.** Sequential investigation — finish Project #1 before starting #2.

```
Project Brief → Investigation Planner → Scrape Plan (with cost estimate)
                                              ↓
                                    Budget Controller (approve/deny)
                                              ↓
                                    Scraper Coordinator → Bright Data APIs
                                              ↓
                                    Evidence Records → Investigation Log
```

### Creative Evidence Sources (ranked by cost-effectiveness)

**Tier 1 — Cheap & Definitive ($0.50-2.00 each)**
- Secretary of State business entity search (is the company active?)
- CSLB contractor license lookup (valid license? employees?)
- SAM.gov federal registration check
- SERP search for "[company name] + fraud/lawsuit/complaint"

**Tier 2 — Moderate & Valuable ($2.00-5.00 each)**
- LinkedIn company page (employee count, company age, industry)
- Google Maps/Street View at project address (physical evidence of work)
- County assessor records (property ownership at project site)
- BBB / business review sites

**Tier 3 — Expensive & Deep ($5.00-15.00 each)**
- County permit portal scraping (JS-heavy, may need Scraping Browser)
- Court records / PACER search
- News archive deep scrape
- Satellite imagery comparison (before/after project dates)

**Strategy:** Always hit Tier 1 first. If Tier 1 already confirms fraud signals, Tier 2-3 is gravy. If Tier 1 clears the project, move on — don't burn budget on a clean target.

---

## Stage 3: Findings & Deliverables

### For the Hackathon Submission
1. **Working demo:** Run the full pipeline end-to-end (targeting + scraping + report for at least one project)
2. **Investigation log:** The structured record of every project investigated — this IS the demo
3. **Findings report:** AI-generated synthesis of all evidence
4. **3-minute video:** Show the pipeline running, explain the agent architecture, highlight findings
5. **Budget report:** Show responsible use of Bright Data credits (judges will appreciate this)

### Investigation Log Format
Each project gets a log entry:
- Initial red flags from Stage 1
- Investigation plan with cost estimates
- Evidence gathered (source, timestamp, cost, finding)
- Running budget tracker
- Conclusion: **FLAGGED** / **CLEARED** / **INCONCLUSIVE**
- Rationale for the conclusion

---

## Budget Allocation Plan ($250 total)

| Allocation | Amount | Purpose |
|-----------|--------|---------|
| Development & testing | $30 | Test scraper configs, debug parsers |
| Project #1 investigation | $60 | Full investigation of top target |
| Project #2 investigation | $50 | Full investigation of second target |
| Project #3 investigation | $50 | Full investigation (if budget allows) |
| Projects #4-5 (light) | $30 | Tier 1 checks only |
| Buffer for retries/errors | $20 | Failed requests, rate limit retries |
| Reserve (never touch) | $10 | Emergency only |
| **Total** | **$250** | |

---

## Tech Stack

| Component | Tool | Notes |
|-----------|------|-------|
| Pipeline orchestration | Python | Coordinates agents and data flow |
| ETL | Python / pandas | Data cleaning, no LLM needed |
| Red Flag Analyst | Gemini 2.5 Pro | Core reasoning engine — bulk analysis |
| Ranking Agent | Gemini 2.5 Pro | Highest-leverage reasoning step |
| Investigation Planner | Gemini 2.5 Pro | Plan generation |
| Scraper Coordinator | Python + Bright Data SDK | API orchestration |
| Data Extraction | Gemini 2.5 Flash | Cheap parsing of HTML/PDFs |
| Budget Controller | Python (deterministic) | JSON ledger, no LLM |
| Synthesis Agent | Claude (optional) | Final report polish — via personal account |
| Storage | SQLite | Local DB, zero cost, easy to query |

### LLM Cost Strategy

- **Primary model: Gemini 2.5 Pro** — handles all Stage 1 analysis and Stage 2 planning. Free tier or low cost through Google AI Studio / Vertex AI.
- **Extraction model: Gemini 2.5 Flash** — cheap bulk parsing of scraped HTML/PDFs into structured data.
- **Optional polish: Claude** — if you want higher-quality writing for the final Stage 3 synthesis report, route it through a personal Claude Max ($20/mo) account. This is low volume (a few reports total), so it fits within normal usage. Not required — Gemini 2.5 Pro can handle synthesis too.
- **Anthropic API budget: $0 for hackathon.** Keep it free. If you add Claude later for synthesis, it's through the personal account, not paid API credits.
