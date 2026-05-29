"""
Track B Flag Validator — kill EIN-match false positives, surface real signal.

The Round 3 Track B run had MADD flagged as "state funding > revenue" because
ProPublica name-matching picked a tiny local chapter EIN (revenue $5K), not
the national org (revenue $50M+). This script validates every FLAGGED entry:

  1. Re-check the EIN match — does the name overlap + state make sense?
  2. Sanity-check the financial scale — a $5K-revenue org getting $2M from
     the state is more likely a wrong-EIN than a real off-books transfer.
  3. For STATE_FUNDING_EXCEEDS_REPORTED_REVENUE, require the ratio be
     plausible (not extreme like 400x).
  4. For YoY exec comp spikes, pull the 990 PDF URL and capture it for
     manual review.

Outputs:
  data/track_b/validated_flags.json  — only the cases that survive validation
  data/track_b/validated_report.md   — human-readable summary

Usage:
    python -m src.track_b.validate_flags
    python -m src.track_b.validate_flags --use-brightdata --budget 5
"""

import argparse
import json
import re
from pathlib import Path

from src.track_b.propublica import ProPublicaClient

OUTPUT_DIR = Path("data/track_b")
INPUT_PATH = OUTPUT_DIR / "overhead_results.json"
OUTPUT_PATH = OUTPUT_DIR / "validated_flags.json"
REPORT_PATH = OUTPUT_DIR / "validated_report.md"


def name_overlap(a: str, b: str) -> float:
    a_tokens = set(re.findall(r"\b\w+\b", a.lower()))
    b_tokens = set(re.findall(r"\b\w+\b", b.lower()))
    if not a_tokens or not b_tokens:
        return 0.0
    return len(a_tokens & b_tokens) / max(len(a_tokens), len(b_tokens))


def validate_entry(entry: dict, pp: ProPublicaClient) -> dict:
    """Apply validation rules. Return entry with validation_status set."""
    name = entry["name"]
    ein = entry.get("ein")
    flags = entry.get("flags", [])

    # Re-fetch org metadata to check state + name match
    org_data = pp.get_org(str(ein)) if ein else {}
    org = org_data.get("organization", {})
    matched_name = org.get("name", "")
    matched_state = (org.get("state") or "").upper()

    name_sim = name_overlap(name, matched_name)

    validation = {
        "matched_name": matched_name,
        "matched_state": matched_state,
        "name_overlap": round(name_sim, 3),
    }

    # Reject obvious wrong-EIN matches: low name overlap AND wrong state
    if name_sim < 0.4 and matched_state and matched_state != "CA":
        validation["status"] = "REJECTED_BAD_EIN_MATCH"
        validation["reason"] = (f"name overlap {name_sim:.0%} and state "
                                f"{matched_state} (not CA)")
        return {**entry, "validation": validation}

    # Sanity-check each flag
    surviving_flags = []
    rejected_flags = []
    revenue = entry.get("latest_total_revenue") or 0
    state_grants = entry.get("total_state_grants") or 0

    for flag in flags:
        ftype = flag["type"]

        if ftype == "STATE_FUNDING_EXCEEDS_REPORTED_REVENUE":
            # Real signal: state funding is 1.5-10x reported revenue
            # Likely EIN mismatch: state funding is >50x reported revenue
            #   (means we matched a tiny chapter, not the real org)
            if revenue <= 0:
                rejected_flags.append({**flag, "reject_reason":
                                       "revenue is 0/null — likely wrong EIN"})
                continue
            ratio = state_grants / revenue if revenue > 0 else float("inf")
            if ratio > 50:
                rejected_flags.append({**flag, "reject_reason":
                                       f"state/revenue ratio {ratio:.0f}x — "
                                       f"almost certainly wrong EIN match"})
                continue
            surviving_flags.append({**flag, "state_to_revenue_ratio": round(ratio, 2)})

        elif ftype in ("HIGH_OFFICER_COMP_SMALL_ORG",
                       "HIGH_OFFICER_COMP_RATIO",
                       "MGMT_OVERHEAD_YOY_SPIKE",
                       "LOW_PROGRAM_RATIO",
                       "HIGH_MGMT_OVERHEAD"):
            # These survive validation by default — they're real even if
            # the org is real (not the wrong EIN)
            surviving_flags.append(flag)
        else:
            surviving_flags.append(flag)

    # If all flags rejected, the validation is REJECTED
    if not surviving_flags:
        validation["status"] = "REJECTED_ALL_FLAGS_FAILED_SANITY"
        return {**entry, "validation": validation,
                "rejected_flags": rejected_flags}

    # Otherwise compute new verdict from surviving flags
    high_priority_types = {"STATE_FUNDING_EXCEEDS_REPORTED_REVENUE",
                           "MGMT_OVERHEAD_YOY_SPIKE"}
    has_high = any(f["type"] in high_priority_types for f in surviving_flags)
    if len(surviving_flags) >= 3 or has_high:
        new_verdict = "VALIDATED_HIGH_PRIORITY"
    else:
        new_verdict = "VALIDATED"

    validation["status"] = new_verdict

    # Pull the 990 PDF URL for the latest year so user can manually review
    filings = org_data.get("filings_with_data", []) or org_data.get("filings", [])
    pdf_url = None
    for f in filings:
        if f.get("pdf_url"):
            pdf_url = f["pdf_url"]
            break
    if pdf_url:
        validation["latest_990_pdf"] = pdf_url

    return {**entry, "validation": validation,
            "surviving_flags": surviving_flags,
            "rejected_flags": rejected_flags}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--use-brightdata", action="store_true")
    parser.add_argument("--budget", type=float, default=5.0)
    args = parser.parse_args()

    if not INPUT_PATH.exists():
        print(f"Need {INPUT_PATH} — run src.track_b.overhead_audit first")
        return

    with open(INPUT_PATH) as f:
        data = json.load(f)
    entries = data.get("entities", [])
    flagged = [e for e in entries if str(e.get("verdict", "")).startswith("FLAGGED")]
    print(f"Validating {len(flagged)} flagged entries...")

    bd_client = None
    if args.use_brightdata:
        from src.bright_data.client import BrightDataClient
        bd_client = BrightDataClient(budget_cap=args.budget, label="track_b_validate")

    pp = ProPublicaClient(brightdata_client=bd_client, delay=0.25)

    validated = []
    rejected_count = 0
    for i, entry in enumerate(flagged, 1):
        result = validate_entry(entry, pp)
        validated.append(result)
        status = result["validation"]["status"]
        if status.startswith("REJECTED"):
            rejected_count += 1
        safe = entry["name"].encode("ascii", "ignore").decode("ascii")
        print(f"[{i}/{len(flagged)}] {safe[:40]:40s} -> {status}")

    with open(OUTPUT_PATH, "w") as f:
        json.dump({
            "input_flagged_count": len(flagged),
            "rejected": rejected_count,
            "validated": len(validated) - rejected_count,
            "entities": validated,
        }, f, indent=2, default=str)

    # Report
    high = [v for v in validated
            if v["validation"]["status"] == "VALIDATED_HIGH_PRIORITY"]
    normal = [v for v in validated if v["validation"]["status"] == "VALIDATED"]

    lines = ["# Track B Validated Flags\n",
             f"- Input flagged: {len(flagged)}",
             f"- Rejected (likely EIN mismatch): {rejected_count}",
             f"- Validated (survives sanity check): {len(high) + len(normal)}",
             f"  - HIGH priority: {len(high)}",
             f"  - Normal: {len(normal)}\n"]

    if high:
        lines.append("## HIGH PRIORITY — Validated Anomalies\n")
        for v in high:
            vd = v["validation"]
            lines.append(f"### {v['name']}")
            lines.append(f"- EIN: {v.get('ein')} (matched: {vd.get('matched_name')}, "
                         f"state {vd.get('matched_state', '?')}, "
                         f"name overlap {vd.get('name_overlap', 0)*100:.0f}%)")
            lines.append(f"- State grants: ${v.get('total_state_grants', 0):,.0f}")
            lines.append(f"- Latest year: {v.get('latest_year', '?')}")
            lines.append(f"- Total expenses: ${v.get('latest_total_expenses', 0):,.0f}")
            lines.append(f"- Total revenue: ${v.get('latest_total_revenue', 0):,.0f}")
            lines.append("- Surviving flags:")
            for f in v.get("surviving_flags", []):
                lines.append(f"  - **{f['type']}**: {f.get('note', '')}")
            if vd.get("latest_990_pdf"):
                lines.append(f"- 990 PDF: {vd['latest_990_pdf']}")
            lines.append("")

    if normal:
        lines.append("\n## Validated (Normal Priority)\n")
        for v in normal[:30]:
            lines.append(f"- **{v['name']}** — "
                         f"${v.get('total_state_grants', 0):,.0f} in state grants, "
                         f"{len(v.get('surviving_flags', []))} flags")

    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(lines))

    print(f"\n{'='*60}")
    print(f"TRACK B VALIDATION COMPLETE")
    print(f"  Rejected (likely EIN mismatch): {rejected_count}")
    print(f"  HIGH priority survivors: {len(high)}")
    print(f"  Report: {REPORT_PATH}")
    if bd_client:
        print(f"  {bd_client.report()}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
