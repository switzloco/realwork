"""
Orchestrator — main pipeline controller.
Runs Stage 1 (ETL → Red Flag Analyst → Ranking).
Stage 2 (Investigation) and Stage 3 (Synthesis) stubs are here, not yet implemented.
"""

import argparse
import json
from rich.console import Console
from rich.table import Table

from src.db import init_db
from src.budget import BudgetController
from src import etl, analysis

console = Console()
budget  = BudgetController()


def run_stage1(source: str = "auto") -> list[dict]:
    console.rule("[bold blue]Stage 1: Target Selection")

    console.print("\n[bold]ETL Agent[/bold] — loading CA grant data")
    projects = etl.ingest.run(source=source)

    console.print(f"\n[bold]Red Flag Analyst[/bold] — analyzing {len(projects)} projects")
    assessments = analysis.red_flag_analyst.run(projects)

    console.print(f"\n[bold]Ranking Agent[/bold] — selecting top targets")
    rankings = analysis.ranking_agent.run(assessments)

    _print_rankings(rankings)
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

    table = Table(title="Investigation Targets")
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


def main():
    parser = argparse.ArgumentParser(description="RealWork fraud detection pipeline")
    parser.add_argument("--stage", choices=["1", "2", "3", "all"], default="1")
    parser.add_argument("--source", choices=["api", "csv", "auto"], default="auto",
                        help="Data source for ETL (auto tries API then CSV)")
    args = parser.parse_args()

    init_db()

    if args.stage in ("1", "all"):
        rankings = run_stage1(source=args.source)

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
