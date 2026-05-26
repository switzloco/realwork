"""
Scraper Coordinator — Stage 2
Executes the approved scrape plan using Bright Data APIs.
Extracts structured findings using Gemini 2.5 Flash.

Bright Data products used:
- SERP API: structured search results (Google, Bing)
- Web Unlocker: bypass bot detection on any URL
- Scraping Browser: JS-heavy interactive sites (not yet implemented)
"""

import json
import os
import requests
import textwrap
from datetime import datetime, timezone
from urllib.parse import quote_plus
import google.generativeai as genai
from rich.console import Console

from src.db import get_conn
from src.budget import BudgetController

console = Console()
budget = BudgetController()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
EXTRACTION_MODEL = "gemini-2.5-flash"

# Bright Data credentials
BRIGHT_DATA_API_KEY = os.getenv("BRIGHT_DATA_API_KEY", "")
BRIGHT_DATA_SERP_ZONE = os.getenv("BRIGHT_DATA_SERP_ZONE", "realwork_serp")
BRIGHT_DATA_UNLOCKER_ZONE = os.getenv("BRIGHT_DATA_UNLOCKER_ZONE", "realwork_unlocker")

EXTRACTION_SYSTEM_PROMPT = textwrap.dedent("""
    You are an AI data extractor. You are given the raw content (HTML, JSON, or text)
    of a webpage that was scraped to investigate a potential fraud case.

    You will also receive:
    - The name of the source (e.g., "CA Secretary of State", "LinkedIn", "Google Search")
    - The target URL
    - The project details and red flags being investigated

    Your job is to analyze the raw content and extract structured findings.
    Identify key information:
    - Business registry: entity name, registration date, status (active/suspended), corporate address, officers.
    - Licenses (CSLB): license status, classification, workers' comp info, bonding.
    - Web search/Social media: evidence of the company's existence, size, operations, projects, employee count.

    Assess whether the information supports the fraud hypothesis, contradicts it, or is inconclusive.

    Return ONLY a JSON object with this exact schema:
    {
      "extracted": {
        "entity_name": str,
        "status": str,
        "registration_date": str,
        "address": str,
        "key_people": [str],
        "additional_details": dict
      },
      "finding": str,
      "supports_fraud": bool | null
    }
""").strip()


def _scrape_serp(query: str) -> tuple[str, float]:
    """
    Use Bright Data SERP API for search engine queries.
    Returns (response_text, cost).
    """
    if not BRIGHT_DATA_API_KEY:
        console.print("    [red][SKIP] No BRIGHT_DATA_API_KEY set. Cannot execute SERP query.[/red]")
        return "", 0.0

    url = "https://api.brightdata.com/request"
    headers = {
        "Authorization": f"Bearer {BRIGHT_DATA_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "zone": BRIGHT_DATA_SERP_ZONE,
        "url": f"https://www.google.com/search?q={quote_plus(query)}",
        "format": "json",
    }

    try:
        console.print(f"    [dim]SERP API: searching \"{query}\"[/dim]")
        r = requests.post(url, headers=headers, json=payload, timeout=30)
        if r.status_code == 200:
            console.print("    [green][OK] SERP API response received[/green]")
            return r.text, 0.50
        else:
            console.print(f"    [red][FAIL] SERP API returned {r.status_code}: {r.text[:200]}[/red]")
            return "", 0.0
    except Exception as e:
        console.print(f"    [red][FAIL] SERP API error: {e}[/red]")
        return "", 0.0


def _scrape_unlocker(url: str) -> tuple[str, float]:
    """
    Use Bright Data Web Unlocker for direct URL scraping.
    Bypasses bot detection, CAPTCHAs, and geo-blocks.
    Returns (response_text, cost).
    """
    if not BRIGHT_DATA_API_KEY:
        console.print("    [red][SKIP] No BRIGHT_DATA_API_KEY set. Cannot execute scrape.[/red]")
        return "", 0.0

    api_url = "https://api.brightdata.com/request"
    headers = {
        "Authorization": f"Bearer {BRIGHT_DATA_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "zone": BRIGHT_DATA_UNLOCKER_ZONE,
        "url": url,
        "format": "raw",
    }

    try:
        console.print(f"    [dim]Web Unlocker: fetching {url[:80]}...[/dim]")
        r = requests.post(api_url, headers=headers, json=payload, timeout=30)
        if r.status_code == 200:
            console.print("    [green][OK] Web Unlocker response received[/green]")
            return r.text, 1.00
        else:
            console.print(f"    [red][FAIL] Web Unlocker returned {r.status_code}: {r.text[:200]}[/red]")
            return "", 0.0
    except Exception as e:
        console.print(f"    [red][FAIL] Web Unlocker error: {e}[/red]")
        return "", 0.0


def _fetch_page(url: str, product: str) -> tuple[str, float]:
    """
    Route to the correct Bright Data product.
    Returns (content, actual_cost). If the call fails, returns ("", 0.0).
    No mock fallbacks — failed scrapes are recorded as empty.
    """
    if product == "serp_api":
        query = url
        if "google.com/search" in url:
            from urllib.parse import urlparse, parse_qs
            parsed = parse_qs(urlparse(url).query)
            query = parsed.get("q", [url])[0]
        return _scrape_serp(query)

    elif product == "scraper_api" or product == "web_unlocker":
        return _scrape_unlocker(url)

    elif product == "scraping_browser":
        console.print("    [yellow][SKIP] Scraping Browser not yet implemented. Recording as empty.[/yellow]")
        return "", 0.0

    else:
        console.print(f"    [yellow][SKIP] Unknown product '{product}'. Recording as empty.[/yellow]")
        return "", 0.0


def _extract_findings(raw_data: str, source: str, url: str, project_brief: dict) -> dict:
    """Use Gemini 2.5 Flash to extract structured findings from raw scraped content."""
    if not raw_data:
        return {
            "extracted": {},
            "finding": f"No data retrieved from {source}. Source may be blocked or unavailable.",
            "supports_fraud": None,
        }

    prompt = textwrap.dedent(f"""
        Extract findings from the following scraped content.

        SOURCE: {source}
        URL: {url}

        PROJECT CONTEXT:
        - Recipient: {project_brief.get('recipient_name', 'N/A')}
        - Description: {project_brief.get('description', 'N/A')}
        - Award Amount: ${project_brief.get('award_amount', 0.0):,.2f}

        RAW SCRAPED CONTENT (truncated):
        {raw_data[:50000]}

        Return ONLY a JSON object matching the requested schema.
    """).strip()

    model = genai.GenerativeModel(
        model_name=EXTRACTION_MODEL,
        system_instruction=EXTRACTION_SYSTEM_PROMPT,
    )

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        return json.loads(text.strip())
    except Exception as e:
        console.print(f"    [red][ERROR] Gemini extraction error: {e}[/red]")
        return {
            "extracted": {},
            "finding": f"Extraction failed: {e}",
            "supports_fraud": None,
        }


def _get_project_brief(project_id: str) -> dict:
    with get_conn() as conn:
        p = conn.execute("SELECT * FROM projects WHERE project_id = ?", (project_id,)).fetchone()
        return dict(p) if p else {}


def run(plan: dict) -> dict:
    """
    Execute all steps in the scrape plan.
    Saves evidence to the database and records costs via the Budget Controller.
    """
    project_id = plan["project_id"]
    steps = plan["steps"]
    project_brief = _get_project_brief(project_id)

    console.print(f"\n[bold yellow]Scraper Coordinator[/bold yellow]: executing {len(steps)} steps for {project_id}")

    evidence_records = []
    total_actual_cost = 0.0

    for step in sorted(steps, key=lambda s: s["order"]):
        order = step["order"]
        source = step["source"]
        url = step["target_url"]
        product = step["bright_data_product"]
        estimated_cost = step["estimated_cost"]
        rationale = step["rationale"]

        console.print(f"\n  [bold]Step {order}: {source}[/bold] ({product})")
        console.print(f"    URL: {url}")
        console.print(f"    Rationale: {rationale}")

        res = budget.reserve(estimated_cost, f"Step {order} for {project_id}", project_id)
        if not res["approved"]:
            console.print(f"    [red][DENIED] {res['reason']}[/red]")
            continue

        console.print(f"    [green][APPROVED] Headroom after: ${res.get('remaining_after', 0.0):.2f}[/green]")

        raw_data, actual_cost = _fetch_page(url, product)
        total_actual_cost += actual_cost

        findings = _extract_findings(raw_data, source, url, project_brief)
        console.print(f"    [cyan]Finding:[/cyan] {findings.get('finding', 'N/A')}")

        supports = findings.get("supports_fraud")
        label = "SUPPORTS" if supports is True else ("CONTRADICTS" if supports is False else "INCONCLUSIVE")
        console.print(f"    [cyan]Fraud hypothesis:[/cyan] {label}")

        budget.record(
            project_id=project_id,
            source=source,
            product=product,
            estimated_cost=estimated_cost,
            actual_cost=actual_cost,
            description=f"Bright Data {product} — {source}",
        )

        with get_conn() as conn:
            conn.execute("""
                INSERT INTO evidence
                (project_id, source, url_scraped, timestamp, actual_cost, raw_data, extracted, finding, supports_fraud)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                project_id,
                source,
                url,
                datetime.now(timezone.utc).isoformat(),
                actual_cost,
                raw_data[:20000] if raw_data else None,
                json.dumps(findings.get("extracted", {})),
                findings.get("finding", ""),
                1 if supports is True else (0 if supports is False else None),
            ))

        evidence_records.append({
            "source": source,
            "url_scraped": url,
            "actual_cost": actual_cost,
            "finding": findings.get("finding", ""),
            "supports_fraud": supports,
        })

    return {
        "project_id": project_id,
        "evidence": evidence_records,
        "total_actual_cost": round(total_actual_cost, 2),
    }
