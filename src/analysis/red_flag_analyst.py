"""
Red Flag Analyst — Stage 1
Uses Gemini 2.5 Pro to score each project for fraud indicators.
Projects are batched to stay within context limits.
"""

import json
import os
import textwrap
from typing import Any

import google.generativeai as genai
from pydantic import BaseModel

from src.db import get_conn

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-pro"

BATCH_SIZE = 20


class Flag(BaseModel):
    flag: str
    severity: str       # HIGH | MEDIUM | LOW
    reasoning: str


class ProjectAssessment(BaseModel):
    project_id: str
    flags: list[Flag]
    fraud_probability: str  # HIGH | MEDIUM | LOW
    summary: str


SYSTEM_PROMPT = textwrap.dedent("""
    You are a forensic analyst specializing in California public infrastructure grant fraud.
    You will be given batches of grant records and must assess each one for fraud indicators.

    CONTEXT — what "normal" looks like for CA infrastructure grants:
    - Typical construction/infrastructure grants: $500K–$5M
    - Typical remediation grants: $200K–$2M
    - Grant recipients usually have prior public contract history and active contractor licenses
    - Physical projects (construction, road work, remediation) require contractor licenses and local permits
    - Award dates follow budget cycles (June 30 fiscal year end — late June awards warrant scrutiny)
    - Sole-source awards above $250K are unusual and require justification
    - Legitimate recipients usually have a physical presence in or near the project location

    FRAUD INDICATORS to check per project:
    - Award amount anomalously high relative to project scope or description
    - Recipient has no prior public contract history
    - Vague, generic, or unusually brief project description
    - Recipient operates in an unrelated industry
    - Award date is suspiciously close to fiscal year end
    - Recipient location is far from project location
    - Sole-source contract above typical thresholds
    - Same recipient appears in multiple awards (related-party patterns)
    - Entity type inconsistent with project type (e.g., consulting firm doing heavy construction)
    - Missing key fields (no location, no description)

    For each project, return a JSON object with:
    - project_id (string)
    - flags: list of {flag, severity (HIGH/MEDIUM/LOW), reasoning}
    - fraud_probability: HIGH | MEDIUM | LOW
    - summary: one sentence explaining your overall assessment

    Return a JSON array of assessments, one per project.
    Only flag things that are genuinely anomalous — don't cry wolf on every project.
""").strip()


def _build_batch_prompt(batch: list[dict]) -> str:
    lines = ["Assess the following CA infrastructure grant records for fraud indicators:\n"]
    for p in batch:
        lines.append(json.dumps({
            "project_id":    p["project_id"],
            "project_name":  p["project_name"],
            "recipient_name": p["recipient_name"],
            "recipient_type": p["recipient_type"],
            "award_amount":  p["award_amount"],
            "award_date":    p["award_date"],
            "category":      p["category"],
            "description":   p["description"],
            "location":      p["location"],
            "funding_source": p["funding_source"],
            "contract_type": p["contract_type"],
        }))
    lines.append("\nReturn ONLY a JSON array of assessment objects. No commentary.")
    return "\n".join(lines)


def _parse_response(text: str) -> list[dict]:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    return json.loads(text.strip())


def _save_assessments(assessments: list[dict]) -> None:
    with get_conn() as conn:
        conn.execute("DELETE FROM red_flags")
        for a in assessments:
            for f in a.get("flags", []):
                conn.execute(
                    "INSERT INTO red_flags (project_id, flag, severity, reasoning) VALUES (?,?,?,?)",
                    (a["project_id"], f["flag"], f["severity"], f.get("reasoning", ""))
                )


def run(projects: list[dict]) -> list[dict]:
    """
    Score each project for fraud indicators.
    Returns list of assessment dicts.
    """
    model = genai.GenerativeModel(
        model_name=MODEL,
        system_instruction=SYSTEM_PROMPT,
    )

    all_assessments = []
    batches = [projects[i:i+BATCH_SIZE] for i in range(0, len(projects), BATCH_SIZE)]

    for i, batch in enumerate(batches):
        print(f"  Analyzing batch {i+1}/{len(batches)} ({len(batch)} projects)...")
        prompt = _build_batch_prompt(batch)

        response = model.generate_content(prompt)
        assessments = _parse_response(response.text)
        all_assessments.extend(assessments)

    print(f"  Assessed {len(all_assessments)} projects")
    _save_assessments(all_assessments)
    return all_assessments
