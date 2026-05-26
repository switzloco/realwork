"""
Synthesis Agent — Stage 3
Synthesizes all gathered evidence and investigation logs
using Gemini 2.5 Pro to produce a final structured and Markdown report.
"""

import json
import os
import textwrap
from datetime import datetime, timezone
import google.generativeai as genai
from rich.console import Console

from src.db import get_conn
from src.budget import BudgetController

console = Console()
budget = BudgetController()

# Initialize Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-pro"

SYSTEM_PROMPT = textwrap.dedent("""
    You are a senior forensic analyst. Your task is to evaluate all evidence gathered during the
    investigation phase and synthesize a final report.
    
    For each project, review:
    - Original details and red flags
    - Scraped evidence records (source, url, findings, and supports_fraud indicators)
    
    Classify each project conclusion as:
    - "FLAGGED": Concrete, suspicious anomalies persist and are supported by the evidence (e.g. entity is inactive/suspended, does not exist, mismatch in business classification, residential address for heavy construction).
    - "CLEARED": Evidence indicates the recipient is a legitimate operator and the flags were false alarms.
    - "INCONCLUSIVE": Insufficient or blocked scraping results make a final judgment impossible.
    
    Determine confidence level ("HIGH" | "MEDIUM" | "LOW") and write a concise, objective summary.
    
    Return ONLY a JSON object with this exact schema:
    {
      "projects": [
        {
          "project_id": str,
          "project_name": str,
          "conclusion": "FLAGGED" | "CLEARED" | "INCONCLUSIVE",
          "confidence": "HIGH" | "MEDIUM" | "LOW",
          "evidence_summary": str,         // 2-3 sentences summarizing the evidence
          "key_findings": [str],           // bullet points of critical discoveries
          "sources_checked": int,          // count of evidence sources checked
          "total_cost": float              // actual cost spent on this project's investigation
        }
      ],
      "methodology": str,                  // description of investigation steps (ETL, Red Flag analysis, grounded search, web scraping validation)
      "budget_summary": {
        "spent": float,
        "remaining": float,
        "cost_per_project": float
      },
      "recommendations": [str]             // next steps (e.g. whistle-blower legal filing, media package, or deprioritization)
    }
""").strip()


def _get_investigation_data() -> dict:
    """Fetch all completed projects, red flags, and gathered evidence from the database."""
    with get_conn() as conn:
        # Get all projects that have evidence gathered
        evidence_pids = [
            row[0] for row in conn.execute("SELECT DISTINCT project_id FROM evidence").fetchall()
        ]
        
        if not evidence_pids:
            return {}

        projects_data = {}
        for pid in evidence_pids:
            project = conn.execute("SELECT * FROM projects WHERE project_id = ?", (pid,)).fetchone()
            ranking = conn.execute("SELECT * FROM rankings WHERE project_id = ?", (pid,)).fetchone()
            flags = conn.execute("SELECT * FROM red_flags WHERE project_id = ?", (pid,)).fetchall()
            evidence = conn.execute("SELECT * FROM evidence WHERE project_id = ?", (pid,)).fetchall()
            
            projects_data[pid] = {
                "project": dict(project) if project else {},
                "ranking": dict(ranking) if ranking else {},
                "flags": [dict(f) for f in flags],
                "evidence": [dict(e) for e in evidence]
            }
            
        return projects_data


def _parse_response(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    return json.loads(text.strip())


def _save_conclusions(results: list[dict]) -> None:
    """Save the final conclusions to the SQLite investigation_log table."""
    with get_conn() as conn:
        for r in results:
            conn.execute("""
                INSERT OR REPLACE INTO investigation_log
                (project_id, status, conclusion, confidence, rationale, total_cost, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                r["project_id"],
                "COMPLETED",
                r["conclusion"],
                r["confidence"],
                r["evidence_summary"],
                r["total_cost"],
                datetime.now(timezone.utc).isoformat()
            ))


def _generate_markdown_report(report_json: dict) -> str:
    """Create a structured, premium markdown report from the JSON results."""
    md = []
    md.append("# RealWork Investigation Findings Report")
    md.append(f"*Generated on: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC*")
    md.append("")
    
    # Budget summary card
    bs = report_json["budget_summary"]
    md.append("## Executive Budget Summary")
    md.append(f"- **Total Spent:** ${bs['spent']:.2f}")
    md.append(f"- **Remaining Budget:** ${bs['remaining']:.2f}")
    md.append(f"- **Average Cost per Project:** ${bs['cost_per_project']:.2f}")
    md.append("")
    
    md.append("## Investigation Methodology")
    md.append(report_json["methodology"])
    md.append("")
    
    md.append("## Project Findings")
    
    for p in report_json["projects"]:
        status_color = "[FLAGGED]" if p["conclusion"] == "FLAGGED" else ("[CLEARED]" if p["conclusion"] == "CLEARED" else "[INCONCLUSIVE]")
        md.append(f"### Project ID: `{p['project_id']}` ({p['project_name']})")
        md.append(f"- **Conclusion:** **{status_color}**")
        md.append(f"- **Confidence Level:** {p['confidence']}")
        md.append(f"- **Evidence Checked:** {p['sources_checked']} sources")
        md.append(f"- **Investigation Cost:** ${p['total_cost']:.2f}")
        md.append("")
        md.append("#### Evidence Summary")
        md.append(p["evidence_summary"])
        md.append("")
        md.append("#### Key Discoveries")
        for finding in p["key_findings"]:
            md.append(f"- {finding}")
        md.append("")
        md.append("---")
        md.append("")
        
    md.append("## Strategic Recommendations")
    for rec in report_json["recommendations"]:
        md.append(f"- {rec}")
        
    return "\n".join(md)


def run() -> dict:
    """Run synthesis over all investigated projects in the DB."""
    console.print("\n[bold green]Synthesis Agent[/bold green] : summarizing all gathered evidence")
    
    data = _get_investigation_data()
    if not data:
        console.print("[red]No evidence gathered yet. Run Stage 2 first.[/red]")
        return {}

    prompt_data = []
    for pid, p_info in data.items():
        # clean raw_data from evidence to avoid prompt overflow
        clean_evidence = []
        for e in p_info["evidence"]:
            ce = dict(e)
            ce.pop("raw_data", None)
            clean_evidence.append(ce)
            
        prompt_data.append({
            "project_id": pid,
            "project_details": p_info["project"],
            "red_flags": p_info["flags"],
            "ranking_brief": p_info["ranking"],
            "evidence_gathered": clean_evidence
        })

    prompt = textwrap.dedent(f"""
        Please review the following investigation data and synthesize a final report.
        
        INVESTIGATION DATA:
        {json.dumps(prompt_data, indent=2)}
        
        Return ONLY the JSON object, matching the requested schema.
    """).strip()

    model = genai.GenerativeModel(
        model_name=MODEL,
        system_instruction=SYSTEM_PROMPT
    )

    response = model.generate_content(prompt)
    report_json = _parse_response(response.text)
    
    # Enrich budget summary
    b_status = budget.status()
    report_json["budget_summary"] = {
        "spent": b_status["spent"],
        "remaining": b_status["remaining"],
        "cost_per_project": round(b_status["spent"] / len(report_json["projects"]), 2) if report_json["projects"] else 0.0
    }

    # Save to SQLite
    _save_conclusions(report_json["projects"])

    # Generate Markdown and write to file
    md_content = _generate_markdown_report(report_json)
    report_path = "findings.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    console.print(f"[green][SUCCESS] Final report generated and written to {report_path}[/green]")
    
    return report_json
