import sqlite3
import json
import csv
import os
import time
from dotenv import load_dotenv

# Ensure we load the GEMINI_API_KEY
load_dotenv()
from src.analysis.search_validator import run

def main():
    conn = sqlite3.connect('realwork.db')
    conn.row_factory = sqlite3.Row
    
    # Get all 90 flagged projects
    # We will build a 'rankings' style list of dicts to pass to run()
    query = """
        SELECT p.project_id, p.project_name, p.recipient_name, p.award_amount
        FROM projects p
        JOIN red_flags r ON p.project_id = r.project_id
        GROUP BY p.project_id
    """
    rows = conn.execute(query).fetchall()
    
    rankings = []
    for i, row in enumerate(rows):
        rankings.append({
            'project_id': row['project_id'],
            'rank': i + 1,
            'investigation_brief': f"Verify if {row['recipient_name']} physically exists or if it's a ghost entity.",
            'composite_score': 90
        })
        
    print(f"Found {len(rankings)} flagged projects to audit.")
    
    # Run the Gemini Search Validator
    print("Running Gemini Search Validator... This will take a while.")
    results = run(rankings)
    
    # Export to CSV
    csv_file = 'audit_report.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Project ID', 'Recipient Name', 'Award Amount', 'Recommendation', 'Search Summary', 'Reasoning'])
        
        for idx, res in enumerate(results):
            # find original row for recipient name
            pid = res['project_id']
            row = next((r for r in rows if r['project_id'] == pid), None)
            recipient = row['recipient_name'] if row else 'Unknown'
            amount = row['award_amount'] if row else 0
            
            writer.writerow([
                pid,
                recipient,
                amount,
                res.get('recommendation', 'UNKNOWN'),
                res.get('search_summary', ''),
                res.get('reasoning', '')
            ])
            
    print(f"Audit report saved to {csv_file}")

if __name__ == '__main__':
    main()
