"""
LA Alliance Red Flag Analyst
Runs Gemini 2.5 Pro with Google Search Grounding against extracted invoice records.
Evaluates the invoice for fraud indicators and outputs a risk assessment.
"""

import argparse
import json
import os
import re
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

try:
    import google.generativeai as genai
except ImportError:
    genai = None

GEMINI_MODEL = "gemini-2.5-pro"
OUT_DIR = Path("data/la_alliance")

ANALYST_PROMPT = """You are a forensic auditor and fraud analyst investigating invoices submitted by homeless-service providers to Los Angeles County under the LA Alliance settlement.

You are evaluating the following extracted invoice record:
{record_json}

Use your Google Search grounding tool to look up the vendor (e.g. news about fraud, their typical size, leadership) and the standard costs for the stated deliverables (e.g. typical cost of a case manager or 'Access to Care' physical patch in LA County).

Go beyond the obvious known issues (like vague deliverables or round numbers). Look for NOVEL and SUBTLE fraud indicators. Specifically:
- **Address & Shell Companies:** Cross-reference the vendor's billing address using Google Search. Is it a residential home, a virtual office, or a UPS store? Does the vendor appear to be a newly formed LLC billing millions?
- **Mismatched Services:** Does the vendor's actual business (e.g., real estate, consulting) mismatch the clinical/homeless services they are billing for?
- **Impossible Ratios & Temporal Anomalies:** Are there impossibly high staff-to-client ratios? Is a massive amount of service billed in a highly condensed or impossible timeframe?
- **Pricing Outliers:** Compare the billed unit rates against standard LA County or Medicare/Medicaid reimbursement rates using Google Search. Are they overbilling by 500%+?

Identify any Red Flags that fit these novel categories or other deep anomalies.

Return a single JSON object with EXACTLY this schema (do not wrap in markdown):
{{
  "flags": [
    {{
      "flag": "Short name of the issue",
      "severity": "HIGH" | "MEDIUM" | "LOW",
      "reasoning": "Detailed explanation of why this is suspicious, citing the web if applicable"
    }}
  ],
  "fraud_probability": "HIGH" | "MEDIUM" | "LOW",
  "summary": "1-2 sentence executive summary of the risk assessment."
}}
"""

def _strip_json(text: str) -> dict:
    text = text.strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.MULTILINE).strip()
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON object in model reply: {text[:200]}")
    return json.loads(text[start:end + 1])

def analyze_record(record: dict) -> dict:
    if genai is None:
        raise RuntimeError("google.generativeai is not installed")
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY not set")

    genai.configure(api_key=key)
    # Enable Google Search Grounding if supported, otherwise fallback to standard
    try:
        model = genai.GenerativeModel(GEMINI_MODEL, tools="google_search")
    except Exception:
        model = genai.GenerativeModel(GEMINI_MODEL)

    prompt = ANALYST_PROMPT.format(record_json=json.dumps(record, indent=2))
    
    try:
        resp = model.generate_content(prompt)
        assessment = _strip_json(resp.text)
        return assessment
    except Exception as e:
        print(f"Exception during generate_content: {e}")
        return {
            "flags": [{"flag": "Analysis Failed", "severity": "LOW", "reasoning": str(e)}],
            "fraud_probability": "LOW",
            "summary": f"Failed to analyze: {e}"
        }

def run(ledger_path: str = "data/la_alliance/ledger.json", threshold: float = 100000.0):
    if not os.path.exists(ledger_path):
        print(f"Ledger not found at {ledger_path}")
        return

    with open(ledger_path, "r") as f:
        records = json.load(f)

    # Filter to riskiest (amount > threshold) and valid records
    risky_records = [
        r for r in records 
        if r.get("billed_amount") is not None and r["billed_amount"] > threshold
        and r.get("vendor") is not None
    ]

    print(f"=== LA Alliance Red Flag Analyst ===")
    print(f"Ledger: {len(records)} records | Filtered (>{threshold}): {len(risky_records)} records")

    assessments = []
    
    for i, rec in enumerate(risky_records, 1):
        vendor = rec.get("vendor")
        amount = rec.get("billed_amount", 0)
        title = rec.get("source_title", "Unknown")
        print(f"[{i}/{len(risky_records)}] Analyzing {vendor} - ${amount:,.2f} ({title})...")
        
        result = analyze_record(rec)
        
        # Merge the original record info so the output is standalone
        combined = {
            "project_id": title,
            "vendor": vendor,
            "billed_amount": amount,
            "deliverables": rec.get("deliverables", []),
            "analysis": result
        }
        assessments.append(combined)
        
        print(f"  -> Fraud Prob: {result.get('fraud_probability')} | Flags: {len(result.get('flags', []))}")
        for flag in result.get("flags", []):
            print(f"     [{flag.get('severity')}] {flag.get('flag')}")

    out_file = OUT_DIR / "risk_assessments.json"
    out_file.write_text(json.dumps(assessments, indent=2))
    print(f"\nSaved {len(assessments)} risk assessments to {out_file}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default="data/la_alliance/ledger.json")
    ap.add_argument("--threshold", type=float, default=100000.0, help="Minimum amount to trigger analysis")
    args = ap.parse_args()
    
    run(ledger_path=args.ledger, threshold=args.threshold)
