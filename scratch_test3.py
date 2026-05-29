import sys
import os
import json
import requests
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from src.bright_data.client import BrightDataClient, ENDPOINT, UNLOCKER_ZONE

client = BrightDataClient(budget_cap=5.0, label="test")
url = "https://bizfileonline.sos.ca.gov/api/Records/businesssearch"
api_payload = {
    "SEARCH_ENTITIES": {
        "FORM_DATA": {
            "SEARCH_VALUE": "Sparkz",
            "SEARCH_TYPE": "NUMBER_OR_NAME"
        }
    }
}
payload = {
    "zone": UNLOCKER_ZONE,
    "url": url,
    "format": "raw",
    "method": "POST",
    "body": json.dumps(api_payload),
    "headers": {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
}

r = client.session.post(ENDPOINT, json=payload, timeout=60)
print(f"Status: {r.status_code}")
print(f"Body: {r.text[:500]}")
