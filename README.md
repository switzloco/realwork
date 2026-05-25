# Project RealWork: Track A (Ghost Infrastructure)

**Environment:** Google Antigravity
**Mission:** Automate the California False Claims Act (CFCA) oversight and find undeniable government fraud.
**Objective:** Target massive state infrastructure grants, weaponize Bright Data to scrape hostile state/county portals, and identify "Ghost Projects" where money was awarded but no work exists.
**Endgame:** Secure whistleblower payouts under seal, while generating open-source datasets to force public accountability.

---

## 1. Hackathon Context: Lablab.ai "Web Data UNLOCKED"
**ATTENTION CODING AGENTS:** This repository is being developed for the Lablab.ai Web Data UNLOCKED Hackathon (May 25–31, 2026). 
* **Mandatory Integration:** The architecture utilizes Bright Data's enterprise web data infrastructure to bypass hostile/protected state databases.
* **Goal:** Do not use friendly APIs (like ProPublica). We are acting as the primary source of truth by unlocking hard-to-reach state and county records.

---

## 2. The Core Architecture

* **Development IDE:** Google Antigravity
* **Pipeline Inference Engine:** Gemini 1.5 Flash (Optimized for deep reasoning and forensic analysis of unstructured scrape data)
* **Backend:** Firebase
* **Data Ingestion (Ground Truth):** California Open Data Portal (State Grants)
* **Data Validation (Reality Check):** Bright Data Proxies/Web Scraper API targeting hostile California databases.

---

## 3. The Methodology (80/20 Approach)

The workflow is broken into three phases designed to maximize impact and ignore low-level noise.

### Phase 1: The Ground Truth (Ingestion & Filtering)
We only care about the "biggies." 
1. **Ingest CA Grants Data:** Pull the latest dataset from the California State Grants Portal.
2. **Filter for Target Vectors:** Filter for Infrastructure, Construction, Environmental Remediation, and Transportation.
3. **The 80/20 Rule:** Sort by `Total Award Amount` descending. Isolate the top 10% of massive grants awarded to private companies/LLCs.

### Phase 2: The Reality Check (Bright Data Scraping)
Take the high-value targets and unleash Bright Data on hostile targets to find discrepancies.

1. **Target A: California Contractors State License Board (CSLB)**
    * *The Strike:* Scrape the license status and workers' comp records. 
    * *The Fraud Signal:* Is the license suspended? Do they claim **zero employees** despite taking a $5.2M construction grant?
2. **Target B: California Secretary of State (Business Search)**
    * *The Strike:* Check business entity status.
    * *The Fraud Signal:* Is the business "Suspended" or "Forfeited"? Did they incorporate *after* the grant was announced?
3. **Target C: Local County Permit Portals**
    * *The Strike:* Search for building permits at the grant's stated project location.
    * *The Fraud Signal:* Multi-million dollar physical project with zero permits pulled locally.

### Phase 3: The Synthesis & The Strike (Outputs)

1. **The Primary Goal (The Whistleblower Packet):** Pass the Ground Truth Data + The Scraped Reality Check Data into **Gemini 1.5 Flash**. The objective is to isolate **ONE incredibly meaty, undeniable case of fraud**. We will generate a comprehensive, forensic "Hit Kit" designed to be handed directly to the state or a *qui tam* attorney.
2. **The Secondary Goal (Data Publishing):** We will become the source of truth. For targets that show anomalies, we will export the structured findings into clean datasets and publish them publicly (e.g., on Kaggle) to bypass gatekeepers and force accountability.
