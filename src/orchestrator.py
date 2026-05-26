"""
Orchestrator — main pipeline controller.
Runs Stage 1 (ETL → Red Flag Analyst → Ranking → Search Validation).
Stage 2 (Investigation) and Stage 3 (Synthesis) stubs are here, not yet implemented.
"""

from dotenv import load_dotenv
load_dotenv()

import argparse
import json
from rich.console import Console
from rich.table import Table

from src.db import init_db
from src.budget import BudgetController
from src.etl import ingest
from src.analysis import red_flag_analyst, ranking_agent, search_validator

console = Console()
budget  = BudgetController()


def run_stage1(source: str = "auto", skip_validation: bool = False) -> list[dict]:
    console.rule("[bold blue]Stage 1: Target Selection")

    console.print("\n[bold]ETL Agent[/bold] — loading CA grant data")
    projects = ingest.run(source=source)

    console.print(f"\n[bold]Red Flag Analyst[/bold] — analyzing {len(projects)} projects")
    assessments = red_flag_analyst.run(projects)

    console.print(f"\n[bold]Ranking Agent[/bold] — selecting top targets")
    rankings = ranking_agent.run(assessments)

    _print_rankings(rankings)

    if not skip_validation:
        console.print(f"\n[bold]Search Validator[/bold] — grounded web search to eliminate false positives")
        validated = search_validator.run(rankings)
        _print_validated(validated)
        return validated

    return rankings


def run_stage2(rankings: list[dict]) -> None:
    console.rule("[bold yellow]Stage 2: Evidence Gathering")
    console.print("[dim]Not yet implemented — coming next[/dim]")
    # TODO: Investigation Planner + Scraper Coordinator


def run_stage3() -> None:
    console.rule("[bold green]Stage 3: Synthesis")
    console.print("[dim]Not yet implemented — coming after Stage 2[/dim]")
    # TODO: Synthesis Agent


def _print_rankings(rankings: list[dict]) -> None:
    if not rankings:
        console.print("[red]No targets selected.[/red]")
        return

    table = Table(title="Investigation Targets (Pre-Validation)")
    table.add_column("Rank", style="bold")
    table.add_column("Project ID")
    table.add_column("Score")
    table.add_column("Brief")

    for r in rankings:
        table.add_row(
            str(r["rank"]),
            r["project_id"],
            f"{r.get('composite_score', 0):.1f}",
            r.get("investigation_brief", "")[:80],
        )
    console.print(table)


def _print_validated(validated: list[dict]) -> None:
    if not validated:
        console.print("[red]All targets cleared by search validation.[/red]")
        return

    table = Table(title="Validated Targets (Post-Search)")
    table.add_column("Rank", style="bold")
    table.add_column("Project ID")
    table.add_column("Recommendation", style="bold")
    table.add_column("Flags Remaining")
    table.add_column("Reasoning")

    for v in validated:
        rec = v.get("recommendation", "?")
        style = "green" if rec == "INVESTIGATE" else "yellow"
        table.add_row(
            str(v.get("validated_rank", "?")),
            v["project_id"],
            f"[{style}]{rec}[/{style}]",
            str(len(v.get("red_flags_remaining", []))),
            v.get("reasoning", "")[:80],
        )
    console.print(table)


def main():
    parser = argparse.ArgumentParser(description="RealWork fraud detection pipeline")
    parser.add_argument("--stage", choices=["1", "2", "3", "all"], default="1")
    parser.add_argument("--source", choices=["api", "csv", "auto"], default="auto",
                        help="Data source for ETL (auto tries API then CSV)")
    parser.add_argument("--skip-validation", action="store_true",
                        help="Skip the search validation step in Stage 1")
    args = parser.parse_args()

    init_db()

    if args.stage in ("1", "all"):
        rankings = run_stage1(source=args.source, skip_validation=args.skip_validation)

    if args.stage in ("2", "all"):
        # Load rankings from DB if not running from stage 1 this session
        if args.stage == "2":
            from src.db import get_conn
            with get_conn() as conn:
                rankings = [dict(r) for r in conn.execute(
                    "SELECT * FROM rankings ORDER BY rank"
                ).fetchall()]
        run_stage2(rankings)

    if args.stage in ("3", "all"):
        run_stage3()

    # Always print budget status
    s = budget.status()
    console.print(f"\n[bold]Bright Data spend:[/bold] ${s['spent']:.2f} / $250 ({s['zone']})")


if __name__ == "__main__":
    main()
