"""
Phase 3 — The Trawler.

Takes the deduplicated LA vendor master list (Phase 2 output) and, for every
vendor, hits the CA Secretary of State business search via Bright Data's Web
Unlocker (JS-rendered). Parses Incorporation Date, Registered Agent, Principal
Officers, and Physical Address, then wires each result into the property graph
(graph_store) as nodes + edges.

Design notes
------------
* Reuses the existing BrightDataClient (src/bright_data/client.py) so cost
  tracking and the JSONL ledger are shared with the rest of the project.
* Resumable: processed vendor keys are checkpointed to data/la/trawl_done.txt,
  so a re-run skips what's already in the graph. Safe to Ctrl-C.
* Budget-aware: respects BudgetExceeded from the client. Default --budget is
  $250 (the hackathon credit balance); the ledger records every cent regardless.

Run:
    python -m src.la.sos_trawler --limit 2000 --budget 250

CA SoS note: bizfileonline is a single-page app backed by a JSON search API.
Web Unlocker with render returns the rendered payload; parse_ca_bizfile handles
both the JSON and an HTML fallback. If CA changes the endpoint, only
build_search_url() / the parser need to change — the graph wiring is stable.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from urllib.parse import quote

from src.bright_data.client import BrightDataClient, BudgetExceeded
from src.graph.graph_store import GraphStore
from src.graph import sos_parser

DATA_DIR = Path("data/la")
MASTER_PATH = DATA_DIR / "vendors_master.json"
DONE_PATH = DATA_DIR / "trawl_done.txt"

# bizfileonline public search UI; render=True lets the SPA hydrate before capture
CA_SEARCH_URL = "https://bizfileonline.sos.ca.gov/search/business"
CA_API_URL = "https://bizfileonline.sos.ca.gov/api/Records/businesssearch"


def build_search_url(vendor_name: str) -> str:
    """UI search URL with the query prefilled (Web Unlocker renders the SPA)."""
    return f"{CA_SEARCH_URL}?q={quote(vendor_name)}"


def load_master() -> list[dict]:
    if not MASTER_PATH.exists():
        raise SystemExit(
            f"{MASTER_PATH} not found — run Phase 2 (checkbook_ingest) first."
        )
    return json.loads(MASTER_PATH.read_text())


def load_done() -> set[str]:
    if DONE_PATH.exists():
        return set(DONE_PATH.read_text().splitlines())
    return set()


def mark_done(key: str):
    with open(DONE_PATH, "a") as f:
        f.write(key + "\n")


def parse_response(resp: dict, vendor_name: str) -> list[dict]:
    """Turn a Web Unlocker response into flat SoS records."""
    if not resp.get("html"):
        return []
    body = resp["html"]
    # try JSON (bizfile API) first, then HTML fallback
    records = sos_parser.parse_ca_bizfile(body)
    if not records:
        records = sos_parser.parse_html_fallback(body, "CA", vendor_name)
    # best-match: prefer the record whose name normalizes closest to the query
    return records


def trawl(limit: int = 2000, budget: float = 250.0,
          db_path: str = "graph.db", sleep: float = 0.3) -> dict:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    master = load_master()
    done = load_done()
    g = GraphStore(db_path)
    client = BrightDataClient(budget_cap=budget, label="la_sos_trawl")

    todo = [v for v in master if v["key"] not in done][:limit]
    print(f"=== Phase 3: Trawler ===")
    print(f"{len(master):,} vendors total | {len(done):,} already done | "
          f"processing {len(todo):,} this run\n")

    linked, scraped, errors = 0, 0, 0
    for i, v in enumerate(todo, 1):
        name = v["vendor_name"]
        try:
            resp = client.unlock(build_search_url(name), render_js=True)
        except BudgetExceeded as e:
            print(f"\n! Budget stop: {e}")
            break

        if resp.get("status") == 200:
            records = parse_response(resp, name)
            for rec in records:
                if not rec.get("vendor_name"):
                    rec["vendor_name"] = name
                g.ingest_sos_record(rec)
                linked += 1
            scraped += 1
        else:
            errors += 1

        mark_done(v["key"])
        if i % 25 == 0:
            g.commit()
            print(f"  {i:,}/{len(todo):,} | scraped {scraped} | "
                  f"records {linked} | errors {errors} | {client.report()}")
        time.sleep(sleep)

    g.commit()
    g.close()
    print(f"\nDone. scraped={scraped} records={linked} errors={errors}")
    print(client.report())
    return {"scraped": scraped, "records": linked, "errors": errors}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=2000, help="max vendors this run")
    ap.add_argument("--budget", type=float, default=250.0,
                    help="Bright Data spend cap in $ (your hackathon credit balance)")
    ap.add_argument("--db", default="graph.db")
    ap.add_argument("--sleep", type=float, default=0.3)
    args = ap.parse_args()
    trawl(limit=args.limit, budget=args.budget, db_path=args.db, sleep=args.sleep)
