"""
Phase 1 — Control-group validation (true-positive test).

Goal: prove the graph-linking logic correctly connects two *distinct* vendor
entities that are in fact related, using a case that was publicly reported as a
procurement-steering matter (the LAUSD / Innive / Hexalytics indictment,
reported March 2026). If our logic can re-discover the link from registry-style
records, it will find unknown shell clusters in the LA Checkbook trawl.

IMPORTANT — read before trusting the output
--------------------------------------------
The registry details below (registered agent, officers, suite) are SYNTHETIC
placeholders that share a deliberate common link, NOT verified facts about real
people. Two reasons:
  1. Per the project's CLAUDE.md, we do not commit real individuals' names as
     asserted fact to a public repo (defamation risk).
  2. The purpose of this test is to validate the LINKING LOGIC, not to publish
     a claim about who the principals are.

To validate against the real case, run the live trawler (Phase 3) against these
two entity names with Bright Data creds set, drop the parsed records into
`fixture_records()` (or load them from a local, gitignored file), and re-run.
The assertion logic does not change.
"""

from __future__ import annotations

import sys

from src.graph.graph_store import GraphStore


def fixture_records() -> list[dict]:
    """
    Two distinct vendors that should resolve to the same cluster because they
    share a registered agent AND a physical suite. Swap these for real parsed
    SoS records to validate against the live case.
    """
    SHARED_AGENT = "Registered Agent Placeholder A"   # synthetic
    SHARED_SUITE = "100 Example Plaza Ste 1200, Austin, TX 78701"  # synthetic
    SHARED_OFFICER = "Principal Placeholder One"       # synthetic

    return [
        {
            "vendor_name": "Innive Inc.",
            "incorporation_date": "2015-06-01",
            "registered_agent": SHARED_AGENT,
            "principal_officers": [SHARED_OFFICER, "Principal Placeholder Two"],
            "address": "880 Example Way Ste 400, Irvine, CA 92618",
            "source_state": "CA",
        },
        {
            "vendor_name": "Hexalytics LLC",
            "incorporation_date": "2021-11-15",
            "registered_agent": SHARED_AGENT,           # <-- the link
            "principal_officers": [SHARED_OFFICER],      # <-- and the link
            "address": SHARED_SUITE,
            "source_state": "TX",
        },
        # a decoy: unrelated vendor that must NOT join the cluster
        {
            "vendor_name": "Unrelated Vendor Co.",
            "incorporation_date": "2010-01-01",
            "registered_agent": "Some Other Agent",
            "principal_officers": ["Nobody Relevant"],
            "address": "1 Decoy Rd, Sacramento, CA 95814",
            "source_state": "CA",
        },
    ]


def find_linked_vendors(g: GraphStore) -> list[tuple[str, str, str]]:
    """
    Return (vendorA, vendorB, shared_node_label) for every pair of distinct
    vendors connected through a shared AGENT or PERSON node. This is the same
    join the Hydra query uses, scoped to relationship-sharing only.
    """
    sql = """
    WITH vendor_links AS (
        -- vendor -> shared AGENT
        SELECT e.src AS vendor_id, n.id AS hub_id, n.kind AS hub_kind, n.label AS hub
        FROM edges e JOIN nodes n ON n.id = e.dst
        WHERE e.rel = 'AGENT_OF'
        UNION ALL
        -- vendor <- shared PERSON (officer)
        SELECT e.dst AS vendor_id, n.id AS hub_id, n.kind AS hub_kind, n.label AS hub
        FROM edges e JOIN nodes n ON n.id = e.src
        WHERE e.rel = 'OFFICER_OF'
    )
    SELECT v1.label AS vendor_a, v2.label AS vendor_b,
           vl1.hub_kind || ': ' || vl1.hub AS shared
    FROM vendor_links vl1
    JOIN vendor_links vl2
      ON vl1.hub_id = vl2.hub_id AND vl1.vendor_id < vl2.vendor_id
    JOIN nodes v1 ON v1.id = vl1.vendor_id
    JOIN nodes v2 ON v2.id = vl2.vendor_id
    GROUP BY vendor_a, vendor_b, shared
    """
    return [(r["vendor_a"], r["vendor_b"], r["shared"])
            for r in g.conn.execute(sql)]


def run(db_path: str = "graph_control.db") -> bool:
    import os
    if os.path.exists(db_path):
        os.remove(db_path)  # fresh control DB each run

    g = GraphStore(db_path)
    for rec in fixture_records():
        g.ingest_sos_record(rec)
    g.commit()

    links = find_linked_vendors(g)

    print("=== Phase 1: Control-group validation ===")
    print(f"Ingested {len(fixture_records())} vendor records into {db_path}\n")
    if links:
        print("Linked vendor pairs discovered:")
        for a, b, shared in links:
            print(f"  • {a}  <—>  {b}   (via {shared})")
    else:
        print("No links found.")

    # assertions: the two related vendors must link; the decoy must not
    pairs = {frozenset((a, b)) for a, b, _ in links}
    target = frozenset(("Innive Inc.", "Hexalytics LLC"))
    decoy_clean = all("Unrelated Vendor Co." not in p for p in pairs)

    ok = target in pairs and decoy_clean
    print()
    print(f"  [{'PASS' if target in pairs else 'FAIL'}] Innive <-> Hexalytics linked")
    print(f"  [{'PASS' if decoy_clean else 'FAIL'}] decoy vendor correctly excluded")
    print(f"\nRESULT: {'PASS — graph logic validated' if ok else 'FAIL'}")
    g.close()
    return ok


if __name__ == "__main__":
    sys.exit(0 if run() else 1)
