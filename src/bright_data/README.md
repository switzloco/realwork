# Bright Data Bulk Verifiers

Scripts that hit the Bright Data API in bulk to verify properties of
flagged grant recipients. All output goes to `data/bright_data/` to stay
out of the way of the existing audit outputs in `data/`.

## Files

| Script | What it does | Cost ceiling |
|--------|--------------|--------------|
| `client.py` | Shared client + cost tracker + JSONL ledger | — |
| `bulk_serp.py` | 5 SERP queries per entity (existence, litigation, enforcement, LinkedIn, directories) | $50 default |
| `sos_check.py` | CA SOS bizfileonline status lookup via Web Unlocker | $20 default |
| `ccld_check.py` | CCLD facility license lookup for childcare grants | $20 default |

## Contracts

- **Read-only** access to existing audit outputs: `data/audit_results.json`,
  `data/services_fraud_results.json`. We never write to these.
- **Exclusive** write access to `data/bright_data/*.json` and
  `data/bright_data/*_ledger.jsonl`. Nothing else touches that directory.
- **Budget caps** are enforced per-run. Exceeding the cap raises
  `BudgetExceeded` and the script saves partial results before exiting.
- **Resumable** via `--resume` flag — scripts skip entities already in
  the output file.

## Required env vars

```
BRIGHT_DATA_API_KEY=...
BRIGHT_DATA_SERP_ZONE=realwork_serp
BRIGHT_DATA_UNLOCKER_ZONE=realwork_unlocker
```

## Run order

1. `python -m src.bright_data.bulk_serp --budget 50 --top 200` (~$50, 5-10 min)
2. `python -m src.bright_data.sos_check --budget 20 --top 200` (~$15-20)
3. `python -m src.bright_data.ccld_check --budget 20` (only NCMR/childcare grants)

Total at full tilt: ~$80-90 of the $208 remaining budget. Each can run
independently and resume if interrupted.
