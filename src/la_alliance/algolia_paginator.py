"""
Algolia index paginator — break past the 1,000-hit ceiling by facet-splitting.

The problem
-----------
The LA Alliance invoicing portal (ceo.lacounty.gov/homeless-initiative/
alliance-invoicing) is backed by an Algolia index. A single Algolia query
returns at most `paginationLimitedTo` hits — 1,000 by default. That's why the
raw dump we scraped (`_alliance_index_dump.json`) capped at exactly 1,000 and
left ~600 documents unreachable. Plain page/hitsPerPage pagination can't help:
the 1,000 IS the ceiling.

The workaround
--------------
The cap is per *query*, not per *index*. If we issue one query per facet value
(here: sds_service_type — 7 values, largest ~259 records), every sub-query
returns well under 1,000, and the union covers the entire index. We dedupe by
objectID and write a manifest the invoice_extractor consumes directly.

Credentials (read-only, safe — these are public search keys baked into the
site's JS; grab them from the browser Network tab on a search request):
    ALGOLIA_APP_ID
    ALGOLIA_SEARCH_KEY
    ALGOLIA_INDEX_NAME

Run:
    export ALGOLIA_APP_ID=... ALGOLIA_SEARCH_KEY=... ALGOLIA_INDEX_NAME=...
    python -m src.la_alliance.algolia_paginator
    # -> data/la_alliance/manifest_full.json   (feed to invoice_extractor)

    python -m src.la_alliance.invoice_extractor \
        --manifest data/la_alliance/manifest_full.json --limit 2000
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import requests

OUT_DIR = Path("data/la_alliance")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Facet we split on. Each value's count is < 1,000, so each query is complete.
FACET = "sds_service_type"

# Fallback facet values observed in the original 1,000-hit dump. The script
# also auto-discovers facet values from the index, so this is just a safety net.
KNOWN_FACET_VALUES = [
    "High Service Need Interim Housing Beds",
    "Substance Use Disorder Beds",
    "Supportive Services in Permanent Housing",
    "Mental Health Beds",
    "Multi-Disciplinary Teams",
    "Enriched Residential Care Beds",
    "",  # blank service type — 10 docs in the dump had this
]


def _endpoint(app_id: str) -> str:
    return f"https://{app_id}-dsn.algolia.net/1/indexes/{{index}}/query"


def _headers(app_id: str, key: str) -> dict:
    return {
        "X-Algolia-Application-Id": app_id,
        "X-Algolia-API-Key": key,
        "Content-Type": "application/json",
    }


def _query(app_id: str, key: str, index: str, body: dict) -> dict:
    url = _endpoint(app_id).format(index=index)
    r = requests.post(url, headers=_headers(app_id, key), json=body, timeout=60)
    r.raise_for_status()
    return r.json()


def discover_facet_values(app_id: str, key: str, index: str) -> list[str]:
    """Ask Algolia for the full set of values for FACET (not hit-capped)."""
    res = _query(app_id, key, index, {
        "query": "",
        "hitsPerPage": 0,
        "facets": [FACET],
        "maxValuesPerFacet": 1000,
    })
    facets = (res.get("facets") or {}).get(FACET, {})
    values = list(facets.keys())
    # Algolia omits the empty-string facet from facet counts; keep our blank too.
    if "" not in values:
        values.append("")
    print(f"  discovered {len(values)} facet value(s) for {FACET}")
    for v, c in sorted(facets.items(), key=lambda kv: -kv[1]):
        print(f"    {c:5}  {v or '(blank)'}")
    return values or KNOWN_FACET_VALUES


def fetch_facet(app_id: str, key: str, index: str, value: str) -> list[dict]:
    """Page through a single facet value (each is < 1,000, so one page suffices,
    but we page defensively in case a value ever exceeds the cap)."""
    hits: list[dict] = []
    page = 0
    while True:
        body = {
            "query": "",
            "hitsPerPage": 1000,
            "page": page,
            "facetFilters": [[f"{FACET}:{value}"]],
        }
        res = _query(app_id, key, index, body)
        batch = res.get("hits") or []
        hits.extend(batch)
        nb_pages = res.get("nbPages", 1)
        label = value or "(blank)"
        print(f"    [{label}] page {page+1}/{nb_pages} -> +{len(batch)} (total {len(hits)})")
        page += 1
        if page >= nb_pages or not batch:
            break
    return hits


def run(app_id: str = "", key: str = "", index: str = "",
        merge_dump: bool = True) -> dict:
    app_id = app_id or os.environ.get("ALGOLIA_APP_ID", "")
    # Accept either name; this is a READ-only search key by design.
    key = key or os.environ.get("ALGOLIA_SEARCH_KEY") \
        or os.environ.get("ALGOLIA_SEARCH_API_KEY", "")
    index = index or os.environ.get("ALGOLIA_INDEX_NAME") \
        or os.environ.get("ALGOLIA_INDEX", "")

    # Safety: never operate with a write/admin key. Pagination is read-only;
    # a write key here would be a needless tamper risk against a public index.
    write_key = os.environ.get("ALGOLIA_WRITE_API_KEY") \
        or os.environ.get("ALGOLIA_WRITE_KEY", "")
    if key and write_key and key == write_key:
        raise SystemExit(
            "Refusing to run: the supplied key matches ALGOLIA_WRITE_API_KEY. "
            "Use the read-only SEARCH key only."
        )

    if not (app_id and key and index):
        raise SystemExit(
            "Need ALGOLIA_APP_ID, ALGOLIA_SEARCH_KEY, ALGOLIA_INDEX_NAME "
            "(env or --app-id/--key/--index). Grab them from the browser "
            "Network tab on any search request at the alliance-invoicing portal."
        )

    print("=== Algolia facet-split paginator ===")
    print(f"App: {app_id} | Index: {index} | Facet: {FACET}\n")

    try:
        values = discover_facet_values(app_id, key, index)
    except Exception as e:
        print(f"  facet discovery failed ({e}); using known values")
        values = KNOWN_FACET_VALUES

    by_id: dict[str, dict] = {}

    # Seed with whatever we already scraped, so we keep prior coverage.
    if merge_dump:
        dump = OUT_DIR / "raw" / "_alliance_index_dump.json"
        if dump.exists():
            prior = json.loads(dump.read_text())
            for h in prior:
                oid = h.get("objectID") or h.get("sds_published_url")
                if oid:
                    by_id[oid] = h
            print(f"  seeded {len(by_id)} record(s) from existing dump\n")

    for value in values:
        try:
            for h in fetch_facet(app_id, key, index, value):
                oid = h.get("objectID") or h.get("sds_published_url")
                if oid:
                    by_id[oid] = h
        except Exception as e:
            print(f"    ! facet '{value or '(blank)'}' failed: {e}")

    records = list(by_id.values())
    out_path = OUT_DIR / "manifest_full.json"
    out_path.write_text(json.dumps(records, indent=2))

    print(f"\nTotal unique documents: {len(records)}")
    print(f"Manifest -> {out_path}")
    print("Next: python -m src.la_alliance.invoice_extractor "
          f"--manifest {out_path} --limit {len(records)}")
    return {"count": len(records), "manifest": str(out_path)}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--app-id", default="")
    ap.add_argument("--key", default="")
    ap.add_argument("--index", default="")
    ap.add_argument("--no-merge", action="store_true",
                    help="don't seed from the existing _alliance_index_dump.json")
    args = ap.parse_args()
    run(app_id=args.app_id, key=args.key, index=args.index,
        merge_dump=not args.no_merge)
