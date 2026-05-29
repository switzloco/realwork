# Round 2 Investigation Findings
*Date:* May 2026
*Analyst:* Antigravity

## What We Looked At
Following the Round 1 audit which successfully validated high-dollar construction and physical infrastructure grants, Round 2 shifted focus to **Service Grants**. 
Service grants represent a higher inherent risk profile because their deliverables (training, consulting, planning) are intangible and harder to verify than physical infrastructure.

We applied a composite risk scoring system across the consolidated `grants_full.csv` dataset, specifically targeting:
1. Private entities (LLCs, LPs, Inc.)
2. Large award amounts
3. Null or Zero disbursements on record
4. Vague or generic project descriptions

## What We Found (Dead Ends & Cleared Anomalies)
The top anomalies flagged by our scans underwent deep-dive verification using SERP presence and Secretary of State registry checks via Bright Data. 

Our investigation surfaced a consistent pattern: the most severe anomalies in the dataset are almost exclusively the result of **data classification edge cases**, not fraud. We cleared the highest-risk entities by identifying the underlying structural reasons for their data signatures.

### Case 1: Large Infrastructure SPVs and Real Estate
- **Examples:** Element Lancaster 1 LLC ($118M), 44049 Sierra Hwy Propco LLC ($84.6M), AggrePlex of Modesto LLC ($26.5M).
- **Verification Chain:** SERP checks revealed that these entities are Special Purpose Vehicles (SPVs) created explicitly for massive, state-sponsored infrastructure projects (e.g., green hydrogen facilities, Behavioral Health Continuum Infrastructure, and recycled resource extraction plants).
- **The Charitable Explanation:** Large bond-financed or tax-credit infrastructure projects frequently use SPVs to isolate financial risk. Furthermore, disbursements often appear as "Null" because these grants are milestone-based, meaning funds are only released (or tax credits applied) after significant construction phases are completed, which may span multiple fiscal years.

### Case 2: Environmental Cleanup Reimbursements
- **Examples:** BEACHCOM, LLC ($960K), MOUSSA MATAR ($541K), GREENWHICH RETAIL INC. ($912K).
- **Verification Chain:** Cross-referencing the project descriptions against SWRCB (State Water Resources Control Board) programs identified these as Orphan Site Cleanup Fund (OSCF) grants.
- **The Charitable Explanation:** These are reimbursements to individual property owners or small businesses for the cleanup of historical contamination (e.g., old gas stations or dry cleaners). They flag as "private entities" with "vague descriptions" but are tightly regulated reimbursement programs.

### Case 3: Future Development LPs
- **Examples:** "A to be determined Limited Partnership" ($26.1M)
- **Verification Chain:** The grant from the Department of Housing and Community Development was for "Agoura Hills Housing".
- **The Charitable Explanation:** Affordable housing developments relying on Low-Income Housing Tax Credits (LIHTC) routinely apply for grants before the final Limited Partnership is legally formed.

### Case 4: Misclassified Non-Profits and Public Entities
- **Examples:** Tule Basin Water Foundation ($6.7M), Watershed Conservation Authority ($5.7M)
- **Verification Chain:** Web verification confirmed these are 501(c)(3) organizations or Joint Powers Authorities (JPAs).
- **The Charitable Explanation:** State data simply categorized them vaguely as "Private" or "Other Legal Entity", artificially inflating their risk score.

## What We Couldn't Verify
**Open FI$Cal Vendor Transactions (`vendor_crossref.py`)**
We were unable to successfully run the vendor cross-reference script. The "Vendor Transactions" dataset is no longer accessible via the `data.ca.gov` CKAN API, and the `open.fiscal.ca.gov/download-expenditures/` portal relies on a client-side rendered application that prevented automated extraction of the monthly CSVs. 
Without this dataset, we could not determine if any high-risk grant recipients were secretly receiving off-books contracting payments via the 5340 account code.

## Recommendations for Follow-Up Investigators
1. **Refine the Dataset Filtering:** Future investigations should explicitly filter out known SPV holding companies and OSCF cleanup reimbursements.
2. **Obtain FI$Cal Data Manually:** An investigator should manually download the Vendor Transactions CSV files from the Open FI$Cal portal, place them in `data/vendor_transactions.csv`, and run:
   ```bash
   python -m src.audit.vendor_crossref --fetch --account 5340
   ```
3. **Cross-Year Analysis:** Since many Null Disbursements are due to milestone payments, investigators should join the FY 22-23 and FY 23-24 datasets. Any entity showing Null Disbursements across *both* years for the same grant warrants deeper scrutiny.

---
### Reproducibility Guide
To reproduce these findings yourself:

**1. Run the Services Fraud Scan**
```bash
python -m src.audit.services_fraud_scan --source csv
```
*(This parses `data/grants_full.csv` and outputs `data/services_fraud_results.json`)*

**2. Run BrightData SERP Checks on the output**
```bash
python -m src.bright_data.bulk_serp --top 50
```
*(Results are logged to `data/bright_data/bulk_serp_ledger.jsonl`)*

**3. Run Secretary of State Verification**
```bash
python -m src.bright_data.sos_check --budget 20 --top 50
```
*(Checks OpenCorporates/CA SOS for active business standing)*
