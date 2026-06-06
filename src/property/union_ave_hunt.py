"""
Union Ave Plan Hunt — single-parcel, exhaustive search for the original 1983
building plans of 135 Union Avenue (our unit: 137 Union Ave Unit E, Campbell,
CA 95008), architect Michael Moyer / Union Avenue Associates, plus any later
alteration plans for Unit E.

This is a PERSONAL property-records hunt, not a fraud-pipeline run. It reuses
the shared Bright Data client (SERP + Web Unlocker) only because those are the
tools that punch through the 403s these government / directory sites throw at
plain fetchers.

WHY A SCRAPER CAN'T JUST "FIND THE DRAWINGS":
    1983 architectural sheets are not on the open web. The stamped plans live
    only as digitized microfiche inside Campbell's internal system
    (we have a handle: "Union 135", filename 11512). California Health & Safety
    Code 19851 forbids the city from *copying* them without written permission
    from (a) the licensed professional who stamped them — Moyer / successor —
    and (b) the owner or, for a condo (common-interest development), the HOA.

    So the scraper's real job is to FEED the official request:
      - pin down the parcel / APN and the recorded condominium plan
        (the condo plan itself is public at the Recorder and may show the
         unit's structural walls outright — possibly answering the post
         question with no microfiche at all),
      - locate Michael Moyer's current firm + CA architect license so the
        city's mandated certified letter to him actually resolves,
      - sweep every secondary representation of the floor plan (prior Unit E
        remodel permits, MLS/listing floor plans, Sanborn maps).

OUTPUT:
    data/property/union_ave_findings.json   — ranked hits + what to pull next
    data/property/<slug>.<ext>              — any PDFs/docs retrieved for review
    data/bright_data/union_ave_hunt_ledger.jsonl  — cost ledger (via client)

USAGE (run locally where BRIGHT_DATA_API_KEY is set):
    python -m src.property.union_ave_hunt --budget 15
    python -m src.property.union_ave_hunt --budget 15 --resume
    python -m src.property.union_ave_hunt --no-unlock     # SERP discovery only
"""

import argparse
import json
import re
import time
from pathlib import Path

from src.bright_data.client import BrightDataClient, BudgetExceeded

# --- Subject facts ---------------------------------------------------------
SUBJECT = {
    "complex_address": "135 Union Avenue, Campbell, CA 95008",
    "unit_address": "137 Union Avenue Unit E, Campbell, CA 95008",
    "apn": "412-14-028",               # Santa Clara County Assessor parcel number
    "grant_deed_doc": "22684526",      # 2014 purchase deed (ownership proof for 19851)
    "architect": "Michael Moyer",
    "developer": "Union Avenue Associates",
    "year": "1983",
    "microfiche_handle": "Union 135 / filename 11512",  # city planning index handle
    "building": "Building 4",          # Unit E sits in Building 4 of the complex
    "unit_plan_type": "B",             # Unit E is built to the "Plan B" layout type
    "have_already": "NOTHING — we know the designation (Building 4, Plan B) but "
                    "hold no drawing. Target = obtain the Plan B sheet for Bldg 4.",
}

OUTPUT_DIR = Path("data/property")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
FINDINGS_PATH = OUTPUT_DIR / "union_ave_findings.json"

# --- Discovery queries -----------------------------------------------------
# (tag, query). Tags drive how hits are scored in classify().
QUERY_TEMPLATES = [
    # Stage A: identifier resolution (parcel / recorded condo plan)
    ("parcel",      '"412-14-028" Santa Clara recorder condominium plan'),
    ("parcel",      '"137 Union Avenue" Campbell APN assessor parcel'),
    ("parcel",      '"135 Union Avenue" Campbell condominium plan recorded map'),
    ("condo_plan",  '"Union Avenue" Campbell condominium plan 1983 tract subdivision map'),
    ("permits",     '"137 Union" OR "135 Union" Campbell building permit history remodel'),
    ("permits",     'Campbell CA "Unit E" "Union Avenue" remodel alteration permit'),
    ("building4",   '"Union Avenue" Campbell "Building 4" condominium plan structural sheets'),

    # Stage B: architect / 19851 permission target
    ("architect",   '"Michael Moyer" architect California license Campbell OR "Palo Alto" OR "Mill Valley"'),
    ("architect",   '"Michael D. Moyer" OR "Moyer Associates" architect license number contact'),
    ("architect",   '"Union Avenue Associates" Campbell 1983 developer architect'),

    # Stage C: secondary representations of the floor plan
    ("floorplan",   '"137 Union Avenue" Unit E Campbell floor plan zillow OR redfin'),
    ("floorplan",   '"135 Union Avenue" Campbell condo floor plan listing'),
    ("microfiche",  'Campbell CA planning microfiche "11512" OR "Union 135" records'),
    ("portal",      'Campbell CA building records online portal laserfiche permit document search'),
]

# --- Direct unlock targets (sites that 403 plain fetchers) -----------------
# These are landing pages / search entry points worth pulling HTML from so we
# can read their actual form actions and result links.
SEED_UNLOCK_TARGETS = [
    ("cab_license",  "https://www.cab.ca.gov/cons/archs/lic_search.shtml"),
    ("assessor",     "https://www.sccassessor.org/index.php/online-services/property-search/real-property"),
    ("recorder",     "https://clerkrecorder.santaclaracounty.gov/services/search-assessor-property-address"),
    ("campbell_recs","https://www.campbellca.gov/1140/Online-Services"),
    ("campbell_docs","https://www.campbellca.gov/206/Documents"),
]

# Signals that a retrieved doc/link is likely to BE (or point to) the plans.
PLAN_TERMS = ["floor plan", "floorplan", "site plan", "elevation", "structural",
              "framing", "foundation", "as-built", "blueprint", "drawing sheet",
              "condominium plan", "condo plan", "load bearing", "load-bearing"]
DOC_EXTS = (".pdf", ".tif", ".tiff", ".png", ".jpg", ".jpeg")


def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:80]


def score_link(organic: dict, tag: str) -> dict:
    """Score a single SERP organic result for how worth-pulling it is."""
    text = (organic.get("title", "") + " " + organic.get("description", "")).lower()
    link = organic.get("link", "")
    plan_hits = [t for t in PLAN_TERMS if t in text]
    is_doc = link.lower().endswith(DOC_EXTS)
    gov = any(d in link for d in ("santaclara", "campbellca.gov", ".gov", "cab.ca.gov"))
    # priority: documents and plan-term gov pages first
    priority = (2 if is_doc else 0) + (2 if plan_hits else 0) + (1 if gov else 0)
    return {
        "tag": tag,
        "title": organic.get("title", ""),
        "url": link,
        "snippet": organic.get("description", "")[:300],
        "plan_terms": plan_hits,
        "is_document": is_doc,
        "gov_source": gov,
        "priority": priority,
    }


def load_existing() -> dict:
    if FINDINGS_PATH.exists():
        with open(FINDINGS_PATH) as f:
            return json.load(f)
    return {}


def write_findings(client, queries_done, links, pulled):
    with open(FINDINGS_PATH, "w") as f:
        json.dump({
            "subject": SUBJECT,
            "spent_usd": round(client.spent, 4),
            "budget_cap": client.budget_cap,
            "queries_run": queries_done,
            "links_ranked": sorted(links, key=lambda x: -x["priority"]),
            "documents_pulled": pulled,
            "next_actions": [
                "Confirm Michael Moyer current firm + CA architect license # "
                "(needed for the city's 19851 certified letter).",
                "Pull the recorded condominium plan from the SCC Recorder — it "
                "may show Unit E structural walls directly.",
                "File Campbell plan-duplication affidavit citing handle "
                + SUBJECT["microfiche_handle"] + ".",
                "Have a licensed structural engineer confirm load-bearing status "
                "on site (definitive, and required for any permit).",
            ],
        }, f, indent=2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=float, default=15.0, help="Max spend in USD")
    ap.add_argument("--resume", action="store_true", help="Skip queries already run")
    ap.add_argument("--no-unlock", action="store_true",
                    help="SERP discovery only; skip pulling pages/PDFs")
    ap.add_argument("--top-pull", type=int, default=12,
                    help="Max number of top-priority links to unlock/fetch")
    ap.add_argument("--delay", type=float, default=0.5)
    args = ap.parse_args()

    prev = load_existing() if args.resume else {}
    done_queries = set(prev.get("queries_run", []))
    ranked_links = prev.get("links_ranked", [])
    pulled = prev.get("documents_pulled", [])
    seen_urls = {l["url"] for l in ranked_links}

    client = BrightDataClient(budget_cap=args.budget, label="union_ave_hunt")
    queries_done = list(done_queries)

    try:
        # --- Stage 1: SERP discovery ---
        for tag, query in QUERY_TEMPLATES:
            if query in done_queries:
                continue
            res = client.serp(query)
            for organic in res.get("organic", []):
                scored = score_link(organic, tag)
                if scored["url"] and scored["url"] not in seen_urls:
                    seen_urls.add(scored["url"])
                    ranked_links.append(scored)
            queries_done.append(query)
            print(f"[serp:{tag}] {query[:50]:50s} -> "
                  f"{len(res.get('organic', []))} hits | {client.report()}")
            time.sleep(args.delay)

        # --- Stage 2: unlock high-priority pages + the seed gov targets ---
        if not args.no_unlock:
            targets = [(t, u) for (t, u) in SEED_UNLOCK_TARGETS] + [
                (l["tag"], l["url"])
                for l in sorted(ranked_links, key=lambda x: -x["priority"])
                if l["priority"] >= 2
            ][:args.top_pull]

            done_pull_urls = {p["url"] for p in pulled}
            for tag, url in targets:
                if url in done_pull_urls:
                    continue
                is_doc = url.lower().endswith(DOC_EXTS)
                if is_doc:
                    r = client.fetch_bytes(url, render_js=False)
                    if r.get("content"):
                        ext = Path(url.split("?")[0]).suffix or ".bin"
                        out = OUTPUT_DIR / f"{tag}-{slugify(url)}{ext}"
                        out.write_bytes(r["content"])
                        pulled.append({"tag": tag, "url": url,
                                       "saved": str(out), "status": r["status"]})
                        print(f"[doc:{tag}] saved {out.name} | {client.report()}")
                    else:
                        pulled.append({"tag": tag, "url": url,
                                       "status": r.get("status"), "error": r.get("error")})
                else:
                    r = client.unlock(url, render_js=True)
                    if r.get("html"):
                        out = OUTPUT_DIR / f"{tag}-{slugify(url)}.html"
                        out.write_text(r["html"], errors="ignore")
                        pulled.append({"tag": tag, "url": url,
                                       "saved": str(out), "status": r["status"]})
                        print(f"[html:{tag}] saved {out.name} | {client.report()}")
                    else:
                        pulled.append({"tag": tag, "url": url,
                                       "status": r.get("status"), "error": r.get("error")})
                done_pull_urls.add(url)
                time.sleep(args.delay)

    except BudgetExceeded as e:
        print(f"\n[!] {e}")
    except KeyboardInterrupt:
        print("\n[!] Interrupted — saving partial results")
    finally:
        write_findings(client, queries_done, ranked_links, pulled)
        print(f"\n{'='*64}")
        print(f"UNION AVE HUNT — {client.report()}")
        print(f"  links ranked:     {len(ranked_links)}")
        print(f"  documents pulled: {len([p for p in pulled if p.get('saved')])}")
        top = sorted(ranked_links, key=lambda x: -x["priority"])[:8]
        print(f"\n  Top leads to review:")
        for l in top:
            flag = "DOC" if l["is_document"] else ("PLAN" if l["plan_terms"] else "   ")
            print(f"   [{flag}] p{l['priority']} {l['title'][:48]:48s} {l['url'][:60]}")
        print(f"\n  -> {FINDINGS_PATH}")
        print(f"{'='*64}")


if __name__ == "__main__":
    main()
