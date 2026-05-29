import json
import os
import re
import requests
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup
from src.bright_data.client import BrightDataClient, ENDPOINT, UNLOCKER_ZONE

def fetch_vendor_data():
    print("Initializing Bright Data client...")
    client = BrightDataClient(budget_cap=5.0, label="vendor_scraper")
    
    url = "https://open.fiscal.ca.gov/download-expenditures/"
    print(f"Unlocking {url}...")
    
    payload = {"zone": UNLOCKER_ZONE, "url": url, "format": "json"}
    r = client.session.post(ENDPOINT, json=payload, timeout=60)
    
    if not r.ok:
        print("Failed:", r.text)
        return
        
    data = r.json()
    html = data.get("body", "")
    
    soup = BeautifulSoup(html, "html.parser")
    
    csv_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "vendor" in href.lower() and href.lower().endswith(".csv"):
            if href.startswith("/"):
                href = "https://open.fiscal.ca.gov" + href
            csv_links.append(href)
            
    print(f"Found {len(csv_links)} vendor CSV links.")
    
    if not csv_links:
        print("No CSV links found.")
        return
        
    target_links = csv_links[:3] 
    
    out_dir = Path("data")
    out_dir.mkdir(exist_ok=True)
    final_path = out_dir / "vendor_transactions.csv"
    
    dfs = []
    for link in target_links:
        print(f"Downloading {link}...")
        try:
            # these are just standard CSV files from data.ca.gov backend, usually no unlocker needed
            res = requests.get(link)
            if res.ok:
                from io import StringIO
                df = pd.read_csv(StringIO(res.text))
                dfs.append(df)
            else:
                print(f"Failed to read {link}: {res.status_code}")
        except Exception as e:
            print(f"Exception downloading {link}: {e}")
            
    if dfs:
        merged = pd.concat(dfs, ignore_index=True)
        print(f"Saving {len(merged)} records to {final_path}")
        merged.to_csv(final_path, index=False)
        print("Done!")
    else:
        print("No data downloaded.")

if __name__ == "__main__":
    fetch_vendor_data()
