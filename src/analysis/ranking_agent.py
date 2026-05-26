"""
Ranking Agent — Stage 1
Takes all Red Flag Analyst assessments and produces a prioritized shortlist.
Uses Gemini 2.5 Pro for the highest-leverage decision in the pipeline.
"""

import json
import os
import textwrap

import google.generativeai as genai

from src.db import get_conn

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-pro"

TARGET_COUNT = int(os.getenv("TARGET_COUNT", "50"))

SYSTEM_PROMPT = textwrap.dedent("""
    You are the chief investigator on a public fraud task force.
    You will receive fraud risk assessments for a set of California infrastructure grant projects.
    Your job is to select the top projects for investigation and rank them by priority.

    Score each project on three axes (1-10):
    - fraud_probability: How likely is this actually fraud? (density + severity of flags)
    - investigation_feasibility: Can we realistically find corroborating evidence online?
      (Is the recipient a searchable entity? Does the project have a physical address?)
    - dollar_magnitude: Normalized score for award size (bigger = higher score)

    composite_score = (fraud_probability * 0.5) + (feasibility * 0.3) + (magnitude * 0.2)

    For each selected project, also write:
    - investigation_brief: 1-2 sentences on what specifically to look for
    - suggested_sources: which evidence tiers to hit first (SoS, CSLB, LinkedIn, Maps, permits, news)

    Return ONLY a JSON array of the top projects, ordered rank 1 (best) to N, each with:
    {
      "rank": int,
      "project_id": str,
      "fraud_probability": float (1-10),
      "investigation_feasibility": float (1-10),
      "dollar_magnitude": float (1-10),
      "composite_score": float,
      "investigation_brief": str,
      "suggested_sources": [str]
    }
""").strip()


def _enrich_assessments(assessments: list[dict]) -> list[dict]:
    """Join assessment data with project data from DB for the ranking prompt."""
    with get_conn() as conn:
        projects = {
            r["project_id"]: dict(r)
            for r in conn.execute("SELECT * FROM projects").fetchall()
        }

    enriched = []
    for a in assessments:
        p = projects.get(a["project_id"], {})
        enriched.append({
            **a,
            "project_name":  p.get("project_name", ""),
            "recipient_name": p.get("recipient_name", ""),
            "award_amount":  p.get("award_amount", 0),
            "award_date":    p.get("award_date", ""),
            "category":      p.get("category", ""),
            "location":      p.get("location", ""),
        })
    return enriched


def _save_rankings(rankings: list[dict]) -> None:
    with get_conn() as conn:
        conn.execute("DELETE FROM rankings")
        for r in rankings:
            conn.execute("""
                INSERT OR REPLACE INTO rankings VALUES (?,?,?,?,?,?,?,?)
            """, (
                r["rank"],
                r["project_id"],
                str(r.get("fraud_probability", "")),
                str(r.get("investigation_feasibility", "")),
                r.get("dollar_magnitude", 0),
                r.get("composite_score", 0),
                r.get("investigation_brief", ""),
                json.dumps(r.get("suggested_sources", [])),
            ))


def run(assessments: list[dict]) -> list[dict]:
    """
    Rank assessed projects and return the top TARGET_COUNT investigation targets.
    """
    enriched = _enrich_assessments(assessments)

    # Only pass projects with at least one flag to the ranking agent
    flagged = [a for a in enriched if a.get("flags")]
    if not flagged:
        print("  No flagged projects found — check ETL and analyst output")
        return []

    print(f"  Ranking {len(flagged)} flagged projects, selecting top {TARGET_COUNT}...")

    model = genai.GenerativeModel(
        model_name=MODEL,
        system_instruction=SYSTEM_PROMPT,
    )

    prompt = textwrap.dedent(f"""
        Select the top {TARGET_COUNT} projects for investigation from the following assessments.
        Return ONLY a JSON array, no commentary.

        {json.dumps(flagged, indent=2)}
    """).strip()

    response = model.generate_content(prompt)
    text = response.text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    rankings = json.loads(text.strip())

    _save_rankings(rankings)

    print(f"  Top {len(rankings)} targets selected:")
    for r in rankings:
        print(f"    #{r['rank']} {r.get('project_id','')} — score {r.get('composite_score','?'):.1f} — {r.get('investigation_brief','')[:80]}")

    return rankings
