import sys
import os
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from src.bright_data.client import BrightDataClient, ENDPOINT, UNLOCKER_ZONE

client = BrightDataClient(budget_cap=5.0, label="test")
url = "https://opencorporates.com/companies/us_ca?q=Sparkz"
payload = {"zone": UNLOCKER_ZONE, "url": url, "format": "json"}

r = client.session.post(ENDPOINT, json=payload, timeout=60)
print(f"Status: {r.status_code}")
try:
    print(list(r.json().keys()))
except Exception as e:
    print(r.text[:500])
