"""
LA Alliance Risk Analyst — slow, grounded, continuous.

Reads extracted invoice records from ledger.json and runs each through
Gemini 2.5 Pro with Google Search grounding. Grounding lets the model look
up what billing codes (D7, PHK, SAM, etc.) actually mean, find the LA County
MOU contracted rates, and compare billed amounts against them.

This resolves the "no baseline" problem: instead of hallucinating a fraud
probability, the model cites public sources for its reasoning.

Designed to run slowly and continuously — even after submission. Results
accumulate in risk_assessments.json as they come in. Resumable: already-
assessed records are skipped on re-run.

Rate: default 1 request per 6 seconds = 10 RPM (safe for free-tier Gemini;
raise --sleep to slow down further, lower to 4s on paid quota).

Run:
    # assess the 22 already-extracted invoices (finishes in ~2 min)
    python -m src.la_alliance.risk_analyst

    # keep running on a growing ledger (post-submission)
    python -m src.la_alliance.risk_analyst --sleep 6 --loop

    # cap spend / records
    python -m src.la_alliance.risk_analyst --limit 50
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

OUT_DIR = Path("data/la_alliance")
LEDGER_PATH = OUT_DIR / "ledger.json"
ASSESSMENTS_PATH = OUT_DIR / "risk_assessments.json"
DONE_PATH = OUT_DIR / "risk_done.txt"

MODEL = "gemini-2.5-pro"

SYSTEM_PROMPT = """You are a forensic auditor reviewing LA County homeless-service
provider invoices submitted under the LA Alliance for Human Rights settlement.

Your job for each invoice:
1. DECODE the deliverable codes (D7, PHK, SAM, MHSA, etc.) — use Google Search
   to find what each code means in the LA County homeless services billing context.
2. FIND the contracted rate — search for the LA County / LA Alliance MOU or
   contract that governs this provider's reimbursement rate for these services.
3. COMPARE billed amount to contracted rate × stated units. Flag if they diverge.
4. FLAG anomalies from this list:
   - Billed amount inconsistent with contracted rate
   - Vague or missing deliverable descriptions
   - Round-number billing (suspiciously even totals)
   - Billing period gaps or overlaps vs. other invoices from the same vendor
   - Unusually high or low cost per unit vs. sector norms

Return a JSON object with exactly these keys — no prose, no markdown fences:
{
  "vendor": string,
  "billed_amount": number|null,
  "decoded_deliverables": [{"code": string, "meaning": string, "source": string}],
  "contracted_rate_found": boolean,
  "contracted_rate_notes": string,
  "flags": [{"flag": string, "severity": "HIGH"|"MEDIUM"|"LOW", "reasoning": string}],
  "fraud_risk": "HIGH"|"MEDIUM"|"LOW"|"UNCLEAR",
  "summary": string,
  "grounding_sources": [string]
}

Base your flags strictly on what you find. If you cannot find a contracted rate,
say so in contracted_rate_notes and mark contracted_rate_found: false. Do not
invent numbers. UNCLEAR is a valid fraud_risk when evidence is insufficient."""


def load_ledger() -> list[dict]:
    if not LEDGER_PATH.exists():
        raise SystemExit(f"{LEDGER_PATH} not found — run invoice_extractor first.")
    return json.loads(LEDGER_PATH.read_text())


def load_done() -> set[str]:
    if DONE_PATH.exists():
        return set(DONE_PATH.read_text().splitlines())
    return set()


def mark_done(key: str):
    with open(DONE_PATH, "a") as f:
        f.write(key + "\n")


def load_assessments() -> list[dict]:
    if ASSESSMENTS_PATH.exists():
        return json.loads(ASSESSMENTS_PATH.read_text())
    return []


def save_assessments(assessments: list[dict]):
    ASSESSMENTS_PATH.write_text(json.dumps(assessments, indent=2))


def record_key(rec: dict) -> str:
    return f"{rec.get('vendor','')}|{rec.get('invoice_date','')}|{rec.get('billed_amount','')}"


def assess(rec: dict) -> dict | None:
    try:
        import google.generativeai as genai
        from google.generativeai import types
    except ImportError:
        raise SystemExit("google-generativeai not installed")

    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise SystemExit("GEMINI_API_KEY not set")
    genai.configure(api_key=key)

    # build the invoice summary to hand the model
    invoice_text = json.dumps({
        "vendor": rec.get("vendor"),
        "invoice_date": rec.get("invoice_date"),
        "billed_amount": rec.get("billed_amount"),
        "deliverables": rec.get("deliverables"),
        "extraction_notes": rec.get("extraction_notes"),
        "source_file": rec.get("source_title"),
    }, indent=2)

    prompt = f"Assess this invoice:\n\n{invoice_text}"

    try:
        model = genai.GenerativeModel(
            MODEL,
            system_instruction=SYSTEM_PROMPT,
            tools=[types.Tool(google_search=types.GoogleSearch())],
        )
        resp = model.generate_content(prompt)
        raw = resp.text.strip()
    except Exception as e:
        return {"error": str(e), "vendor": rec.get("vendor"), "source": rec.get("source_title")}

    # strip markdown fences if present
    import re
    raw = re.sub(r"^```(?:json)?|```$", "", raw, flags=re.MULTILINE).strip()
    s, e = raw.find("{"), raw.rfind("}")
    if s == -1 or e == -1:
        return {"error": f"no JSON in response: {raw[:200]}", "vendor": rec.get("vendor")}

    try:
        result = json.loads(raw[s:e + 1])
        result["source_title"] = rec.get("source_title", "")
        return result
    except json.JSONDecodeError as err:
        return {"error": f"JSON parse error: {err}", "raw": raw[:400], "vendor": rec.get("vendor")}


def _print_assessment(a: dict):
    vendor = a.get("vendor") or a.get("source_title") or "?"
    risk = a.get("fraud_risk", "?")
    flags = a.get("flags") or []
    amount = a.get("billed_amount")
    amt_str = f"${amount:,.2f}" if isinstance(amount, (int, float)) else "?"

    risk_icon = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢", "UNCLEAR": "⚪"}.get(risk, "?")
    print(f"\n  {risk_icon} [{risk}] {vendor} | {amt_str}")
    if flags:
        for f in flags:
            sev = f.get("severity", "")
            print(f"     • [{sev}] {f.get('flag','')}")
            if f.get("reasoning"):
                print(f"       {f['reasoning'][:120]}")
    if a.get("contracted_rate_notes"):
        print(f"     Rate: {a['contracted_rate_notes'][:120]}")
    if a.get("summary"):
        print(f"     {a['summary'][:200]}")
    if a.get("error"):
        print(f"     ⚠ Error: {a['error'][:120]}")


def run(limit: int = 0, sleep: float = 6.0, loop: bool = False):
    print(f"=== LA Alliance Risk Analyst (Gemini 2.5 Pro + grounding) ===")
    print(f"Ledger: {LEDGER_PATH} | sleep: {sleep}s | loop: {loop}\n")

    iteration = 0
    while True:
        iteration += 1
        records = load_ledger()
        done = load_done()
        assessments = load_assessments()

        todo = [r for r in records
                if record_key(r) not in done
                and r.get("vendor")  # skip null-vendor records
                ]
        if limit:
            todo = todo[:limit]

        if not todo:
            if loop:
                print(f"  [iter {iteration}] nothing new — sleeping 30s…")
                time.sleep(30)
                continue
            else:
                print("All records assessed.")
                break

        print(f"[iter {iteration}] {len(todo)} record(s) to assess | "
              f"{len(done)} already done\n")

        for i, rec in enumerate(todo, 1):
            vendor = rec.get("vendor") or rec.get("source_title") or "?"
            print(f"  [{i}/{len(todo)}] Assessing: {vendor[:60]}…", flush=True)

            result = assess(rec)
            _print_assessment(result)

            assessments.append(result)
            save_assessments(assessments)
            mark_done(record_key(rec))

            if i < len(todo):
                time.sleep(sleep)

        print(f"\n  Saved {len(assessments)} assessment(s) → {ASSESSMENTS_PATH}")

        if not loop:
            break

    # write a summary of high/medium findings
    _write_summary(load_assessments())
    print(f"\nRisk summary → {OUT_DIR}/risk_summary.md")


def _write_summary(assessments: list[dict]):
    high = [a for a in assessments if a.get("fraud_risk") == "HIGH"]
    med = [a for a in assessments if a.get("fraud_risk") == "MEDIUM"]

    lines = [
        "# LA Alliance Invoice Risk Summary\n",
        f"Assessed: {len(assessments)} invoices | "
        f"🔴 HIGH: {len(high)} | 🟡 MEDIUM: {len(med)}\n",
        "> Findings are based on public records and contracted rates found via",
        "> Google Search grounding. Not accusations — anomalies for human review.\n",
    ]

    for label, group in [("HIGH RISK", high), ("MEDIUM RISK", med)]:
        if group:
            lines.append(f"## {label}\n")
            for a in group:
                vendor = a.get("vendor") or a.get("source_title") or "?"
                amt = a.get("billed_amount")
                amt_str = f"${amt:,.2f}" if isinstance(amt, (int, float)) else "?"
                lines.append(f"### {vendor} — {amt_str}")
                if a.get("summary"):
                    lines.append(a["summary"])
                for f in (a.get("flags") or []):
                    lines.append(f"- [{f.get('severity')}] {f.get('flag')}: {f.get('reasoning','')[:200]}")
                lines.append("")

    (OUT_DIR / "risk_summary.md").write_text("\n".join(lines))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0,
                    help="max records per iteration (0 = all)")
    ap.add_argument("--sleep", type=float, default=6.0,
                    help="seconds between Gemini calls (6 = 10 RPM, safe for free tier)")
    ap.add_argument("--loop", action="store_true",
                    help="keep running, picking up new ledger entries as they arrive")
    args = ap.parse_args()
    run(limit=args.limit, sleep=args.sleep, loop=args.loop)
