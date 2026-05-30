"""
Parsers that turn raw registry responses into the flat record shape
graph_store.ingest_sos_record() expects:

    {
        "vendor_name": str,
        "incorporation_date": str,      # ISO-ish if we can get it
        "registered_agent": str,
        "principal_officers": [str],
        "address": str,
        "source_state": "CA" | "TX",
    }

Sources supported:
  - CA bizfileonline JSON (parse_ca_bizfile)
  - OpenCorporates HTML — search page (parse_opencorporates_search) +
    detail page (parse_opencorporates_detail)
  - TX SOSDirect / generic HTML fallback (parse_html_fallback)

CA SoS is blocked by Bright Data's government-site policy; OpenCorporates
mirrors the same registry data and is the primary Phase 3 source.
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


# ---- OpenCorporates HTML ---------------------------------------------------
# Two-step: search page gives us the detail URL; detail page gives us fields.
# OC is server-rendered — no render_js needed, plain Web Unlocker works.

_OC_DETAIL_LINK = re.compile(r'href="(/companies/us_ca/[A-Z0-9]+)"', re.IGNORECASE)
_OC_DT_DD = re.compile(
    r"<dt[^>]*>\s*(.*?)\s*</dt>\s*<dd[^>]*>\s*(.*?)\s*</dd>",
    re.DOTALL | re.IGNORECASE,
)
_OC_OFFICER_LINK = re.compile(
    r'href="/officers/[^"]*"[^>]*>\s*([^<]{2,80}?)\s*</a>',
    re.IGNORECASE,
)


def parse_opencorporates_search(html: str) -> str | None:
    """Return the first CA company detail path (/companies/us_ca/CXXXXXX) from
    an OpenCorporates search results page, or None if no match."""
    m = _OC_DETAIL_LINK.search(html)
    return m.group(1) if m else None


def parse_opencorporates_detail(html: str, vendor_name: str = "") -> list[dict]:
    """Parse an OpenCorporates company detail page into a flat registry record.

    Pulls dt/dd attribute pairs for incorporation date, agent name, and
    registered address; extracts officer names from the officers section.
    """
    rec: dict = {
        "vendor_name": vendor_name,
        "incorporation_date": "",
        "registered_agent": "",
        "principal_officers": [],
        "address": "",
        "source_state": "CA",
    }

    for raw_dt, raw_dd in _OC_DT_DD.findall(html):
        label = _clean(raw_dt).lower()
        value = _clean(raw_dd)
        if not value or len(value) < 2:
            continue
        if "incorporation date" in label or "formation date" in label:
            rec["incorporation_date"] = value
        elif "agent name" in label:
            rec["registered_agent"] = value
        elif "registered address" in label and not rec["address"]:
            rec["address"] = value
        elif "principal address" in label and not rec["address"]:
            rec["address"] = value

    # company name from <h1> if caller didn't supply one
    if not rec["vendor_name"]:
        m = re.search(r"<h1[^>]*>\s*([^<]{3,100}?)\s*</h1>", html, re.IGNORECASE)
        if m:
            rec["vendor_name"] = _clean(m.group(1))

    # officers live inside a section/div whose id contains "officers"
    off_m = re.search(
        r'id=["\']officers["\'].*?(?=\sid=["\']|\Z)',
        html, re.DOTALL | re.IGNORECASE,
    )
    if off_m:
        for m in _OC_OFFICER_LINK.finditer(off_m.group(0)):
            name = _clean(m.group(1))
            if name:
                rec["principal_officers"].append(name)

    return [rec] if rec["vendor_name"] else []


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
