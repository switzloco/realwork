"""
Lightweight property-graph stored in SQLite.

Nodes are typed entities (VENDOR, PERSON, ADDRESS, AGENT). Edges are typed
relationships (REGISTERED_AT, OFFICER_OF, AGENT_OF, PAID_BY). Everything is
relational so the "Hydra" cluster query in hydra_query.py is plain SQL — no
graph engine required to keep it portable and zero-cost.

Identity / dedup strategy
-------------------------
Entities are keyed by a normalized natural key so that "Innive, Inc." and
"INNIVE INC" collapse to the same node, and "123 Main St Ste 400" matches
"123 MAIN STREET SUITE 400". Normalization lives in normalize_key(); it is the
single most important correctness lever in the whole pipeline — under-normalize
and real shell clusters stay invisible; over-normalize and you get false links.
"""

from __future__ import annotations

import re
import sqlite3
from pathlib import Path

GRAPH_DB_PATH = "graph.db"

# ---- key normalization -----------------------------------------------------

_CORP_SUFFIXES = re.compile(
    r"\b(incorporated|inc|corporation|corp|company|co|llc|l\.l\.c|llp|lp|"
    r"limited|ltd|holdings|group|enterprises|services|solutions)\b",
    re.IGNORECASE,
)
_STREET_WORDS = {
    "street": "st", "avenue": "ave", "boulevard": "blvd", "drive": "dr",
    "road": "rd", "lane": "ln", "suite": "ste", "floor": "fl", "unit": "ste",
    "#": "ste", "apartment": "ste", "apt": "ste",
}
_WS = re.compile(r"\s+")
_PUNCT = re.compile(r"[.,]")


def normalize_key(kind: str, raw: str) -> str:
    """Collapse cosmetic variants of an entity name/address to one stable key."""
    if not raw:
        return ""
    s = raw.lower().strip()
    s = _PUNCT.sub(" ", s)
    if kind == "ADDRESS":
        # canonicalize street-type words so suite numbers line up
        tokens = [_STREET_WORDS.get(t, t) for t in s.split()]
        s = " ".join(tokens)
    elif kind in ("VENDOR", "AGENT", "PERSON"):
        # strip corporate suffixes so the *entity* matches, not its wrapper
        s = _CORP_SUFFIXES.sub(" ", s)
    s = _WS.sub(" ", s).strip()
    return s


# ---- schema ----------------------------------------------------------------

SCHEMA = """
CREATE TABLE IF NOT EXISTS nodes (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    kind        TEXT NOT NULL,          -- VENDOR | PERSON | ADDRESS | AGENT
    key         TEXT NOT NULL,          -- normalized natural key
    label       TEXT NOT NULL,          -- original human-readable value
    attrs       TEXT,                   -- JSON blob of extra fields
    UNIQUE(kind, key)
);

CREATE TABLE IF NOT EXISTS edges (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    src         INTEGER NOT NULL,
    dst         INTEGER NOT NULL,
    rel         TEXT NOT NULL,          -- REGISTERED_AT | OFFICER_OF | AGENT_OF | PAID_BY
    attrs       TEXT,
    UNIQUE(src, dst, rel),
    FOREIGN KEY (src) REFERENCES nodes(id),
    FOREIGN KEY (dst) REFERENCES nodes(id)
);

-- denormalized payment facts, keyed to a vendor node, for the Hydra query
CREATE TABLE IF NOT EXISTS payments (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_id   INTEGER NOT NULL,
    department  TEXT,
    amount      REAL,
    pay_date    TEXT,
    fund        TEXT,
    raw         TEXT,
    FOREIGN KEY (vendor_id) REFERENCES nodes(id)
);

CREATE INDEX IF NOT EXISTS idx_nodes_kind_key ON nodes(kind, key);
CREATE INDEX IF NOT EXISTS idx_edges_dst_rel  ON edges(dst, rel);
CREATE INDEX IF NOT EXISTS idx_pay_vendor     ON payments(vendor_id);
"""


class GraphStore:
    def __init__(self, db_path: str = GRAPH_DB_PATH):
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)

    # -- nodes & edges -------------------------------------------------------

    def upsert_node(self, kind: str, label: str, attrs: str | None = None) -> int:
        """Get-or-create a node by (kind, normalized key). Returns node id."""
        key = normalize_key(kind, label)
        if not key:
            raise ValueError(f"empty key for {kind!r} label={label!r}")
        cur = self.conn.execute(
            "SELECT id FROM nodes WHERE kind=? AND key=?", (kind, key)
        )
        row = cur.fetchone()
        if row:
            if attrs:  # enrich existing node if we learned more
                self.conn.execute(
                    "UPDATE nodes SET attrs=COALESCE(attrs, ?) WHERE id=?",
                    (attrs, row["id"]),
                )
            return row["id"]
        cur = self.conn.execute(
            "INSERT INTO nodes(kind, key, label, attrs) VALUES (?,?,?,?)",
            (kind, key, label.strip(), attrs),
        )
        return cur.lastrowid

    def add_edge(self, src: int, dst: int, rel: str, attrs: str | None = None) -> None:
        self.conn.execute(
            "INSERT OR IGNORE INTO edges(src, dst, rel, attrs) VALUES (?,?,?,?)",
            (src, dst, rel, attrs),
        )

    def add_payment(self, vendor_id: int, department: str, amount: float,
                    pay_date: str = "", fund: str = "", raw: str = "") -> None:
        self.conn.execute(
            "INSERT INTO payments(vendor_id, department, amount, pay_date, fund, raw) "
            "VALUES (?,?,?,?,?,?)",
            (vendor_id, department, amount, pay_date, fund, raw),
        )

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.commit()
        self.conn.close()

    # -- convenience for a fully-resolved SoS record -------------------------

    def ingest_sos_record(self, rec: dict) -> int:
        """
        Wire one parsed Secretary-of-State record into the graph.

        rec keys (any may be missing/empty):
            vendor_name, incorporation_date, registered_agent,
            principal_officers (list[str]), address
        Returns the vendor node id.
        """
        import json

        vendor_attrs = json.dumps({
            "incorporation_date": rec.get("incorporation_date", ""),
            "source_state": rec.get("source_state", ""),
        })
        vid = self.upsert_node("VENDOR", rec["vendor_name"], vendor_attrs)

        addr = (rec.get("address") or "").strip()
        if addr:
            aid = self.upsert_node("ADDRESS", addr)
            self.add_edge(vid, aid, "REGISTERED_AT")

        agent = (rec.get("registered_agent") or "").strip()
        if agent:
            gid = self.upsert_node("AGENT", agent)
            self.add_edge(vid, gid, "AGENT_OF")

        for officer in rec.get("principal_officers", []) or []:
            officer = (officer or "").strip()
            if officer:
                pid = self.upsert_node("PERSON", officer)
                self.add_edge(pid, vid, "OFFICER_OF")

        return vid
