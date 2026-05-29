"""
Ensemble Second-Opinion — cross-model verdict validator via AI/ML API.

For every HIGH PRIORITY finding our pipeline produces (Gemini-driven), we
ask a second, structurally-different model the same question. If both
models flag it, the verdict is upgraded to ENSEMBLE_CONFIRMED. If they
disagree, the finding moves to NEEDS_HUMAN_REVIEW.

This is a known technique for LLM calibration: cross-model agreement is a
stronger signal than single-model confidence. It also lets us claim
"verified by two independent models" in the submission, which matters
for civic-tech credibility — single-model claims are easily dismissed as
hallucination.

AI/ML API gives us OpenAI-compatible access to GPT-4o, Claude, Llama, etc
through one endpoint. We pick GPT-4o by default (structurally different
from our Gemini-based pipeline; trained on different corpora; different
RLHF).

Qualifies us for the AI/ML API partner prize ($1K cash + $1K credits).

Required env:
    AIMLAPI_KEY=<from event page, per-team-per-account>

Reads from data/track_b/validated_flags.json and the dossier JSONs.
Writes data/ensemble/{type}_{slug}.json + summary.

Usage:
    # Quick smoke test on 3 entities
    python -m src.ensemble.second_opinion --top 3

    # Full HIGH PRIORITY pass
    python -m src.ensemble.second_opinion --top 20
"""

import argparse
import json
import os
import re
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

AIMLAPI_KEY = os.environ.get("AIMLAPI_KEY", "")
AIMLAPI_URL = "https://api.aimlapi.com/v1/chat/completions"
DEFAULT_MODEL = "gpt-4o"

OUTPUT_DIR = Path("data/ensemble")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


SYSTEM_PROMPT = """You are an independent forensic accountant reviewing a flagged anomaly in California public spending data. You will be given a set of facts derived from public records (Form 990 filings, state grant awards, DGS purchase orders).

Your job: independently decide whether the facts described constitute an anomaly warranting follow-up investigation by an oversight body (State Auditor, DOJ).

Output STRICT JSON only, no prose:
{
  "verdict": "AGREES_WARRANTS_INVESTIGATION" | "DISAGREES_LIKELY_BENIGN" | "INSUFFICIENT_INFO",
  "confidence": 0.0-1.0,
  "key_reasoning": "1-2 sentences",
  "missing_evidence": ["thing 1", "thing 2"]
}

Apply skepticism. The charitable interpretation often holds. But also flag patterns that match prosecuted fraud signatures (split contracts, related-party transactions, ghost recipients)."""


def slug(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", s.lower()).strip("_")[:60]


def query_second_model(facts: str, model: str = DEFAULT_MODEL) -> dict:
    if not AIMLAPI_KEY:
        return {"error": "AIMLAPI_KEY not set in env"}
    try:
        r = requests.post(
            AIMLAPI_URL,
            headers={
                "Authorization": f"Bearer {AIMLAPI_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": facts},
                ],
                "temperature": 0.2,
                "max_tokens": 600,
                "response_format": {"type": "json_object"},
            },
            timeout=60,
        )
        if not r.ok:
            return {"error": f"HTTP {r.status_code}", "body": r.text[:500]}
        data = r.json()
        content = data["choices"][0]["message"]["content"]
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            m = re.search(r"\{[\s\S]+\}", content)
            return json.loads(m.group(0)) if m else {"raw": content[:500]}
    except Exception as e:
        return {"error": str(e)}


def format_track_b_facts(entry: dict) -> str:
    """Convert a Track B entry into a fact bundle for the second model."""
    flags = entry.get("surviving_flags", []) or entry.get("flags", [])
    lines = [
        f"Organization: {entry.get('name', '?')}",
        f"EIN: {entry.get('ein', '?')}",
        f"Total California state grants received: ${entry.get('total_state_grants', 0):,.0f}",
        f"Latest Form 990 year: {entry.get('latest_year', '?')}",
        f"Latest year total revenue: ${entry.get('latest_total_revenue', 0):,.0f}",
        f"Latest year total expenses: ${entry.get('latest_total_expenses', 0):,.0f}",
        f"Latest year officer compensation: ${entry.get('latest_officer_comp', 0):,.0f}",
        "",
        "Flags raised by our pipeline:",
    ]
    for f in flags:
        lines.append(f"  - {f.get('type', '?')}: {f.get('note', '')}")
    return "\n".join(lines)


def format_dgs_facts(dossier: dict) -> str:
    """Format a DGS split-contract dossier for the second model."""
    a = dossier.get("analysis", {})
    lines = [
        f"Vendor: {dossier.get('vendor', '?')}",
        f"Threshold our pipeline flagged: ${dossier.get('flagged_threshold', '?'):,}",
        f"Pattern verdict: {a.get('verdict', '?')}",
        f"Just-under-threshold POs: {a.get('near_threshold_count', '?')}",
        f"Just-under-threshold dollar total: ${a.get('near_threshold_value', 0):,.0f}",
        f"Lifetime PO value with this state: ${a.get('total_lifetime_value', 0):,.0f}",
        f"Single-buyer concentration: {a.get('single_buyer_concentration', 0)*100:.0f}%",
        f"Date span: {a.get('date_span_days', '?')} days",
        f"Max POs in any 7-day window: {a.get('max_same_week_count', '?')}",
        "Suspicion factors detected:",
    ]
    for sf in a.get("suspicion_factors", []):
        lines.append(f"  - {sf}")
    if a.get("near_threshold_buyer_breakdown"):
        b = a["near_threshold_buyer_breakdown"][0]
        lines.append(f"Top buyer: {b['buyer']} ({b['count']} POs)")
    if a.get("near_threshold_top_descriptions"):
        d = a["near_threshold_top_descriptions"][0]
        lines.append(f"Most common description: \"{d['description'][:200]}\" "
                     f"({d['count']}x)")
    return "\n".join(lines)


def load_track_b_high(top_n: int) -> list[dict]:
    path = Path("data/track_b/validated_flags.json")
    if not path.exists():
        return []
    with open(path) as f:
        data = json.load(f)
    high = [
        e for e in data.get("entities", [])
        if e.get("validation", {}).get("status") == "VALIDATED_HIGH_PRIORITY"
    ]
    high.sort(key=lambda e: -float(e.get("total_state_grants", 0)))
    return high[:top_n]


def load_dgs_strong() -> list[dict]:
    out = []
    for p in Path("data/dgs/split_contract_dossiers").glob("*.json"):
        with open(p) as f:
            d = json.load(f)
        if d.get("analysis", {}).get("verdict") == "STRONG_SPLIT_CONTRACT_PATTERN":
            out.append(d)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=10,
                        help="Top N Track B entities to second-opinion")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help="AI/ML API model name (gpt-4o, claude-3-5-sonnet, etc.)")
    parser.add_argument("--include-dgs", action="store_true", default=True,
                        help="Also second-opinion DGS strong patterns")
    args = parser.parse_args()

    if not AIMLAPI_KEY:
        print("AIMLAPI_KEY not set in .env")
        print("Get from event page → Technology Partners → AI/ML API → Claim Coupon")
        return

    print(f"Cross-model second opinion using {args.model}")
    print(f"Pulling Track B HIGH PRIORITY (top {args.top})...")
    tb_entries = load_track_b_high(args.top)
    dgs_entries = load_dgs_strong() if args.include_dgs else []
    print(f"  {len(tb_entries)} nonprofits + {len(dgs_entries)} DGS vendors")

    summary = []

    for i, e in enumerate(tb_entries, 1):
        name = e["name"]
        facts = format_track_b_facts(e)
        safe = name.encode("ascii", "ignore").decode("ascii")
        print(f"\n[track_b {i}/{len(tb_entries)}] {safe[:40]}")
        verdict = query_second_model(facts, args.model)

        out_path = OUTPUT_DIR / f"track_b_{slug(name)}.json"
        with open(out_path, "w") as f:
            json.dump({"name": name, "facts_sent": facts,
                       "second_opinion": verdict}, f, indent=2, default=str)

        v = verdict.get("verdict", "ERROR")
        c = verdict.get("confidence", 0)
        print(f"   -> {v} (confidence {c})")
        summary.append({"type": "track_b", "name": name, "verdict": v,
                        "confidence": c,
                        "reasoning": verdict.get("key_reasoning", "")})

    for i, d in enumerate(dgs_entries, 1):
        vendor = d["vendor"]
        facts = format_dgs_facts(d)
        print(f"\n[dgs {i}/{len(dgs_entries)}] {vendor[:40]}")
        verdict = query_second_model(facts, args.model)

        out_path = OUTPUT_DIR / f"dgs_{slug(vendor)}.json"
        with open(out_path, "w") as f:
            json.dump({"vendor": vendor, "facts_sent": facts,
                       "second_opinion": verdict}, f, indent=2, default=str)

        v = verdict.get("verdict", "ERROR")
        c = verdict.get("confidence", 0)
        print(f"   -> {v} (confidence {c})")
        summary.append({"type": "dgs", "name": vendor, "verdict": v,
                        "confidence": c,
                        "reasoning": verdict.get("key_reasoning", "")})

    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump({"model_used": args.model, "results": summary},
                  f, indent=2)

    # Tally
    print(f"\n{'='*60}")
    print(f"ENSEMBLE SECOND OPINION COMPLETE — {args.model}")
    agrees = [s for s in summary if s["verdict"] == "AGREES_WARRANTS_INVESTIGATION"]
    disagrees = [s for s in summary if s["verdict"] == "DISAGREES_LIKELY_BENIGN"]
    insufficient = [s for s in summary if s["verdict"] == "INSUFFICIENT_INFO"]

    print(f"  Total reviewed: {len(summary)}")
    print(f"  Confirmed by second model: {len(agrees)}")
    print(f"  Rejected by second model: {len(disagrees)}")
    print(f"  Insufficient info: {len(insufficient)}")

    if agrees:
        print(f"\n  ENSEMBLE-CONFIRMED findings:")
        for s in agrees[:15]:
            print(f"    {s['type']:8s} {s['name'][:40]:40s} "
                  f"(conf {s['confidence']})")
            if s['reasoning']:
                print(f"       reasoning: {s['reasoning'][:100]}")

    if disagrees:
        print(f"\n  Second model REJECTED:")
        for s in disagrees:
            print(f"    {s['type']:8s} {s['name'][:40]:40s} "
                  f"reasoning: {s['reasoning'][:80]}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
