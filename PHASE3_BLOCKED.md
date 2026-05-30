# Phase 3 (Live Entity-Registry Trawl) — Route Closed

**Status:** BLOCKED. Live scraping of vendor registry data via Bright Data is
not viable. Documented here so the next person doesn't burn time re-trying it.

## What Phase 3 was supposed to do

Take the deduplicated LA Checkbook vendor list (~2,500 vendors, Phase 2) and,
for each, look up its registered agent / principal officers / incorporation
address, so the Hydra query (Phase 4) could find clusters of distinct vendors
sharing a hidden hub while each collects sub-threshold payments from the same
department.

The graph layer, the entity-key normalization, and the Hydra cluster SQL are
all built and **validated against synthetic fixtures** (see below). The only
missing input is real registry data — and that's what we couldn't fetch.

## What blocked it

Two independent walls, both confirmed against the live Bright Data ledger:

1. **CA Secretary of State (`bizfileonline.sos.ca.gov`) — policy block.**
   Bright Data refuses the target outright:
   ```
   502  x-brd-error: Access denied: bizfileonline.sos.ca.gov is classified as
                      Government and blocked by Bright Data as it might breach
                      Bright Data usage policy.
   ```
   The Scraping Browser and Residential zones enforce the same platform-wide
   government-site policy. A direct (non-Bright-Data) request is stopped by the
   site's Imperva/Incapsula WAF JS challenge.

2. **OpenCorporates (`opencorporates.com`) — CAPTCHA wall.**
   Pivoted here as a non-government mirror of the same CA registry data. The
   Web Unlocker could not get through OpenCorporates' HAProxy CAPTCHA defense:
   even with the read timeout raised to 180s, requests either hang in a CAPTCHA
   loop until timeout or return `200 OK` with a **0-byte body**. No usable HTML
   was ever retrieved.

Net: the two authoritative sources for registered-agent data are, respectively,
policy-blocked and bot-walled for our tooling. No special hackathon zone that
bypasses the government policy was available.

## What we did NOT do (and why)

We did **not** hand-mock OpenCorporates/CA SoS records for real LA vendor names
to force the parser to succeed. Doing so would manufacture a "shell cluster"
out of invented inputs and present it as a finding — fabrication, and a direct
violation of this project's rule against synthetic/hallucinated findings and
against asserting claims about real entities. A real query over fake data is
still a fake result.

## What IS proven (legitimately)

The detection logic is validated with **openly-synthetic, obviously-fictional**
fixtures — no real entity is implicated:

- `python -m src.graph.validate_control` — Phase 1 control group: correctly
  links two distinct vendors that share an agent + officer, and excludes the
  decoy. **PASS.**
- `python -m src.graph.hydra_query --demo` — seeds a labeled synthetic shell
  cluster (Vega Systems / Orion Data / Pleiades Tech) plus clean decoys, then
  detects the sub-threshold structuring signature and ignores the decoys.
  **PASS.**

These prove the SQL and graph wiring work. They make no claim about any real
vendor.

## If someone wants to finish Phase 3 later

The graph/query code is source-agnostic — it just needs records in the shape
`{vendor_name, registered_agent, principal_officers, address}`. Viable inputs:

- A **bulk registry data license** (OpenCorporates sells API/bulk access;
  CA SoS publishes bulk business data downloads) — legitimate, no scraping.
- A **headless stealth browser run locally** (`playwright-stealth` /
  `undetected-chromedriver`) against OpenCorporates, outside Bright Data.
  Slower, but bypasses the CAPTCHA the Unlocker couldn't.
- Any other registry export dropped into the `ingest_sos_record()` interface.

Until then, Phase 3 is closed and the cluster pipeline stands on its synthetic
validation only.
