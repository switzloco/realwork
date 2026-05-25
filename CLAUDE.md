# CLAUDE.md — Project Context for AI Assistants

This file is read by Claude Code (web/CLI) at session start. It provides the context needed to contribute to this project without re-reading the full README.

## What This Is

RealWork is a multi-agent fraud detection pipeline targeting California public infrastructure spending. AI analyzes state grant data to identify likely fraud targets, then Bright Data scrapers gather corroborating evidence.

See README.md for the full agent architecture and methodology.

## Co-Development Setup

This project is built across two environments:

| Environment | Tool | Primary Role |
|-------------|------|-------------|
| Cloud | Claude Code (web) | Architecture, agent logic, documentation, code review |
| Local | Google Antigravity (Gemini) | Bright Data integration, local testing, UI |

### Coordination Rules
- **README.md** is the source of truth for architecture decisions. Update it when the design changes.
- **AGENTS.md** describes each agent's interface contract. If you change an agent's inputs/outputs, update AGENTS.md first.
- Commit frequently with descriptive messages. The other environment catches up via git pull.
- Don't refactor the other environment's code without noting it in the commit message.
- Keep the budget controller logic in a single file — both environments need to trust it.

## Project Structure (planned)

```
realwork/
├── README.md              # Architecture and methodology
├── CLAUDE.md              # This file (AI assistant context)
├── AGENTS.md              # Agent interface contracts
├── src/
│   ├── orchestrator.py    # Pipeline controller
│   ├── etl/               # Stage 1: data ingestion
│   ├── analysis/          # Stage 1: red flag analyst + ranking
│   ├── investigation/     # Stage 2: planner + scraper coordinator
│   ├── synthesis/         # Stage 3: report generation
│   └── budget.py          # Budget controller (shared service)
├── data/                  # Raw and processed datasets (gitignored if large)
├── logs/                  # Investigation logs (per-project JSON)
└── tests/
```

## Key Constraints
- Bright Data budget: $250 hard cap. Budget controller gates every API call.
- Stage 1 uses no Bright Data — only public datasets and LLM analysis.
- Sequential investigation: finish one project before starting the next.
- All findings must be framed as "anomalies warranting investigation," not accusations.

## Tech Stack
- Python for orchestration and ETL
- Gemini 2.5 Pro for reasoning agents (Stage 1 analysis, Stage 2 planning)
- Gemini 2.5 Flash for cheap HTML/PDF parsing
- Claude via personal Max account (optional, Stage 3 synthesis only)
- Bright Data SDK for web scraping
- SQLite for storage (single file, zero cost, portable)
