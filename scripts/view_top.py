import json
data = json.load(open("data/smart_hunt_results.json"))
for i, s in enumerate(data[:16]):
    flags = ", ".join(s["flags"][:3])
    print(f"#{i+1} Score:{s['suspicion_score']} | ${s['award_amount']:,.0f} | {s['recipient']} | {s['grant_title'][:50]} | {flags}")
