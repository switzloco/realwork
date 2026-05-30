"""
Shared Bright Data client — used by all bulk verification scripts.

All output goes to data/bright_data/ to keep it cleanly separated from the
existing audit outputs that Antigravity may be regenerating.
"""

import json
import os
import time
from pathlib import Path
from urllib.parse import quote_plus

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("BRIGHT_DATA_API_KEY", "")
SERP_ZONE = os.environ.get("BRIGHT_DATA_SERP_ZONE", "realwork_serp")
UNLOCKER_ZONE = os.environ.get("BRIGHT_DATA_UNLOCKER_ZONE", "realwork_unlocker")
ENDPOINT = "https://api.brightdata.com/request"

OUTPUT_DIR = Path("data/bright_data")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class BudgetExceeded(Exception):
    pass


class BrightDataClient:
    """Thin wrapper around Bright Data with cost tracking and resumable runs."""

    SERP_COST = 0.005       # ~$5 per 1000 SERP queries
    UNLOCKER_COST = 0.0015  # ~$1.50 per 1000 Web Unlocker requests (HTML)

    def __init__(self, budget_cap: float = 50.0, label: str = "run"):
        if not API_KEY:
            raise RuntimeError("BRIGHT_DATA_API_KEY not set in environment")
        self.budget_cap = budget_cap
        self.spent = 0.0
        self.label = label
        self.ledger_path = OUTPUT_DIR / f"{label}_ledger.jsonl"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        })

    def _check_budget(self, cost: float):
        if self.spent + cost > self.budget_cap:
            raise BudgetExceeded(
                f"Budget cap ${self.budget_cap:.2f} would be exceeded "
                f"(spent ${self.spent:.3f}, next request ${cost:.4f})"
            )

    def _log(self, entry: dict):
        with open(self.ledger_path, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def serp(self, query: str, country: str = "us") -> dict:
        self._check_budget(self.SERP_COST)
        url = f"https://www.google.com/search?q={quote_plus(query)}&gl={country}&brd_json=1"
        payload = {"zone": SERP_ZONE, "url": url, "format": "json"}
        try:
            r = self.session.post(ENDPOINT, json=payload, timeout=45)
            self.spent += self.SERP_COST
            result = {"query": query, "status": r.status_code, "organic": [], "raw": None}

            if r.status_code == 200:
                try:
                    data = r.json()
                    if "body" in data and isinstance(data["body"], str):
                        try:
                            data = json.loads(data["body"])
                        except Exception:
                            pass
                    result["organic"] = data.get("organic", [])
                    result["raw"] = data
                except Exception as e:
                    result["error"] = f"json parse: {e}"
            else:
                result["error"] = r.text[:500]

            self._log({"type": "serp", "query": query, "status": r.status_code,
                       "results": len(result["organic"]), "cost": self.SERP_COST})
            return result
        except Exception as e:
            self._log({"type": "serp", "query": query, "error": str(e), "cost": 0})
            return {"query": query, "status": -1, "organic": [], "error": str(e)}

    def unlock(self, url: str, render_js: bool = False) -> dict:
        self._check_budget(self.UNLOCKER_COST)
        payload = {"zone": UNLOCKER_ZONE, "url": url, "format": "raw"}
        if render_js:
            payload["render"] = True
        try:
            r = self.session.post(ENDPOINT, json=payload, timeout=180)
            self.spent += self.UNLOCKER_COST
            self._log({"type": "unlock", "url": url, "status": r.status_code,
                       "size": len(r.content), "cost": self.UNLOCKER_COST})
            return {
                "url": url,
                "status": r.status_code,
                "html": r.text if r.ok else None,
                "error": None if r.ok else r.text[:500],
            }
        except Exception as e:
            self._log({"type": "unlock", "url": url, "error": str(e), "cost": 0})
            return {"url": url, "status": -1, "html": None, "error": str(e)}

    def fetch_bytes(self, url: str, render_js: bool = False) -> dict:
        """Like unlock(), but returns the raw response *bytes* — for binary
        targets such as PDFs where r.text would corrupt the payload.

        Used by the LA Alliance invoice extractor to pull scanned-PDF invoices
        through the Unlocker before handing them to a multimodal LLM.
        """
        self._check_budget(self.UNLOCKER_COST)
        payload = {"zone": UNLOCKER_ZONE, "url": url, "format": "raw"}
        if render_js:
            payload["render"] = True
        try:
            r = self.session.post(ENDPOINT, json=payload, timeout=120)
            self.spent += self.UNLOCKER_COST
            self._log({"type": "fetch_bytes", "url": url, "status": r.status_code,
                       "size": len(r.content), "cost": self.UNLOCKER_COST})
            return {
                "url": url,
                "status": r.status_code,
                "content": r.content if r.ok else None,
                "error": None if r.ok else r.text[:500],
            }
        except Exception as e:
            self._log({"type": "fetch_bytes", "url": url, "error": str(e), "cost": 0})
            return {"url": url, "status": -1, "content": None, "error": str(e)}

    def report(self) -> str:
        return f"[{self.label}] spent ${self.spent:.3f} of ${self.budget_cap:.2f} cap"
