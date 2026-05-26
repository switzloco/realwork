# RealWork Investigation Findings Report
*Generated on: 2026-05-26 18:13:10 UTC*

## Executive Budget Summary
- **Total Spent:** $14.50
- **Remaining Budget:** $235.50
- **Average Cost per Project:** $2.90

## Investigation Methodology
The investigation followed a four-stage process. First, grant data was extracted, transformed, and loaded (ETL) into a structured format. Second, an automated system analyzed records for anomalies, generating red flags based on predefined risk indicators. Third, a grounded search strategy was developed for high-risk projects, identifying key entities, locations, and terms for verification. Finally, a web scraping and OSINT process was executed to gather and evaluate evidence from official government databases (Secretary of State, contractor licensing boards, permit portals) and public sources (search engines, business directories, social media) to validate or invalidate the initial red flags.

## Project Findings
### Project ID: `8dc4889ab35c` (South Berkeley Senior Center Seismic Retrofit)
- **Conclusion:** **[CLEARED]**
- **Confidence Level:** HIGH
- **Evidence Checked:** 9 sources
- **Investigation Cost:** $1.00

#### Evidence Summary
The investigation determined that the grant record erroneously conflated details from two separate, legitimate public projects. Evidence confirms the existence of both the 'South Berkeley Senior Center Seismic Retrofit' managed by the City of Berkeley, and the 'Western Municipal Water District' backup pump installation. The significant discrepancy identified in the red flag is the result of a data entry error, not fraudulent activity.

#### Key Discoveries
- The grant record incorrectly combines the title and recipient of one project with the description of a completely different project.
- Evidence confirms the 'South Berkeley Senior Center Seismic Retrofit' is a real project under the City of Berkeley's management.
- Evidence also confirms the 'Western Municipal Water District' pump project is a legitimate initiative, supported by official watershed authority documents.
- The inconsistency is a data integrity issue within the funding source's reporting, not an indication of fraud by the recipient.

---

### Project ID: `cae8ec61ce0a` (New Construction and Major Renovation (NCMR))
- **Conclusion:** **[FLAGGED]**
- **Confidence Level:** HIGH
- **Evidence Checked:** 10 sources
- **Investigation Cost:** $3.00

#### Evidence Summary
The investigation confirmed that the recipient, Teknol Inc, is a software development and digital marketing firm located in Santa Clara County. This business activity is fundamentally inconsistent with the grant's stated purpose of 'New Construction and Major Renovation'. No evidence was found to suggest the company has any capability or history in the construction industry, supporting the initial red flag.

#### Key Discoveries
- The recipient, Teknol Inc, is verified as a software and marketing company.
- The company's core business is entirely unrelated to construction or renovation.
- The mismatch between the recipient's industry and the grant's purpose is a major, unresolved anomaly.
- Official state business registration and contractor license searches were consistently blocked, preventing full corporate verification.

---

### Project ID: `2d53e796c5e5` (New Construction and Major Renovation (NCMR))
- **Conclusion:** **[CLEARED]**
- **Confidence Level:** HIGH
- **Evidence Checked:** 12 sources
- **Investigation Cost:** $3.00

#### Evidence Summary
Evidence shows that the recipient, JM3 Holdings, LLC, operates a licensed child day care center in Merced. As the funding originates from the Department of Social Services, a grant for new construction and renovation of a childcare facility is a logical and appropriate use of funds. The initial red flag regarding the recipient being a 'holding company' was a false alarm, as this is the legal entity for the operating daycare.

#### Key Discoveries
- JM3 Holdings, LLC, operates a licensed child day care center in Merced, CA.
- The company is a registered federal contractor under the NAICS code for 'Child Day Care Services'.
- The grant's purpose and funding source (Dept. of Social Services) are consistent with the recipient's established business of providing childcare.
- The entity type is consistent with the grant's intent to fund social service infrastructure.

---

### Project ID: `afc551688790` (New Construction and Major Renovation (NCMR))
- **Conclusion:** **[FLAGGED]**
- **Confidence Level:** MEDIUM
- **Evidence Checked:** 11 sources
- **Investigation Cost:** $4.00

#### Evidence Summary
An extensive open-source investigation failed to find any evidence of a company named 'Suarez Holdings, LLC' involved in construction in Sacramento. While several similarly named entities exist in other states or industries, no verifiable information connects the specific recipient to the grant's location and purpose. The complete absence of a digital footprint or public record is highly suspicious, though the conclusion is tempered by the inability to access blocked official state databases.

#### Key Discoveries
- No public records or online presence could be found for 'Suarez Holdings, LLC' operating in the Sacramento construction sector.
- Searches returned information for unrelated entities with similar names in different locations.
- The lack of any verifiable existence for the recipient is a significant anomaly.
- Inaccessible state and county databases prevent a high-confidence conclusion.

---

### Project ID: `a700ebbeb6bb` (New Construction and Major Renovation (NCMR))
- **Conclusion:** **[CLEARED]**
- **Confidence Level:** MEDIUM
- **Evidence Checked:** 12 sources
- **Investigation Cost:** $3.50

#### Evidence Summary
The investigation confirmed that 'Infinite Sky Inc.' holds an active 'A - General Engineering Contractor' and 'B - General Building Contractor' license from the California Contractors State License Board. This finding directly refutes the primary red flag that the recipient was in an unrelated industry. While the company's registered address is in Van Nuys, not the project location of Placer County, it is common for contractors to work statewide.

#### Key Discoveries
- Infinite Sky Inc. is a licensed and active General Building Contractor in California (License #1110009).
- The recipient's business classification is appropriate for a new construction and renovation grant, resolving the initial suspicion.
- A geographic mismatch exists between the company's address (Van Nuys) and the project location (Placer County), but this is not a definitive indicator of fraud.
- Open-source searches for a company presence in Placer County were inconclusive.

---

## Strategic Recommendations
- Initiate a formal legal review for flagged projects 'Teknol Inc' (cae8ec61ce0a) and 'Suarez Holdings, LLC' (afc551688790) to consider subpoenas for banking and corporate records.
- Notify the Governor's Office of Emergency Services about the data entry error in project '8dc4889ab35c' to ensure their public records are corrected.
- Close and archive investigations for cleared projects 'JM3 Holdings, LLC' (2d53e796c5e5) and 'Infinite Sky Inc.' (a700ebbeb6bb).
- Develop technical countermeasures or alternative data acquisition strategies to address the frequent blocking of investigator access to the CA Secretary of State and other official public record portals.