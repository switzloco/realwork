"""
Schedule L Analyzer — Related-Party Transactions in Form 990s.

Schedule L of Form 990 discloses transactions between the nonprofit and
"interested persons" — officers, directors, key employees, their family
members, and entities they control. This is where actual nonprofit
self-dealing surfaces:

  - Loans between the org and an officer
  - Grants from the org to a board member's other organization
  - The org renting space from the executive director
  - "Consulting" contracts to the spouse of a board chair

These are reportable on Schedule L but the disclosure threshold is high
enough that many smaller transactions don't get scrutinized.

This script:
  1. Pulls the latest Form 990 PDF for each VALIDATED_HIGH_PRIORITY org
  2. Uses Bright Data Web Unlocker to fetch the PDF (ProPublica's storage
     is geo-restricted in some networks)
  3. Extracts text via PyPDF
  4. Searches for Schedule L indicators and key phrases
  5. Outputs a per-org markdown summary

Reads from data/track_b/validated_flags.json (READ ONLY).
Writes to data/track_b/schedule_l/{ein}.md per org + summary.

Cost: ~$0.001 per PDF (Web Unlocker), ~$0.02 total for top 20.

Usage:
    pip install pypdf
    python -m src.track_b.schedule_l_analyzer --top 10 --use-brightdata --budget 2
"""

import argparse
import json
import re
from pathlib import Path

OUTPUT_DIR = Path("data/track_b/schedule_l")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
INPUT_PATH = Path("data/track_b/validated_flags.json")

# Phrases that strongly suggest related-party activity
RELATED_PARTY_PHRASES = [
    "interested person",
    "related party",
    "related person",
    "schedule l",
    "key employee",
    "family member",
    "loan to officer",
    "loan from officer",
    "business transaction",
    "compensation to family",
    "controlled entity",
    "disqualified person",
    "excess benefit",
]

# Section headers that show Schedule L is being filled in (not just listed)
SCHEDULE_L_ACTIVE_MARKERS = [
    re.compile(r"schedule\s+l\b.{0,200}interested\s+person", re.I | re.S),
    re.compile(r"part\s+i{1,4}.{0,100}business\s+transactions", re.I | re.S),
    re.compile(r"part\s+ii.{0,100}loans", re.I | re.S),
    re.compile(r"part\s+iii.{0,100}grants.{0,100}assistance", re.I | re.S),
]


def slug(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", s.lower()).strip("_")[:60]


def load_high_priority(top_n: int = 20) -> list[dict]:
    if not INPUT_PATH.exists():
        print(f"Need {INPUT_PATH} — run validate_flags.py first")
        return []
    with open(INPUT_PATH) as f:
        data = json.load(f)
    entries = data.get("entities", [])
    high = [
        e for e in entries
        if e.get("validation", {}).get("status") == "VALIDATED_HIGH_PRIORITY"
        and e.get("validation", {}).get("latest_990_pdf")
    ]
    high.sort(key=lambda e: -float(e.get("total_state_grants", 0)))
    return high[:top_n]


def fetch_pdf(url: str, bd_client) -> bytes | None:
    if bd_client:
        # Web Unlocker
        from src.bright_data.client import ENDPOINT, UNLOCKER_ZONE
        try:
            bd_client._check_budget(bd_client.UNLOCKER_COST)
            r = bd_client.session.post(ENDPOINT, json={
                "zone": UNLOCKER_ZONE,
                "url": url,
                "format": "raw",
            }, timeout=120)
            bd_client.spent += bd_client.UNLOCKER_COST
            bd_client._log({"type": "pdf_fetch", "url": url,
                            "status": r.status_code, "size": len(r.content),
                            "cost": bd_client.UNLOCKER_COST})
            return r.content if r.ok else None
        except Exception as e:
            print(f"  PDF fetch failed: {e}")
            return None
    else:
        import requests
        try:
            r = requests.get(url, timeout=60)
            return r.content if r.ok else None
        except Exception:
            return None


def extract_text(pdf_bytes: bytes) -> str:
    try:
        from pypdf import PdfReader
        from io import BytesIO
        reader = PdfReader(BytesIO(pdf_bytes))
        return "\n".join(p.extract_text() or "" for p in reader.pages)
    except ImportError:
        print("  pypdf not installed — pip install pypdf")
        return ""
    except Exception as e:
        print(f"  PDF parse error: {e}")
        return ""


def analyze_text(text: str, org_name: str) -> dict:
    if not text:
        return {"status": "NO_TEXT"}

    text_lower = text.lower()

    # Quick check: was Schedule L checked "Yes" on Form 990 Part IV line 25-28?
    part_iv_yes = bool(
        re.search(
            r"(2[5-8])\s*[a-d]?\s*.*?\b(yes|x)\b.{0,80}schedule\s+l",
            text_lower, re.S,
        )
    )

    # Count phrase hits
    phrase_hits = {}
    for phrase in RELATED_PARTY_PHRASES:
        cnt = text_lower.count(phrase)
        if cnt > 0:
            phrase_hits[phrase] = cnt

    # Detect active Schedule L sections
    active_sections = []
    for pattern in SCHEDULE_L_ACTIVE_MARKERS:
        if pattern.search(text):
            active_sections.append(pattern.pattern[:60])

    # Find $ amounts near "interested person" mentions
    transactions = []
    for m in re.finditer(
        r"interested\s+person.{0,500}?\$\s*([\d,]+)",
        text_lower, re.S,
    ):
        amt_str = m.group(1).replace(",", "")
        try:
            amt = int(amt_str)
            if amt >= 1000:
                ctx_start = max(0, m.start() - 200)
                ctx_end = min(len(text_lower), m.end() + 100)
                transactions.append({
                    "amount": amt,
                    "context": text_lower[ctx_start:ctx_end][:400],
                })
        except ValueError:
            continue

    # Officer names appearing in loan contexts
    name_pattern = re.compile(
        r"\b([A-Z][a-z]+\s+[A-Z]\.?\s*[A-Z][a-z]+)\b",
    )
    officer_names_found = list(set(name_pattern.findall(text))[:20])

    # Verdict
    score = 0
    if part_iv_yes:
        score += 3
    if active_sections:
        score += 2
    if len(phrase_hits) >= 5:
        score += 1
    if transactions:
        score += min(len(transactions), 3)

    if score >= 5:
        verdict = "SCHEDULE_L_ACTIVE_HIGH_SIGNAL"
    elif score >= 3:
        verdict = "SCHEDULE_L_PRESENT"
    elif score >= 1:
        verdict = "MINIMAL_SIGNAL"
    else:
        verdict = "NO_SCHEDULE_L_INDICATORS"

    return {
        "verdict": verdict,
        "score": score,
        "part_iv_yes": part_iv_yes,
        "active_sections": active_sections,
        "phrase_hits": phrase_hits,
        "transactions_near_interested_person": transactions[:10],
        "potential_officer_names": officer_names_found,
        "text_length": len(text),
    }


def write_org_report(entry: dict, analysis: dict):
    name = entry["name"]
    path = OUTPUT_DIR / f"{slug(name)}.md"
    lines = [
        f"# Schedule L Analysis — {name}\n",
        f"- EIN: {entry.get('ein')}",
        f"- State grants: ${entry.get('total_state_grants', 0):,.0f}",
        f"- Tax year: {entry.get('latest_year', '?')}",
        f"- 990 PDF: {entry.get('validation', {}).get('latest_990_pdf', '?')}",
        f"\n## Verdict: **{analysis.get('verdict', '?')}** "
        f"(score {analysis.get('score', 0)})\n",
        f"- Part IV Schedule L 'Yes' indicator: {analysis.get('part_iv_yes')}",
        f"- Active section markers: {len(analysis.get('active_sections', []))}",
        f"- Related-party phrase hits: "
        f"{sum(analysis.get('phrase_hits', {}).values())}",
        f"- Transactions near 'interested person': "
        f"{len(analysis.get('transactions_near_interested_person', []))}",
    ]

    if analysis.get("phrase_hits"):
        lines.append("\n### Phrase hits\n")
        for phrase, count in sorted(analysis["phrase_hits"].items(),
                                    key=lambda x: -x[1]):
            lines.append(f"- `{phrase}` × {count}")

    tx = analysis.get("transactions_near_interested_person", [])
    if tx:
        lines.append("\n### Dollar amounts in 'interested person' context\n")
        for t in tx[:5]:
            lines.append(f"- **${t['amount']:,}** — context: "
                         f"`...{t['context'][:300]}...`")

    if analysis.get("potential_officer_names"):
        lines.append("\n### Names extracted from document (may include officers)\n")
        for n in analysis["potential_officer_names"][:10]:
            lines.append(f"- {n}")

    with open(path, "w") as f:
        f.write("\n".join(lines))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--use-brightdata", action="store_true")
    parser.add_argument("--budget", type=float, default=2.0)
    args = parser.parse_args()

    entries = load_high_priority(top_n=args.top)
    if not entries:
        return
    print(f"Analyzing Schedule L for {len(entries)} HIGH priority orgs...")

    bd_client = None
    if args.use_brightdata:
        from src.bright_data.client import BrightDataClient
        bd_client = BrightDataClient(budget_cap=args.budget,
                                     label="schedule_l")

    summary = []
    for i, entry in enumerate(entries, 1):
        name = entry["name"]
        url = entry["validation"]["latest_990_pdf"]
        safe = name.encode("ascii", "ignore").decode("ascii")
        print(f"[{i}/{len(entries)}] {safe[:40]:40s}", end="", flush=True)

        pdf_bytes = fetch_pdf(url, bd_client)
        if not pdf_bytes:
            print(" -> FETCH_FAIL")
            summary.append({"name": name, "verdict": "FETCH_FAIL",
                            "ein": entry.get("ein")})
            continue

        text = extract_text(pdf_bytes)
        analysis = analyze_text(text, name)
        write_org_report(entry, analysis)
        verdict = analysis.get("verdict", "?")
        score = analysis.get("score", 0)
        print(f" -> {verdict} (score {score})")
        summary.append({
            "name": name,
            "ein": entry.get("ein"),
            "state_grants": entry.get("total_state_grants"),
            "verdict": verdict,
            "score": score,
            "transactions_count": len(analysis.get(
                "transactions_near_interested_person", [])),
        })

    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump({
            "analyzed": len(entries),
            "summary": summary,
        }, f, indent=2, default=str)

    print(f"\n{'='*60}")
    print(f"SCHEDULE L ANALYSIS COMPLETE")
    high = [s for s in summary if s["verdict"] == "SCHEDULE_L_ACTIVE_HIGH_SIGNAL"]
    present = [s for s in summary if s["verdict"] == "SCHEDULE_L_PRESENT"]
    if high:
        print(f"\n  🚨 HIGH signal — Schedule L active with transactions:")
        for s in high:
            print(f"    {s['name'][:40]:40s} score {s['score']} "
                  f"(${s['state_grants']:,.0f} state grants)")
    if present:
        print(f"\n  ⚠️  Schedule L present but lower signal:")
        for s in present:
            print(f"    {s['name'][:40]:40s} score {s['score']}")
    if bd_client:
        print(f"\n  {bd_client.report()}")
    print(f"\n  Per-org reports: data/track_b/schedule_l/*.md")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
