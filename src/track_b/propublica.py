"""
ProPublica Nonprofit Explorer adapter.

Free API, no auth required. Documentation:
  https://projects.propublica.org/nonprofits/api

Endpoints we use:
  GET /search.json?q={name}                       — name search, returns EINs
  GET /organizations/{ein}.json                   — full org + all filings

We extract the 990 financial line items needed for overhead/exec-comp ratios.

ProPublica is heavily rate-limited (5 req/sec from one IP). We route through
Bright Data Web Unlocker so the limit is per-zone, not per-our-IP. The free
direct API also works for low-volume runs.
"""

import json
import time
from urllib.parse import quote_plus

import requests

PROPUBLICA_BASE = "https://projects.propublica.org/nonprofits/api/v2"


# Form 990 line items — these are stable ProPublica field names from the API.
# Source: https://projects.propublica.org/nonprofits/api (Filings schema)
FILING_FIELDS = {
    "tax_prd_yr":   "tax_year",
    "totrevenue":   "total_revenue",
    "totfuncexpns": "total_expenses",
    "compnsatncurrofcr": "officer_comp_total",
    "lessdirfndrsng": "fundraising_direct_expense",
    "totprgmrevnue": "program_service_revenue",
    "totcntrbgfts": "contributions_total",
    "totassetsend": "total_assets_end",
    "totliabend":   "total_liabilities_end",
}

# Functional expense breakdown (Part IX of Form 990)
EXPENSE_FIELDS = {
    "prgmservexpns": "program_expenses",
    "mgmtgenlexpns": "mgmt_general_expenses",
    "fndrsngexpns":  "fundraising_expenses",
}


class ProPublicaClient:
    def __init__(self, brightdata_client=None, delay: float = 0.25):
        """
        brightdata_client: optional BrightDataClient — if provided, requests
        route through Web Unlocker (per-zone rate limit instead of per-IP).
        """
        self.bd = brightdata_client
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "realwork-audit/1.0"})

    def _get(self, url: str) -> dict:
        if self.bd:
            resp = self.bd.unlock(url, render_js=False)
            if resp.get("status") == 200 and resp.get("html"):
                try:
                    return json.loads(resp["html"])
                except Exception:
                    return {}
            return {}
        # Direct mode (free, rate-limited)
        try:
            r = self.session.get(url, timeout=30)
            time.sleep(self.delay)
            return r.json() if r.ok else {}
        except Exception:
            return {}

    def search(self, name: str) -> list[dict]:
        url = f"{PROPUBLICA_BASE}/search.json?q={quote_plus(name)}"
        data = self._get(url)
        return data.get("organizations", [])

    def get_org(self, ein: str) -> dict:
        ein = str(ein).replace("-", "").strip()
        url = f"{PROPUBLICA_BASE}/organizations/{ein}.json"
        return self._get(url)

    def best_match(self, name: str, state: str = "CA") -> dict | None:
        """Pick the best EIN match for a name; prefer same-state, same-name."""
        results = self.search(name)
        if not results:
            return None
        
        import re
        name_norm = name.lower().strip()
        input_tokens = set(re.findall(r'\b\w+\b', name_norm))
        if not input_tokens:
            return None

        # Subsidiary words to penalize to avoid matching secondary entities
        subsidiary_words = {
            "bookstore", "club", "association", "assn", "auxiliary", "aux", 
            "fellowship", "ministry", "benefits", "trust", "foundation", 
            "alumni", "students", "womens", "mens", "sports", "athletic",
            "fund", "center", "institute", "hospital", "clinic", "department", "dept"
        }

        def score(r):
            r_name = (r.get("name") or "").lower().strip()
            if r_name == name_norm:
                return 2.0  # Perfect exact match
            
            candidate_tokens = set(re.findall(r'\b\w+\b', r_name))
            if not candidate_tokens:
                return 0.0
                
            overlap = len(input_tokens.intersection(candidate_tokens)) / len(input_tokens)
            s = overlap
            
            # State match bonus
            if (r.get("state") or "").upper() == state.upper():
                s += 0.3
                
            # Subsidiary penalty
            has_sub = any(w in subsidiary_words for w in candidate_tokens)
            if has_sub:
                s -= 0.4
                
            return s

        best = max(results, key=score)
        return best if score(best) >= 0.5 else None


def extract_financials(filing: dict) -> dict:
    """Pull the line items we care about from one ProPublica filing record."""
    out = {}
    for src, dst in {**FILING_FIELDS, **EXPENSE_FIELDS}.items():
        v = filing.get(src)
        if v is not None:
            try:
                out[dst] = float(v)
            except (TypeError, ValueError):
                out[dst] = None
    return out


def compute_ratios(fin: dict) -> dict:
    """The four ratios that tell the story."""
    total_exp = fin.get("total_expenses")
    prog = fin.get("program_expenses")
    mgmt = fin.get("mgmt_general_expenses")
    fund = fin.get("fundraising_expenses")
    officer = fin.get("officer_comp_total")
    revenue = fin.get("total_revenue")

    def safe_div(n, d):
        if n is None or d is None or d <= 0:
            return None
        return round(n / d, 4)

    return {
        "program_expense_ratio": safe_div(prog, total_exp),
        "mgmt_overhead_ratio":   safe_div(mgmt, total_exp),
        "fundraising_ratio":     safe_div(fund, total_exp),
        "officer_comp_ratio":    safe_div(officer, total_exp),
        "officer_comp_to_revenue": safe_div(officer, revenue),
        "exp_to_revenue":        safe_div(total_exp, revenue),
    }
