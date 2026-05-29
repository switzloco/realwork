import sys
import os
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from src.bright_data.client import BrightDataClient

client = BrightDataClient(budget_cap=5.0, label="test")
url = "https://data.ca.gov/api/3/action/package_show?id=vendor-transactions"
resp = client.unlock(url, render_js=False)
html = resp.get("html") or ""
print(html[:1000])
with open("vendor_package.json", "w") as f:
    f.write(html)
