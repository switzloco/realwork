# California Public Infrastructure Data Sources & Fraud Patterns
## Research for RealWork Pipeline — 2026-05-25

---

## 1. PRIMARY DATASET: California Grants Portal (data.ca.gov)

### Dataset URLs
| Dataset | URL |
|---------|-----|
| Grants Offered (updated daily) | https://data.ca.gov/dataset/california-grants-portal/resource/111c8c88-21f6-453c-ae2c-b4785a0624f5 |
| Grant Awards FY 2024-2025 | https://data.ca.gov/dataset/california-grants-portal-grant-awards-2024-2025 |
| Grant Awards FY 2023-2024 | https://data.ca.gov/dataset/california-grants-portal-grant-awards-2023-2024/resource/018f3523-652d-4197-a4a8-a055bfd1544f |
| Grant Awards FY 2022-2023 | https://data.ca.gov/dataset/california-grants-portal-grant-awards-2022-2023/resource/86870d5c-e9fa-46f5-8f86-2a9893662ce1 |

### Direct CSV Downloads
- FY 2023-2024: `https://data.ca.gov/dataset/572d06aa-4f1f-44ad-80a4-167bec020881/resource/018f3523-652d-4197-a4a8-a055bfd1544f/download/grant-awards-fiscal-year-2023-2024.csv`
- FY 2022-2023: `https://data.ca.gov/dataset/0ae62873-b7f0-498e-a595-476fa8478b0b/resource/86870d5c-e9fa-46f5-8f86-2a9893662ce1/download/grant-awards-fiscal-year-2022-2023.csv`

### API Access (CKAN)
```
# Datastore search
https://data.ca.gov/api/3/action/datastore_search?resource_id=018f3523-652d-4197-a4a8-a055bfd1544f&limit=100

# SQL-style query
https://data.ca.gov/api/3/action/datastore_search_sql?sql=SELECT * FROM "018f3523-652d-4197-a4a8-a055bfd1544f" LIMIT 10
```

### Schema (Post-Award Fields per AB132 / Gov Code 8333)
Based on the JSON submission schema and legislation, the Grant Awards dataset includes:

| Field Name (JSON/CSV) | Description |
|------------------------|-------------|
| primaryRecipientName | Name of the grant recipient organization |
| primaryRecipientFirstName | First name (for individual recipients) |
| primaryRecipientLastName | Last name (for individual recipients) |
| secondaryRecipients | Additional recipients |
| totalAwardAmount | Total dollar amount awarded |
| totalAwardUsed | Amount of award expended |
| matchingFundingAmount | Matching funds from recipient |
| grantTitle | Title of the grant opportunity |
| grantNumber / grantID | Unique grant identifier |
| geographicLocationServed | Region/jurisdiction served |
| recipientType | Type of recipient entity |

**Note:** The exact CSV column headers need verification by downloading a sample file. The data.ca.gov portal was returning 403 errors during this research; the CKAN API endpoint should work programmatically.

### Legal Mandate
- **Grant Information Act of 2018** (AB 2252, Gov Code 8333-8334.1)
- **AB 132**: Requires grantmakers to submit post-award data for grants closing on/after July 1, 2022
- Data updated daily at 8:45 PM
- Formats: CSV, TSV, JSON, XML

---

## 2. SECONDARY DATASETS: State Expenditures & Contracts

### Open FISCal (State Controller / FI$Cal)
**URL:** https://open.fiscal.ca.gov/

Two main datasets available via CKAN API on data.ca.gov:

**Spending Transactions** (all expenditures, no vendor names):
```
https://data.ca.gov/api/3/action/package_show?id=spending-transactions
```

**Vendor Transactions** (subset with vendor names):
```
https://data.ca.gov/api/3/action/package_show?id=vendor-transactions
```

#### Vendor Transactions Field Names:
| Field | Description |
|-------|-------------|
| fiscal_year_begin | Fiscal year |
| accounting_period | Period within fiscal year |
| accounting_date | Date of transaction |
| agency_name | State agency |
| department_name | Department |
| business_unit | Business unit code |
| program_code | Program identifier |
| program_description | Program name |
| fund_code | Fund identifier |
| fund_description | Fund name |
| fund_group | Fund grouping |
| account | Account code |
| account_description | Account name |
| account_type | Type of account |
| account_category | Category |
| account_sub_category | Sub-category |
| budget_reference | Budget ref code |
| budget_reference_description | Budget ref name |
| budget_reference_category | Category |
| budget_reference_sub_category | Sub-category |
| year_of_enactment | Year budget enacted |
| monetary_amount | Dollar amount |
| document_id | Transaction document ID |
| related_document | Related document ref |
| vendor_name | Vendor/payee name |

#### API Query Examples:
```
# Search for a vendor
https://data.ca.gov/api/3/action/datastore_search?resource_id={id}&q=jones&limit=5

# SQL filter by account code (e.g., 5442000 = construction)
https://data.ca.gov/api/3/action/datastore_search_sql?sql=SELECT * FROM "{id}" WHERE "account" LIKE '5442000'

# Pagination: max 32,000 rows per request, use offset
&limit=32000&offset=32000
```

**Coverage:** 151 departments (188 business units), ~79% of state expenditures. Updated monthly.

### DGS Purchase Orders
**URL:** https://data.ca.gov/dataset/purchase-order-data

### Cal eProcure (DGS Procurement)
**URL:** https://caleprocure.ca.gov/pages/public-search.aspx
- SCPRS: State contracts and purchases over $5,000 (since 2003)
- CSCR: Bid opportunities
- Weekly data exports available; results downloadable as spreadsheet

### State Controller's ByTheNumbers
**URL:** https://bythenumbers.sco.ca.gov/
- 12 years of financial data from 58 counties and 450+ cities
- Revenues, expenditures, debt by local government

### State Controller's Local Government Data
**URL:** https://cities.bythenumbers.sco.ca.gov/
- City-level financial data

---

## 3. FEDERAL INFRASTRUCTURE SPENDING IN CALIFORNIA

| Source | URL | Notes |
|--------|-----|-------|
| USAspending.gov | https://www.usaspending.gov/ | All federal awards to CA entities |
| Urban Institute IIJA Tracker | https://apps.urban.org/features/infrastructure-spending-states-counties/state/06/ | CA-specific infrastructure spending |
| SAM.gov | https://sam.gov/ | Entity registration, opportunities |

California has received ~$30 billion in federal Infrastructure Investment and Jobs Act (IIJA) funding.

---

## 4. KNOWN FRAUD PATTERNS IN CA PUBLIC INFRASTRUCTURE

### Pattern 1: Bid Rigging (Caltrans Case, 2015-2019)
**Case:** USA v. Yong, Miller, Opp (Eastern District of California)
- **Scheme:** Caltrans contract manager coordinated with contractors to submit "sham" (noncompetitive) bids
- **Scale:** $800,000+ in bribes (cash, wine, furniture, home remodeling)
- **Sentences:** 49 months (Yong), 78 months (Miller); ~$3M total restitution
- **Red Flags:**
  - Same contractors repeatedly winning from same manager
  - Related companies (spouse's company) submitting competing bids
  - Lifestyle inconsistent with salary
  - Narrow bid spreads between "competitors"

### Pattern 2: Change Order Manipulation
- Low initial bid wins contract, then costs balloon via change orders
- Same employee repeatedly approves change orders for same contractor
- Vague original specs create justification for additions
- **Red Flag:** Projects consistently 30-50%+ over original award

### Pattern 3: Prevailing Wage Fraud
- Contractors submit fraudulent certified payroll (certify compliance while paying workers less)
- Common in subcontractor relationships (prime looks clean, subs cheat)
- **Red Flag:** Bids significantly lower than competitors (funded by wage theft)

### Pattern 4: Shell Companies / Pass-Through Schemes
- Employee creates shell company, buys materials at market rate, resells to employer at markup
- DBE (Disadvantaged Business Enterprise) fraud: legitimate DBE listed but doesn't do actual work
- **Red Flags:**
  - Vendor not in business directories
  - Same address/phone as other entities
  - Invoiced goods/services can't be verified
  - Company formed shortly before receiving awards

### Pattern 5: False Claims / Overbilling
- Billing for work not performed or materials not delivered
- Inflating quantities on progress reports
- Charging for higher-grade materials while using cheaper ones
- **Legal tool:** California False Claims Act (allows qui tam / whistleblower suits)

### Pattern 6: Grant Fund Diversion
- Using grant money for purposes other than stated project
- Fabricating matching fund documentation
- Claiming completion for incomplete projects
- **Red Flag:** Award amount significantly higher than market rate for described scope

---

## 5. DOJ ENFORCEMENT FRAMEWORK

**Procurement Collusion Strike Force** (est. November 2019)
- URL: https://www.justice.gov/atr/procurement-collusion-strike-force
- Results: 100+ investigations, 45+ guilty pleas, 60+ prosecuted, $60M+ in fines
- Focus: Government contracts at all levels (federal, state, local)

**California DIR Public Works Enforcement**
- URL: https://www.dir.ca.gov/Public-Works/Enforcement.html
- Investigates prevailing wage violations on public construction projects

**California State Auditor**
- URL: https://www.auditor.ca.gov/reports/
- Key reports: I2025-1, I2024-1 (Investigations of Improper Activities)
- High-Risk Audit Program: 2025-601

---

## 6. RECOMMENDED DATA STRATEGY FOR REALWORK

### Stage 1 (No Bright Data needed):
1. **Download Grant Awards CSVs** (FY 2022-2025) from data.ca.gov
2. **Query Vendor Transactions** via CKAN API for infrastructure-related account codes
3. **Cross-reference** grant recipients with vendor transaction data
4. **Red flag scoring** based on:
   - Recipients receiving multiple large awards in short timeframes
   - Awards significantly above program averages
   - Recipients in multiple unrelated grant categories
   - Geographic clustering of awards to same entities
   - New entities (formed recently) receiving large awards

### Stage 2 (Bright Data):
- Verify entity existence (business registrations, physical addresses)
- Check for related entities (shared addresses, officers, phone numbers)
- Look for news articles about recipients
- Cross-reference officer names with public employee databases
- Check for debarment or past violations

### Key Account Codes (Open FISCal):
- Construction services: 5442xxx
- Professional services: 5340xxx
- Infrastructure improvements: research needed (download full account code list)
