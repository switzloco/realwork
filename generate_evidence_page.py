"""Generate a structured evidence document from the investigation database."""
from dotenv import load_dotenv
load_dotenv()

import sqlite3
import json
import sys
from datetime import datetime, timezone

# Ensure stdout uses UTF-8 to prevent console output crashes on Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

conn = sqlite3.connect("realwork.db")
conn.row_factory = sqlite3.Row

md = []
md.append("# RealWork: Structured Evidence Report")
md.append(f"*Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}*")
md.append("")
md.append("> **Notice:** This document presents anomalies identified through automated analysis")
md.append("> of publicly available California grant data. All findings are preliminary observations,")
md.append("> not accusations. Further investigation by qualified authorities is recommended for")
md.append("> any flagged items.")
md.append("")
md.append("---")
md.append("")

# Budget summary
spent = conn.execute("SELECT COALESCE(SUM(actual_cost), 0) FROM budget_ledger").fetchone()[0]
entries = conn.execute("SELECT COUNT(*) FROM budget_ledger").fetchone()[0]
md.append("## Investigation Budget")
md.append(f"- **Total Bright Data spend:** ${spent:.2f} of $250.00 budget")
md.append(f"- **API calls made:** {entries}")
md.append(f"- **Budget zone:** {'GREEN' if spent < 150 else 'YELLOW' if spent < 200 else 'RED'}")
md.append("")

# Methodology
md.append("## Methodology")
md.append("1. **Data Source:** California Grants Portal (data.ca.gov), FY 2022-2023 grant awards")
md.append("   - Dataset: `86870d5c-e9fa-46f5-8f86-2a9893662ce1`")
md.append("   - 11,698 total grant records")
md.append("2. **Filtering:** Records filtered to $50K-$5M range in infrastructure-related categories")
md.append("3. **Red Flag Analysis:** Gemini 2.5 Pro scored each record against 10 fraud indicators")
md.append("4. **Ranking:** Top candidates selected by composite score (fraud probability × feasibility × dollar magnitude)")
md.append("5. **Evidence Gathering:** Bright Data SERP API used for targeted web searches per project")
md.append("6. **Synthesis:** Gemini 2.5 Pro evaluated all gathered evidence for final conclusions")
md.append("")
md.append("---")
md.append("")

# Per-project evidence sections
investigated = conn.execute("""
    SELECT DISTINCT e.project_id 
    FROM evidence e 
    JOIN investigation_log il ON e.project_id = il.project_id
    ORDER BY il.conclusion DESC, il.confidence DESC
""").fetchall()

for row in investigated:
    pid = row[0]
    project = conn.execute("SELECT * FROM projects WHERE project_id = ?", (pid,)).fetchone()
    log = conn.execute("SELECT * FROM investigation_log WHERE project_id = ?", (pid,)).fetchone()
    flags = conn.execute("SELECT * FROM red_flags WHERE project_id = ?", (pid,)).fetchall()
    evidence = conn.execute("SELECT * FROM evidence WHERE project_id = ? ORDER BY timestamp", (pid,)).fetchall()
    ranking = conn.execute("SELECT * FROM rankings WHERE project_id = ?", (pid,)).fetchone()
    
    if not project or not log:
        continue
    
    conclusion = log['conclusion'] or 'UNKNOWN'
    emoji = '[FLAGGED] 🔴' if conclusion == 'FLAGGED' else ('[CLEARED] 🟢' if conclusion == 'CLEARED' else '[INCONCLUSIVE] 🟡')
    
    md.append(f"## {emoji} {project['project_name']} ({pid})")
    md.append("")
    md.append("### Grant Record")
    md.append(f"| Field | Value |")
    md.append(f"|-------|-------|")
    md.append(f"| Recipient | {project['recipient_name']} |")
    md.append(f"| Recipient Type | {project['recipient_type']} |")
    md.append(f"| Award Amount | ${project['award_amount']:,.2f} |")
    md.append(f"| Award Date | {project['award_date']} |")
    md.append(f"| Location | {project['location']} |")
    md.append(f"| Funding Source | {project['funding_source']} |")
    md.append(f"| Description | {project['description'][:300]} |")
    md.append("")
    
    md.append(f"### Conclusion: **{conclusion}** (Confidence: {log['confidence']})")
    md.append(f"*Investigation cost: ${log['total_cost']:.2f}*")
    md.append("")
    md.append(log['rationale'] or 'No rationale recorded.')
    md.append("")
    
    if flags:
        md.append("### Red Flags Identified")
        for f in flags:
            severity_emoji = '🔴' if f['severity'] == 'HIGH' else ('🟡' if f['severity'] == 'MEDIUM' else '⚪')
            md.append(f"- {severity_emoji} **[{f['severity']}]** {f['flag']}")
            if f['reasoning']:
                md.append(f"  - *{f['reasoning'][:200]}*")
        md.append("")
    
    if evidence:
        md.append("### Evidence Gathered")
        md.append(f"*{len(evidence)} sources checked*")
        md.append("")
        for i, e in enumerate(evidence, 1):
            supports = e['supports_fraud']
            indicator = '🔴 Supports fraud hypothesis' if supports == 1 else ('🟢 Contradicts fraud hypothesis' if supports == 0 else '⚪ Inconclusive')
            md.append(f"#### Source {i}: {e['source']}")
            md.append(f"- **URL:** `{e['url_scraped']}`")
            md.append(f"- **Cost:** ${e['actual_cost']:.2f}")
            md.append(f"- **Assessment:** {indicator}")
            md.append(f"- **Finding:** {e['finding']}")
            md.append("")
    
    md.append("---")
    md.append("")

# Recommendations
md.append("## Appendix: Data Source Verification")
md.append("The source dataset can be independently verified at:")
md.append("- **URL:** https://data.ca.gov/dataset/california-grants-portal-grant-awards-2022-2023")
md.append("- **Resource ID:** 86870d5c-e9fa-46f5-8f86-2a9893662ce1")
md.append("- **Download:** https://data.ca.gov/datastore/dump/86870d5c-e9fa-46f5-8f86-2a9893662ce1")
md.append("")

output = "\n".join(md)
with open("evidence_report.md", "w", encoding="utf-8") as f:
    f.write(output)

print(f"Evidence report written to evidence_report.md ({len(output)} chars, {len(investigated)} projects)")
conn.close()
