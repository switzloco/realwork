"""
Phase 4 — The "Hydra" analysis query.

Core thesis: find clusters of *distinct* vendor entities that
  (a) share the exact same Registered Agent OR physical suite/address, AND
  (b) each receive SEPARATE sub-threshold payments (< $50,000) FROM THE SAME
      city department.

That shape — one hidden hand (shared agent/address) collecting many just-under-
threshold payments from a single buyer — is the classic split/structured
procurement signature. This query surfaces candidates; it is NOT an accusation.
Every cluster is an "anomaly warranting investigation."

Run against a populated graph.db (Phases 2 + 3):
    python -m src.graph.hydra_query --threshold 50000 --min-vendors 2

Run the built-in demo (seeds a synthetic shell cluster + decoys, then queries):
    python -m src.graph.hydra_query --demo
"""

from __future__ import annotations

import argparse
import json

from src.graph.graph_store import GraphStore

HYDRA_SQL = """
WITH vendor_hub AS (
    -- a vendor connected to a shared hub node (its agent or its address)
    SELECT e.src AS vendor_id, n.id AS hub_id, n.kind AS hub_kind, n.label AS hub_label
    FROM edges e JOIN nodes n ON n.id = e.dst
    WHERE e.rel IN ('AGENT_OF', 'REGISTERED_AT')
),
sub_threshold AS (
    -- each vendor's sub-threshold payments, per department
    SELECT vendor_id, department,
           COUNT(*)  AS pay_count,
           SUM(amount) AS pay_total
    FROM payments
    WHERE amount < :threshold AND amount > 0
    GROUP BY vendor_id, department
)
SELECT
    vh.hub_kind,
    vh.hub_label,
    st.department,
    COUNT(DISTINCT vh.vendor_id)              AS vendor_count,
    GROUP_CONCAT(DISTINCT v.label)            AS vendors,
    SUM(st.pay_count)                         AS total_payments,
    SUM(st.pay_total)                         AS total_dollars
FROM vendor_hub vh
JOIN sub_threshold st ON st.vendor_id = vh.vendor_id
JOIN nodes v          ON v.id = vh.vendor_id
GROUP BY vh.hub_id, st.department
HAVING COUNT(DISTINCT vh.vendor_id) >= :min_vendors
ORDER BY total_dollars DESC
"""


def run_query(db_path: str = "graph.db", threshold: float = 50_000.0,
              min_vendors: int = 2) -> list[dict]:
    g = GraphStore(db_path)
    cur = g.conn.execute(
        HYDRA_SQL, {"threshold": threshold, "min_vendors": min_vendors}
    )
    clusters = [dict(r) for r in cur.fetchall()]
    g.close()
    return clusters


def print_clusters(clusters: list[dict], threshold: float):
    print(f"\n=== Phase 4: Hydra clusters (sub-${threshold:,.0f}, shared hub) ===")
    if not clusters:
        print("No clusters found.")
        return
    print(f"{len(clusters)} cluster(s) warranting investigation:\n")
    for i, c in enumerate(clusters, 1):
        vendors = (c["vendors"] or "").split(",")
        print(f"[{i}] Shared {c['hub_kind']}: {c['hub_label']}")
        print(f"    Department : {c['department']}")
        print(f"    Vendors    : {c['vendor_count']} distinct "
              f"({', '.join(v.strip() for v in vendors)})")
        print(f"    Payments   : {c['total_payments']} sub-threshold payments")
        print(f"    Dollars    : ${c['total_dollars']:,.2f}")
        print(f"    Signature  : {c['vendor_count']} vendors behind one "
              f"{c['hub_kind'].lower()}, all paid under threshold by one buyer\n")


# ---------------------------------------------------------------------------
# Demo: seed a synthetic shell cluster + clean decoys, then run the query.
# Proves the structuring signature is detected and normal vendors are ignored.
# ---------------------------------------------------------------------------

def _demo_seed(db_path: str):
    import os
    if os.path.exists(db_path):
        os.remove(db_path)
    g = GraphStore(db_path)

    SHARED_AGENT = "Acme Registered Agents LLC"
    DEPT = "Information Technology Agency"

    # cluster: 3 distinct vendors, same agent, all paid just under $50k by ITA
    for vname in ["Vega Systems Inc.", "Orion Data LLC", "Pleiades Tech Corp."]:
        g.ingest_sos_record({
            "vendor_name": vname,
            "registered_agent": SHARED_AGENT,
            "principal_officers": [],
            "address": "500 Shell Plaza Ste 900, Las Vegas, NV 89101",
            "source_state": "NV",
        })
    # payments (each vendor gets a couple sub-threshold hits from the same dept)
    for vname, amts in [
        ("Vega Systems Inc.", [49_500, 48_900]),
        ("Orion Data LLC", [49_950, 47_000]),
        ("Pleiades Tech Corp.", [49_000]),
    ]:
        vid = g.upsert_node("VENDOR", vname)
        for a in amts:
            g.add_payment(vid, DEPT, a, "2025-08-01", "General Fund")

    # decoy 1: a single legitimate vendor with a big above-threshold contract
    big = g.upsert_node("VENDOR", "Honest Engineering Co.")
    g.add_payment(big, DEPT, 1_200_000, "2025-07-01", "General Fund")

    # decoy 2: vendors sharing an agent but NO common department + above threshold
    for vname in ["Unrelated A Inc.", "Unrelated B LLC"]:
        g.ingest_sos_record({
            "vendor_name": vname,
            "registered_agent": "Different Agent Group",
            "principal_officers": [],
            "address": f"{vname} HQ, Sacramento, CA",
            "source_state": "CA",
        })
        vid = g.upsert_node("VENDOR", vname)
        g.add_payment(vid, "Public Works", 75_000, "2025-06-01", "Gas Tax")

    g.close()


def run_demo():
    db = "graph_demo.db"
    _demo_seed(db)
    clusters = run_query(db, threshold=50_000, min_vendors=2)
    print_clusters(clusters, 50_000)
    # The shell cluster surfaces via BOTH its shared agent and shared address —
    # both are legitimate detections of the same network. Assert that every
    # cluster is the 3-vendor ITA shell, and that no decoy vendor leaks in.
    decoys = {"Honest Engineering Co.", "Unrelated A Inc.", "Unrelated B LLC"}
    all_vendors = {v.strip() for c in clusters for v in (c["vendors"] or "").split(",")}
    ok = (
        len(clusters) >= 1
        and all(c["vendor_count"] == 3 for c in clusters)
        and all(c["department"] == "Information Technology Agency" for c in clusters)
        and not (all_vendors & decoys)
    )
    print(f"RESULT: {'PASS — structuring signature detected, decoys ignored' if ok else 'FAIL'}")
    return ok


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="graph.db")
    ap.add_argument("--threshold", type=float, default=50_000.0)
    ap.add_argument("--min-vendors", type=int, default=2)
    ap.add_argument("--demo", action="store_true", help="run self-contained demo")
    ap.add_argument("--json", action="store_true", help="emit clusters as JSON")
    args = ap.parse_args()

    if args.demo:
        raise SystemExit(0 if run_demo() else 1)

    clusters = run_query(args.db, args.threshold, args.min_vendors)
    if args.json:
        print(json.dumps(clusters, indent=2))
    else:
        print_clusters(clusters, args.threshold)
