"""
Parsers that turn raw Secretary-of-State responses into the flat record shape
graph_store.ingest_sos_record() expects:

    {
        "vendor_name": str,
        "incorporation_date": str,      # ISO-ish if we can get it
        "registered_agent": str,
        "principal_officers": [str],
        "address": str,
        "source_state": "CA" | "TX",
    }

CA's bizfileonline.sos.ca.gov is a single-page app backed by a JSON search API,
so the trawler usually hands us parsed JSON. TX (and CA HTML fallbacks) are
regex-scraped. Both paths normalize into the same dict so the graph layer never
has to know which state a record came from.
"""

from __future__ import annotations

import json
import re

_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")


def _clean(s: str) -> str:
    return _WS.sub(" ", _TAG.sub(" ", s or "")).strip()


# ---- CA: bizfileonline JSON ------------------------------------------------

def parse_ca_bizfile(payload) -> list[dict]:
    """
    Accepts the JSON returned by bizfileonline's search/detail endpoints
    (either a dict already, or a raw JSON string) and yields flat records.

    The endpoint nests entity detail under varying keys across versions, so we
    probe a small set of known field aliases rather than hard-coding one shape.
    """
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except json.JSONDecodeError:
            return parse_html_fallback(payload, source_state="CA")

    rows = []
    # search responses wrap hits under "rows" or "results"; detail is a bare obj
    hits = payload.get("rows") or payload.get("results") or [payload]
    for h in hits:
        agent = (
            _first(h, "agent", "registeredAgent", "AgentName", "agent_name")
            or _nested(h, "agent", "name")
        )
        officers = _officers(h)
        rows.append({
            "vendor_name": _first(h, "TITLE", "entityName", "name", "EntityName") or "",
            "incorporation_date": _first(
                h, "initialFilingDate", "registrationDate", "FilingDate",
                "incorporation_date",
            ) or "",
            "registered_agent": agent or "",
            "principal_officers": officers,
            "address": _address(h),
            "source_state": "CA",
        })
    return [r for r in rows if r["vendor_name"]]


def _first(d: dict, *keys):
    for k in keys:
        v = d.get(k)
        if v:
            return _clean(v) if isinstance(v, str) else v
    return None


def _nested(d: dict, *path):
    cur = d
    for p in path:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(p)
    return _clean(cur) if isinstance(cur, str) else cur


def _officers(h: dict) -> list[str]:
    raw = (
        h.get("principals") or h.get("officers") or h.get("Principals") or []
    )
    out = []
    for p in raw:
        if isinstance(p, dict):
            name = _first(p, "name", "Name", "fullName")
            if name:
                out.append(name)
        elif isinstance(p, str):
            out.append(_clean(p))
    return out


def _address(h: dict) -> str:
    a = h.get("address") or h.get("principalAddress") or h.get("mailingAddress")
    if isinstance(a, str):
        return _clean(a)
    if isinstance(a, dict):
        parts = [
            a.get("line1") or a.get("street") or "",
            a.get("line2") or a.get("suite") or "",
            a.get("city") or "",
            a.get("state") or "",
            a.get("zip") or a.get("postalCode") or "",
        ]
        return _clean(" ".join(p for p in parts if p))
    return ""


# ---- TX / generic HTML fallback --------------------------------------------

_LABELS = {
    "incorporation_date": [r"Registration Date", r"Formation Date", r"Filing Date"],
    "registered_agent": [r"Registered Agent", r"Agent Name"],
    "address": [r"Registered Office", r"Principal Office", r"Mailing Address"],
}


def parse_html_fallback(html: str, source_state: str = "TX",
                        vendor_name: str = "") -> list[dict]:
    """Best-effort label:value scrape for TX SOSDirect-style result pages."""
    text = _clean(html)
    rec = {
        "vendor_name": vendor_name,
        "incorporation_date": "",
        "registered_agent": "",
        "principal_officers": [],
        "address": "",
        "source_state": source_state,
    }
    for field, labels in _LABELS.items():
        for lab in labels:
            m = re.search(lab + r"\s*[:\-]?\s*([^|<]{3,80})", text, re.IGNORECASE)
            if m:
                rec[field] = m.group(1).strip(" :-")
                break
    # officers often appear as "Director: NAME" / "President: NAME"
    for m in re.finditer(
        r"(?:President|Director|Officer|Manager|Member)\s*[:\-]\s*([A-Z][A-Za-z .,'-]{3,60})",
        text,
    ):
        rec["principal_officers"].append(m.group(1).strip())
    return [rec] if rec["vendor_name"] else []
