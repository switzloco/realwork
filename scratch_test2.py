import sys
import os
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from src.bright_data.client import BrightDataClient

client = BrightDataClient(budget_cap=5.0, label="test")
url = "https://bizfileonline.sos.ca.gov/search/business?SearchType=NUMBER_OR_NAME&SearchCriteria=Sparkz&SearchSubType=ALL"
resp = client.unlock(url, render_js=True)
html = resp.get("html") or ""
print(f"Status: {resp.get('status')}")
print(f"Length: {len(html)}")
with open("test_sos.html", "w", encoding="utf-8") as f:
    f.write(html)
