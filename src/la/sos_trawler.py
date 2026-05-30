"""
Phase 3 — The Trawler.

Takes the deduplicated LA vendor master list (Phase 2 output) and, for every
vendor, looks up the entity on OpenCorporates (us_ca jurisdiction) via Bright
Data Web Unlocker. Extracts Incorporation Date, Registered Agent, Principal
Officers, and Physical Address, then wires each result into the property graph
as nodes + edges.

Why OpenCorporates instead of CA SoS directly:
  Bright Data's platform blocks bizfileonline.sos.ca.gov (government-site
  policy). OpenCorporates mirrors the same CA registry data and is a
  legitimate scraping target. Two requests per vendor: search → detail.

Design notes
------------
* Reuses BrightDataClient (src/bright_data/client.py) — cost tracking and
  JSONL ledger shared with the rest of the project.
* Resumable: processed vendor keys checkpointed to data/la/trawl_done.txt.
  Safe to Ctrl-C and resume.
* Budget-aware: BudgetExceeded from the client halts the loop cleanly.
* render_js=False: OpenCorporates is server-rendered, plain Web Unlocker
  suffices (cheaper and faster than JS rendering).

Run:
    python -m src.la.sos_trawler --limit 2000 --budget 250
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

OC_SEARCH_URL = "https://opencorporates.com/companies"
OC_BASE_URL = "https://opencorporates.com"


def build_search_url(vendor_name: str) -> str:
    return f"{OC_SEARCH_URL}?q={quote(vendor_name)}&jurisdiction_code=us_ca"


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


def fetch_vendor(name: str, client: BrightDataClient,
                 sleep: float) -> list[dict]:
    """Two-step fetch: search page → detail page → parsed records.

    Returns empty list if nothing useful comes back. Raises BudgetExceeded
    upward so the outer loop can stop cleanly.
    """
    # Step 1: search
    search_resp = client.unlock(build_search_url(name), render_js=False)
    time.sleep(sleep)

    if search_resp.get("status") != 200 or not search_resp.get("html"):
        return []

    detail_path = sos_parser.parse_opencorporates_search(search_resp["html"])
    if not detail_path:
        # no CA match found — vendor may not be incorporated in CA
        return sos_parser.parse_html_fallback(search_resp["html"], "CA", name)

    # Step 2: detail page
    detail_resp = client.unlock(
        f"{OC_BASE_URL}{detail_path}", render_js=False
    )
    time.sleep(sleep)

    if detail_resp.get("status") != 200 or not detail_resp.get("html"):
        return []

    records = sos_parser.parse_opencorporates_detail(detail_resp["html"], name)
    return records


def trawl(limit: int = 2000, budget: float = 250.0,
          db_path: str = "graph.db", sleep: float = 0.3) -> dict:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    master = load_master()
    done = load_done()
    g = GraphStore(db_path)
    client = BrightDataClient(budget_cap=budget, label="la_sos_trawl")

    todo = [v for v in master if v["key"] not in done][:limit]
    print("=== Phase 3: Trawler (OpenCorporates) ===")
    print(f"{len(master):,} vendors total | {len(done):,} already done | "
          f"processing {len(todo):,} this run\n")

    linked, scraped, errors = 0, 0, 0
    for i, v in enumerate(todo, 1):
        name = v["vendor_name"]
        try:
            records = fetch_vendor(name, client, sleep)
        except BudgetExceeded as e:
            print(f"\n! Budget stop: {e}")
            break

        for rec in records:
            if not rec.get("vendor_name"):
                rec["vendor_name"] = name
            g.ingest_sos_record(rec)
            linked += 1

        if records:
            scraped += 1
        else:
            errors += 1

        mark_done(v["key"])
        if i % 25 == 0:
            g.commit()
            print(f"  {i:,}/{len(todo):,} | scraped {scraped} | "
                  f"records {linked} | errors {errors} | {client.report()}")

    g.commit()
    g.close()
    print(f"\nDone. scraped={scraped} records={linked} errors={errors}")
    print(client.report())
    return {"scraped": scraped, "records": linked, "errors": errors}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=2000,
                    help="max vendors this run")
    ap.add_argument("--budget", type=float, default=250.0,
                    help="Bright Data spend cap in $ (your hackathon credit balance)")
    ap.add_argument("--db", default="graph.db")
    ap.add_argument("--sleep", type=float, default=0.3)
    args = ap.parse_args()
    trawl(limit=args.limit, budget=args.budget, db_path=args.db,
          sleep=args.sleep)
