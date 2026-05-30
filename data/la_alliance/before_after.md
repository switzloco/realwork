# LA Alliance Invoices — Before / After

Left: an unstructured scanned invoice the county published as a PDF.
Right: the normalized ledger row our agent extracted autonomously.

## 23-1022-S4_caf_04-01-25

**Source:** `data\la_alliance\raw\23-1022-S4_caf_04-01-25.pdf`  ·  105.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | — |
| Invoice date | 2025-04-01 |
| Billed amount | — |
| Deliverables | — |
| Confidence | low |
| Notes | The document is an official action record from the City of Los Angeles, not an invoice or billing document from a homeless-service provider. As such, fields like 'vendor', 'billed_amount', and 'deliverables' (as line-item services) are not present in the expected context. The 'invoice_date' is extracted from 'Council Meeting Date'. |

## 23-1022-S4_caf_6-21-24

**Source:** `data\la_alliance\raw\23-1022-S4_caf_6-21-24.pdf`  ·  101.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | — |
| Invoice date | — |
| Billed amount | — |
| Deliverables | — |
| Confidence | low |
| Notes | The document is an official action report from the City of Los Angeles, not an invoice or billing document from a homeless service provider. Therefore, 'vendor', 'invoice_date', 'billed_amount', and 'deliverables' (as line-item services) are not present. The 'Council Meeting Date' is June 21, 2024, but this is not an invoice date. |

## 23-1022-S4_rpt_cao_2-24-25

**Source:** `data\la_alliance\raw\23-1022-S4_rpt_cao_2-24-25.pdf`  ·  2431.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | — |
| Invoice date | 2025-02-24 |
| Billed amount | — |
| Deliverables | ADOPT the recommended Multi-Disciplinary Team outreach coordination structure outlined in this report; INSTRUCT the City Administrative Officer (CAO) and Chief Legislative Analyst (CLA) to work with the County to memorialize this structure; REQUEST the Los Angeles Homeless Services Authority (LAHSA) to update the outreach dashboards that are made available to Council Offices weekly; INSTRUCT the CAO to coordinate with Council Offices to determine if additional LAHSA dashboard licenses are needed and to identify funding for additional licenses, not to exceed two additional licenses per Council Office, as requested |
| Confidence | medium |
| Notes | The document is an Inter-Departmental Correspondence from the City of Los Angeles, not an invoice or billing document from a homeless-service provider submitted to Los Angeles County. Therefore, the 'vendor' field is null as this document is not a bill from an external provider. The 'billed_amount' is null as the document is a recommendation report and explicitly states 'There is no General Fund impact as a result of the recommendations in this report'. |

## 23-1022-S4_rpt_CAO_5-31-24

**Source:** `data\la_alliance\raw\23-1022-S4_rpt_CAO_5-31-24.pdf`  ·  5028.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | City of Los Angeles |
| Invoice date | 2024-05-31 |
| Billed amount | $259000000.00 |
| Deliverables | Funding and expanding housing, outreach, and supportive services for persons experiencing homelessness (PEH); Facilitating data-sharing and other forms of collaboration; Reimbursement for interim housing beds (up to 3,100 units) established under the Alliance Settlement Agreement; Provision of Mainstream Services to clients in interim housing beds; Contracting for and funding permanent supportive housing (PSH) services for PSH units (up to 10,200 units); Assignment of Multi-Disciplinary Teams (MDTs) and Homeless Outreach and Mobile Engagement (HOME) teams for outreach in the City; Provision of access to County DMH, DHS, DPSS, and DPH services for City-funded outreach teams; Collection and provision of MDT outreach data on a quarterly basis; Provision of access to City-funded outreach teams to refer City PEH to Homeless Initiative-funded unlicensed high service need interim housing beds; Prioritization of PEH in City-funded interim housing for County Homeless Initiative-funded unlicensed high service need interim housing beds; Prioritization of placement for City PEH exiting County Homeless Initiative-funded unlicensed high service need interim housing beds for City interim housing beds; Process for City PEH to access existing and new mental health and Substance Use Disorder (SUD) beds; Prioritization of City PEH in selection process for City PSH placements; Prioritization of referrals of PEH in the City to PSH placements in project-based units; Discussions on strategic maximization of local homeless and housing revenue sources; Provision of land inventory for the creation of new interim or permanent housing units |
| Confidence | medium |
| Notes | This document is an inter-departmental correspondence regarding a Memorandum of Understanding (MOU), not a standard invoice. The 'vendor' is identified as the City of Los Angeles because the document describes the County allocating funds to the City and the City invoicing the County. The 'invoice_date' is the date of the correspondence itself. The 'billed_amount' is stated as a 'not to exceed' allocation for interim housing bed rates under the MOU. Deliverables are summarized from the detailed services and responsibilities outlined in the MOU. |

## ABrighterDay_MHBeds_Oct2024

**Source:** `data\la_alliance\raw\ABrighterDay_MHBeds_Oct2024.pdf`  ·  510.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | 19KU A BRIGHTER DAY - BRANDY HOUSE |
| Invoice date | 2024-12-19 |
| Billed amount | — |
| Deliverables | LIFE SUPPORT; TRANSITIONAL RESIDENTIAL- ADULT 18-64; TCM; ORAL MEDICATION ADMIN; ADULT RESIDENTIAL-GERIATRIC 65+, NON-MC; ADULT RESIDENTIAL- GERIATRIC 65+ |
| Confidence | medium |
| Notes | The document is a summary of claims for October 2024, submitted as of 12/19/2024. The 'invoice_date' is extracted as this submission date for the summary document. No single 'billed_amount' for the entire document (total of all claims) is present, so it is returned as null. Deliverables are extracted directly from the 'service_value' column. Note that 'ADULT RESIDENTIAL-GERIATRIC 65+, NON-MC' and 'ADULT RESIDENTIAL- GERIATRIC 65+' are listed as separate deliverables due to differences in spacing and wording as stated in the OCR output. |

## Del Amo Hospital Acute Inpatient Invoice Feb 2025

**Source:** `data\la_alliance\raw\Del Amo Hospital Acute Inpatient Invoice Feb 2025.pdf`  ·  762.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Del Amo Hospital- IMD Exclusion |
| Invoice date | — |
| Billed amount | $1198800.00 |
| Deliverables | Acute Amount Claimed; Admin Amount Claimed |
| Confidence | medium |
| Notes | Invoice date is not explicitly stated. 'CLAIM PERIOD Feb-25' indicates a billing period but is not a specific invoice date in YYYY-MM-DD format. The date '12/11/2025' is an administration approval date, not the invoice date. |

## Del Amo Hospital Acute Inpatient Invoice Mar 2025

**Source:** `data\la_alliance\raw\Del Amo Hospital Acute Inpatient Invoice Mar 2025.pdf`  ·  940.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Del Amo Hospital- Exclusion |
| Invoice date | 2025-05-09 |
| Billed amount | $1459650.00 |
| Deliverables | Acute Amount Claimed; Admin Amount Claimed |
| Confidence | medium |
| Notes | Invoice date was extracted from the 'FOR IMD ADMINISTRATION USE ONLY' section (5/9/2025), which may represent an approval date rather than the invoice issue date. No explicit 'Invoice Date' field was found on the document. The 'CLAIM PERIOD' is Mar-25, which is a period and not a specific date. |

## DWC_SupportiveServices_Oct2024

**Source:** `data\la_alliance\raw\DWC_SupportiveServices_Oct2024.pdf`  ·  491.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Downtown Women's Center |
| Invoice date | 11/12/2024 |
| Billed amount | $111780.00 |
| Deliverables | ARPA; D7; DHS; SAM; MHSA |
| Confidence | high |
| Notes | The deliverables are extracted from the 'Fund' categories listed in the 'BILLING SUMMARY' on page 26, which represent the distinct service categories or programs for which costs are reported. The document also includes a separate 'NOTIFICATION OF PAYMENT RECOVERY DUE TO DISALLOWED COSTS' on pages 27-28, which details a recovery amount ($4,398.75) that is distinct from the billed amount for this invoice report. |

## HeritageClinic_SupportiveServices_Oct2024

**Source:** `data\la_alliance\raw\HeritageClinic_SupportiveServices_Oct2024.pdf`  ·  14684.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Heritage Clinic |
| Invoice date | 2024-11-12 |
| Billed amount | $253833.75 |
| Deliverables | ARPA; CFCI 2; D7; PHK (D7); MHSA; SRAP |
| Confidence | high |
| Notes | — |

## invoice_1_sliced

**Source:** `data\la_alliance\raw\invoice_1_sliced.pdf`  ·  42.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Sliced Invoices |
| Invoice date | 2016-01-25 |
| Billed amount | $93.50 |
| Deliverables | Web Design |
| Confidence | high |
| Notes | — |

## invoice_2

**Source:** `data\la_alliance\raw\invoice_2.pdf`  ·  938.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Ocean Discovery Institute |
| Invoice date | September 29, 2025 |
| Billed amount | — |
| Deliverables | INDEPENDENT AUDITOR'S REPORT; Statement of Financial Position; Statement of Activities; Statement of Functional Expenses; Statement of Cash Flows; Notes to Financial Statements |
| Confidence | low |
| Notes | The attached file is an Audited Financial Statement, not an invoice or billing document. Therefore, 'billed_amount' is null. 'Vendor' was extracted as 'Ocean Discovery Institute' as it is the service provider whose financials are being audited, though the document does not explicitly state it is a 'homeless-service provider'. 'Invoice_date' is the date of the Independent Auditor's Report. 'Deliverables' are the components of the audit report as listed in the Table of Contents. |

## invoice_2_financials

**Source:** `data\la_alliance\raw\invoice_2_financials.pdf`  ·  938.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | MUNGER & COMPANY, CPAS |
| Invoice date | September 29, 2025 |
| Billed amount | — |
| Deliverables | INDEPENDENT AUDITOR'S REPORT; FINANCIAL STATEMENTS; Statement of Financial Position; Statement of Activities; Statement of Functional Expenses; Statement of Cash Flows; Notes to Financial Statements |
| Confidence | medium |
| Notes | The document is an Audited Financial Statements report issued by MUNGER & COMPANY, CPAS for Ocean Discovery Institute, not a standard invoice. The total billed amount for the audit service is not explicitly stated as a line item in this document. The document's content (science education non-profit audit) does not align with the prompt's description of a 'homeless-service provider submitted to Los Angeles County'. |

## invoice_3_990

**Source:** `data\la_alliance\raw\invoice_3_990.pdf`  ·  1421.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | INSIGHT GARDEN PROGRAM |
| Invoice date | 2023-11-15 |
| Billed amount | $1928947.00 |
| Deliverables | WITH AN EVIDENCE-BASED "INNERX AND "OUTER" GARDENING APPROACH TO CHANGE, THE IGP DOES THE ESSENTIAL WORK OF PROVIDING PEOPLE IN PRISON WITH INTEGRATED VOCATIONAL AND LIFE SKILLS, FACILITATING THEIR TRANSFORMATION FROM THE "INSIDE-OUT" SO THEY BECOME PRODUCTIVE MEMBERS OF SOCIETY WHEN THEY LEAVE PRISON; IN-PRISON PROGRAMS: IGP OFFERS EVIDENCE-BASED IN-PRISON PROGRAMS IN ELEVEN PRISONS THROUGHOUT CALIFORNIA, TWO IN INDIANA, AND ONE IN OHIO, SERVING MEN, WOMEN, AND YOUTH.; RE-ENTRY: BUILDING ON INSIGHT GARDEN PROGRAM'S IN-PRISON WORK, IGP WILL PILOT THE WARM HAND-OFF REENTRY SERVICES PROGRAM WITH PEOPLE IN FOUR PRISONS AND RETURNING TO 14 CALIFORNIA COUNTIES. WITH THIS PROGRAM IGP WILL REACH PEOPLE THROUGH IN PRISON REACH-IN SERVICES, THROUGH IMMEDIATE GATE AND 24-HOUR WARM HAND-OFF RAPID RESPONSE SERVICES, AND THROUGH LONG-TERM WARM HAND-OFF SERVICES. THIS INITIATIVE WILL SIGNIFICANTLY REDUCE RECIDIVISM AND IMPROVE HOUSING, EMPLOYMENT, FINANCIAL, HEALTH, AND LEGAL OUTCOMES FOR PEOPLE WHILE INCARCERATED, UPON RELEASE, AND AS THEY REENTER CALIFORNIA COMMUNITIES. |
| Confidence | medium |
| Notes | The attached file is a Form 990, Return of Organization Exempt From Income Tax, not a typical invoice or billing document. 'Invoice_date' has been interpreted as the document's signature/filing date (2023-11-15). The tax year for which this return applies ended on 2022-12-31. 'Billed_amount' has been interpreted as the 'Total revenue' reported in Part I, line 12 of the Form 990, as this represents the total funds received by the organization. 'Deliverables' are extracted from the organization's mission statement and program service accomplishments. |

## LAFH_SupportiveServices_Oct2024

**Source:** `data\la_alliance\raw\LAFH_SupportiveServices_Oct2024.pdf`  ·  1803.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Family Housing (LAFH) |
| Invoice date | 2024-11-01 |
| Billed amount | $491538.75 |
| Deliverables | D7; PHK (D7); SAM; D7 Flex; DHS; MHSA |
| Confidence | high |
| Notes | The invoice date '11/1/24' was converted to ISO YYYY-MM-DD format. Deliverables were extracted from the 'BILLING SUMMARY' section on page 64, representing the top-level categories of funds/services that contribute to the total billed amount, as no detailed line-item service descriptions with individual costs were present on a single page summary. |

## Landmark Invoice Apr 2025 SNF-STP

**Source:** `data\la_alliance\raw\Landmark Invoice Apr 2025 SNF-STP.pdf`  ·  1366.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services Inc. |
| Invoice date | 2025-04-30 |
| Billed amount | $600256.82 |
| Deliverables | Daily Rate Service; Category I - Access to Care; Category II - Physical Patch; Category III - Behavioral Patch; Category IV - Other |
| Confidence | high |
| Notes | The invoice date is derived from the 'CLAIM PERIOD' (Apr-25) and the 'Svc Thru' date (4/30/2025) as a specific invoice date is not explicitly present; the end of the service period is used. |

## Landmark Invoice Aug 2025 SNF-STP

**Source:** `data\la_alliance\raw\Landmark Invoice Aug 2025 SNF-STP.pdf`  ·  625.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services, Inc. |
| Invoice date | 2025-09-10 |
| Billed amount | $644740.96 |
| Deliverables | PATCHES:; Retro SOC |
| Confidence | high |
| Notes | The century for the invoice date '9/10/25' was inferred as 2025 based on the '9/30/2025' date present on the document. |

## Landmark Invoice Feb 2025 SNF-STP

**Source:** `data\la_alliance\raw\Landmark Invoice Feb 2025 SNF-STP.pdf`  ·  589.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services Inc. |
| Invoice date | 2025-04-08 |
| Billed amount | $562305.21 |
| Deliverables | AMOUNT CLAIMED; RETRO SOC; PATCHES |
| Confidence | high |
| Notes | — |

## Landmark Invoice Jan 2025 SNF-STP

**Source:** `data\la_alliance\raw\Landmark Invoice Jan 2025 SNF-STP.pdf`  ·  801.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services Inc. |
| Invoice date | — |
| Billed amount | $608077.15 |
| Deliverables | Access to Care; Physical Patch; Behavorial Patch; Other; RETRO SOC; PATCHES |
| Confidence | high |
| Notes | invoice_date is null because an explicit invoice issuance date is not present on the document. Dates found are for the claim period (Jan-25) and various approval signatures (1/19/25, 2/25/25), but not the invoice date itself. Vendor name 'Landmark Medical Services Inc.' was chosen over 'Landmark Med Ctr' as it appeared in the 'MAKE CHECK' section on page 3, indicating the full payee name. |

## Landmark Invoice Jul 2025 SNF-STP

**Source:** `data\la_alliance\raw\Landmark Invoice Jul 2025 SNF-STP.pdf`  ·  643.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services, Inc. |
| Invoice date | Jul-25 |
| Billed amount | $630801.56 |
| Deliverables | Category I - Access to Care; Category II - Physical Patch; Category III - Behavorial Patch; Category IV - Other |
| Confidence | high |
| Notes | Invoice date 'Jul-25' is used as printed because a specific day (DD) is not determinable to convert to YYYY-MM-DD format. Deliverables are extracted from the service categories listed on page 3, as these represent the line-item services. |

## Landmark Invoice Jun 2025 SNF-STP

**Source:** `data\la_alliance\raw\Landmark Invoice Jun 2025 SNF-STP.pdf`  ·  612.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services Inc. |
| Invoice date | 2025-07-30 |
| Billed amount | $604978.73 |
| Deliverables | Category I - Access to Care; Category II - Physical Patch; Category III - Behavioral Patch; Category IV - Other; RETRO SOC PAYMENT |
| Confidence | high |
| Notes | — |

## Landmark Invoice Mar 2025 SNF-STP

**Source:** `data\la_alliance\raw\Landmark Invoice Mar 2025 SNF-STP.pdf`  ·  1386.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services Inc. |
| Invoice date | 2025-04-21 |
| Billed amount | $589946.25 |
| Deliverables | Category I - Access to Care; Category II - Physical Patch; Category III - Behavorial Patch; Category IV - Other; RETRO SOC; PATCHES |
| Confidence | high |
| Notes | Invoice date is taken from the Administrator/Operator's signature date (4/21/25) as no explicit 'Invoice Date' field exists. Vendor name chosen from 'MAKE CHECK PAYABLE TO:' field, as other variations exist on the document. The approval signature date '4/21/28' appears to be a typo compared to other dates. |

## Landmark Invoice May 2025 SNF-STP

**Source:** `data\la_alliance\raw\Landmark Invoice May 2025 SNF-STP.pdf`  ·  1393.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services Inc. |
| Invoice date | 2025-06-10 |
| Billed amount | $614718.34 |
| Deliverables | Access to Care; Physical Patch; Behavorial Patch; Other; RETRO SOC; PATCHES |
| Confidence | high |
| Notes | The vendor name was taken from the 'MAKE CHECK PAYABLE TO:' field on page 3, which is more specific than 'PROVIDER NAME' on page 1. The invoice date is derived from the earliest signature dates (6/10/25) on the 'PAYMENT REQUEST SUMMARY' which relate to the preparation and certification of the claim for the 'CLAIM PERIOD May-25'. The billed amount is taken from 'NET BILLING' under 'TOTAL CLAIMED' and 'APPROVED CLAIM AMOUNT', which are consistent. Deliverables are extracted from the distinct line items and categories contributing to the billed amount across both pages. |

## Landmark Invoice Oct 2025 SNF-STP

**Source:** `data\la_alliance\raw\Landmark Invoice Oct 2025 SNF-STP.pdf`  ·  645.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services, Inc. |
| Invoice date | 2025-11-26 |
| Billed amount | $680492.82 |
| Deliverables | AMOUNT CLAIMED; PATCHES; Retro SOC |
| Confidence | high |
| Notes | The invoice date is taken as the IMD administration approval date, which is the latest date on the document signifying its finalization. Deliverables are extracted as the main line items from the 'PAYMENT REQUEST SUMMARY' table. |

## Landmark Invoice Sept 2025 SNF-STP

**Source:** `data\la_alliance\raw\Landmark Invoice Sept 2025 SNF-STP.pdf`  ·  952.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services, Inc. |
| Invoice date | — |
| Billed amount | $633265.66 |
| Deliverables | AMOUNT CLAIMED; PATCHES:; Retro SOC |
| Confidence | medium |
| Notes | A specific invoice date (YYYY-MM-DD) is not present. 'Sep-25' is noted as a CLAIM PERIOD, and other dates (10/15/25, 10/29/2025) are signature/approval dates, not the invoice date itself. |

## MentalHealthAmerica_SupportiveServices_Oct2024

**Source:** `data\la_alliance\raw\MentalHealthAmerica_SupportiveServices_Oct2024.pdf`  ·  305.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Mental Health America (MHA), Long Beach |
| Invoice date | 11/4/2024 |
| Billed amount | $269013.75 |
| Deliverables | ARPA/FHSP; D7; DHS; SAM; Housing for Healthy CA; D7 Flex; HFMH (D7); MHSA |
| Confidence | high |
| Notes | — |
