"""
Search Validator — Stage 1.5
Uses Gemini 2.5 Pro with Google Search grounding to validate flagged projects
before committing Bright Data budget. Eliminates false positives cheaply.

This sits between the Ranking Agent and Stage 2 Investigation.
For each ranked target, it does a quick grounded web search to check if
the red flags have obvious explanations (e.g., the project is well-documented
publicly but just had bad data entry in the state database).
"""

import json
import os
import textwrap

import google.generativeai as genai
from google.generativeai.types import Tool

from src.db import get_conn

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-pro"

SYSTEM_PROMPT = textwrap.dedent("""
    You are a research validator. You've been given a California infrastructure
    grant project that was flagged as potentially fraudulent by an AI analyst.
    Your job is to do a quick reality check using web search.

    For each project, search for:
    1. The recipient name — do they exist? Are they a known entity?
    2. The project name/description — is this a known, documented project?
    3. Any news articles, government press releases, or public records about this project

    Then assess:
    - Can the red flags be explained by bad data entry (missing fields in the database)?
    - Is this a well-known, legitimate project that just had incomplete records?
    - Or do the red flags hold up even after searching?

    Return a JSON object:
    {
      "project_id": str,
      "search_summary": str,        // 2-3 sentences on what you found
      "red_flags_resolved": [str],  // which flags have innocent explanations
      "red_flags_remaining": [str], // which flags still look suspicious after search
      "revised_fraud_probability": "HIGH" | "MEDIUM" | "LOW" | "CLEARED",
      "recommendation": "INVESTIGATE" | "DEPRIORITIZE" | "CLEAR",
      "reasoning": str              // 1-2 sentences
    }
""").strip()


def _build_prompt(ranking: dict, project: dict, flags: list[dict]) -> str:
    return textwrap.dedent(f"""
        Validate this flagged project using web search:

        PROJECT:
        - Name: {project.get('project_name', 'N/A')}
        - Recipient: {project.get('recipient_name', 'N/A')}
        - Amount: ${project.get('award_amount', 0):,.0f}
        - Date: {project.get('award_date', 'N/A')}
        - Category: {project.get('category', 'N/A')}
        - Location: {project.get('location', 'N/A')}
        - Description: {project.get('description', 'N/A')}

        RED FLAGS IDENTIFIED:
        {json.dumps(flags, indent=2)}

        INVESTIGATION BRIEF:
        {ranking.get('investigation_brief', '')}

        Search the web for this project and recipient. Determine if the red flags
        have innocent explanations or if they hold up. Return ONLY a JSON object.
    """).strip()


def _parse_response(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    return json.loads(text.strip())


def validate_target(ranking: dict, project: dict, flags: list[dict]) -> dict:
    """Validate a single target using grounded search."""
    google_search_tool = Tool(google_search={})

    model = genai.GenerativeModel(
        model_name=MODEL,
        system_instruction=SYSTEM_PROMPT,
        tools=[google_search_tool],
    )

    prompt = _build_prompt(ranking, project, flags)
    response = model.generate_content(prompt)
    return _parse_response(response.text)


def run(rankings: list[dict]) -> list[dict]:
    """
    Validate all ranked targets. Returns re-ranked list with
    CLEARED projects removed and scores adjusted.
    """
    with get_conn() as conn:
        projects = {
            r["project_id"]: dict(r)
            for r in conn.execute("SELECT * FROM projects").fetchall()
        }
        all_flags = {}
        for r in conn.execute("SELECT * FROM red_flags").fetchall():
            pid = r["project_id"]
            all_flags.setdefault(pid, []).append(dict(r))

    validated = []
    for ranking in rankings:
        pid = ranking["project_id"]
        project = projects.get(pid, {})
        flags = all_flags.get(pid, [])

        print(f"  Validating #{ranking['rank']} ({pid}): {project.get('recipient_name', '?')[:40]}...")

        result = validate_target(ranking, project, flags)
        result["original_rank"] = ranking["rank"]
        result["original_score"] = ranking.get("composite_score", 0)
        result["project_id"] = pid

        if result.get("recommendation") == "CLEAR":
            print(f"    → CLEARED: {result.get('reasoning', '')[:80]}")
        elif result.get("recommendation") == "DEPRIORITIZE":
            print(f"    → DEPRIORITIZED: {result.get('reasoning', '')[:80]}")
        else:
            print(f"    → INVESTIGATE: {result.get('reasoning', '')[:80]}")

        validated.append(result)

    # Re-rank: INVESTIGATE first, then DEPRIORITIZE, remove CLEAR
    investigate = [v for v in validated if v.get("recommendation") == "INVESTIGATE"]
    deprioritize = [v for v in validated if v.get("recommendation") == "DEPRIORITIZE"]
    cleared = [v for v in validated if v.get("recommendation") == "CLEAR"]

    final_targets = investigate + deprioritize
    for i, t in enumerate(final_targets):
        t["validated_rank"] = i + 1

    print(f"\n  Results: {len(investigate)} to investigate, {len(deprioritize)} deprioritized, {len(cleared)} cleared")
    return final_targets
