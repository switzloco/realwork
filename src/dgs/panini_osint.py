"""
Panini Time OSINT sweep — social + web presence via Bright Data SERP + Unlocker.

Panini Time surfaced in the DGS threshold-edge analysis: 12 purchase orders at
exactly $49,950 (one dollar below CA's $50k competitive-bidding threshold), all
concentrated to Cal Fire, multiple signed by a single procurement officer within
a 17-day window during active wildfire operations.

This script tries to answer the follow-up questions:
  - Is there a LinkedIn company page? How big/old is the company?
  - Are there any public bios of people involved — and do any show Cal Fire ties?
  - Any news, press, litigation, regulatory, SAM.gov, or FedBizOpps mentions?
  - What does the company actually say it does? Does it match "emergency supplies"?
  - Any other government contracts outside Cal Fire?

Approach: SERP API for discovery (cheap, broad), then targeted Web Unlocker
fetches for the specific pages that look most useful.

NOTE ON OUTPUT: findings are written to data/dgs/panini_osint/ and to the
terminal. Real individual names must NOT be committed to the repo as asserted
fact per CLAUDE.md (defamation risk). The ledger JSONL and JSON output are in
.gitignore scope — review locally before deciding what to include in any report.

Run:
    python -m src.dgs.panini_osint
    python -m src.dgs.panini_osint --budget 10 --json   # keep cost low, emit JSON
"""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

from src.bright_data.client import BrightDataClient, BudgetExceeded

OUT_DIR = Path("data/dgs/panini_osint")
OUT_DIR.mkdir(parents=True, exist_ok=True)

TARGET = "Panini Time"

# ── SERP queries: broad discovery first, then narrowing ─────────────────────

SERP_QUERIES = [
    # company identity
    f'"{TARGET}" California company',
    f'"{TARGET}" LLC OR Inc California',
    f'"{TARGET}" site:linkedin.com',
    f'"{TARGET}" site:facebook.com OR site:instagram.com OR site:twitter.com',
    # government contract context
    f'"{TARGET}" "Cal Fire" OR "CALFIRE" contract',
    f'"{TARGET}" California government contract procurement',
    f'"{TARGET}" site:sam.gov OR site:fpds.gov',
    # red-flag signals
    f'"{TARGET}" lawsuit OR litigation OR complaint OR violation',
    f'"{TARGET}" "secretary of state" OR "business license" California',
    # procurement officer angle (anonymized in output — find the connection, don't name)
    f'"{TARGET}" "purchase order" California 2025',
]

# ── URL patterns worth fetching once SERP surfaces them ─────────────────────

FETCH_PATTERNS = [
    re.compile(r"linkedin\.com/(company|in)/[^?#\s\"']+", re.IGNORECASE),
    re.compile(r"sam\.gov/[^\s\"']+", re.IGNORECASE),
    re.compile(r"fpds\.gov/[^\s\"']+", re.IGNORECASE),
    re.compile(r"opencorporates\.com/companies/us_ca/[^\s\"']+", re.IGNORECASE),
]

_URL_RE = re.compile(r'https?://[^\s"\'<>]+')


def _extract_urls(results: list[dict]) -> list[str]:
    urls = []
    for r in results:
        for field in ("link", "url", "displayed_link", "snippet"):
            v = r.get(field, "")
            if v and v.startswith("http"):
                urls.append(v)
            elif v:
                for m in _URL_RE.finditer(v):
                    urls.append(m.group(0))
    return list(dict.fromkeys(urls))  # dedupe, preserve order


def _interesting_url(url: str) -> bool:
    return any(p.search(url) for p in FETCH_PATTERNS)


def _summarize_html(html: str, max_chars: int = 1200) -> str:
    """Strip tags and collapse whitespace for a readable snippet."""
    stripped = re.sub(r"<[^>]+>", " ", html or "")
    stripped = re.sub(r"\s+", " ", stripped).strip()
    return stripped[:max_chars] + ("…" if len(stripped) > max_chars else "")


# ── Main sweep ───────────────────────────────────────────────────────────────

def run(budget: float = 15.0, emit_json: bool = False) -> dict:
    client = BrightDataClient(budget_cap=budget, label="panini_osint")

    serp_hits: list[dict] = []
    fetched_pages: list[dict] = []
    already_fetched: set[str] = set()

    print(f"=== Panini Time OSINT sweep ===")
    print(f"Budget: ${budget:.2f} | {len(SERP_QUERIES)} SERP queries\n")

    # ── Phase A: SERP ────────────────────────────────────────────────────────
    for i, q in enumerate(SERP_QUERIES, 1):
        try:
            res = client.serp(q)
        except BudgetExceeded as e:
            print(f"\n! Budget stop at SERP phase: {e}")
            break

        organic = res.get("organic") or []
        print(f"  [{i:02}/{len(SERP_QUERIES)}] {q[:70]}")
        print(f"         -> {len(organic)} results  |  {client.report()}")

        for r in organic[:5]:
            serp_hits.append({
                "query": q,
                "title": r.get("title", ""),
                "link": r.get("link", r.get("url", "")),
                "snippet": r.get("description", r.get("snippet", ""))[:300],
            })

        time.sleep(0.25)

    # ── Phase B: targeted fetches for high-signal URLs ───────────────────────
    interesting = [
        h["link"] for h in serp_hits
        if _interesting_url(h["link"]) and h["link"] not in already_fetched
    ]
    interesting = list(dict.fromkeys(interesting))[:12]  # cap at 12 fetches

    if interesting:
        print(f"\n  Fetching {len(interesting)} high-signal URL(s)...")
        for url in interesting:
            if url in already_fetched:
                continue
            try:
                resp = client.unlock(url, render_js=False)
            except BudgetExceeded as e:
                print(f"\n! Budget stop at fetch phase: {e}")
                break

            already_fetched.add(url)
            if resp.get("status") == 200 and resp.get("html"):
                summary = _summarize_html(resp["html"])
                fetched_pages.append({"url": url, "summary": summary})
                print(f"    [OK] {url[:70]}")
                print(f"      {summary[:120]}...")
            else:
                print(f"    [ERR] {url[:70]}  ({resp.get('status')} / {(resp.get('error') or '')[:60]})")
            time.sleep(0.4)

    # ── Write outputs ────────────────────────────────────────────────────────
    out = {
        "target": TARGET,
        "serp_hits": serp_hits,
        "fetched_pages": fetched_pages,
        "spend": client.spent,
    }

    (OUT_DIR / "raw_results.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    _write_digest(serp_hits, fetched_pages)

    print(f"\n{client.report()}")
    print(f"Raw results  -> {OUT_DIR}/raw_results.json")
    print(f"Digest       -> {OUT_DIR}/digest.md")

    if emit_json:
        print(json.dumps(out, indent=2))

    return out


def _write_digest(serp_hits: list[dict], fetched_pages: list[dict]):
    """Write a human-readable digest — OMIT any individual names per CLAUDE.md."""
    lines = [
        f"# {TARGET} — OSINT Digest\n",
        f"> All findings from public records / public web. Individual names",
        f"> have been redacted per project policy — review raw_results.json",
        f"> locally before including any names in a report.\n",
        "## SERP signal by query\n",
    ]
    seen_queries: dict[str, list] = {}
    for h in serp_hits:
        seen_queries.setdefault(h["query"], []).append(h)

    for q, hits in seen_queries.items():
        lines.append(f"### `{q}`")
        for h in hits:
            lines.append(f"- **{h['title']}**")
            if h.get("snippet"):
                lines.append(f"  {h['snippet'][:200]}")
            lines.append(f"  <{h['link']}>")
        lines.append("")

    if fetched_pages:
        lines += ["\n## Fetched page summaries\n"]
        for p in fetched_pages:
            lines.append(f"### {p['url']}")
            lines.append(p["summary"][:600])
            lines.append("")

    (OUT_DIR / "digest.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=float, default=15.0,
                    help="Bright Data spend cap for this run")
    ap.add_argument("--json", action="store_true", dest="emit_json",
                    help="also print full JSON to stdout")
    args = ap.parse_args()
    run(budget=args.budget, emit_json=args.emit_json)
