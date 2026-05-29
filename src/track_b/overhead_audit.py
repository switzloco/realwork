"""
Track B — Non-profit overhead audit.

For every nonprofit recipient that received a CA state grant, we:
  1. Match by name to a ProPublica EIN
  2. Pull the last 3 years of Form 990 filings
  3. Compute overhead / executive comp ratios
  4. Detect year-over-year spikes correlated with state funding receipt
  5. Flag organizations whose program expense ratio < 0.65 (sector median ~0.80)
     OR whose officer compensation > $300K running an org <$5M total budget
     OR whose mgmt overhead grew >50% YoY

This is the "Track B: Executive Bloat" that was in Antigravity's original spec
but never built. The fraud pattern: state grants flow in, admin/exec comp
spikes, program delivery stays flat. The state can't see this; ProPublica can.

Reads grants from data/grants_full.csv (READ ONLY) or from
data/audit_results.json's recipient_type=Nonprofit subset.

Writes:
  data/track_b/org_index.json       — name → EIN mapping (cache)
  data/track_b/filings/{ein}.json   — per-org filings (cache)
  data/track_b/overhead_results.json — final flagged list
  data/track_b/overhead_report.md   — human-readable report

Usage:
    # Test with 10 nonprofits, no Bright Data
    python -m src.track_b.overhead_audit --top 10

    # Production: full sweep through Bright Data
    python -m src.track_b.overhead_audit --top 500 --use-brightdata --budget 30
"""

import argparse
import csv
import json
import os
import re
import sys
import time
from pathlib import Path

from src.track_b.propublica import (
    ProPublicaClient,
    extract_financials,
    compute_ratios,
)

OUTPUT_DIR = Path("data/track_b")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "filings").mkdir(parents=True, exist_ok=True)

ORG_INDEX_PATH = OUTPUT_DIR / "org_index.json"
RESULTS_PATH = OUTPUT_DIR / "overhead_results.json"
REPORT_PATH = OUTPUT_DIR / "overhead_report.md"

# Sector medians (rough; from CharityNavigator / GuideStar published norms)
SECTOR_MEDIAN_PROGRAM_RATIO = 0.80
SECTOR_MEDIAN_MGMT_RATIO    = 0.10
SECTOR_MEDIAN_FUND_RATIO    = 0.07

# Flag thresholds — chosen to be sensitive without flooding
FLAG_LOW_PROGRAM_RATIO       = 0.65   # < this = looks more like admin shop than program org
FLAG_HIGH_MGMT_RATIO         = 0.25
FLAG_HIGH_OFFICER_COMP_ABS   = 300_000
FLAG_HIGH_OFFICER_COMP_RATIO = 0.10   # >10% of total expenses going to one officer
FLAG_YOY_MGMT_GROWTH         = 0.50   # mgmt overhead >50% YoY


def load_nonprofit_recipients(top_n: int = 500) -> list[dict]:
    """Load nonprofits from the grants dataset."""
    recipients: dict[str, dict] = {}

    csv_path = Path("data/grants_full.csv")
    if csv_path.exists():
        import pandas as pd
        df = pd.read_csv(csv_path, low_memory=False)
        # Normalize columns
        col_map = {}
        for c in df.columns:
            cl = c.lower().strip()
            if "totalawardamount" in cl:
                col_map[c] = "award_amount"
            elif "recipientname" in cl or "primaryrecipient" in cl:
                col_map[c] = "recipient_name"
            elif "recipienttype" in cl:
                col_map[c] = "recipient_type"
            elif "agencydept" in cl or "fundingsource" in cl:
                col_map[c] = "funding_source"
            elif "granttitle" in cl or "projecttitle" in cl:
                col_map[c] = "grant_title"
        df = df.rename(columns=col_map)
        if "award_amount" in df:
            df["award_amount"] = pd.to_numeric(
                df["award_amount"].astype(str).str.replace(r"[^\d.]", "", regex=True),
                errors="coerce",
            )

        nonprofits = df[df["recipient_type"].astype(str).str.lower() == "nonprofit"]
        for _, row in nonprofits.iterrows():
            name = str(row.get("recipient_name", "")).strip()
            if not name or name.lower() in ("nan", "unknown"):
                continue
            amt = float(row.get("award_amount") or 0)
            if name not in recipients:
                recipients[name] = {
                    "name": name,
                    "total_state_grants": 0,
                    "grant_count": 0,
                    "funding_sources": set(),
                    "grant_titles": [],
                }
            recipients[name]["total_state_grants"] += amt
            recipients[name]["grant_count"] += 1
            recipients[name]["funding_sources"].add(str(row.get("funding_source", "")))
            recipients[name]["grant_titles"].append(str(row.get("grant_title", "")))

    if not recipients:
        # Fallback: pull from audit JSON
        for path in ["data/audit_results.json", "data/services_fraud_results.json"]:
            if not Path(path).exists():
                continue
            with open(path) as f:
                data = json.load(f)
            for key in ("high_risk_private_null_disbursement", "high_risk_service_grants"):
                for e in data.get(key, []):
                    rt = (e.get("recipient_type") or "").lower()
                    if "nonprofit" not in rt:
                        continue
                    name = e.get("recipient", "").strip()
                    if name and name not in recipients:
                        recipients[name] = {
                            "name": name,
                            "total_state_grants": float(e.get("award_amount", 0)),
                            "grant_count": 1,
                            "funding_sources": {e.get("funding_source", "")},
                            "grant_titles": [e.get("grant_title", "")],
                        }

    # Serialize sets, sort by grant total
    out = []
    for r in recipients.values():
        r["funding_sources"] = sorted(s for s in r["funding_sources"] if s)
        out.append(r)
    out.sort(key=lambda r: -r["total_state_grants"])
    return out[:top_n]


def load_org_index() -> dict:
    if ORG_INDEX_PATH.exists():
        with open(ORG_INDEX_PATH) as f:
            return json.load(f)
    return {}


def save_org_index(idx: dict):
    with open(ORG_INDEX_PATH, "w") as f:
        json.dump(idx, f, indent=2)


def cache_filings(ein: str, filings: list[dict]):
    with open(OUTPUT_DIR / "filings" / f"{ein}.json", "w") as f:
        json.dump(filings, f, indent=2)


def cached_filings(ein: str) -> list[dict] | None:
    p = OUTPUT_DIR / "filings" / f"{ein}.json"
    if p.exists():
        with open(p) as f:
            return json.load(f)
    return None


def score_org(filings: list[dict], state_funding: float) -> dict:
    """Run the analysis on a single org's filings. Return verdict + flags."""
    if not filings:
        return {"verdict": "NO_FILINGS", "flags": []}

    # Sort by year descending
    series = []
    for f in filings:
        fin = extract_financials(f)
        ratios = compute_ratios(fin)
        if fin.get("tax_year"):
            series.append({"year": int(fin["tax_year"]), **fin, **ratios})
    series.sort(key=lambda x: -x.get("year", 0))

    if not series:
        return {"verdict": "NO_USABLE_DATA", "flags": []}

    latest = series[0]
    flags = []

    # 1. Low program expense ratio
    prog_ratio = latest.get("program_expense_ratio")
    if prog_ratio is not None and prog_ratio < FLAG_LOW_PROGRAM_RATIO:
        flags.append({
            "type": "LOW_PROGRAM_RATIO",
            "value": prog_ratio,
            "threshold": FLAG_LOW_PROGRAM_RATIO,
            "note": f"Only {prog_ratio*100:.1f}% of expenses go to programs "
                    f"(sector median: {SECTOR_MEDIAN_PROGRAM_RATIO*100:.0f}%)",
        })

    # 2. High mgmt overhead
    mgmt_ratio = latest.get("mgmt_overhead_ratio")
    if mgmt_ratio is not None and mgmt_ratio > FLAG_HIGH_MGMT_RATIO:
        flags.append({
            "type": "HIGH_MGMT_OVERHEAD",
            "value": mgmt_ratio,
            "threshold": FLAG_HIGH_MGMT_RATIO,
            "note": f"{mgmt_ratio*100:.1f}% of expenses are management overhead "
                    f"(sector median: {SECTOR_MEDIAN_MGMT_RATIO*100:.0f}%)",
        })

    # 3. High officer comp
    officer = latest.get("officer_comp_total") or 0
    officer_ratio = latest.get("officer_comp_ratio")
    total_exp = latest.get("total_expenses") or 0
    if officer >= FLAG_HIGH_OFFICER_COMP_ABS and total_exp < 5_000_000:
        flags.append({
            "type": "HIGH_OFFICER_COMP_SMALL_ORG",
            "value": officer,
            "note": f"${officer:,.0f} officer comp at an org with ${total_exp:,.0f} "
                    f"in total expenses",
        })
    if officer_ratio is not None and officer_ratio > FLAG_HIGH_OFFICER_COMP_RATIO:
        flags.append({
            "type": "HIGH_OFFICER_COMP_RATIO",
            "value": officer_ratio,
            "threshold": FLAG_HIGH_OFFICER_COMP_RATIO,
            "note": f"{officer_ratio*100:.1f}% of expenses to officer comp",
        })

    # 4. YoY spike in mgmt overhead
    if len(series) >= 2:
        prev = series[1]
        prev_mgmt = prev.get("mgmt_general_expenses") or 0
        curr_mgmt = latest.get("mgmt_general_expenses") or 0
        if prev_mgmt > 0:
            growth = (curr_mgmt - prev_mgmt) / prev_mgmt
            if growth > FLAG_YOY_MGMT_GROWTH:
                flags.append({
                    "type": "MGMT_OVERHEAD_YOY_SPIKE",
                    "value": growth,
                    "threshold": FLAG_YOY_MGMT_GROWTH,
                    "note": f"Mgmt overhead grew {growth*100:.1f}% YoY "
                            f"(${prev_mgmt:,.0f} → ${curr_mgmt:,.0f})",
                })

    # 5. State funding ≫ reported revenue (possible off-books pass-through)
    revenue = latest.get("total_revenue") or 0
    if state_funding > 0 and revenue > 0 and state_funding > revenue * 1.5:
        flags.append({
            "type": "STATE_FUNDING_EXCEEDS_REPORTED_REVENUE",
            "note": f"Received ${state_funding:,.0f} in CA grants but reports "
                    f"${revenue:,.0f} total revenue on Form 990",
        })

    if not flags:
        verdict = "CLEAN"
    elif len(flags) >= 3 or any(f["type"] == "STATE_FUNDING_EXCEEDS_REPORTED_REVENUE"
                                for f in flags):
        verdict = "FLAGGED_HIGH"
    else:
        verdict = "FLAGGED"

    return {
        "verdict": verdict,
        "flags": flags,
        "latest_year": latest.get("year"),
        "latest_program_ratio": prog_ratio,
        "latest_mgmt_ratio": mgmt_ratio,
        "latest_officer_comp": officer,
        "latest_total_expenses": total_exp,
        "latest_total_revenue": revenue,
        "filings_analyzed": len(series),
        "series": series,
    }


def run(args):
    use_bd = args.use_brightdata
    bd_client = None
    if use_bd:
        from src.bright_data.client import BrightDataClient
        bd_client = BrightDataClient(budget_cap=args.budget, label="track_b")
        print(f"Routing ProPublica through Web Unlocker (budget ${args.budget})")

    pp = ProPublicaClient(brightdata_client=bd_client, delay=args.delay)

    recipients = load_nonprofit_recipients(top_n=args.top)
    print(f"Loaded {len(recipients)} nonprofit grant recipients")

    org_index = load_org_index()
    results = []
    flagged_count = 0

    try:
        for i, rec in enumerate(recipients, 1):
            name = rec["name"]
            state_grants = rec["total_state_grants"]

            # Step 1: resolve EIN
            if name in org_index:
                cached = org_index[name]
                ein = cached.get("ein")
            else:
                match = pp.best_match(name, state="CA")
                ein = match.get("ein") if match else None
                org_index[name] = {
                    "ein": ein,
                    "matched_name": match.get("name") if match else None,
                    "state": match.get("state") if match else None,
                }

            if not ein:
                results.append({**rec, "verdict": "NO_EIN_MATCH"})
                print(f"[{i}/{len(recipients)}] {name[:40]:40s} -> NO_EIN_MATCH")
                continue

            # Step 2: pull filings (use cache)
            filings = cached_filings(str(ein))
            if filings is None:
                org = pp.get_org(str(ein))
                filings = org.get("filings_with_data", []) or org.get("filings", [])
                cache_filings(str(ein), filings)

            # Step 3: score
            score = score_org(filings, state_grants)
            entry = {**rec, "ein": ein, **score}
            results.append(entry)

            tag = score["verdict"]
            if tag.startswith("FLAGGED"):
                flagged_count += 1
            alert = "  ⚠️" if tag.startswith("FLAGGED") else ""
            safe = name.encode("ascii", "ignore").decode("ascii")
            print(f"[{i}/{len(recipients)}] {safe[:40]:40s} -> {tag}{alert}")

            if i % 25 == 0:
                save_org_index(org_index)
                _write_results(results)

    except KeyboardInterrupt:
        print("\n⚠️  Interrupted — saving partial results")
    finally:
        save_org_index(org_index)
        _write_results(results)
        _write_report(results)

    print(f"\n{'='*60}")
    print(f"TRACK B OVERHEAD AUDIT COMPLETE")
    print(f"  Organizations analyzed: {len(results)}")
    print(f"  Flagged: {flagged_count}")
    if bd_client:
        print(f"  Bright Data: {bd_client.report()}")
    high = [r for r in results if r.get("verdict") == "FLAGGED_HIGH"]
    if high:
        print(f"\n  HIGH-PRIORITY flags ({len(high)}):")
        for r in high[:25]:
            print(f"    {r['name'][:40]:40s} state ${r['total_state_grants']:>12,.0f}")
            for f in r.get("flags", [])[:3]:
                print(f"      - {f['type']}: {f['note']}")
    print(f"{'='*60}")


def _write_results(results: list):
    with open(RESULTS_PATH, "w") as f:
        json.dump({"count": len(results), "entities": results}, f, indent=2,
                  default=str)


def _write_report(results: list):
    lines = ["# Track B — Nonprofit Overhead Audit\n"]
    flagged = [r for r in results if r.get("verdict", "").startswith("FLAGGED")]
    high = [r for r in results if r.get("verdict") == "FLAGGED_HIGH"]
    lines.append(f"- Organizations analyzed: **{len(results)}**")
    lines.append(f"- Flagged: **{len(flagged)}** ({len(high)} HIGH priority)\n")

    if high:
        lines.append("## High-Priority Flags\n")
        lines.append("| Org | State Grants | Year | Prog Ratio | Mgmt Ratio | Officer Comp | Flags |")
        lines.append("|-----|--------------|------|------------|------------|--------------|-------|")
        for r in high:
            pr = r.get("latest_program_ratio")
            mr = r.get("latest_mgmt_ratio")
            oc = r.get("latest_officer_comp") or 0
            flag_types = ", ".join(f["type"] for f in r.get("flags", []))
            lines.append(f"| {r['name'][:40]} | ${r['total_state_grants']:,.0f} "
                         f"| {r.get('latest_year','?')} "
                         f"| {pr*100:.1f}% if pr else '?' "
                         f"| {mr*100:.1f}% if mr else '?' "
                         f"| ${oc:,.0f} | {flag_types} |")

    other = [r for r in flagged if r.get("verdict") != "FLAGGED_HIGH"]
    if other:
        lines.append("\n## Other Flags\n")
        for r in other[:50]:
            lines.append(f"### {r['name']} — ${r['total_state_grants']:,.0f} in state grants")
            lines.append(f"- EIN: {r.get('ein','?')}, "
                         f"Latest year: {r.get('latest_year','?')}")
            for f in r.get("flags", []):
                lines.append(f"- **{f['type']}**: {f['note']}")
            lines.append("")

    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(lines))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=100)
    parser.add_argument("--use-brightdata", action="store_true",
                        help="Route ProPublica calls through Web Unlocker")
    parser.add_argument("--budget", type=float, default=30.0)
    parser.add_argument("--delay", type=float, default=0.25)
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
