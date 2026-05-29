import json
import collections

with open('data/bright_data/bulk_serp_ledger.jsonl') as f:
    lines = f.readlines()

counts = collections.defaultdict(int)
for line in lines:
    try:
        data = json.loads(line)
        if data.get('type') == 'serp':
            q = data.get('query', '')
            if '"' in q:
                entity = q.split('"')[1]
                counts[entity] += data.get('results', 0)
    except:
        pass

for k, v in sorted(counts.items(), key=lambda x: x[1])[:20]:
    print(f"{v} results: {k}")
