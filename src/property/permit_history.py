"""
Permit-History Hunt — 137 Union Avenue, Unit E, Campbell CA (APN 412-14-028).

We believe an alteration was done to Unit E but we hold no documents and the
city plan files are gated. This module sweeps every source that holds Campbell
permit data and assembles a deduped TIMELINE of any recorded change to the unit
— even bare metadata (permit #, date, scope, contractor, status) is enough to
then demand the specific permit file from the city.

WHY THESE SOURCES:
  - MGO Connect (mgoconnect.org) is Campbell's actual permitting system. Its
    public search is the authoritative record but is a JS app, so it needs the
    Web Unlocker with render_js=True.
  - Permit aggregators (BuildZoom, Jaspector, PropertyShark, HelloData...)
    re-publish Campbell permits per address and are often the easiest to pull;
    they sometimes retain rows the city UI buries.
  - The Assessor parcel record carries an indirect signal: a permitted remodel
    usually triggers a base-year / "new construction" reassessment event.
  - The Clerk-Recorder can hold contractor mechanics' liens / NOCs — secondary
    evidence that work happened.

All these 403 plain fetchers, which is why we route through the shared Bright
Data client (SERP + Unlocker).

OUTPUT:
  data/property/permit_history_137E.json   — deduped timeline + ranked sources
  data/property/permit_raw/<slug>.html     — raw pages saved for review / LLM pass

USAGE (run locally where BRIGHT_DATA_API_KEY is set):
  python -m src.property.permit_history --budget 10
  python -m src.property.permit_history --budget 10 --resume
  python -m src.property.permit_history --no-unlock      # SERP discovery only
"""

import argparse
import json
import re
import time
from pathlib import Path

from src.bright_data.client import BrightDataClient, BudgetExceeded

APN = "412-14-028"
OUTPUT_DIR = Path("data/property")
RAW_DIR = OUTPUT_DIR / "permit_raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)
TIMELINE_PATH = OUTPUT_DIR / "permit_history_137E.json"

# Every spelling the various systems might store. We search them all, then
# filter results to ones that actually mention Unit E (or the APN).
ADDRESS_VARIANTS = [
    "137 Union Ave Unit E Campbell",
    "137 Union Avenue Unit E Campbell",
    "137 Union Av Unit E Campbell",
    "137 Union Ave E Campbell",
    "137 Union Avenue Campbell 95008",
    APN,
]

# SERP queries: find the aggregator/portal pages that hold permit rows.
PERMIT_QUERIES = [
    'site:buildzoom.com "137 Union" Campbell',
    'site:jaspector.com "137 Union" Campbell',
    'site:propertyshark.com "137 Union" Campbell',
    '"137 Union Ave" "Unit E" Campbell permit (remodel OR alteration OR kitchen OR bath OR wall)',
    '"137 Union Avenue" Campbell building permit history',
    f'"{APN}" Campbell permit OR building OR alteration',
    'mgoconnect.org "137 Union" OR "412-14-028" Campbell permit',
    '"137 Union" Campbell Unit E (mechanics lien OR "notice of completion" OR contractor)',
]

# Direct unlock entry points (JS apps / 403 sites).
SEED_UNLOCK = [
    ("mgo_search",  "https://www.mgoconnect.org/cp/search-permits", True),
    ("assessor",    "https://www.sccassessor.org/index.php/online-services/property-search/real-property", True),
]

# Relevance gate: a candidate page must actually refer to THIS parcel, or the
# SERP fills up with unrelated permit pages. Strong tokens are unambiguous.
STRONG_TOKENS = ["412-14-028", "412 14 028", "41214028", "137 union", "135 union"]


def is_relevant(text: str) -> bool:
    t = text.lower()
    if any(tok in t for tok in STRONG_TOKENS):
        return True
    # Campbell + Union Avenue together (avoids Union City / other Union Aves)
    return "campbell" in t and ("union ave" in t or "union avenue" in t)

# What a permit row tends to contain.
PERMIT_NUM_RE = re.compile(
    r"\b(?:BLD|PLN|BP|B|ME|PL|EL|PM|MEC|PLM|ELE)?[-/ ]?(?:19|20)?\d{2}[-/]?\d{3,6}\b",
    re.IGNORECASE,
)
DATE_RE = re.compile(r"\b(?:0?[1-9]|1[0-2])[/\-](?:0?[1-9]|[12]\d|3[01])[/\-](?:19|20)\d{2}\b")
SCOPE_TERMS = ["remodel", "alteration", "addition", "kitchen", "bath", "wall",
               "structural", "framing", "beam", "post", "interior", "tenant improvement",
               "demolition", "demo", "electrical", "plumbing", "mechanical", "reroof",
               "window", "deck", "foundation"]
UNIT_E_RE = re.compile(r"\bunit\s*e\b|\b137[\s\-]*e\b|\b137-e\b|412[\-\s]?14[\-\s]?028", re.IGNORECASE)


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:90]


def extract_permit_rows(text: str, source_url: str) -> list[dict]:
    """Heuristically pull candidate permit records out of page text.

    We don't try to perfectly parse each aggregator's layout — we surface
    every line that smells like a permit (has a date AND a scope term, or a
    permit-number token) so a human / LLM pass can confirm. Lines are also
    flagged for whether they reference Unit E specifically.
    """
    rows = []
    for raw_line in re.split(r"[\n\r]|<br\s*/?>", text):
        line = re.sub(r"<[^>]+>", " ", raw_line)          # strip tags
        line = re.sub(r"\s+", " ", line).strip()
        if len(line) < 8 or len(line) > 400:
            continue
        low = line.lower()
        has_date = bool(DATE_RE.search(line))
        scope_hits = [t for t in SCOPE_TERMS if t in low]
        has_permit_num = bool(PERMIT_NUM_RE.search(line)) and any(c.isdigit() for c in line)
        if (has_date and scope_hits) or (has_permit_num and scope_hits):
            rows.append({
                "line": line[:400],
                "date": (DATE_RE.search(line).group(0) if has_date else None),
                "permit_num": (PERMIT_NUM_RE.search(line).group(0) if has_permit_num else None),
                "scope_terms": scope_hits,
                "mentions_unit_e": bool(UNIT_E_RE.search(line)),
                "source": source_url,
            })
    return rows


def dedupe(rows: list[dict]) -> list[dict]:
    seen, out = set(), []
    for r in rows:
        key = (r.get("permit_num"), r.get("date"), r["line"][:60])
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    # Unit-E-specific and dated rows first
    out.sort(key=lambda r: (not r["mentions_unit_e"], r.get("date") is None, r.get("date") or ""))
    return out


def load_prev() -> dict:
    if TIMELINE_PATH.exists():
        with open(TIMELINE_PATH) as f:
            return json.load(f)
    return {}


def write_timeline(client, queries_done, candidate_urls, rows, pulled):
    deduped = dedupe(rows)
    unit_e = [r for r in deduped if r["mentions_unit_e"]]
    with open(TIMELINE_PATH, "w") as f:
        json.dump({
            "subject": "137 Union Ave Unit E, Campbell CA (APN 412-14-028)",
            "spent_usd": round(client.spent, 4),
            "queries_run": queries_done,
            "candidate_source_urls": candidate_urls,
            "pages_pulled": pulled,
            "timeline_all": deduped,
            "timeline_unit_e_only": unit_e,
            "summary": {
                "candidate_records": len(deduped),
                "unit_e_records": len(unit_e),
            },
            "next_actions": [
                "For any permit # found, request that permit's file from Campbell "
                "Building (408-866-2130) citing the # + APN 412-14-028 — far easier "
                "than a blind plan request.",
                "If a remodel permit exists, its plan set shows whether the post is "
                "structural; if NO permit exists, the work may be unpermitted (which "
                "is itself useful leverage / a safety flag).",
                "Authoritative source is MGO Connect — if the scrape is thin, run a "
                "manual search by APN at mgoconnect.org/cp/search-permits.",
            ],
        }, f, indent=2)
    return deduped, unit_e


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=float, default=10.0)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--no-unlock", action="store_true", help="SERP discovery only")
    ap.add_argument("--top-pull", type=int, default=10)
    ap.add_argument("--delay", type=float, default=0.5)
    args = ap.parse_args()

    prev = load_prev() if args.resume else {}
    queries_done = list(prev.get("queries_run", []))
    candidate_urls = prev.get("candidate_source_urls", [])
    rows = prev.get("timeline_all", [])
    pulled = prev.get("pages_pulled", [])
    seen_urls = {c["url"] for c in candidate_urls}
    pulled_urls = {p["url"] for p in pulled}

    client = BrightDataClient(budget_cap=args.budget, label="permit_history_137E")

    try:
        # --- Stage 1: discover source pages via SERP ---
        for q in PERMIT_QUERIES:
            if q in queries_done:
                continue
            res = client.serp(q)
            for o in res.get("organic", []):
                url = o.get("link", "")
                if not url or url in seen_urls:
                    continue
                blob = (o.get("title", "") + " " + o.get("description", "")
                        + " " + url).lower()
                # RELEVANCE GATE: must reference this parcel
                if not is_relevant(blob):
                    continue
                seen_urls.add(url)
                candidate_urls.append({
                    "url": url,
                    "title": o.get("title", ""),
                    "mentions_unit_e": bool(UNIT_E_RE.search(blob)),
                    "is_aggregator": any(d in url for d in
                        ("buildzoom", "jaspector", "propertyshark", "mgoconnect",
                         "hellodata", "permit")),
                })
            queries_done.append(q)
            print(f"[serp] {q[:54]:54s} -> {len(res.get('organic', []))} hits | {client.report()}")
            time.sleep(args.delay)

        # --- Stage 2: unlock the best source pages + seeds, extract rows ---
        if not args.no_unlock:
            ranked = sorted(candidate_urls,
                            key=lambda c: (not c["mentions_unit_e"], not c["is_aggregator"]))
            targets = [(s[0], s[1], s[2]) for s in SEED_UNLOCK]
            targets += [("source", c["url"], False) for c in ranked][:args.top_pull]

            for tag, url, render in targets:
                if url in pulled_urls:
                    continue
                r = client.unlock(url, render_js=render)
                if r.get("html"):
                    out = RAW_DIR / f"{tag}-{slug(url)}.html"
                    out.write_text(r["html"], errors="ignore")
                    new_rows = extract_permit_rows(r["html"], url)
                    rows.extend(new_rows)
                    pulled.append({"tag": tag, "url": url, "status": r["status"],
                                   "saved": str(out), "rows_found": len(new_rows)})
                    print(f"[pull] {url[:58]:58s} -> {len(new_rows)} rows | {client.report()}")
                else:
                    pulled.append({"tag": tag, "url": url, "status": r.get("status"),
                                   "error": r.get("error")})
                    print(f"[pull] {url[:58]:58s} -> FAILED {r.get('status')}")
                pulled_urls.add(url)
                time.sleep(args.delay)

    except BudgetExceeded as e:
        print(f"\n[!] {e}")
    except KeyboardInterrupt:
        print("\n[!] Interrupted — saving partial results")
    finally:
        deduped, unit_e = write_timeline(client, queries_done, candidate_urls, rows, pulled)
        print(f"\n{'='*66}")
        print(f"PERMIT HISTORY — 137 Union Ave Unit E — {client.report()}")
        print(f"  candidate records: {len(deduped)}   |   Unit-E-specific: {len(unit_e)}")
        if unit_e:
            print(f"\n  >>> UNIT E RECORDS:")
            for r in unit_e[:15]:
                print(f"   {r.get('date') or '    ?    '}  #{r.get('permit_num') or '—'}  "
                      f"{','.join(r['scope_terms'])[:30]:30s} {r['line'][:60]}")
        else:
            print("  (no Unit-E-specific rows yet — check timeline_all and the saved "
                  "MGO page; may need a manual APN search at mgoconnect.org)")
        print(f"\n  -> {TIMELINE_PATH}")
        print(f"{'='*66}")


if __name__ == "__main__":
    main()
