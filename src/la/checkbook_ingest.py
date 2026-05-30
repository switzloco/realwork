"""
Phase 2 — Ingest the LA City "Checkbook" vendor-payment dataset (Socrata).

Endpoint: https://controllerdata.lacity.org/resource/pggv-e4fn.json

Pulls payment records in pages of $limit, loads the payment facts into the
graph's `payments` table (keyed to a VENDOR node), and writes a deduplicated
master vendor list to data/la/vendors_master.json for the Phase 3 trawler.

Uses raw requests (no sodapy dependency). If you have a Socrata app token, set
SOCRATA_APP_TOKEN in the env to raise rate limits — it works without one.

Run:
    python -m src.la.checkbook_ingest --max 100000
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

import requests

from src.graph.graph_store import GraphStore, normalize_key

ENDPOINT = "https://controllerdata.lacity.org/resource/pggv-e4fn.json"
OUT_DIR = Path("data/la")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Socrata column names on pggv-e4fn. Aliased defensively in case the dataset
# revisions rename fields — we probe each candidate in order.
COL_VENDOR = ["vendor_name", "vendor", "payee_name"]
COL_DEPT = ["department_name", "department", "dept_name"]
COL_AMOUNT = ["payment_amount", "amount", "check_amount"]
COL_DATE = ["payment_date", "check_date", "issue_date"]
COL_FUND = ["fund_name", "fund", "fund_description"]


def _pick(row: dict, candidates: list[str]) -> str:
    for c in candidates:
        if c in row and row[c] not in (None, ""):
            return str(row[c])
    return ""


def _to_float(s: str) -> float:
    try:
        return float(str(s).replace("$", "").replace(",", ""))
    except (ValueError, TypeError):
        return 0.0


def fetch_page(offset: int, limit: int, session: requests.Session) -> list[dict]:
    params = {
        "$limit": limit,
        "$offset": offset,
        "$order": ":id",   # stable pagination
    }
    token = os.environ.get("SOCRATA_APP_TOKEN")
    headers = {"X-App-Token": token} if token else {}
    r = session.get(ENDPOINT, params=params, headers=headers, timeout=60)
    r.raise_for_status()
    return r.json()


def ingest(max_records: int = 100_000, page: int = 5000,
           db_path: str = "graph.db") -> dict:
    g = GraphStore(db_path)
    session = requests.Session()

    seen_vendor_keys: dict[str, str] = {}   # normalized key -> original label
    total = 0
    offset = 0

    print(f"=== Phase 2: Checkbook LA ingest (target {max_records:,} records) ===")
    while total < max_records:
        limit = min(page, max_records - total)
        try:
            rows = fetch_page(offset, limit, session)
        except requests.HTTPError as e:
            print(f"  ! HTTP error at offset {offset}: {e}")
            break
        if not rows:
            print("  reached end of dataset")
            break

        for row in rows:
            vendor = _pick(row, COL_VENDOR).strip()
            if not vendor:
                continue
            key = normalize_key("VENDOR", vendor)
            if not key:
                continue
            seen_vendor_keys.setdefault(key, vendor)

            vid = g.upsert_node("VENDOR", vendor)
            g.add_payment(
                vendor_id=vid,
                department=_pick(row, COL_DEPT),
                amount=_to_float(_pick(row, COL_AMOUNT)),
                pay_date=_pick(row, COL_DATE),
                fund=_pick(row, COL_FUND),
                raw=json.dumps(row),
            )

        total += len(rows)
        offset += len(rows)
        g.commit()
        print(f"  ingested {total:,} payments | {len(seen_vendor_keys):,} unique vendors")
        time.sleep(0.2)  # be polite to the open-data portal

    # write the master vendor list for the trawler
    master = [{"key": k, "vendor_name": v} for k, v in sorted(seen_vendor_keys.items())]
    out_path = OUT_DIR / "vendors_master.json"
    out_path.write_text(json.dumps(master, indent=2))
    g.close()

    print(f"\nDone. {total:,} payments, {len(master):,} unique vendors.")
    print(f"Master vendor list -> {out_path}")
    return {"payments": total, "unique_vendors": len(master), "master_path": str(out_path)}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=100_000, help="max payment records to pull")
    ap.add_argument("--page", type=int, default=5000, help="page size ($limit)")
    ap.add_argument("--db", default="graph.db")
    args = ap.parse_args()
    ingest(max_records=args.max, page=args.page, db_path=args.db)
