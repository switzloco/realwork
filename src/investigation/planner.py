"""
Investigation Planner — Stage 2
Uses Gemini 2.5 Pro to outline a step-by-step web scraping plan
based on specific red flags and the remaining budget.
"""

import json
import os
import textwrap
import google.generativeai as genai

from src.db import get_conn

# Initialize Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-pro"

SYSTEM_PROMPT = textwrap.dedent("""
    You are an expert fraud investigator. Your task is to design a targeted, cost-effective
    web scraping and research plan to gather evidence on a project flagged for potential fraud.
    
    You will be given the project details, the red flags raised, the ranking brief, and the remaining budget.
    
    You must output a list of 2 to 4 scraping steps to investigate this project.
    For each step, recommend the best Bright Data product:
    - "serp_api": For search engine queries (e.g., verifying if the business exists, looking up news, finding websites).
      The target_url should be a google search query URL, e.g., "https://www.google.com/search?q=..."
    - "scraper_api": For structured portals (e.g., Secretary of State registries, licensing boards like CSLB, SAM.gov).
    - "scraping_browser": For JS-heavy, dynamic websites (e.g., local permit databases, LinkedIn company pages, Google Maps Street View).
    
    Estimate a realistic cost in USD for each step:
    - serp_api: $0.50 - $1.00 per query
    - scraper_api: $0.50 - $2.00 per page
    - scraping_browser: $2.00 - $5.00 per session
    
    Respect the budget status:
    - GREEN zone: Plan freely up to $15 total budget.
    - YELLOW zone (spent $150-$200): Plan conservatively up to $10 total budget.
    - RED zone (spent $200-$240): High-confidence, critical steps only, max $5 total budget.
    - HARD_STOP zone: Do not plan any steps.
    
    Return ONLY a JSON object with this exact schema:
    {
      "project_id": str,
      "steps": [
        {
          "order": int,
          "source": str,              // e.g. "CA Secretary of State", "LinkedIn", "Google Search"
          "target_url": str,          // URL to scrape/search
          "bright_data_product": "scraper_api" | "scraping_browser" | "serp_api",
          "search_params": dict,      // e.g. {"q": "Teknol Inc California"} or empty
          "estimated_cost": float,
          "rationale": str            // why this source matters for this project
        }
      ],
      "total_estimated_cost": float,
      "budget_remaining_after": float
    }
""").strip()


def _get_project_data(project_id: str) -> dict:
    """Fetch project details, red flags, and ranking brief from the database."""
    with get_conn() as conn:
        project = conn.execute(
            "SELECT * FROM projects WHERE project_id = ?", (project_id,)
        ).fetchone()
        
        ranking = conn.execute(
            "SELECT * FROM rankings WHERE project_id = ?", (project_id,)
        ).fetchone()
        
        flags = conn.execute(
            "SELECT flag, severity, reasoning FROM red_flags WHERE project_id = ?", (project_id,)
        ).fetchall()

    if not project or not ranking:
        raise ValueError(f"Project or ranking not found for ID: {project_id}")

    return {
        "project": dict(project),
        "ranking": dict(ranking),
        "flags": [dict(f) for f in flags]
    }


def _parse_response(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    return json.loads(text.strip())


def run(project_id: str, budget_status: dict) -> dict:
    """
    Generate an itemized scraping plan for the specified project.
    budget_status is expected to contain: {"spent": float, "remaining": float, "zone": str}
    """
    data = _get_project_data(project_id)
    project = data["project"]
    ranking = data["ranking"]
    flags = data["flags"]

    print(f"  Planning investigation for project {project_id} ({project.get('recipient_name')})...")
    
    prompt = textwrap.dedent(f"""
        Please generate an investigation scrape plan for the following project.
        
        BUDGET STATUS:
        - Spent: ${budget_status.get('spent', 0.0):.2f}
        - Remaining: ${budget_status.get('remaining', 250.0):.2f}
        - Zone: {budget_status.get('zone', 'GREEN')}
        
        PROJECT DETAILS:
        - ID: {project_id}
        - Name: {project.get('project_name', 'N/A')}
        - Recipient: {project.get('recipient_name', 'N/A')}
        - Recipient Type: {project.get('recipient_type', 'N/A')}
        - Amount: ${project.get('award_amount', 0.0):,.2f}
        - Category: {project.get('category', 'N/A')}
        - Location: {project.get('location', 'N/A')}
        - Description: {project.get('description', 'N/A')}
        
        RED FLAGS:
        {json.dumps(flags, indent=2)}
        
        INVESTIGATION BRIEF:
        {ranking.get('investigation_brief', '')}
        
        SUGGESTED SOURCES FROM RANKING AGENT:
        {ranking.get('suggested_sources', '[]')}
        
        Return ONLY the JSON object, matching the requested schema.
    """).strip()

    model = genai.GenerativeModel(
        model_name=MODEL,
        system_instruction=SYSTEM_PROMPT
    )

    response = model.generate_content(prompt)
    plan = _parse_response(response.text)
    
    # Calculate totals and inject budget remaining after estimate
    total_cost = sum(step["estimated_cost"] for step in plan["steps"])
    plan["project_id"] = project_id
    plan["total_estimated_cost"] = round(total_cost, 2)
    plan["budget_remaining_after"] = round(budget_status.get("remaining", 250.0) - total_cost, 2)
    
    return plan
