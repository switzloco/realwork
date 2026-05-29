import sys
import os
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from src.bright_data.client import BrightDataClient

client = BrightDataClient(budget_cap=5.0, label="test")
query = '"Sparkz" site:opencorporates.com/companies/us_ca'
resp = client.serp(query)
print(json.dumps(resp, indent=2))
