import sqlite3
import json
import os
from dotenv import load_dotenv
load_dotenv()
from src.analysis.search_validator import run

def main():
    conn = sqlite3.connect('realwork.db')
    conn.row_factory = sqlite3.Row
    names = ['JM3 Holdings', 'Suarez Holdings', 'SBA Enterprises', 'Infinite Sky']
    rankings = []

    for i, name in enumerate(names):
        row = conn.execute('SELECT project_id FROM projects WHERE recipient_name LIKE ?', ('%' + name + '%',)).fetchone()
        if row:
            pid = row['project_id']
            rankings.append({
                'project_id': pid,
                'rank': i+1,
                'investigation_brief': f'Verify if {name} is a ghost entity or if it actually pulled permits for construction.',
                'composite_score': 99
            })

    print(f'Found {len(rankings)} targets in DB.')
    results = run(rankings)
    print(json.dumps(results, indent=2))

if __name__ == '__main__':
    main()
