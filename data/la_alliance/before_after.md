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
| Notes | The document is an official Los Angeles City Council action report, not an invoice or billing document from a homeless-service provider. As such, 'vendor', 'billed_amount', and 'deliverables' (as line-item services) are not present. |

## 23-1022-S4_caf_6-21-24

**Source:** `data\la_alliance\raw\23-1022-S4_caf_6-21-24.pdf`  ·  101.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | — |
| Invoice date | — |
| Billed amount | — |
| Deliverables | — |
| Confidence | low |
| Notes | The document provided is an official action record of the Los Angeles City Council, not an invoice or billing document from a homeless-service provider. As such, fields like vendor (billing organization), invoice date, billed amount, and line-item deliverables are not present on this document. The 'Agenda Description' describes the subject of the council action, not services being billed. |

## 23-1022-S4_rpt_CAO_5-31-24

**Source:** `data\la_alliance\raw\23-1022-S4_rpt_CAO_5-31-24.pdf`  ·  5028.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | City of Los Angeles |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Reimbursement for interim housing bed rates; Mainstream Services for clients in interim housing beds; Permanent Supportive Housing (PSH) services; Multi-Disciplinary Teams (MDTs) and Homeless Outreach and Mobile Engagement (HOME) teams outreach services; Access to County Department of Mental Health (DMH), Department of Health Services (DHS), Department of Public Social Services (DPSS), and Department of Public Health (DPH) services for City-funded outreach teams; Access to Homeless Initiative-funded unlicensed high service need interim housing beds; Prioritization of PEH in City-funded interim housing for County Homeless Initiative-funded unlicensed high service need interim housing beds; Access to existing and new mental health and Substance Use Disorder (SUD) beds; Prioritization of Housing Placements for City PEH; Partnership on City-/County Owned Land for the creation of new interim or permanent housing units |
| Confidence | low |
| Notes | This document is an inter-departmental correspondence from the City of Los Angeles to its City Council regarding a Memorandum of Understanding (MOU) between the County of Los Angeles and the City of Los Angeles. It is not an invoice or billing document from a homeless-service provider submitted to Los Angeles County as specified in the prompt. Therefore, 'invoice_date' and 'billed_amount' are null as they do not exist on this document. The 'vendor' is identified as the 'City of Los Angeles' as it is the entity responsible for invoicing the County for certain services as outlined in the MOU. The 'deliverables' are extracted from the services and responsibilities detailed in the MOU, rather than line items on an invoice. |

## 23-1022-S4_rpt_cao_2-24-25

**Source:** `data\la_alliance\raw\23-1022-S4_rpt_cao_2-24-25.pdf`  ·  2431.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CITY OF LOS ANGELES |
| Invoice date | 2025-02-24 |
| Billed amount | — |
| Deliverables | — |
| Confidence | low |
| Notes | The attached document is an 'Inter-Departmental Correspondence' report from the City of Los Angeles to its City Council, not an invoice or billing document from a homeless-service provider submitted to Los Angeles County as specified in the prompt. Therefore, 'billed_amount' and 'deliverables' (in a billing context) are not present. The 'vendor' is identified as the originating organization of this correspondence as stated on the document's letterhead. The 'invoice_date' is taken from the 'Date' field on the first page. No line-item services/deliverables for billing are stated in this document. |

## ABrighterDay_MHBeds_Oct2024

**Source:** `data\la_alliance\raw\ABrighterDay_MHBeds_Oct2024.pdf`  ·  510.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | 19KU A BRIGHTER DAY - BRANDY HOUSE |
| Invoice date | 2024-12-19 |
| Billed amount | — |
| Deliverables | LIFE SUPPORT; TRANSITIONAL RESIDENTIAL- ADULT 18-64; TCM; ORAL MEDICATION ADMIN; ADULT RESIDENTIAL-GERIATRIC 65+, NON-MC |
| Confidence | medium |
| Notes | The document is a claims report for services rendered in October 2024, submitted as of 12/19/2024, not a single invoice. Therefore, a single 'billed_amount' (total) is not explicitly stated on the document and has been returned as null to avoid inference. The 'invoice_date' reflects the document's stated submission date (12/19/2024). |

## DWC_SupportiveServices_Oct2024

**Source:** `data\la_alliance\raw\DWC_SupportiveServices_Oct2024.pdf`  ·  491.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Downtown Women's Center |
| Invoice date | 2024-11-12 |
| Billed amount | $111780.00 |
| Deliverables | ARPA; D7; DHS; SAM; MHSA |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE SUBMITTED' on page 1. Deliverables are the 'Fund' categories from the 'BILLING SUMMARY' table on page 26, as these represent the line-item categories for which costs are incurred. |

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

## LAFH_SupportiveServices_Oct2024

**Source:** `data\la_alliance\raw\LAFH_SupportiveServices_Oct2024.pdf`  ·  1803.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Family Housing (LAFH) |
| Invoice date | 2024-11-01 |
| Billed amount | $491538.75 |
| Deliverables | D7 Program Slots; PHK (D7) Program Slots; SAM Program Slots; D7 Flex Program Slots; DHS Program Slots; MHSA Program Slots |
| Confidence | high |
| Notes | Invoice date was extracted from 'DATE SUBMITTED'. Billed amount was extracted from 'AMOUNT REQUESTED' and confirmed by the 'Total Cost' in the 'BILLING SUMMARY'. Deliverables are derived from the 'Fund' categories listed in the 'BILLING SUMMARY' which aggregate vacant and occupied slot costs. |

## MentalHealthAmerica_SupportiveServices_Oct2024

**Source:** `data\la_alliance\raw\MentalHealthAmerica_SupportiveServices_Oct2024.pdf`  ·  305.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Mental Health America (MHA), Long Beach |
| Invoice date | 2024-11-04 |
| Billed amount | $269013.75 |
| Deliverables | ARPA/FHSP; D7; DHS; SAM; Housing for Healthy CA; D7 Flex; HFMH (D7); MHSA |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE SUBMITTED' on page 1. Deliverables are summarized from the 'BILLING SUMMARY' section on page 48 under the 'Fund' column, representing distinct categories of services/funds billed. |

## PATH_SupportiveServices_Oct2024

**Source:** `data\la_alliance\raw\PATH_SupportiveServices_Oct2024.pdf`  ·  1253.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | PATH |
| Invoice date | 2024-11-06 |
| Billed amount | $980662.50 |
| Deliverables | ARPA; ARPA/FHSP; D7; D2; D7 Flex; DHS; SAM; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA; PHK (D7); SRAP |
| Confidence | high |
| Notes | — |

## StarView_RanchoLosAmigos_MHBeds_Oct2024

**Source:** `data\la_alliance\raw\StarView_RanchoLosAmigos_MHBeds_Oct2024.pdf`  ·  804.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | 19JM STAR VIEW RANCHO LOS AMIGOS CRTP |
| Invoice date | 2024-12-19 |
| Billed amount | — |
| Deliverables | CRISIS RESIDENTIAL ADULT 18-64; LIFE SUPPORT; E&M OP, ESTAB CLT, 40-54M VID; ORAL MEDICATION ADMIN; E&M OP, ESTAB CLT, 20-29M VID; E&M OP, ESTAB CLT,30-39M VID; TCM; TARGETED CASE MGMT: PHONE; E&M OP, ESTAB CLT, 10-19M VID; CRISIS RESIDENTIAL ADULT 18-64 NON-MC; E&M OP, ESTAB CLIENT, 40+MIN (NON MC); TCM NON-MC; ORAL MEDICATION ADMIN (NON MC); E&M OP, ESTAB CLIENT, 25-39MIN (NON MC) |
| Confidence | high |
| Notes | The document is a report of claims submitted on 12/19/2024, which is used as the invoice_date. No single 'billed_amount' or total is explicitly stated on the document; calculation would be required, which is not permitted, hence it is returned as null. |

## TarzanaTreatment_SUD_Oct2024

**Source:** `data\la_alliance\raw\TarzanaTreatment_SUD_Oct2024.pdf`  ·  317.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TARZANA TREATMENT CENTERS INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | No single 'invoice_date' is explicitly stated on the document. The document header indicates the services are for 'October 2024'. No grand total 'billed_amount' is present on the document; only individual line item charges are listed. |

## ValleyStar_LACUSC_MHBeds_Oct2024

**Source:** `data\la_alliance\raw\ValleyStar_LACUSC_MHBeds_Oct2024.pdf`  ·  757.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | 19KP VALLEY STAR LAC-USC CRTP |
| Invoice date | — |
| Billed amount | $430561.73 |
| Deliverables | CRISIS RESIDENTIAL ADULT 18-64; LIFE SUPPORT; E&M OP, ESTAB CLT, 30-39M VID; ORAL MEDICATION ADMIN; E&M OP, ESTAB CLT, 40-54M VID; TCM; E&M OP, ESTAB CLT, 20-29M VID; CRISIS RESIDENTIAL ADULT 18-64 NON-MC; E&M OP, ESTAB CLIENT, 15-24MIN (NON MC); E&M OP, ESTAB CLIENT, 25-39MIN (NON MC); E&M OP, ESTAB CLT, 10-19M VID |
| Confidence | high |
| Notes | The document is a claims report for October 2024, not a single invoice. Therefore, a single 'invoice_date' is not present. The 'billed_amount' is the sum of all 'ContractedRate' values across all pages of the document. The date '12/19/2024' is stated as the submission date for the claims report. |

## WeingartCenter_SupportiveServices_Oct2024

**Source:** `data\la_alliance\raw\WeingartCenter_SupportiveServices_Oct2024.pdf`  ·  9727.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Weingart Center Association |
| Invoice date | 2024-11-07 |
| Billed amount | $243656.25 |
| Deliverables | D7; PHK (D7); D7 Flex; DHS |
| Confidence | high |
| Notes | — |

## invoice_1_sliced

**Source:** `data\la_alliance\raw\invoice_1_sliced.pdf`  ·  42.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | DEMO - Sliced Invoices |
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
| Invoice date | 2024-12-31 |
| Billed amount | — |
| Deliverables | — |
| Confidence | low |
| Notes | The document is an Audited Financial Statement for Ocean Discovery Institute for the year ended December 31, 2024, not an invoice or billing document. As such, there is no 'billed_amount' or specific 'deliverables' in the context of a client billing. The 'invoice_date' field is populated with the 'as of' date for the financial statements. |

## invoice_2_financials

**Source:** `data\la_alliance\raw\invoice_2_financials.pdf`  ·  938.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | MUNGER & COMPANY, CPAS |
| Invoice date | 2025-09-29 |
| Billed amount | — |
| Deliverables | INDEPENDENT AUDITOR'S REPORT; Audited Financial Statements; Statement of Financial Position; Statement of Activities; Statement of Functional Expenses; Statement of Cash Flows; Notes to Financial Statements |
| Confidence | medium |
| Notes | The document is an audit report issued by MUNGER & COMPANY, CPAS, not an invoice for their services. The 'billed_amount' for MUNGER & COMPANY, CPAS is not explicitly stated on the document. While 'Professional fees' are listed as an expense of Ocean Discovery Institute on page 6, this is a general category and does not specifically detail the amount billed by MUNGER & COMPANY, CPAS for this audit. |

## invoice_3_990

**Source:** `data\la_alliance\raw\invoice_3_990.pdf`  ·  1421.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | INSIGHT GARDEN PROGRAM |
| Invoice date | 2023-11-15 |
| Billed amount | $1928947.00 |
| Deliverables | WITH AN EVIDENCE-BASED "INNERX AND "OUTER" GARDENING APPROACH TO CHANGE, THE IGP DOES THE ESSENTIAL WORK OF PROVIDING PEOPLE IN PRISON WITH INTEGRATED VOCATIONAL AND LIFE SKILLS, FACILITATING THEIR TRANSFORMATION FROM THE "INSIDE-OUT" SO THEY BECOME PRODUCTIVE MEMBERS OF SOCIETY WHEN THEY LEAVE PRISON; IN-PRISON PROGRAMS: IGP OFFERS EVIDENCE-BASED IN-PRISON PROGRAMS IN ELEVEN PRISONS THROUGHOUT CALIFORNIA, TWO IN INDIANA, AND ONE IN OHIO, SERVING MEN, WOMEN, AND YOUTH.; RE-ENTRY: BUILDING ON INSIGHT GARDEN PROGRAM'S IN-PRISON WORK, IGP WILL PILOT THE WARM HAND-OFF REENTRY SERVICES PROGRAM WITH PEOPLE IN FOUR PRISONS AND RETURNING TO 14 CALIFORNIA COUNTIES. WITH THIS PROGRAM IGP WILL REACH PEOPLE THROUGH IN PRISON REACH-IN SERVICES, THROUGH IMMEDIATE GATE AND 24-HOUR WARM HAND-OFF RAPID RESPONSE SERVICES, AND THROUGH LONG-TERM WARM HAND-OFF SERVICES. THIS INITIATIVE WILL SIGNIFICANTLY REDUCE RECIDIVISM AND IMPROVE HOUSING, EMPLOYMENT, FINANCIAL, HEALTH, AND LEGAL OUTCOMES FOR PEOPLE WHILE INCARCERATED, UPON RELEASE, AND AS THEY REENTER CALIFORNIA COMMUNITIES. |
| Confidence | medium |
| Notes | The document provided is a Form 990 (Return of Organization Exempt From Income Tax), not a traditional invoice or billing document. Therefore, 'invoice_date' and 'billed_amount' are interpreted from the available financial reporting data. 'Invoice date' is extracted as the signature date of the return (2023-11-15). 'Billed amount' is extracted as the 'Total revenue' for the current year (Line 12, Part I Summary, and Line 12, Part VIII Statement of Revenue), which is the closest analogous value for total funds associated with services in this document type. No specific 'billed amount' is present on this document. |
