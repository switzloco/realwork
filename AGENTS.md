# Agent Interface Contracts

Each agent has defined inputs, outputs, and responsibilities. Update this file when changing an agent's contract — the other dev environment depends on it.

---

## Orchestrator

**Runs:** The full pipeline, sequentially.
**Input:** Config (which stages to run, budget limits, target count)
**Output:** Final investigation report + logs
**Calls:** ETL → Red Flag Analyst → Ranking → (per project) Investigation Planner → Scraper Coordinator → Synthesis
**Notes:** Enforces "finish project N before starting project N+1" rule.

---

## ETL Agent

**Stage:** 1
**Input:** CA Open Data Portal URL / CSV path
**Output:** Normalized project table (list of dicts or DataFrame)
**Schema:**
```
{
  "project_id": str,
  "project_name": str,
  "recipient_name": str,
  "recipient_type": str,        # LLC, Corp, Nonprofit, Gov, etc.
  "award_amount": float,
  "award_date": str,            # ISO 8601
  "category": str,              # Infrastructure, Construction, etc.
  "project_description": str,
  "project_location": str,      # address or county
  "funding_source": str,
  "contract_type": str,         # sole-source, competitive, etc.
  "raw_record": dict            # original unmodified record
}
```
**No LLM. No Bright Data.**

---

## Red Flag Analyst

**Stage:** 1
**Input:** Batch of normalized project records + category baselines (median amounts, typical durations)
**Output:** Per-project fraud risk assessment
**Schema:**
```
{
  "project_id": str,
  "flags": [
    {"flag": str, "severity": "HIGH|MEDIUM|LOW", "reasoning": str}
  ],
  "fraud_probability": "HIGH|MEDIUM|LOW",
  "summary": str
}
```
**Model:** Gemini 2.5 Pro
**No Bright Data.**

---

## Ranking Agent

**Stage:** 1
**Input:** All fraud risk assessments from Red Flag Analyst
**Output:** Ordered list of 3-5 project briefs
**Schema:**
```
{
  "rank": int,
  "project_id": str,
  "fraud_probability": "HIGH|MEDIUM|LOW",
  "investigation_feasibility": "HIGH|MEDIUM|LOW",
  "dollar_magnitude": float,
  "composite_score": float,
  "investigation_brief": str,     # 1 paragraph, what to look for
  "suggested_sources": [str]      # which evidence tiers to prioritize
}
```
**Model:** Gemini 2.5 Pro (or Claude via personal Max account)

---

## Investigation Planner

**Stage:** 2
**Input:** Single project brief from Ranking Agent + current budget status
**Output:** Scrape plan with itemized cost estimates
**Schema:**
```
{
  "project_id": str,
  "steps": [
    {
      "order": int,
      "source": str,              # e.g. "CA Secretary of State"
      "target_url": str,
      "bright_data_product": str, # "scraper_api" | "scraping_browser" | "serp_api"
      "search_params": dict,
      "estimated_cost": float,
      "rationale": str            # why this source matters for this project
    }
  ],
  "total_estimated_cost": float,
  "budget_remaining_after": float
}
```
**Model:** Gemini 2.5 Pro
**Requires Budget Controller approval before Scraper Coordinator executes.**

---

## Scraper Coordinator

**Stage:** 2
**Input:** Approved scrape plan
**Output:** Evidence records per source
**Schema:**
```
{
  "project_id": str,
  "evidence": [
    {
      "source": str,
      "url_scraped": str,
      "timestamp": str,
      "actual_cost": float,
      "raw_data": str,            # raw HTML/JSON
      "extracted": dict,          # structured findings
      "finding": str,             # one-line summary
      "supports_fraud": bool | null
    }
  ],
  "total_actual_cost": float
}
```
**Uses:** Bright Data SDK + Gemini 2.5 Flash (for extraction)
**Every API call goes through Budget Controller.**

---

## Budget Controller

**NOT an LLM agent.** Pure Python.
**Interface:**
```python
budget.status()              # → {spent, remaining, zone, ledger}
budget.reserve(amount, desc) # → {approved: bool, reason: str}
budget.record(call_record)   # → logs actual spend
budget.report()              # → full spend report for deliverables
```
**Zones:** Green ($0-150), Yellow ($150-200), Red ($200-240), Hard Stop ($240+)
**Ledger fields:** timestamp, project_id, source, bright_data_product, estimated_cost, actual_cost, approved_by

---

## Synthesis Agent

**Stage:** 3
**Input:** All investigation logs + evidence records
**Output:** Final report
**Schema:**
```
{
  "projects": [
    {
      "project_id": str,
      "project_name": str,
      "conclusion": "FLAGGED|CLEARED|INCONCLUSIVE",
      "confidence": "HIGH|MEDIUM|LOW",
      "evidence_summary": str,
      "key_findings": [str],
      "sources_checked": int,
      "total_cost": float
    }
  ],
  "methodology": str,
  "budget_summary": {spent, remaining, cost_per_project},
  "recommendations": [str]
}
```
**Model:** Gemini 2.5 Pro (or Claude via personal Max account)
