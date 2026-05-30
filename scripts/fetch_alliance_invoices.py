"""
Fetch LA Alliance homeless services invoicing documents from the County's
public Algolia search index. This is the same index that powers
https://ceo.lacounty.gov/homeless-initiative/alliance-invoicing/

We query for all documents, extract PDF URLs, and download them.
"""

import json
import sys
import urllib.request
import urllib.parse
import os
import ssl

# Algolia credentials from the County's public-facing page
ALGOLIA_APP_ID = "USY9HV4C4P"
ALGOLIA_API_KEY = "a66f1d6fe5ef613ce81b6cf0138b4c16"
ALGOLIA_INDEX = "asphiprod"

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "la_alliance", "raw")

def search_algolia(query="", filters="", hits_per_page=100):
    """Query the Algolia index used by the LA County Alliance invoicing portal."""
    url = f"https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/{ALGOLIA_INDEX}/query"
    
    payload = {
        "query": query,
        "hitsPerPage": hits_per_page,
        "advancedSyntax": True,
        "attributesToRetrieve": [
            "sds_title", "sds_published_url", "sds_org_name",
            "sds_service_type", "sds_document_dt", "date"
        ],
    }
    if filters:
        payload["filters"] = filters

    data = json.dumps(payload).encode("utf-8")
    
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("X-Algolia-Application-Id", ALGOLIA_APP_ID)
    req.add_header("X-Algolia-API-Key", ALGOLIA_API_KEY)
    
    # Allow self-signed certs in some corporate environments
    ctx = ssl.create_default_context()
    
    with urllib.request.urlopen(req, context=ctx) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download_pdf(url, filename, out_dir):
    """Download a PDF from url to out_dir/filename."""
    filepath = os.path.join(out_dir, filename)
    if os.path.exists(filepath):
        print(f"  [SKIP] {filename} already exists")
        return filepath
    
    try:
        ctx = ssl.create_default_context()
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (research)")
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            content = resp.read()
            with open(filepath, "wb") as f:
                f.write(content)
            print(f"  [OK] {filename} ({len(content):,} bytes)")
            return filepath
    except Exception as e:
        print(f"  [FAIL] {filename}: {e}")
        return None


def sanitize_filename(title, ext=".pdf"):
    """Make a safe filename from a document title."""
    safe = title.replace("/", "-").replace("\\", "-").replace(":", "-")
    safe = safe.replace("?", "").replace('"', "").replace("<", "").replace(">", "")
    safe = safe.replace("|", "-").replace("*", "")
    safe = safe[:120]  # truncate
    if not safe.lower().endswith(ext):
        safe += ext
    return safe


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    
    # Search for ALL documents (no filter) to see what's there
    print("=" * 70)
    print("LA ALLIANCE HOMELESS SERVICES INVOICING - DOCUMENT DISCOVERY")
    print("=" * 70)
    
    # First, get total count with empty query
    result = search_algolia(query="", hits_per_page=0)
    total = result.get("nbHits", 0)
    print(f"\nTotal documents in index: {total}")
    
    # Now get all hits (up to 1000)
    result = search_algolia(query="", hits_per_page=min(total, 1000))
    hits = result.get("hits", [])
    print(f"Retrieved: {len(hits)} documents\n")
    
    # Categorize by service type and department
    by_dept = {}
    by_type = {}
    for hit in hits:
        dept = hit.get("sds_org_name", "Unknown")
        stype = hit.get("sds_service_type", "Unknown")
        by_dept.setdefault(dept, []).append(hit)
        by_type.setdefault(stype, []).append(hit)
    
    print("--- BY DEPARTMENT ---")
    for dept, docs in sorted(by_dept.items()):
        print(f"  {dept}: {len(docs)} docs")
    
    print("\n--- BY SERVICE TYPE ---")
    for stype, docs in sorted(by_type.items()):
        print(f"  {stype}: {len(docs)} docs")
    
    # Print all document titles + URLs
    print("\n--- ALL DOCUMENTS ---")
    for i, hit in enumerate(hits):
        title = hit.get("sds_title", "Untitled")
        url = hit.get("sds_published_url", "No URL")
        dept = hit.get("sds_org_name", "?")
        stype = hit.get("sds_service_type", "?")
        dt = hit.get("sds_document_dt", "?")
        print(f"\n[{i+1}] {title}")
        print(f"    Dept: {dept} | Type: {stype} | Date: {dt}")
        print(f"    URL: {url}")
    
    # Now download a sample — prioritize "invoice" in the title
    print("\n" + "=" * 70)
    print("DOWNLOADING INVOICE-RELATED PDFs")
    print("=" * 70)
    
    # Filter for docs with "invoice" in title
    invoice_docs = [h for h in hits if "invoice" in h.get("sds_title", "").lower()]
    # Also grab payment, billing, reimbursement docs
    payment_docs = [h for h in hits if any(kw in h.get("sds_title", "").lower() 
                    for kw in ["payment", "billing", "reimburse", "expenditure", "cost"])]
    
    # Combine and deduplicate
    download_candidates = {h.get("sds_published_url"): h for h in invoice_docs + payment_docs}
    
    if not download_candidates:
        # If no specific invoice docs, download first 10 as samples
        print("No docs with 'invoice/payment/billing' in title. Downloading first 10 samples...")
        download_candidates = {h.get("sds_published_url"): h for h in hits[:10]}
    
    print(f"\nFound {len(download_candidates)} candidate documents to download\n")
    
    downloaded = []
    for url, hit in list(download_candidates.items())[:15]:  # limit to 15
        if not url or not url.startswith("http"):
            continue
        title = hit.get("sds_title", "untitled")
        filename = sanitize_filename(title)
        result = download_pdf(url, filename, OUT_DIR)
        if result:
            downloaded.append(result)
    
    print(f"\n{'='*70}")
    print(f"Downloaded {len(downloaded)} files to {OUT_DIR}")
    print(f"{'='*70}")
    
    # Save the full index dump as JSON for reference
    index_path = os.path.join(OUT_DIR, "_alliance_index_dump.json")
    with open(index_path, "w") as f:
        json.dump(hits, f, indent=2, default=str)
    print(f"\nFull index saved to: {index_path}")


if __name__ == "__main__":
    main()
