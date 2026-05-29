import sys
import os
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from src.bright_data.client import BrightDataClient

client = BrightDataClient(budget_cap=5.0, label="test")
url = "https://opencorporates.com/companies/us_ca?q=Sparkz"
resp = client.unlock(url, render_js=False)
html = resp.get("html") or ""
print(f"Status: {resp.get('status')}")
print(f"Length: {len(html)}")
with open("test_opencorp.html", "w", encoding="utf-8") as f:
    f.write(html)
