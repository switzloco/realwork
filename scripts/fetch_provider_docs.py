"""
Download targeted provider invoices/documents from the LA Alliance index.
Focus on the providers the user specifically wants:
PATH, Weingart Center, DWC, LAFH, Union Station, etc.
"""
import json
import os
import urllib.request
import ssl

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "la_alliance", "raw")

def download_pdf(url, filename):
    filepath = os.path.join(OUT_DIR, filename)
    if os.path.exists(filepath):
        print(f"  [SKIP] {filename}")
        return filepath
    try:
        ctx = ssl.create_default_context()
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (research)")
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            content = resp.read()
            with open(filepath, "wb") as f:
                f.write(content)
            print(f"  [OK] {filename} ({len(content):,} bytes)")
            return filepath
    except Exception as e:
        print(f"  [FAIL] {filename}: {e}")
        return None

# Key provider documents to download from the index
TARGETS = [
    # PATH
    ("https://file.lacounty.gov/SDSInter/ceo/asp/1191816_PATH-Oct2024.pdf",
     "PATH_SupportiveServices_Oct2024.pdf"),
    # Weingart Center
    ("https://file.lacounty.gov/SDSInter/ceo/asp/1191801_WeingartCenter-Oct2024.pdf",
     "WeingartCenter_SupportiveServices_Oct2024.pdf"),
    # DWC (Downtown Women's Center)
    ("https://file.lacounty.gov/SDSInter/ceo/asp/1191805_DWC-Oct2024.pdf",
     "DWC_SupportiveServices_Oct2024.pdf"),
    # LAFH (LA Family Housing)
    ("https://file.lacounty.gov/SDSInter/ceo/asp/1191812_LAFH-Oct2024.pdf",
     "LAFH_SupportiveServices_Oct2024.pdf"),
    # Mental Health America
    ("https://file.lacounty.gov/SDSInter/ceo/asp/1191815_MentalHealthAmerica-Oct2024.pdf",
     "MentalHealthAmerica_SupportiveServices_Oct2024.pdf"),
    # Tarzana Treatment Centers (SUD Beds)
    ("https://file.lacounty.gov/SDSInter/ceo/asp/1179563_TarzanaTreatmentCentersInc.-RecoveryBridgeHousing-October2024.pdf",
     "TarzanaTreatment_SUD_Oct2024.pdf"),
    # Star View Rancho Los Amigos - Mental Health Beds
    ("https://file.lacounty.gov/SDSInter/ceo/asp/1183480_StarViewRanchoLosAmigos-CRTP-Oct2024.pdf",
     "StarView_RanchoLosAmigos_MHBeds_Oct2024.pdf"),
    # Valley Star LAC-USC CRTP - Mental Health Beds
    ("https://file.lacounty.gov/SDSInter/ceo/asp/1183479_ValleyStarLAC-USCCRTP-October2024.pdf",
     "ValleyStar_LACUSC_MHBeds_Oct2024.pdf"),
    # Heritage Clinic
    ("https://file.lacounty.gov/SDSInter/ceo/asp/1191807_HeritageClinic-Oct2024.pdf",
     "HeritageClinic_SupportiveServices_Oct2024.pdf"),
    # A Brighter Day - Brandy House - Mental Health Beds
    ("https://file.lacounty.gov/SDSInter/ceo/asp/1183488_ABrighterDay-BrandyHouse-Oct2024.pdf",
     "ABrighterDay_MHBeds_Oct2024.pdf"),
]

print("=" * 60)
print("DOWNLOADING KEY PROVIDER DOCUMENTS")
print("=" * 60)

downloaded = 0
for url, fname in TARGETS:
    result = download_pdf(url, fname)
    if result:
        downloaded += 1

print(f"\nDownloaded {downloaded}/{len(TARGETS)} provider documents")
