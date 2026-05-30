# LA Alliance Invoices — Before / After

Left: an unstructured scanned invoice the county published as a PDF.
Right: the normalized ledger row our agent extracted autonomously.

## A BRIGHTER DAY CRTP - Aug 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207775_ABRIGHTERDAYCRTP-Aug2025.pdf`  ·  477.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | 19KU A BRIGHTER DAY - BRANDY HOUSE |
| Invoice date | — |
| Billed amount | — |
| Deliverables | TRANSITIONAL RESIDENTIAL- ADULT 18-64; ORAL MEDICATION ADMIN; TCM; COORDINATION OF CARE; E&M OP, ESTAB CLIENT, 25-39MIN; LIFE SUPPORT; ADULT RESIDENTIAL- GERIATRIC 65+ |
| Confidence | high |
| Notes | No single invoice date (YYYY-MM-DD format) is explicitly stated on the document. 'Claims for August 2025' indicates the service period, and 'November 25, 2025' is noted as the report's accuracy date, not an invoice date. No total billed amount for the entire document is present; only individual line item rates are listed. |

## Beit Tshuvah - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202204_BeitTshuvah-RecoveryBridgeHousing-November2025.pdf`  ·  217.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Belt Tuvah |
| Invoice date | — |
| Billed amount | $6440.00 |
| Deliverables | Recovery Bridge Housing (H0034) |
| Confidence | high |
| Notes | The document is a spreadsheet detailing services over a period, not a single invoice with an explicit invoice date. The 'invoice_date' field is null because no clear single invoice issuance date was present. The title 'November 2025' appears to indicate a reporting period, while the actual service dates are in November 2024. The billed_amount was calculated by summing the 'Total Charge' for all 80 line items ($80.50 each). |

## Beit Tshuvah - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202223_BeitTshuvah-RecoveryBridgeHousing-October2025.pdf`  ·  218.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | BEIT TSHUVAH |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | No single invoice date was explicitly stated; only a range of 'Date of Service' entries and a monthly header 'October 2025'. No explicit 'total billed amount' was stated; calculating a sum from line items would be an inference, which is not permitted by the instructions. |

## Beit Tshuvah - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202163_BeitTshuvah-RecoveryBridgeHousing-October2025.pdf`  ·  218.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | BEIT TSHUVAH |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | invoice_date is null because the document is a statement of services for a period (October 2025) rather than a single invoice with a specific invoice date for the entire document. billed_amount is null because a grand total amount is not explicitly stated or summed on the document, only individual line item charges are provided. |

## Beit Tshuvah - Recovery Bridge Housing - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200976_BeitTshuvah-RecoveryBridgeHousing-September2025.pdf`  ·  219.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | BEIT TSHUVAH |
| Invoice date | — |
| Billed amount | $1815.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a statement of services for the month of September 2025. A single 'invoice_date' is not present; instead, there are individual 'Date of Service' entries for each day in September 2025. The billed_amount is calculated by summing all 30 daily charges of $60.50. |

## Building Bridges - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201011_BuildingBridges-October2025-Redacted.pdf`  ·  443.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Building Bridges Consultant |
| Invoice date | 2025-11-05 |
| Billed amount | $19370.64 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | The invoice date is derived from the latest signature date on the document (11/5/2025). The billing period is stated as October 2025. |

## Building Bridges - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200995_BuildingBridges-September2025-Redacted.pdf`  ·  367.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Building Bridges Consultant |
| Invoice date | 2025-10-07 |
| Billed amount | $19288.80 |
| Deliverables | Base Rate; Housing Navigation; LVN or Equivalent; MH Clinician |
| Confidence | high |
| Notes | Invoice date inferred from the latest signature date on the document, as a specific 'Invoice Date' field was not present. 'Billing Month/Year' indicates the service period. |

## Building Bridges - November 2025 

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207776_BuildingBridges-November2025-Redacted.pdf`  ·  762.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Building Bridges Consultant |
| Invoice date | 2025-11-30 |
| Billed amount | $18487.20 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician |
| Confidence | medium |
| Notes | The invoice date was not explicitly labeled. The date '2025-11-30' was extracted from the certification date on page 3, which aligns with the end of the 'November 2025' billing period. Other signature dates of '2025-12-09' are also present but are later than the certification for the billing period. |

## Butterfly's Haven - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201012_Butterfly_sHaven-October2025-Redacted.pdf`  ·  939.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Butterfly's Haven |
| Invoice date | 2025-11-05 |
| Billed amount | $329005.48 |
| Deliverables | Individual Beds (Base Rate); Individual Beds (Housing Navigation); Individual Beds (LVN or Equivalent); Family Units (Base Rate); Family Units (Housing Navigation); Family Units (LVN or Equivalent) |
| Confidence | high |
| Notes | The invoice date was chosen as the latest signature date (11/05/2025) as two different signature dates (11/04/2025 and 11/05/2025) are present across the document pages. The vendor name 'Butterfly's Haven' was chosen based on pages 2 and 3, clarifying 'Carlton Village' as a site name rather than part of the primary vendor name. Deliverables were extracted from the 'Invoice Category' columns on pages 2 and 3, prefixed with the corresponding 'Site Name' for context. |

## Butterfly's Haven - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200996_Butterfly_sHaven-September2025-Redacted.pdf`  ·  5178.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Butterfly's Haven |
| Invoice date | 2025-10-08 |
| Billed amount | $303046.52 |
| Deliverables | Individual Beds; Family Units; Base Rate; Housing Navigation; LVN or Equivalent |
| Confidence | high |
| Notes | Invoice date was taken from the signature dates on the cover sheet (page 1), as it represents the approval date for the September 2025 billing period. Deliverables were consolidated from the cover sheet and detailed claim pages. |

## Butterfly's Haven - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207777_Butterfly_sHaven-November2025-Redacted.pdf`  ·  1292.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Butterfly's Haven |
| Invoice date | 2025-12-03 |
| Billed amount | $318392.40 |
| Deliverables | Individual Beds - Base Rate; Individual Beds - Housing Navigation; Individual Beds - LVN or Equivalent; Family Units - Base Rate; Family Units - Housing Navigation; Family Units - LVN or Equivalent |
| Confidence | high |
| Notes | The provider name on page 1 included 'Carlton Village' which is clarified as a site name on subsequent pages, so only 'Butterfly's Haven' was used for the vendor. The invoice date is derived from the signature date on the cover sheet, as no explicit 'Invoice Date' field exists, and 'Billing Month/Year' refers to the service period. The deliverables were combined from the high-level categories on page 1 and the detailed line items on pages 2 and 3. |

## Chances 4 Change - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201013_Chances4Change-October2025-Redacted.pdf`  ·  339.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Chances 4 Change |
| Invoice date | 2025-11-04 |
| Billed amount | $42359.64 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | — |

## Chances 4 Change - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200997_Chances4Change-September2025-Redacted.pdf`  ·  503.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Chances 4 Change |
| Invoice date | — |
| Billed amount | $46621.20 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent; July 2025 Reimbursment; August 2025 Reimbursment |
| Confidence | high |
| Notes | The document provides 'Billing Month/Year: September 2025' but no field explicitly labeled 'invoice_date', so it is returned as null. The vendor name appears as 'Chances 4 Change' consistently on pages 1 and 2 under 'Provider Name', while page 3 shows 'Chances 4 Change, Inc.' under 'IHP Site Name'. 'Chances 4 Change' was chosen as it is explicitly labeled 'Provider Name' on the cover sheet and summary. |

## Chances 4 Change - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207778_Chances4Change-November2025-Redacted.pdf`  ·  416.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Chances 4 Change, Inc. |
| Invoice date | 2025-12-05 |
| Billed amount | $40993.20 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | — |

## Clare Matrix - Residential - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202224_ClareMatrix-Residential-October2025.pdf`  ·  226.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CLARKE MATER |
| Invoice date | 2023-10-01 |
| Billed amount | $356074.68 |
| Deliverables | Residential addiction program, subacute detoxification (M Approved); Long Term Residential Day Rate (2023-LC); Long Term Residential Day Rate (2023-UG); Long Term Residential Day Rate (2023-US) |
| Confidence | high |
| Notes | The document is a data export/spreadsheet, not a traditional invoice. The invoice_date is inferred from the document title ("October 2023") as there's no single "invoice date" field, so the first day of the month is used. The billed_amount is calculated by summing the "Total Charge" column for all line items (842 entries of 419.79 and 10 entries of 261.77). |

## Clare Matrix - Residential - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200958_ClareMatrix-Residential-September2025.pdf`  ·  224.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CLARE MATRIX |
| Invoice date | — |
| Billed amount | $83222.17 |
| Deliverables | Residential addiction program, subacute detoxification (H) Approved; Long Term Residential Day Rate (H0019:U3) Approved |
| Confidence | high |
| Notes | invoice_date is null because the document is a spreadsheet of services with service dates (all in September 2025), not a single invoice with an invoice date. The document mentions a 'data extraction' date of 12/09/2021, but this is not an invoice date. The total billed amount was calculated by summing the 'Total Delivered' column for all 199 line items across both pages of the document. |

## Cri-Help Inc. - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202205_Cri-HelpInc.-RecoveryBridgeHousing-November2025.pdf`  ·  233.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | OH-HELP, INC. |
| Invoice date | — |
| Billed amount | $1078638.00 |
| Deliverables | Recovery Bridge Housing (P00334) |
| Confidence | high |
| Notes | A single 'invoice_date' is not present on the document. The document is a ledger of services for November 2023, extracted on 2024-01-09. The billed_amount was calculated by summing all line items (13392 entries * $80.50/entry). |

## Cri-Help Inc. - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202225_Cri-HelpInc.-RecoveryBridgeHousing-October2025.pdf`  ·  235.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRI-HELP, INC. |
| Invoice date | — |
| Billed amount | $1875.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | A specific 'invoice_date' for the entire document is not explicitly stated. The document is a data extract listing services for October 2025. The total billed amount was calculated by summing all 'Total Charge' line items (31 entries * $60.50), as no overall total was provided on the document itself. |

## Divine Healthcare Services Inc. - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202206_DivineHealthcareServicesInc.-RecoveryBridgeHousing-November2025.pdf`  ·  251.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | DIVINE HEALTHCARE SERVICES, INC. |
| Invoice date | 2024-11-30 |
| Billed amount | $17242.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The invoice date is determined as the end of the billing period, 'November 2024', indicated in the document title. The billed amount is the sum of all 'Total Charge' line items ($60.50 each) across all five pages (285 lines total). |

## Divine Healthcare Services Inc. - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202226_DivineHealthcareServicesInc.-RecoveryBridgeHousing-October2025.pdf`  ·  241.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | DIVINE HEALTHCARE SERVICES, INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The document is a service report for the month of October 2025, not a single invoice with a specific invoice date or a grand total billed amount. Each line item has a total charge, but no overall total for the document is provided. Therefore, 'invoice_date' and 'billed_amount' are null as they are not explicitly stated on the document as single values. |

## Divine Healthcare Services Inc. - Recovery Bridge Housing - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200959_DivineHealthcareServicesInc.-RecoveryBridgeHousing-September2025.pdf`  ·  247.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | DIVINE HEALTHCARE SERVICES, INC. |
| Invoice date | — |
| Billed amount | $11555.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | invoice_date is not explicitly stated. The document is a service report for September 2025, with service dates ranging from 9/1/2025 to 9/30/2025, and was generated on 11/09/2023. The billed_amount was calculated by summing 191 line items, each for $60.50, as no overall total was provided on the document itself. |

## ERC - December 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207793_ERC-December2025.pdf`  ·  383.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Brilliant Corners |
| Invoice date | — |
| Billed amount | — |
| Deliverables | PNI - Personal Needs and Incidentals; BC Subsidy; ERC - Enhanced Services; ERC Rent Subsidy In Arrears |
| Confidence | medium |
| Notes | Vendor inferred as 'Brilliant Corners' based on document overview stating DMH receives data from them as a fiscal intermediary for this billing report. Invoice date refers to a billing period ('December 2025') rather than a specific date for the entire document. No single total billed amount is present for the entire document, as it is a multi-page report detailing numerous individual transactions. |

## ERC - January 2026

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207792_ERC-January2026.pdf`  ·  385.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Brilliant Corners |
| Invoice date | — |
| Billed amount | — |
| Deliverables | PNI - Personal Needs and Incidentals; ERC - Enhanced Services; BC Subsidy; ERC Rent Subsidy In Arrears |
| Confidence | low |
| Notes | The document is a multi-page billing details summary for January 2026, submitted by Brilliant Corners to Los Angeles County (DMH), rather than a single invoice from a specific provider for a single transaction. Therefore, a specific invoice date and total billed amount for this summary document are not present. The 'vendor' is interpreted as Brilliant Corners based on the overview stating DMH receives the data from them. 'Deliverables' are extracted from the 'Subsidy Type' column, representing the categories of services/payments detailed in the report. |

## ERC - Nov. 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202162_ERC-Nov.2025.pdf`  ·  240.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Brilliant Corners |
| Invoice date | — |
| Billed amount | $683071.13 |
| Deliverables | PNI - Personal Needs and Incidentals; ERC - Enhanced Services; BC Subsidy; ERC Rent Subsidy In Arrears |
| Confidence | high |
| Notes | The document is a multi-page 'Billing Details' spreadsheet, not a single invoice with a single stated total. The 'vendor' is identified from the overview stating 'Brilliant Corners' runs the billing reconciliation report. No single 'invoice_date' is present; the document title 'November 2025 Billing Details' indicates the billing period, and all transaction dates are within November 2025. The 'billed_amount' is calculated as the sum of all 'Debit' entries minus the sum of all 'Credit*' entries across all pages, based on the overview indicating 'Debit' as subsidy payments made by Brilliant Corners and 'Credit*' as credits paid to the County. |

## ERC - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201029_ERC-October2025.pdf`  ·  245.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Brilliant Corners |
| Invoice date | — |
| Billed amount | $342681.44 |
| Deliverables | ERC - Enhanced Services; ERC Rent Subsidy In Arrears; PNI - Personal Needs and Incidentals; BC Subsidy |
| Confidence | medium |
| Notes | Invoice date 'October 2025 Billing Details' refers to the billing period, not a specific invoice issuance date, thus null is returned for ISO YYYY-MM-DD. Billed amount is the sum of all 'Debit' entries across the document, interpreting this as the total billed by the listed vendors for the period, as no single 'total billed' is explicitly stated on the document. |

## ERC - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201030_ERC-September2025.pdf`  ·  243.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Brilliant Corners |
| Invoice date | September 2025 |
| Billed amount | — |
| Deliverables | BC Subsidy; ERC Rent Subsidy In Arrears; ERC - Enhanced Services; PNI - Personal Needs and Incidentals |
| Confidence | medium |
| Notes | The vendor, Brilliant Corners, is identified as the fiscal intermediary preparing this billing reconciliation report for Los Angeles County. The invoice_date is derived from the report title, but a specific day is not present. There is no single total billed amount explicitly stated on this multi-page reconciliation report; instead, it lists numerous debit and credit transactions. The deliverables are extracted from the 'Subsidy Type' column. |

## Ella's Foundation - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201014_Ella_sFoundation-October2025-Redacted.pdf`  ·  9294.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Ella's Foundation |
| Invoice date | — |
| Billed amount | $89692.92 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | medium |
| Notes | No explicit 'Invoice Date' field found. The billing period is October 2025, and various signature dates (11/5/2025, 11/14/2025) are present, but not explicitly for the 'invoice_date' itself. |

## Ella's Foundation - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200998_Ella_sFoundation-September2025-Redacted.pdf`  ·  440.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Ella's Foundation |
| Invoice date | 2025-10-10 |
| Billed amount | $86799.60 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | The invoice date was chosen as '2025-10-10' from the Payment Invoice Cover Sheet (Page 1), which appeared as the approval date. An earlier signature date of '2025-10-07' was also present on Page 3, but the cover sheet date was considered more indicative of the invoice submission date. |

## Ella's Foundation - November 2025 - Redacted

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207779_Ella_sFoundation-November2025-Redacted.pdf`  ·  965.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Ella's Foundation |
| Invoice date | 2025-12-03 |
| Billed amount | $86799.60 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | — |

## Encompass - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201015_Encompass-October2025-Redacted.pdf`  ·  1005.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Encompass Housing - Hatfield Interim Housing |
| Invoice date | 2025-11-12 |
| Billed amount | $183792.80 |
| Deliverables | Base Rate (Beds in Single Rooms); Housing Navigation (Beds in Single Rooms); MH Clinician (Beds in Single Rooms); LVN or Equivalent (Beds in Single Rooms); Base Rate (Beds in Double Rooms); Housing Navigation (Beds in Double Rooms); MH Clinician (Beds in Double Rooms); LVN or Equivalent (Beds in Double Rooms) |
| Confidence | high |
| Notes | invoice_date is taken from the approval date on the cover sheet (page 1) as 11/12/2025, which is later than the internal approval date on page 4 (11/5/2025). The billing month is October 2025. Vendor is derived from the 'Provider Name' on the cover sheet. Deliverables are combined from the detailed line items on pages 2 and 3, grouped by bed type as indicated on page 1. |

## Encompass - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200999_Encompass-September2025-Redacted.pdf`  ·  633.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Encompass Housing - Hatfield Interim Housing |
| Invoice date | 2025-10-15 |
| Billed amount | $162403.28 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | The invoice date is derived from the signature dates on the cover sheet. The billing period for the services is September 2025. Deliverables are taken from the 'Invoice Category' line items detailed on pages 2 and 3. |

## Encompass - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207780_Encompass-November2025-Redacted.pdf`  ·  1142.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Encompass Housing |
| Invoice date | 2025-12-09 |
| Billed amount | $181872.00 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | Invoice date was determined from the latest signature date on the cover sheet (12/9/2025), as no explicit 'invoice date' field was present. The 'Billing Month/Year' refers to the service period (November 2025). |

## Exodus Recovery Inc. - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201212_ExodusRecoveryInc.-August2025.pdf`  ·  763.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Exodus Recovery, Inc |
| Invoice date | 2025-09-10 |
| Billed amount | $23690.56 |
| Deliverables | Program Manager; CM Housing-City/County Team; CM SUD-City/County Team; LVN-City/County Team; Community Worker-City/County Team; Mental Health Clinician/Team Lead - City/County Team 1/Team; EMPLOYEE BENEFITS; Client/Member Expenses; Equipment Lease; Training/Staff Development; Office Supplies, Postage, Printing; Staff Mileage/Parking; Telephone/Communications/Utilities; Purchased Services: Security; General Liability Insurance; Vehicle Maintenance & Insurance; Vehicle; Office Space; Equipment/Furniture Purchase (One Time); IT Software and Set-up (One Time); ADMINISTRATIVE OVERHEAD/COSTS @ 10% |
| Confidence | high |
| Notes | The invoice date was derived from the 'DATE SUBMITTED' field (9/10/25) as no explicit 'invoice issue date' was present, and this represents the vendor's submission date for the claim period of Aug-25. All other fields were clearly stated. |

## Exodus Recovery Inc. - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202207_ExodusRecoveryInc.-RecoveryBridgeHousing-November2025.pdf`  ·  229.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | — |
| Billed amount | $37638.54 |
| Deliverables | Recovery Bridge Housing (P03334) |
| Confidence | high |
| Notes | Invoice date is not explicitly stated on the document. 'November 2025' appears in the header but seems to indicate a reporting period rather than a specific invoice date. |

## Exodus Recovery Inc. - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202227_ExodusRecoveryInc.-RecoveryBridgeHousing-October2025.pdf`  ·  241.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | — |
| Billed amount | $38538.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | Invoice date is null as the document is a report covering a period ('October September 2025') rather than a single invoice with a specific date. The billed_amount is the sum of all 'Total Charge' values across all pages (637 lines * $60.50/line). |

## Exodus Recovery Inc. - Recovery Bridge Housing - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200960_ExodusRecoveryInc.-RecoveryBridgeHousing-September2025.pdf`  ·  238.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H0034) |
| Confidence | medium |
| Notes | The document is a detailed service log for a reporting period (September 2023), not a single invoice. Therefore, a specific 'invoice_date' (issuance date) is not present. Each line item has a 'Total Charge' of $86.50, but a cumulative 'billed_amount' (grand total) for the entire document is not explicitly stated and would require inference/calculation, which is not permitted. The services are all of the same type, 'Recovery Bridge Housing (H0034)'. |

## Exodus Recovery, Inc. - September 2025 Supplemental

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201906_ExodusRecovery_Inc.-September2025Supplemental.pdf`  ·  662.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Exodus Recovery, Inc |
| Invoice date | 2025-06-17 |
| Billed amount | $187.42 |
| Deliverables | Office Space; Subtotal Administrative Overhead |
| Confidence | high |
| Notes | Invoice date 2025-06-17 is a future date relative to the current year, but extracted as stated on the document under 'DATE SUBMITTED'. Deliverables are identified from the 'EXPENDED THIS MONTH' column on page 2, which sums to the total billed amount. |

## Fred Browns Recovery Services Inc. - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202209_FredBrownsRecoveryServicesInc.-RecoveryBridgeHousing-November2025.pdf`  ·  367.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H0034) |
| Confidence | high |
| Notes | Invoice date not explicitly stated as a single ISO YYYY-MM-DD date. The document header mentions 'November 2023' as a billing period, but this is not a specific date. Furthermore, the 'Date of Service' column lists dates in '2024', creating a conflict with the 'November 2023' header. No grand total 'billed_amount' is explicitly stated on the document; the document presents a detailed listing of individual charges per service ($60.50 each) rather than a summary invoice with a single total amount. |

## Fred Browns Recovery Services Inc. - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202228_FredBrownsRecoveryServicesInc.-RecoveryBridgeHousing-October2025.pdf`  ·  354.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | $484242.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a data extract covering a period from September to October 2025, not a single invoice, so a specific invoice_date is not present. |

## Fred Browns Recovery Services Inc. - Recovery Bridge Housing - September2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200961_FredBrownsRecoveryServicesInc.-RecoveryBridgeHousing-September2025.pdf`  ·  334.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | low |
| Notes | The document is a report summarizing multiple billing line items over a period (September 2025), not a single consolidated invoice. No single 'invoice_date' or aggregate 'billed_amount' for the entire document is explicitly stated. The 'billed_amount' would require summing individual line item charges, which is an inference not permitted by the instructions. |

## Fred Browns Recovery Services Inc. - Residential - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202210_FredBrownsRecoveryServicesInc.-Residential-November2025.pdf`  ·  223.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | $4907.10 |
| Deliverables | Long Term Residential Day Rate (H0019:U1) |
| Confidence | medium |
| Notes | Invoice date is not explicitly stated as a single date. The document header refers to "November 2024" as a reporting period, and line items have "Date of Service" ranging from 11/1/2024 to 11/22/2024. The 'billed_amount' is calculated from the 22 line items provided in the OCR text snippet. If the full visual document contains additional line items not present in the provided OCR snippet, the total billed amount would be higher. |

## Fred Browns Recovery Services Inc. - Residential - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202229_FredBrownsRecoveryServicesInc.-Residential-October2025.pdf`  ·  229.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | BROWN'S RECOVERY SERVICES INC. |
| Invoice date | October 2025 |
| Billed amount | $158517.59 |
| Deliverables | Long Term Residential Day Rate (09019 U1); Long Term Residential Day Rate (09019 U2) |
| Confidence | high |
| Notes | A specific invoice day (YYYY-MM-DD) is not present. The document title specifies 'October 2025' as the billing period. The billed amount was calculated by summing 661 line items from the 'Total Charge' column. |

## Fred Browns Recovery Services Inc. - Residential - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200962_FredBrownsRecoveryServicesInc.-Residential-September2025.pdf`  ·  229.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Long Term Residential Day Rate (00019 U1) |
| Confidence | medium |
| Notes | Invoice date is not a single date but a period ('September August 2025'). Total billed amount is not explicitly stated as a grand total on the document; only individual line item charges are present. |

## Grandview Foundation Inc. - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202211_GrandviewFoundationInc.-RecoveryBridgeHousing-November2025.pdf`  ·  235.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANDVIEW FOUNDATION, INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | No specific invoice date was stated on the document. 'November 2025' is part of the document title, not explicitly an invoice date. The document appears to be a partial report or ledger (indicated by 'page 3' in the OCR). The total billed amount for the entire document cannot be determined from the single provided page, only individual line item amounts ($60.50 each) are present. |

## Grandview Foundation Inc. - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202230_GrandviewFoundationInc.-RecoveryBridgeHousing-October2025.pdf`  ·  237.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANDVIEW FOUNDATION, INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H0034) |
| Confidence | high |
| Notes | The document is a data extract showing multiple service dates (10/1/2015 - 10/31/2015) and a data extraction date (1/1/2016), but no single, overarching 'invoice date' for the entire document is present. A grand total 'billed_amount' for all listed services is not provided; only individual line item charges are shown. |

## Grandview Foundation Inc. - Recovery Bridge Housing - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200963_GrandviewFoundationInc.-RecoveryBridgeHousing-September2025.pdf`  ·  237.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANDVIEW FOUNDATION, INC. |
| Invoice date | 2023-09-30 |
| Billed amount | $15570.00 |
| Deliverables | Recovery Bridge Housing (H0034) |
| Confidence | high |
| Notes | Invoice date is inferred as the end of the service period stated in the document title 'September 2023'. The billed amount is a summation of all 'Total Delivered' line items, as no explicit grand total is provided on the document. |

## Healthright 360 - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202212_Healthright360-RecoveryBridgeHousing-November2025.pdf`  ·  247.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | — |
| Billed amount | $98554.50 |
| Deliverables | Recovery Bridge Housing (H0034) |
| Confidence | high |
| Notes | invoice_date is null because no explicit invoice date field was found. The document title mentions 'November 2024', but the dates of service range from 11/01/2024 to 12/31/2024. billed_amount was calculated by summing all 1629 line items as no grand total was explicitly stated on the document. Each line item was $60.50. |

## Healthright 360 - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202231_Healthright360-RecoveryBridgeHousing-October2025.pdf`  ·  265.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | — |
| Billed amount | $27180.00 |
| Deliverables | Recovery Bridge Housing (PH0334) |
| Confidence | high |
| Notes | Invoice date is not explicitly stated as a single date; the document title indicates a billing period of 'October 2025' but not a specific invoice date. The billed_amount is calculated by summing all 'Total Charge' line items (453 entries * $60.00). |

## Healthright 360 - Recovery Bridge Housing - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200965_Healthright360-RecoveryBridgeHousing-September2025.pdf`  ·  260.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | September 2025 |
| Billed amount | $26620.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | Vendor identified as "HEALTHRIGHT 360" from the top-left of the document. Invoice date "September 2025" is stated in the report title as the billing period, not a specific single date. Billed amount was calculated by summing the "Total Charge" of $60.50 for each unique service event. Service events were identified by the "HEALTHRIGHT X" identifier in the "Provider Name" column, ranging from HEALTHRIGHT 1 to HEALTHRIGHT 440. Page 6 of the provided images contained duplicate service events (HEALTHRIGHT 361 to HEALTHRIGHT 398) which were already present on previous pages and thus were not double-counted in the total. No explicit grand total was provided on the document. |

## Holliday's Helping Hands Hope Haven & Heart Haven - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201016_Holliday_sHelpingHandsHopeHaven_HeartHaven-October2025-Redacted.pdf`  ·  2587.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Holliday's Helping Hand |
| Invoice date | — |
| Billed amount | $273042.02 |
| Deliverables | Hope Haven (Individual Beds); Hope Haven (Family Units); Heart Haven; Base Rate; LVN or Equivalent; MH Clinician |
| Confidence | high |
| Notes | No specific 'invoice_date' in YYYY-MM-DD format is explicitly stated; only the billing month/year ('October 2025') and various approval dates are present. 'Housing Navigation Rate BHBH' is listed as a rate component but not as a distinct line-item service with a claim amount. |

## Holliday's Helping Hands Hope Haven & Heart Haven - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201000_Holliday_sHelpingHandsHopeHaven_HeartHaven-September2025-Redacted.pdf`  ·  2182.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Holliday's Helping Hand |
| Invoice date | 2025-10-10 |
| Billed amount | $227526.00 |
| Deliverables | Hope Haven (Individual Beds) - Base Rate; Hope Haven (Individual Beds) - LVN or Equivalent; Hope Haven (Individual Beds) - MH Clinician; Hope Haven (Family Units) - Base Rate; Hope Haven (Family Units) - LVN or Equivalent; Hope Haven (Family Units) - MH Clinician; Heart Haven - Base Rate; Heart Haven - LVN or Equivalent; Heart Haven - MH Clinician; Heart Haven - Base Rate; Heart Haven - LVN or Equivalent; Heart Haven - MH Clinician |
| Confidence | high |
| Notes | Payment Address is redacted on the document. |

## Holliday's Helping Hands Hope Haven & Heart Haven - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207781_Holliday_sHelpingHandsHopeHaven_HeartHaven-November2025-Redacted.pdf`  ·  2414.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Holliday's Helping Hand |
| Invoice date | 2025-12-12 |
| Billed amount | $281153.46 |
| Deliverables | Hope Haven (Individual Beds) - Base Rate; Hope Haven (Individual Beds) - LVN or Equivalent; Hope Haven (Individual Beds) - MH Clinician; Hope Haven (Family Units) - Base Rate; Hope Haven (Family Units) - LVN or Equivalent; Hope Haven (Family Units) - MH Clinician; Heart Haven - Base Rate; Heart Haven - LVN or Equivalent; Heart Haven - MH Clinician (staffed at 25% for 5 days); Heart Haven - MH Clinician (staffed at 100% for 25 days); Heart Haven - MH Clinician (MSW reimbursement pay for October 2025 for 22 days) |
| Confidence | high |
| Notes | The invoice date is taken from the signatures on the cover sheet (Page 1). Other pages (Pages 5-10) have a certification date of '12/3/25' which is different, but the cover sheet date is considered the primary invoice date. |

## Hollywood Walk of Fame - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201017_HollywoodWalkofFame-October2025-Recact.pdf`  ·  1101.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Hollywood Walk of Fame Hotel |
| Invoice date | 2025-11-07 |
| Billed amount | $319962.16 |
| Deliverables | 49 Beds |
| Confidence | high |
| Notes | Multiple dates were present for invoice issuance (11-5-25 on page 2, and 11/7/2025 twice on page 1); 2025-11-07 was chosen as the most prominent date on the summary page. Client names on page 2 were redacted and therefore not extracted. |

## Hollywood Walk of Fame - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201001_HollywoodWalkofFame-September2025-Redacted.pdf`  ·  937.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Hollywood Walk of Fame Hotel |
| Invoice date | 2025-10-08 |
| Billed amount | $309640.80 |
| Deliverables | 49 Beds |
| Confidence | high |
| Notes | — |

## Hollywood Walk of Fame - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207782_HollywoodWalkofFame-November2025-Redacted.pdf`  ·  976.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Hollywood Walk of Fame Hotel |
| Invoice date | 2025-12-09 |
| Billed amount | $309640.80 |
| Deliverables | 49 Beds |
| Confidence | high |
| Notes | invoice_date was taken from the approval date on the 'H2.0 PAYMENT INVOICE' (page 1), as no dedicated invoice issuance date field was present. The 'Month/Year: November 2025' represents the service period. Deliverables were extracted strictly as the text in the 'Number of Beds/Units' column on page 1. The 'Total Number of Days' (30) is presented in a separate column and not concatenated with the deliverable description. |

## Home at Last - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201018_HomeatLast-October2025-Redacted.pdf`  ·  446.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Home at Last Community Development Corporation |
| Invoice date | 2025-11-20 |
| Billed amount | $701083.00 |
| Deliverables | Base Rate; Housing Navigation; LVN or Equivalent; MH Clinician |
| Confidence | high |
| Notes | Invoice date derived from the 'Date' next to Billing Coordinator Signature on the cover sheet, which represents the overall invoice date. Other dates (Billing Month/Year: October 2025, Provider Invoice Date: 11/5/2025) are present but 11/20/2025 is the latest date for the consolidated payment invoice. Payment Address is redacted. Client names on supporting pages 4-6 are redacted. |

## Home at Last - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201002_HomeatLast-September2025-Redacted.pdf`  ·  759.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Home at Last Community Development Corporation |
| Invoice date | 2025-10-15 |
| Billed amount | $678225.00 |
| Deliverables | ESA Long Beach (Single Beds) - Base Rate; ESA Long Beach (Single Beds) - Housing Navigation; ESA Long Beach (Single Beds) - LVN or Equivalent; ESA Long Beach (Single Beds) - MH Clinician; ESA Long Beach (Double Beds) - Base Rate; ESA Long Beach (Double Beds) - Housing Navigation; ESA Long Beach (Double Beds) - LVN or Equivalent; ESA Long Beach (Double Beds) - MH Clinician |
| Confidence | high |
| Notes | The invoice date is taken from the 'Date' field next to the Billing Coordinator and Program Manager signatures on the cover sheet (Page 1), as this represents the document's approval date. The 'Billing Month/Year' of September 2025 is the service period. The billed amount is the 'Total Claim' from the cover sheet (Page 1), which is confirmed by summing the individual totals for 'ESA Long Beach (Single Beds)' (Page 2) and 'ESA Long Beach (Double Beds)' (Page 3). Deliverables combine the site names with the detailed invoice categories. Page 4, referencing 'Home at Last-Skybridge' and lacking a monetary total, appears to be a supporting detail sheet for a different site or a component not summarized in the primary invoice total, and thus its specific line items for client days were not included in the 'deliverables' as financial line items. |

## Home at Last - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207783_HomeatLast-November2025-Redacted.pdf`  ·  366.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Home at Last Community Development Corporation |
| Invoice date | 2025-12-08 |
| Billed amount | $662430.00 |
| Deliverables | ESA Long Beach (Single Beds); ESA Long Beach (Double Beds); Base Rate; Housing Navigation; LVN or Equivalent; MH Clinician |
| Confidence | high |
| Notes | Invoice date interpreted as the signature date (12/8/2025), as 'November 2025' is a billing period. The billed_amount reflects the 'Total Claim' on the cover sheet, which explicitly summarizes services for 'ESA Long Beach (Single Beds)' and 'ESA Long Beach (Double Beds)'. Detailed pages for 'Home at Last-Skybridge' (pages 4-7) are present but do not have a summary total included in the overall billed_amount on the cover page. |

## Homeless Health Los Angeles - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201195_HomelessHealthLosAngeles-August2025.pdf`  ·  7001.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Homeless Health Los Angeles |
| Invoice date | 2025-09-26 |
| Billed amount | $82931.41 |
| Deliverables | Wages; Payroll Taxes; Workers Compensation; Group Insurance; Group Insurance Dental; Group Insurance-Vision; Group Insurance LTD; Employer 401K Matching Contribution; Rent; Facility Maintenance & Repair; Vehicle Maintenance; Telephone; Equip Repair & Rental; Program Supplies & Food; Office Supplies; Insurance; Client Related Expenses; Utilities; Bank & Misc Fees; Recruiting Expenses; Outside Services; Emergency Food; Employee Education; Local Travel & Parking; Depreciation Expense; Indirect Administration |
| Confidence | high |
| Notes | All values were clearly stated on the document and corroborated across multiple pages. |

## Homeless Health Los Angeles 2 - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201196_HomelessHealthLosAngeles2-August2025.pdf`  ·  2580.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Homeless Health Los Angeles |
| Invoice date | 2025-09-26 |
| Billed amount | $50360.60 |
| Deliverables | Peer Specialist; Substance Use Specialist; RNI; Team Lead MDT3; Director of Outreach/Director of; Mental Health Therapist; Case Manager; Employee Benefits; Facility Maintenance; Vehicle Maintenance; Telephone; Program Supplies; Office Supplies; Utilities; Liability Insurance; Client Expenses; Emergency Housing; Staff Training; Parking and Mileage; Recruitment - Advertisement for positions; Miscellaneous Fees; Depreciation; Payroll Fees; Administrative Overhead; Office space Lease; Copier Lease; Vehicle Lease |
| Confidence | high |
| Notes | — |

## Hope the Mission - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201197_HopetheMission-August2025.pdf`  ·  288.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOPE THE MISSION |
| Invoice date | 2025-09-26 |
| Billed amount | $65260.94 |
| Deliverables | ICMS - Street-Based Engagement; Program Supervisor; Field Supervisor; Outreach Field Supervisor; SUD Counselor Trainee; Outreach Peer Specialist; SUD Outreach Counselor; Case Manger |
| Confidence | medium |
| Notes | The 'deliverables' field required interpretation of 'line-item services/deliverables' in an invoice that provides a budget breakdown for a main service category. The overarching 'SERVICE CATEGORY' and distinct 'PERSONNEL TITLE' roles were extracted as direct deliverables. Other budget categories like 'Services & Supplies', 'Subcontractors', and 'Overhead' were considered cost categories rather than direct deliverables from the vendor. |

## House of Hope Foundation Inc. - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202213_HouseofHopeFoundationInc.-RecoveryBridgeHousing-November2025.pdf`  ·  241.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOUSE OF HOPE FOUNDATION INC. |
| Invoice date | — |
| Billed amount | $23514.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | No single invoice date is present on the document; 'Date of Service' entries are provided instead. The billed_amount is the sum of 389 line items, each for $60.50, totaling $23514.50. |

## House of Hope Foundation Inc. - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202232_HouseofHopeFoundationInc.-RecoveryBridgeHousing-October2025.pdf`  ·  233.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOUSE OF HOPE FOUNDATION INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | Invoice date and total billed amount are not explicitly stated on the document. The document presents a report of services rendered over a month, with individual service dates and charges per line item, but no overall invoice date or total sum. 'DPH SAPC Foundation Inc.' is mentioned in the header, but 'HOUSE OF HOPE FOUNDATION INC.' is consistently listed as the 'Provider Name' for all line items. |

## House of Hope Foundation Inc. - Recovery Bridge Housing - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200966_HouseofHopeFoundationInc.-RecoveryBridgeHousing-September2025.pdf`  ·  238.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOUSE OF HOPE FOUNDATION INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | invoice_date is not explicitly stated; the document indicates a billing period (September 2025) and a data extraction date (12/09/2021), but no single invoice date. billed_amount (total for the entire document) is not explicitly stated; individual line item charges are provided, but no grand total. |

## Illumination Foundation (IF) 2 - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201178_IlluminationFoundation_IF_2-IH-August2025.pdf`  ·  361.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Illumination Foundation (IF) |
| Invoice date | 2025-08-01 |
| Billed amount | $395250.00 |
| Deliverables | Interim Housing -IHS; Recuperative Care |
| Confidence | high |
| Notes | — |

## JWCH Institute Inc. - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201179_JWCHInstituteInc.-IH-August2025.pdf`  ·  383.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH Institute Inc. |
| Invoice date | 2025-07-31 |
| Billed amount | $214365.00 |
| Deliverables | Recuperative Care |
| Confidence | high |
| Notes | The invoice date was taken from the 'AUTHORIZED SIGNATURE' date, as no explicit 'Invoice Date' field was present. 'Recuperative Care' was chosen as the deliverable because it is explicitly listed as a 'PROGRAM TYPE' with a corresponding amount, representing a specific line-item service. |

## JWCH Institute Inc. 2 - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201180_JWCHInstituteInc.2-IH-August2025.pdf`  ·  390.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH Institute Inc. |
| Invoice date | 2025-07-31 |
| Billed amount | $594518.00 |
| Deliverables | Interim Housing -IHS; Recuperative Care |
| Confidence | high |
| Notes | — |

## JWCH Institute Inc. 3 - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201181_JWCHInstituteInc.3-IH-August2025.pdf`  ·  376.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH Institute Inc. |
| Invoice date | 2025-07-31 |
| Billed amount | $520800.00 |
| Deliverables | Interim Housing -IHS; Recuperative Care |
| Confidence | high |
| Notes | — |

## JWCH Institute Inc. 4 - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201182_JWCHInstituteInc.4-IH-August2025.pdf`  ·  386.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH Institute Inc. |
| Invoice date | 2025-07-31 |
| Billed amount | $254200.00 |
| Deliverables | Recuperative Care |
| Confidence | high |
| Notes | Invoice date extracted from the date of authorization. Deliverables extracted from the 'PROGRAM TYPE' column on page 2, as it represents the specific service provided. |

## Jwch Institute Inc. - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202214_JwchInstituteInc.-RecoveryBridgeHousing-November2025.pdf`  ·  266.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH INSTITUTE, INC. |
| Invoice date | — |
| Billed amount | $52403.00 |
| Deliverables | Recovery Bridge Housing (H2034-C); Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | Invoice date is null as the document is a spreadsheet report covering a period and does not contain a single, clearly labeled 'invoice date' field. The document header mentions 'November 2025', but all service dates within the report are in 2024, making a specific ISO YYYY-MM-DD invoice date undeterminable from the document's content. The billed amount is calculated as the sum of all 866 'Total Charge' line items ($60.50 each). |

## Jwch Institute Inc. - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202233_JwchInstituteInc.-RecoveryBridgeHousing-October2025.pdf`  ·  267.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH INSTITUTE, INC. |
| Invoice date | — |
| Billed amount | $102221.50 |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034-C) |
| Confidence | high |
| Notes | The document lists 'Date of Service' for individual line items but does not provide a single 'Invoice Date'. The document title mentions 'October 2025' indicating the reporting period, not a specific invoice date. The 'billed_amount' was calculated by summing all 'Total Charge' values across all 7 pages of the document. OCR had some minor misinterpretations of the service codes, e.g., 'H20' as part of 'Housing', but context allowed for correct extraction as 'H2034' and 'H2034-C'. |

## Jwch Institute Inc. - Recovery Bridge Housing - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200967_JwchInstituteInc.-RecoveryBridgeHousing-September2025.pdf`  ·  271.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWMH Institute Inc. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H0034-C) |
| Confidence | medium |
| Notes | Invoice date is not explicitly stated as a single date on the document; 'September 2023' is stated as the reporting period. Total billed amount is not explicitly stated as a single sum; only line-item totals ('Total Delivered') are present. |

## LA Centers for Alcohol and Drug Abuse - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202215_LACentersforAlcoholandDrugAbuse-RecoveryBridgeHousing-November2025.pdf`  ·  386.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA CENTERS FOR ALCOHOL AND DRUG ABUSE |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034-C); Recovery Bridge Housing (H2034:HD); Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The document is a multi-page data extract/report, not a traditional single invoice with a consolidated invoice date or total billed amount. The header states 'November 2025' but individual service dates are from 2024, and the data extraction date is 2026, making a single 'invoice_date' for the entire document ambiguous. No overall billed amount is presented; only per-line item charges are shown across multiple pages. |

## LA Centers for Alcohol and Drug Abuse - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202234_LACentersforAlcoholandDrugAbuse-RecoveryBridgeHousing-October2025.pdf`  ·  435.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA CENTERS FOR ALCOHOL AND DRUG ABUSE |
| Invoice date | — |
| Billed amount | $52585.00 |
| Deliverables | Recovery Bridge Housing (H00334); Recovery Bridge Housing (H00334-C) |
| Confidence | high |
| Notes | No explicit invoice date was found. The title 'October September 2025' and the latest date of data extraction '1/1/2026' refer to reporting periods or extraction dates, not a singular invoice date. The billed amount was calculated by summing the 'Total Charge' for all 809 line items, each at $65.00. Two distinct service types were identified from the 'Service Type' column: 'Recovery Bridge Housing (H00334)' and 'Recovery Bridge Housing (H00334-C)'. |

## LA Centers for Alcohol and Drug Abuse - Recovery Bridge Housing - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200968_LACentersforAlcoholandDrugAbuse-RecoveryBridgeHousing-September2025.pdf`  ·  430.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA CENTERS FOR ALCOHOL AND DRUG ABUSE |
| Invoice date | September 2025 |
| Billed amount | $92365.00 |
| Deliverables | Recovery Bridge Housing (H2034:HD); Recovery Bridge Housing (H2034-C) |
| Confidence | high |
| Notes | The document is a detailed service report for the month of September 2025, not a traditional single-page invoice with a specific 'invoice date' field. 'September 2025' from the document header is used as the invoice date, indicating the billing period. The total billed amount was calculated by summing all 1421 individual line items (each $65.00) across all 25 pages, as no grand total was provided. |

## LA Family Housing (LAFH) - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201183_LAFamilyHousing_LAFH_-IH-August2025.pdf`  ·  338.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Family Housing (LAFH) |
| Invoice date | 2025-08-01 |
| Billed amount | $112530.00 |
| Deliverables | Interim Housing -IHS; Stabilization |
| Confidence | high |
| Notes | — |

## LA Family Housing Corporation - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201198_LAFamilyHousingCorporation-August2025.pdf`  ·  13247.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Family Housing |
| Invoice date | 2025-08-31 |
| Billed amount | $113074.13 |
| Deliverables | Wages, Administration; Wages, Programs; Wages, Administration - Overtime; Wages, Programs - Overtime; Employer, OASDI; Employer, Medicare; Employer, CA SUI; Employer Health Insurance Contribution; Employer Dental Insurance Contribution; Employer Life Insurance Contribution; Employer Vision Insurance Contribution; Employer Retirement Contribution; Workers Comp; Staff Training; Staff Transportation (Mileage/Parking); Professional Fees - Other; Office Supplies; Postage & Shipping; Vehicle, Fuel; Vehicle, Insurance; Vehicle, Maintenance, Repair & Other; Insurance, General Liability; Rent Storage/Parking Facilities; Water, Electricity & Gas; Telephone & Communications; Rubbish; Computer & Software Expense; Client Needs; Client Lodging; Client Security Deposits; Client Rental Assistance; Client: Program Vehicle Lease; Subcontractors; Admin |
| Confidence | high |
| Notes | — |

## LA Family Housing Corporation 2 - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201199_LAFamilyHousingCorporation2-August2025.pdf`  ·  9663.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Family Housing |
| Invoice date | 2025-08-31 |
| Billed amount | $242082.22 |
| Deliverables | Director of Engagement; Assistant Director of Outreach; Outreach Manager MDT 2, Public Spaces; Outreach Manger, MDT 3, City/County Expansion; Outreach Manger MDT 1, MDT4; (Weekend); Case Manger- MHS MDT1; Case Manager - Mental Health Specialist; Case Manger - MHS MDT 3; Case Manager - Substance Abuse Specialist; Case Manager - Outreach Specialist; Case Manager - Outreach Specialist (Weekend); Case Manager - Peer Specialist; Case Manager - Peer Specialist (Weekend); Outreach Specialist - Public Spaces; Outreach Program Assistant; Data Coordinator; Employee Benefits @ 27%; Client/Member Expenses; Program Supplies; Office Supplies, Postage, Printing; Staff Training/Development; Telephone/Communications/IT; Utilities; Professional/Liability Insurance; Vehicle Maintenance (Fuel, repairs, maintenance); Northeast Valley Health Coporation (NEVHC); Vehicle; Office Space; ADMINISTRATIVE OVERHEAD/COSTS @ 15% |
| Confidence | high |
| Notes | The invoice_date is derived from the dates of the individual billed amounts on page 7 (8/31/2025), which aligns with the 'Aug'25' claim period on page 1. The 'DATE SUBMITTED' (9/17/25) on page 1 refers to the submission date of this invoice document, not the billing date for services rendered. |

## LA Global Care - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201184_LAGlobalCare-IH-August2025.pdf`  ·  833.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Global Care |
| Invoice date | 2025-08-01 |
| Billed amount | $114700.00 |
| Deliverables | Interim Housing -IHS; Stabilization; Stabilization; Stabilization |
| Confidence | high |
| Notes | — |

## Landmark Invoice Aug 2025 SNF-STP

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202152_LandmarkInvoiceAug2025SNF-STP.pdf`  ·  625.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services, Inc. |
| Invoice date | 2025-09-10 |
| Billed amount | $644740.96 |
| Deliverables | PATCHES; Retro SOC |
| Confidence | high |
| Notes | An explicit 'invoice_date' field is not present. The date 2025-09-10 is the earliest certification date by the provider/administrator. The main service component (1986 total units) is not explicitly named as a deliverable; therefore, only the explicitly named line items 'PATCHES' and 'Retro SOC' are included. |

## Landmark Invoice Oct 2025 SNF-STP

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202159_LandmarkInvoiceOct2025SNF-STP.pdf`  ·  645.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services, Inc. |
| Invoice date | 2025-11-26 |
| Billed amount | $680492.82 |
| Deliverables | AMOUNT CLAIMED; PATCHES:; Retro SOC |
| Confidence | high |
| Notes | Invoice date was derived from the 'IMD ADMINISTRATION APPROVAL SIGNATURE DATE' as no explicit 'invoice date' field was present on the document. The 'CLAIM PERIOD Oct-25' was too ambiguous to be used as a specific date. |

## Landmark Invoice Sept 2025 SNF-STP

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202160_LandmarkInvoiceSept2025SNF-STP.pdf`  ·  952.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Landmark Medical Services, Inc. |
| Invoice date | 2025-10-29 |
| Billed amount | $633265.66 |
| Deliverables | AMOUNT CLAIMED; PATCHES; Retro SOC |
| Confidence | high |
| Notes | The 'invoice_date' was determined from the 'IMD ADMINISTRATION APPROVAL SIGNATURE DATE' as the most appropriate specific date for this payment request summary, rather than the 'CLAIM PERIOD Sep-25' which indicates a billing period. |

## Mental Health America of Los Angeles - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201200_MentalHealthAmericaofLosAngeles-August2025.pdf`  ·  1778.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Mental Health America of Los Angeles |
| Invoice date | 2025-09-23 |
| Billed amount | $71291.59 |
| Deliverables | Chief Science Officer South County; Senior Director of Outreach; Assistant Director/Nursing; Clinical Supervisor, Licensed; Field Based Program Manager, ASW; Outreach Speciallist, LVN; Outreach Specialist; Outreach Specialist, SUD Specialist; Accounting Staff; EMPLOYEE BENEFITS @ 35.8392%; Client Expenses; Insurance; Program Supplies; Office Supplies & Postage; Staff Mileage/Parking; Staff Recruitment/Training/Development; Repair & Maintenance; Utilities/Alarm System; Property taxes and Depreciation; Telephone/Communications; Administrative Overhead; Copiers/Printing (Equipment Lease); Vehicle; Parking Space; Office Space |
| Confidence | high |
| Notes | The invoice date is extracted from 'DATE SUBMITTED'. Line items for 'III. SUBCONTRACTORS' and 'V. SUBCONTRACTORS IN EXCESS OF $50,000' were not included as they did not have specific billed amounts for this month, and the sub-items were placeholders. |

## Mental Health America of Los Angeles 2 - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201201_MentalHealthAmericaofLosAngeles2-August2025.pdf`  ·  1772.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Mental Health of America of Los Angeles (SPA 8) |
| Invoice date | 9/23/25 |
| Billed amount | $235125.63 |
| Deliverables | Chief Service Officer South County; Senior Director of Outreach Services/Street Based Medicine; Assistant Director/Nursing Director; Clinical Supervisor, Licensed; Program Manager; Field Based Program Manager, ASW (Sat to Wed); Generallist Outreach Worker-Public Spaces; Outreach Specialist MSW-Sat to Wed; Outreach Specialist -APCC; Outreach Specialist - MSW; Outreach Specialist, LVN; Outreach Specialist, RN; Outreach Specialist, RN (Part-time); Outreach Specialist-Substance Abuse; Outreach Specialist-Substance Abuse - Sat to Wed; Senior Director of Evaluation & Compliance; Quality Assurance/Quality Improvement position; Quality Assurance Data Entry Specialist; Accounting Staff; EMPLOYEE BENEFITS; Client Expenses; Insurance; Program Supplies; Office Supplies, Postage, Printing (Business Card); Staff Mileage/Parking; Staff Recruitment/Training/Development; Telephone/Communications; Vehicle Maintenance and Gas; Utilities/Alarm System; Repair & Maintenance; Property taxes and Depreciation; Equipment; Medical Oversight/Consultation; Administrative Overhead; (Printing) Equipment Lease; Vehicle; Office Space; Parking for Office Space |
| Confidence | high |
| Notes | — |

## PATH Cares - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201185_PATHCares-IH-August2025.pdf`  ·  161.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | PATH Cares |
| Invoice date | 2025-08-01 |
| Billed amount | $36828.00 |
| Deliverables | Interim Housing -IHS; Stabilization (11 beds @ $108.00 per day for 31 days) |
| Confidence | high |
| Notes | Invoice date inferred from 'DATE' field next to 'AUTHORIZED SIGNATURE' and consistent with 'CLAIM PERIOD' and invoice number month. |

## PATH Cares - IH - May 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201807_PATHCares-IH-May2025.pdf`  ·  159.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | PATH Cares |
| Invoice date | 2025-05-01 |
| Billed amount | $132432.00 |
| Deliverables | Interim Housing -IHS; Stabilization |
| Confidence | high |
| Notes | — |

## Pleasant Beginnings - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201019_PleasantBeginnings-October2025-Redacted.pdf`  ·  407.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Pleasant Beginnings Foundation |
| Invoice date | 2025-11-03 |
| Billed amount | $39525.00 |
| Deliverables | Base Rate; Housing Navigation |
| Confidence | high |
| Notes | All requested fields were clearly stated and consistent across the document pages. The invoice date was taken from the earliest signature date on page 3, which is a common practice for invoice finalization. |

## Pleasant Beginnings - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201003_PleasantBeginnings-September2025-Redacted.pdf`  ·  590.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Pleasant Beginnings Foundation |
| Invoice date | 2025-10-07 |
| Billed amount | $36241.92 |
| Deliverables | Base Rate; LVN or Equivalent |
| Confidence | medium |
| Notes | The document contains two distinct invoices for the same provider and billing month (September 2025), each with its own total amount and signature date. The data extracted pertains to the first invoice presented in the document (pages 1-2), dated 2025-10-07 with a total of $36,241.92. The second invoice (pages 3-4) has a total of $2,970.00 and is dated 2025-10-30. Page 5 is a client detail sheet and does not state a billed amount. No grand total summing the distinct invoices was found on the document. |

## Pleasant Beginnings - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207784_PleasantBeginnings-November2025-Redacted.pdf`  ·  340.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Pleasant Beginnings Foundation |
| Invoice date | 2025-11-30 |
| Billed amount | $40694.88 |
| Deliverables | Base Rate; Housing Navigation; LVN or Equivalent; LVN or Equivalent |
| Confidence | high |
| Notes | Invoice date was chosen as the certification date from page 3 (11/30/2025) which corresponds to the end of the billing month, rather than the later signature date on the cover sheet (12/3/2025). |

## SRO Housing - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201191_SROHousing-IH-August2025.pdf`  ·  230.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SRO Housing |
| Invoice date | 2025-08-01 |
| Billed amount | $200880.00 |
| Deliverables | Interim Housing -IHS; Stabilization (60 # of BEDS, $108.00 BED RATE, 31 DAYS) |
| Confidence | high |
| Notes | — |

## SSG JTNH & Pine Lodge - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201020_SSGJTNH_PineLodge-October2025-Redacted.pdf`  ·  1099.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Special Service For Groups |
| Invoice date | 2025-11-12 |
| Billed amount | $274061.70 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | The invoice date is taken from the signing date on the cover sheet (Page 1), as it represents the overall document's approval/submission date. 'October 2025' is identified as the billing period covered by the invoice. Deliverables are derived from the 'Invoice Category' line items on pages 2 and 3. |

## SSG JTNH & Pine Lodge - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201004_SSGJTNH_PineLodge-September2025-Redacted.pdf`  ·  586.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Special Service For Groups |
| Invoice date | 2025-10-10 |
| Billed amount | $265221.00 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | Vendor name taken from the cover sheet. Invoice date is derived from the signature date on the cover sheet, which is the most prominent overall invoice date. Billed amount is the 'Total Claim' on the cover sheet, which sums the claims from the detailed pages. Deliverables are the unique 'Invoice Category' line items identified on the detailed sheets for 'Journey to New Horizons' and 'Pine Lodge'. |

## SSG JTNH & Pine Lodge - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207785_SSGJTNH_PineLodge-November2025-Redacted.pdf`  ·  1139.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Special Service For Groups |
| Invoice date | 2025-12-08 |
| Billed amount | $265221.00 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | Vendor name "Special Service For Groups" is taken from the cover sheet, which is the most complete name, with "SSG" used as an abbreviation on subsequent pages. The invoice date is based on the latest approval signature date (12/8/2025) on the cover sheet. The billing month is stated as November 2025. Deliverables are the unique service categories listed in the detailed tables for both sites. |

## SSG Kohler - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201021_SSGKohler-October2025-Redacted.pdf`  ·  432.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Special Service For Groups |
| Invoice date | 2025-11-12 |
| Billed amount | $248756.40 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | — |

## SSG Kohler - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201005_SSGKohler-September2025-Redacted.pdf`  ·  360.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Special Service For Groups |
| Invoice date | 2025-10-10 |
| Billed amount | $240732.00 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | Invoice covers billing month/year September 2025. The invoice date is taken from the latest approval date (10/10/2025). Vendor name also appears as 'SSG' in other sections. |

## SSG Kohler - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207786_SSGKohler-November2025-Redacted.pdf`  ·  371.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Special Service For Groups |
| Invoice date | 2025-12-08 |
| Billed amount | $240732.00 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | Invoice date inferred from the approval/signature date, as no explicit 'invoice date' field was present. |

## SSG Mark Twain - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201022_SSGMarkTwain-October2025-Redacted.pdf`  ·  479.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Special Service For Groups |
| Invoice date | 2025-11-12 |
| Billed amount | $350220.64 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | — |

## SSG Mark Twain - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201006_SSGMarkTwain-September2025-Redacted.pdf`  ·  480.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Special Service For Groups |
| Invoice date | 2025-10-10 |
| Billed amount | $338923.20 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | Invoice date ambiguity: The cover sheet (page 1) shows signature dates of 10/10/2025, while the detailed client lists (pages 3 and 4) show a signature date of 10/01/2025. The later date from the cover sheet was selected as the invoice date. |

## SSG Mark Twain - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207787_SSGMarkTwain-November2025-Redacted.pdf`  ·  489.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Special Service For Groups |
| Invoice date | 2025-12-01 |
| Billed amount | $338923.20 |
| Deliverables | Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | Vendor name 'SSG' on page 2 is an abbreviation of 'Special Service For Groups' on page 1. The invoice date is taken from the certification date on pages 3 and 4, which is the earliest discernible date for the invoice's creation/certification, given the billing month of November 2025. |

## Sadler Healthcare Inc. - Residential - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202216_SadlerHealthcareInc.-Residential-November2025.pdf`  ·  314.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Long Term Residential Day Rate (XH019 US); Residential addiction program, subacute detoxification (IF approved) |
| Confidence | medium |
| Notes | No single invoice date is explicitly stated; the document title indicates a period of 'November 2024'. No grand total billed amount is explicitly stated on the document, it would require summing individual line items. |

## Sadler Healthcare Inc. - Residential - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202235_SadlerHealthcareInc.-Residential-October2025.pdf`  ·  293.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Long Term Residential Day Rate (H0019:U3); Residential addiction program, subacute detoxification (H0012:U9) |
| Confidence | low |
| Notes | Invoice date is not explicitly stated; 'October 2025' in the header indicates a billing period, not a single invoice date. Total billed amount is not explicitly stated as a grand total on the document; it would require summing line items across multiple pages, which are not fully provided. |

## Sadler Healthcare Inc. - Residential - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200969_SadlerHealthcareInc.-Residential-September2025.pdf`  ·  363.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC |
| Invoice date | — |
| Billed amount | $410452.56 |
| Deliverables | Long Term Residential Day Rate (MBI919-U5) |
| Confidence | high |
| Notes | invoice_date is null as the document is a data extract for a service period (September 2025) and does not contain a single invoice date. Billed amount calculated by multiplying the count of unique 'Provider Program' entries (66 unique residential locations from 5233 to 5363 East Beverly Boulevard, incrementing by 2) by the number of service days (29, from 9/1/2025 to 9/29/2025) by the 'Total Charge' per line item ($214.44). |

## Safe Refuge - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202217_SafeRefuge-RecoveryBridgeHousing-November2025.pdf`  ·  300.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SAFE REFUGE |
| Invoice date | 2026-03-09 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The document provided consists of 11 identical pages, each showing only a portion of the service lines. A total billed amount for the entire report is not present on any of the provided pages, therefore billed_amount is null. The invoice_date is extracted from the 'dates of data extraction' (03/09/2026) mentioned in the introductory text, as there is no explicit 'invoice date'. The title 'November 2025' and service dates in 'November 2024' create ambiguity for an overall invoice date, making the data extraction date the most plausible date for this report's generation. |

## Safe Refuge - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202236_SafeRefuge-RecoveryBridgeHousing-October2025.pdf`  ·  302.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SAFE REFUGE |
| Invoice date | — |
| Billed amount | $62517.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The vendor, 'SAFE REFUGE', is consistently listed as the 'Provider Name' on each line item. No single 'invoice_date' is explicitly stated on the document. The document title indicates 'October 2025' and individual 'Date of Service' entries range from 10/1/2025 to 10/31/2025. The 'billed_amount' was calculated by summing the 'Total Charge' of $60.50 for each of the 1035 service lines spread across the 11-page document. The number of lines per 'Contracting Provider Program' varied on the last page. The 'deliverables' were extracted from the 'Service Type' column, which consistently showed 'Recovery Bridge Housing (H2034)'. |

## Safe Refuge - Recovery Bridge Housing - Septmeber 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200970_SafeRefuge-RecoveryBridgeHousing-Septmeber2025.pdf`  ·  298.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SAFE REFUGE |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | Invoice date not explicitly stated; 'September 2025' in the header indicates a billing period. Total billed amount for the entire document is not explicitly stated; only individual line item charges are present. |

## Salvation Army (SAL) - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201186_SalvationArmy_SAL_-IH-August2025.pdf`  ·  133.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Salvation Army (SAL) |
| Invoice date | 2025-06-30 |
| Billed amount | $133354.56 |
| Deliverables | Interim Housing -IHS; Stabilization |
| Confidence | high |
| Notes | — |

## San Fernando Valley Community Health Center (SFVCMHC) - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201187_SanFernandoValleyCommunityHealthCenter_SFVCMHC_-IH-August2025.pdf`  ·  295.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | San Fernando Valley Community Health Center (SFVCMHC) |
| Invoice date | Aug-2025 |
| Billed amount | $174344.00 |
| Deliverables | Interim Housing -IHS; Stabilization |
| Confidence | medium |
| Notes | The invoice_date (Aug-2025) was extracted from the 'INVOICE NO.' and 'CLAIM PERIOD (MO./YR)'. A specific day for the invoice issuance was not determinable without inference, so the value is 'as printed' rather than full ISO YYYY-MM-DD. Deliverables were extracted from 'SERVICE CATEGORY' on page 1 and 'PROGRAM TYPE' on page 2, representing distinct service descriptions. |

## Serenity Recuperative Care Inc. - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201188_SerenityRecuperativeCareInc.-IH-August2025.pdf`  ·  112.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Serenity Recuperative Care Inc |
| Invoice date | 2025-07-29 |
| Billed amount | $92070.00 |
| Deliverables | Interim Housing -IHS; Stabilization |
| Confidence | high |
| Notes | — |

## Serenity Recuperative Care Inc. 2 - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201189_SerenityRecuperativeCareInc.2-IH-August2025.pdf`  ·  80.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Serenity Recuperative Care (SRC) |
| Invoice date | 2025-07-29 |
| Billed amount | $322276.00 |
| Deliverables | Recuperat ve Care |
| Confidence | high |
| Notes | The invoice_date '2025-07-29' was determined from 'Tuesday, Juy 29, 2025' and 'DATE INVOICE RECEIVED: 07/29/2025', noting 'Juy' as a likely OCR typo for 'July'. The deliverables line item is stated as 'Recuperat ve Care', which appears to be an OCR error for 'Recuperative Care'. |

## Sleep Tight Tonight Healing Solutions - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201190_SleepTightTonightHealingSolutions-IH-August2025.pdf`  ·  302.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Sleep Tight Tonight Healing Solutions |
| Invoice date | 2025-08-01 |
| Billed amount | $135408.00 |
| Deliverables | Interim Housing -IHS; Psych Recup |
| Confidence | high |
| Notes | — |

## Social Model Recovery Systems Inc. - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202218_SocialModelRecoverySystemsInc.-RecoveryBridgeHousing-November2025.pdf`  ·  295.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SOCIAL MODEL RECOVERY SYSTEMS, INC. |
| Invoice date | 2026-03-09 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The document is an 'Overview' or 'spreadsheet extract' rather than a traditional invoice. The 'invoice_date' is taken as the 'Date of the data extraction' (03/09/2026) as it represents the creation date of this billing document. This conflicts with 'November 2025' in the document title and the 'Date of Service' columns, which consistently show dates in November 2024. The 'billed_amount' is null because no grand total or overall billed amount is explicitly stated on the document; only individual line item charges are present, and summing them would be an inference. |

## Social Model Recovery Systems Inc. - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202237_SocialModelRecoverySystemsInc.-RecoveryBridgeHousing-October2025.pdf`  ·  295.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SOCIAL MODEL RECOVERY SYSTEMS, INC. |
| Invoice date | — |
| Billed amount | $8893.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The document is a multi-page report detailing individual charges for the month of October 2025, rather than a single summary invoice with a specific invoice date. The 'invoice_date' field is returned as null as there is no single, explicit invoice date for the entire document, only service dates within October 2025 and a report period mentioned as "October 2025" in the header. The billed amount is a sum of 147 line items, each for $60.50. |

## Social Model Recovery Systems Inc. - Recovery Bridge Housing - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200971_SocialModelRecoverySystemsInc.-RecoveryBridgeHousing-September2025.pdf`  ·  287.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SOCIAL MODEL RECOVERY SYSTEMS, INC. |
| Invoice date | — |
| Billed amount | $25008.50 |
| Deliverables | Recovery Bridge Housing (H0034) |
| Confidence | medium |
| Notes | No specific 'invoice date' was found on the document. The document title indicates a service period of 'September 2025'. The billed amount was calculated by summing the 'Total Charge' for all 289 line items (289 * $86.50). The document appears to be a summary report of services rather than a traditional invoice requesting payment. |

## Southern CA Alcohol and Drug Programs Inc. - Residential - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202219_SouthernCAAlcoholandDrugProgramsInc.-Residential-November2025.pdf`  ·  248.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SO CAL ALCOHOL AND DRUG PROGRAMS, INC. |
| Invoice date | — |
| Billed amount | $46866.39 |
| Deliverables | Long Term Residential Day Rate (H0019:U1) |
| Confidence | medium |
| Notes | Invoice date is ambiguous. The document header states 'November 2025', while 'Date of Service' line items are for November 2024, and the data extraction date is stated as '03/09/2026'. No single explicit 'Invoice Date' field is present. The billed amount was calculated by summing all 'Total Charge' line items (213 lines * $220.03). |

## Southern CA Alcohol and Drug Programs Inc. - Residential - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202238_SouthernCAAlcoholandDrugProgramsInc.-Residential-October2025.pdf`  ·  263.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SOUTHERN CA ALCOHOL AND DRUG PROGRAMS, INC. |
| Invoice date | 2025-10-31 |
| Billed amount | $18784.57 |
| Deliverables | Long Term Residential Day Rate (H0019:U1); Long Term Residential Day Rate (H0019:U3:HD); Long Term Residential Day Rate (H0019:U3) |
| Confidence | medium |
| Notes | The vendor name is extracted from the document header. The invoice_date is inferred as the last day of the 'October 2025' billing period mentioned in the document header, as no explicit single invoice date is present. The attached file's image is labeled '1 of 6', but the provided OCR text explicitly states '==Start of OCR for page 6==' and '==End of OCR for page 6=='. The billed_amount is calculated by summing the 'Total Charge' column from the provided OCR content for page 6 only. If this is part of a larger multi-page document, the total billed amount would be higher. Deliverables are unique service types extracted from the 'Service Type' column within the provided OCR content. |

## Southern CA Alcohol and Drug Programs Inc. - Residential - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200972_SouthernCAAlcoholandDrugProgramsInc.-Residential-September2025.pdf`  ·  254.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SO CAL ALCOHOL AND DRUG PROGRAMS, INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Long Term Residential Day Rate (H0019:U1); Residential addiction program, subacute detoxification (H0014:HF); Long Term Residential Day Rate (H0019:U3:HD) |
| Confidence | high |
| Notes | A single 'invoice_date' is not present; the document represents a service period of September 2025. A single 'billed_amount' (grand total) is not present; the document provides line-item totals only. |

## Special Services of Groups Inc. - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201202_SpecialServicesofGroupsInc.-August2025.pdf`  ·  1276.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Special Group for Groups - SPA 6 |
| Invoice date | 2025-09-15 |
| Billed amount | $379054.38 |
| Deliverables | I. PERSONNEL TITLE AND % FTE; II. SERVICES & SUPPLIES (ONGOING); IV. ADMINISTRATIVE OVERHEAD/COSTS @ 10%; VII. OTHER COSTS EXCLUDED FROM DE MINIMIS RATE |
| Confidence | high |
| Notes | Deliverables are extracted as the main categories listed on page 2, which provides a detailed breakdown of services. |

## Special Services of Groups Inc. 2 - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201203_SpecialServicesofGroupsInc.2-August2025.pdf`  ·  1433.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Special Services for Groups, Inc. |
| Invoice date | 2025-09-15 |
| Billed amount | $88892.29 |
| Deliverables | I. PERSONNEL; II. SERVICES & SUPPLIES (ONGOING); III. SUBCONTRACTORS; IV. ADMINISTRATIVE; V. SUBCONTRACTORS IN EXCESS OF $25,000; VI. OTHER COSTS EXCLUDED FROM DE MINIMIS RATE |
| Confidence | high |
| Notes | Invoice date is extracted from the 'DATE SUBMITTED' field (9/15/25) rather than the 'CLAIM PERIOD' (Aug 2025). Deliverables are extracted from the main section headers on page 2, which represent the top-level categories of billed services. |

## St. Joseph Center - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201204_St.JosephCenter-August2025.pdf`  ·  3844.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | St. Joseph Center - SPA 5 |
| Invoice date | 2025-09-18 |
| Billed amount | $160887.23 |
| Deliverables | AVP, Program; Director, Outreach; Associate Director, Outreach; Street-Based Engagement, Program Manag; Case Manager (Lead); Case Manager; Case Manager - Mental Health (Lead); Case Manager - Mental Health; Case Manager - Peer; Case Manager - Substance Abuse; Registered Nurse; Support Specialist; Public Space Generalist 1; Public Space Generalist 2; EMPLOYEE BENEFITS @ 20.52%; Client/Member Expenses; Equipment Lease, Maint/Repair; Training/Staff Development; Program/Office Supplies, Postage, Printing; Staff Mileage/Parking; Telephone/Communications/Utilities; Other Operating (Building, Security, etc.); General Liability and Harassment Insurance; Vehicle Maintenance & Insurance; Purchasing Medical Supplies; Subcontractor (1) Venice Family Clinic; Administrative Overhead; Vehicle; Office Space; Equipment Lease (Fax, Copier, Printers, Postage, etc.); Equipment Purchase (including One Time) |
| Confidence | high |
| Notes | The billed_amount had a slight discrepancy (160,887.23 vs 160,887.22) between the main invoice sections (page 1, item 8 and page 2, item 69) and a summary table on page 9. The value from the main invoice sections was used. |

## St. Joseph Center - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201192_St.JosephCenter-IH-August2025.pdf`  ·  300.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | St. Joseph Center |
| Invoice date | 2025-08-01 |
| Billed amount | $42617.25 |
| Deliverables | Stabilization |
| Confidence | high |
| Notes | — |

## St. Joseph Center 2 - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201205_St.JosephCenter2-August2025.pdf`  ·  873.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | St. Joseph Center |
| Invoice date | 2025-09-17 |
| Billed amount | $21300.94 |
| Deliverables | Director, Outreach; Street-Based Engagement, Program Manag; Case Manager; Case Manager - Peer; Case Manager - Substance Abuse 4; Licensed Vocational Nurse; Case Manager; EMPLOYEE BENEFITS @ 23%; Client/Member Expenses; Equipment Lease, Maint/Repair; Training/Staff Development; Program/Office Supplies, Postage, Printing; Staff Mileage/Parking; Telephone/Communications/Utilities; Other Operating (Building, Security, etc.); General Liability and Harassment Insurance; Vehicle Maintenance & Insurance; Purchasing Medical Supplies; Subcontractor (1); Subcontractor (2); Subcontractor (3); Venice Family Clinic; Administrative Overhead; Subcontractor (1); Subcontractor (2); Subcontractor (3); Vehicle; Office Space; Equipment Lease (Fax, Copier, Printers, Postage, etc.); Equipment Purchase (including One Time) |
| Confidence | medium |
| Notes | The billed_amount of $21,300.94 was extracted from item 8 on page 1 and line 51 on page 2. Pages 4 and 8 of the General Ledger Report show a 'Total Billed' amount of $21,300.95, a slight discrepancy of $0.01. The invoice date was consistently 09/17/2025 across multiple fields. |

## TDD - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201023_TDD-October2025-Redacted.pdf`  ·  537.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TDD Supportive Living, Inc. |
| Invoice date | 2025-11-18 |
| Billed amount | $114616.92 |
| Deliverables | Base Rate; Housing Navigation; LVN or Equivalent; MH Clinician |
| Confidence | high |
| Notes | Multiple dates were present. '11/18/2025' was chosen as the invoice date as it appears on the cover sheet alongside overall claim approval signatures, representing the latest approval date for the summarized claim. The 'Billing Month/Year' of 'October 2025' refers to the service period, not the invoice issuance date. |

## TDD - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201007_TDD-September2025-Redacted.pdf`  ·  538.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TDD Supportive Living, Inc. |
| Invoice date | 2025-10-10 |
| Billed amount | $106759.44 |
| Deliverables | Base Rate; Housing Navigation; LVN or Equivalent; MH Clinician |
| Confidence | high |
| Notes | The invoice date was determined from the latest signature date for the overall invoice (Program Manager Signature on Page 1). Billing Month/Year is stated as September 2025. |

## TDD - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207788_TDD-November2025-Redacted.pdf`  ·  530.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TDD Supportive Living, Inc. |
| Invoice date | 2025-12-17 |
| Billed amount | $110919.60 |
| Deliverables | Base Rate; Housing Navigation; LVN or Equivalent; MH Clinician |
| Confidence | high |
| Notes | Invoice date is taken from the latest signature date on the cover sheet (Page 1) which refers to the overall 'Payment Invoice'. Deliverables are extracted from the 'Invoice Category' columns on Pages 2 and 3, representing the distinct services provided for both 'Single Beds' and 'Double Beds' sites. |

## TLC Room and Board - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201025_TLCRoomandBoard-October2025-Redacted.pdf`  ·  429.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TLC Room and Board |
| Invoice date | 2025-11-01 |
| Billed amount | $27178.32 |
| Deliverables | Base Rate; Housing Navigation; LVN or Equivalent |
| Confidence | high |
| Notes | — |

## TLC Room and Board - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201009_TLCRoomandBoard-September2025-Redacted.pdf`  ·  489.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TLC Room and Board |
| Invoice date | 2025-10-10 |
| Billed amount | $26301.60 |
| Deliverables | Base Rate; Housing Navigation; LVN or Equivalent |
| Confidence | high |
| Notes | Invoice date inferred from the latest signature date on Page 1, as no explicit 'invoice date' field was present. |

## TLC Room and Board - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207790_TLCRoomandBoard-November2025-Redacted.pdf`  ·  480.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TLC Room and Board |
| Invoice date | 2025-12-09 |
| Billed amount | $26301.60 |
| Deliverables | Base Rate; Housing Navigation; LVN or Equivalent |
| Confidence | high |
| Notes | Invoice date inferred from the latest signature date (12/9/2025) on the cover sheet, as no explicit 'Invoice Date' field was present. Another signature date of 12/1/25 was found on page 3. |

## Tarzana Treatment Centers Inc. - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202220_TarzanaTreatmentCentersInc.-RecoveryBridgeHousing-November2025.pdf`  ·  400.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TARZANA TREATMENT CENTERS, INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034:HD) |
| Confidence | medium |
| Notes | The document is a data extraction spreadsheet, not a traditional single invoice. No single invoice date is present. The header mentions 'November 2025', but all service dates are in November 2024, creating ambiguity. No total billed amount for the entire document is present; only individual line item charges are listed. |

## Tarzana Treatment Centers Inc. - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202239_TarzanaTreatmentCentersInc.-RecoveryBridgeHousing-October2025.pdf`  ·  386.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TARZANA TREATMENT CENTERS INC. |
| Invoice date | — |
| Billed amount | $88800.00 |
| Deliverables | Recovery Bridge Housing (H0034) |
| Confidence | high |
| Notes | invoice_date is null because the document provides a reporting period ("October 2025") and individual service dates, but no single invoice date. The billed_amount was calculated by summing 1480 line items, each with a "Total Charge" of $60.00. |

## Tarzana Treatment Centers Inc. - Recovery Bridge Housing - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200973_TarzanaTreatmentCentersInc.-RecoveryBridgeHousing-September2025.pdf`  ·  383.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TARZANA TREATMENT CENTERS, INC. |
| Invoice date | September 2025 |
| Billed amount | $350718.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a detailed service report for the month of September 2025, rather than a traditional invoice with an explicit issuance date. The 'invoice_date' is extracted from the document header, indicating the period covered. The 'billed_amount' is calculated by summing all individual 'Total Charge' line items ($60.50 each) across all 20 pages of the document (5797 lines in total), as no grand total is explicitly stated. |

## Testimonial Whittier - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201024_TestimonialWhittier-October2025-Redacted.pdf`  ·  1985.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Testimonial Community Love Center |
| Invoice date | 2025-11-07 |
| Billed amount | $274747.42 |
| Deliverables | Testimonial Whittier - Family Units - Base Rate; Testimonial Whittier - Family Units - Housing Navigation; Testimonial Whittier - Family Units - MH Clinician; Testimonial Whittier - Family Units - LVN or Equivalent; Testimonial Whittier - Single Rooms - Base Rate; Testimonial Whittier - Single Rooms - Housing Navigation; Testimonial Whittier - Single Rooms - MH Clinician; Testimonial Whittier - Single Rooms - LVN or Equivalent; Testimonial Whittier - Double Rooms - Base Rate; Testimonial Whittier - Double Rooms - Housing Navigation; Testimonial Whittier - Double Rooms - MH Clinician; Testimonial Whittier - Double Rooms - LVN or Equivalent |
| Confidence | high |
| Notes | The invoice date is derived from the latest signature date on the cover sheet (11/7/2025). Pages 5 and 6 show a certification date of 11/3/25, but the cover sheet provides the overall invoice date. Deliverables are extracted by combining the site name with the specific service categories listed on the detailed pages. |

## Testimonial Whittier - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201008_TestimonialWhittier-September2025-Redacted.pdf`  ·  2132.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Testimonial Community Love Center |
| Invoice date | 2025-10-09 |
| Billed amount | $265884.60 |
| Deliverables | Testimonial Whittier - Family Units; Testimonial Whittier - Single Rooms; Testimonial Whittier - Double Rooms |
| Confidence | medium |
| Notes | invoice_date: '2025-10-09' was chosen as the invoice date as it is the latest approval/signature date found on the cover sheet. 'September 2025' is stated as the 'Billing Month/Year', but a specific day for that month is not provided, and no field is explicitly labeled 'Invoice Date'. Deliverables were extracted from the 'Site Name' column on the cover sheet, representing the main billed line items. |

## Testimonial Whittier - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207789_TestimonialWhittier-November2025-Redacted.pdf`  ·  1782.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Testimonial Community Love Center |
| Invoice date | 2025-12-08 |
| Billed amount | $265884.60 |
| Deliverables | Testimonial Whittier - Family Units; Testimonial Whittier - Single Rooms; Testimonial Whittier - Double Rooms; Base Rate; Housing Navigation; MH Clinician; LVN or Equivalent |
| Confidence | high |
| Notes | — |

## The Beacon House Association of San Pedro - Recovery Bridge Housing - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202221_TheBeaconHouseAssociationofSanPedro-RecoveryBridgeHousing-November2025.pdf`  ·  277.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | THE BEACON HOUSE ASSC OF SAN PEDRO |
| Invoice date | — |
| Billed amount | $29040.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The document does not contain a single clear 'invoice_date'. The document's title mentions 'November 2025', while the individual line items list 'Date of Service' in 'November 2024'. Additionally, a note on the first page mentions 'invoice date of the data extraction, 02/09/2026'. Due to these conflicting dates and the lack of a specific 'invoice date' field, the value for 'invoice_date' is returned as null. The 'billed_amount' was calculated by summing the 'Total Charge' of $60.50 for each of the 480 line items present across 8 pages (60 lines per page). |

## The Beacon House Association of San Pedro - Recovery Bridge Housing - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202240_TheBeaconHouseAssociationofSanPedro-RecoveryBridgeHousing-October2025.pdf`  ·  294.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | THE BEACON HOUSE ASSC OF SAN PEDRO |
| Invoice date | — |
| Billed amount | $57172.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The document is a data export/spreadsheet for services provided during 'October 2025', not a traditional invoice with a single explicit invoice date or a grand total explicitly stated. The 'invoice_date' field is returned as null because no single invoice date is present; the document covers a billing period (October 2025). The 'billed_amount' is calculated by summing all 'Total Billed' entries ($60.50 per entry) across all 10 provided pages of the document, totaling 945 entries. The page numbering or ordering of the provided images seems unusual (e.g., page 10 starts with lower street numbers and fewer entries than previous pages), but all presented data has been extracted. |

## The Beacon House Association of San Pedro - Recovery Bridge Housing - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200974_TheBeaconHouseAssociationofSanPedro-RecoveryBridgeHousing-September2025.pdf`  ·  287.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | THE BEACON HOUSE ASSC OF SAN PEDRO |
| Invoice date | — |
| Billed amount | $54147.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | A specific 'invoice date' (YYYY-MM-DD) is not present on the document. The document title indicates services for 'September 2025'. The billed amount is calculated by summing the 'Total Charge' ($60.50) for all 895 line items across all 9 pages of the document. |

## The Center in Hollywood - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201206_TheCenterinHollywood-August2025.pdf`  ·  408.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The Center in Hollywood |
| Invoice date | 2025-09-15 |
| Billed amount | $27951.86 |
| Deliverables | I. PERSONNEL TITLE AND % FTE; Program Manager, Clinical; Outreach Case Manager; Substance Abuse specialist; Peer Advocate; Director of Programs; Clinical Director; Employee Benefits @ 19.798%; II. SERVICES & SUPPLIES (ONGOING); Parking and Mileage; Training/Staff Development; Client Expenses; Program Supplies; Office Supplies and Expenses; Telephone/Communications; Professional/Liability Insurance; III. Consultants/Vendors; Subcontractor (Maximum $50,000 per subcontractor); Purchasing Medical Services; IV. ADMINISTRATIVE OVERHEAD/COSTS @ 15%; Administrative Overhead; V. LEASE; Office Space Lease |
| Confidence | high |
| Notes | Vendor name extracted from 'AGENCY NAME' on Page 1. Invoice date extracted from 'DATE SUBMITTED' on Page 1 and confirmed with 'DATE INVOICE RECEIVED' on Page 1. Billed amount extracted from 'AMOUNT REQUESTED' on Page 1 and confirmed as 'EXPENDED THIS MONTH' on Line 51, Page 2. Deliverables are derived from the 'BUDGETED LINE ITEM' column on Page 2, including main categories and their specific sub-items that show expenditures for the current month. |

## The People Concern (TPC) - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201193_ThePeopleConcern_TPC_-IH-August2025.pdf`  ·  312.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The People Concern (TPC) |
| Invoice date | 2025-07-31 |
| Billed amount | $149420.00 |
| Deliverables | Stabilization; Enhanced Services Beds (ESB) |
| Confidence | high |
| Notes | — |

## The People Concern (TPC) 2 - IH - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201194_ThePeopleConcern_TPC_2-IH-August2025.pdf`  ·  310.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The People Concern (TPC) |
| Invoice date | 2025-07-31 |
| Billed amount | $218448.32 |
| Deliverables | Interim Housing -IHS; Recuperative Care |
| Confidence | high |
| Notes | Invoice date derived from 'DATE INVOICE RECEIVED' and 'AUTHORIZED SIGNATURE' date, as no explicit 'invoice date' field was present. |

## The People Concern - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201207_ThePeopleConcern-August2025.pdf`  ·  3828.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The People Concern |
| Invoice date | 2025-10-01 |
| Billed amount | $286814.53 |
| Deliverables | Personnel; Employee Benefits; Client Support Funds; Program/Office Supplies; Recruitment Placement Costs; Staff Parking; Staff mileage; Vehicle Costs - Insurance, Maintenance, Gas etc.; General Liability Insurance; Training Related Costs (Fees, dues etc.); Telecommunications: Cellphone Services/telephone, Internet etc.; Facility Costs - Repair, maintenance, Janitorial, and utilities; IT Network. Support and small Supplies; Medical Subcontractor-LA Christian Health Centers; Medical Subcontractor-Saban Community Clinic; Clinical Supervisors Contractor; Administrative Overhead 15%; Office Space; Equipment Lease; Equipment/Furniture Purchase (One Time); IT Software and Set-up (One Time); Vehicle Lease (Including One Time); Facility Costs - (one time cost) |
| Confidence | high |
| Notes | — |

## The People Concern 2 - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201208_ThePeopleConcern2-August2025.pdf`  ·  2312.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The People Concern |
| Invoice date | 2025-09-25 |
| Billed amount | $100595.04 |
| Deliverables | ICMS - Street-Based Engagement; Client Support Funds; Medical Contractor - LA Christian Health Centers; Clinical Supervisors Contractor |
| Confidence | medium |
| Notes | Deliverables field interpretation focused on the primary service category and distinct direct/subcontracted services explicitly stated as line items, rather than all internal expense line items or personnel roles, which are costs associated with delivering the main service. |

## The People Concern 3 - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201209_ThePeopleConcern3-August2025.pdf`  ·  1418.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The People Concern |
| Invoice date | 2025-09-30 |
| Billed amount | $65302.78 |
| Deliverables | Assistant Director; Program Manager; Mental Health Lead; Outreach Case Manager; Substance Use Case Manager; Administrative/Data; Facilities and Maintenance Engineer II; Staff Psychiatrist; EMPLOYEE BENEFITS; Recruitment Placement Costs; Program/Office Supplies; Staff Parking; Vehicle costs: insurance, maintenance, gas etc.; General Liability Insurance; Training; Facility Costs - Repair, Maintenance, janitorial, and utilities; Telecommunications: Cellphone Services/telephone, Internet etc.; IT Network, Service and Supplies; Medical Services - LA Christian Health Center; Administrative Overhead; Purchase Services - LA Christian Health Centers; Office Space; Equipment Lease; Equipment/Furniture Purchase (One Time); IT Software and Set-up (One Time); Vehicle Lease (including One Time) |
| Confidence | high |
| Notes | The invoice date is inferred from the 'DATE SUBMITTED' field (9/30/25) as there is no explicit 'Invoice Date' field, but it aligns with the 'CLAIM PERIOD' (08/25) being billed. 'Outreach Case Manager' appears multiple times for different FTEs/individuals on page 2, but is consolidated into a single deliverable entry as per the instruction to extract line-item services/deliverables 'as stated'. Generic placeholders like 'Subcontractor (2)' and 'Subcontractor (3)' were not included as they do not represent specific service names. |

## The People Concern 4 - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201210_ThePeopleConcern4-August2025.pdf`  ·  1238.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | THE PEOPLE CONCERN |
| Invoice date | — |
| Billed amount | $33497.93 |
| Deliverables | Program Manager; Lead Client Service Specialist; Client Service Specialist; Client Service Specialist; Facilities and Maintenance Engineer II; Safety and Engagement Specialist; EMPLOYEE BENEFITS @; Client/Member Services; Program/Office Supplies; Staff Parking; Staff Local Mileage; General Liability Insurance; Faculty Costs - Repair, Maintenance, janitorial, rent and utilities; Telephone Services/ Communications/ Internet Services; IT Network, Equipment rental and Supplies; Administrative Overhead @ 15%; Equipment/Furniture Purchase (One Time) |
| Confidence | medium |
| Notes | The 'invoice_date' is not explicitly stated on the document. 'DATE SUBMITTED' (09-23-25) and 'CLAIM PERIOD (MO./YR): 08/25' are present, but neither represents the invoice's issue date. Deliverables are extracted from the 'BUDGETED LINE ITEM' column on Page 2 for which an amount is expended in the 'THIS MONTH' column. |

## The People Concern 5 - August 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201211_ThePeopleConcern5-August2025.pdf`  ·  8933.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | THE PEOPLE CONCERN |
| Invoice date | 2025-10-08 |
| Billed amount | $186355.35 |
| Deliverables | Chief Program Officer; Director; Assistant Director; Clinical Program Manager; Program Manager; Case Manager; Case Manager(Senior); Case Manager - Substance Abuse; Case Manager (Sr.) - Substance Abuse; Facilities and Maintenance Engineer II; Psychiatrist; EMPLOYEE BENEFITS @; Recruitment Placement Costs; Client Support Funds; Program/ Office Supplies; Staff Parking; Staff Mileage; Vehicle Maintenance, Gas & Other Costs; General Lability Insurance; Training related costs (fees, dues, etc.); Telecommunication: Cell Phone Services/ Telephone, Internet etc.; Facility Costs - Repair, Maintenance, janitorial, rent and utilities; IT Network, Service and Supplies; Vendor Medical Services (LA Christian Health Center); Administrative Overhead (15%) TPC; Equipment/Furniture Purchase (One Time); IT Software and Set-up (One Time); Vehicle Lease (including One Time) |
| Confidence | high |
| Notes | The invoice date was extracted from the 'DATE SUBMITTED' field. The billed amount was taken from 'AMOUNT REQUESTED' and confirmed by 'INVOICE AMOUNT' for 'THIS MONTH' on page 2. Deliverables are unique line-item descriptions from Page 2 with non-zero 'EXPENDED THIS MONTH' values. Multiple instances of the same job title (e.g., 'Case Manager') appearing in the personnel section were consolidated into a single entry in the deliverables list. |

## Upward Bound House - IH - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201026_UpwardBoundHouse-October2025-Redacted.pdf`  ·  401.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Upward Bound House |
| Invoice date | 2025-11-01 |
| Billed amount | $95871.20 |
| Deliverables | Base Rate; MH Clinician |
| Confidence | medium |
| Notes | The invoice_date was determined from the earliest signature date (11/1/2025) found on the combined document, as there is no explicit 'Invoice Date' field. The document indicates a billing month/year of October 2025, but a specific date of invoice issuance is not present. The provided date is the date of certification/signature. |

## Upward Bound House - IH - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1201010_UpwardBoundHouse-September2025-Redacted.pdf`  ·  509.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Upward Bound House |
| Invoice date | 2025-10-01 |
| Billed amount | $88800.00 |
| Deliverables | Interim Housing Program - Base Rate |
| Confidence | high |
| Notes | Invoice date derived from the earliest signature date on the document (Page 3). Page 3 details services for a different site ("Dalton") and is not included in the primary billed amount for "Bright Futures IV" detailed on pages 1 and 2. |

## Upward Bound House - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1207791_UpwardBoundHouse-November2025-Redacted.pdf`  ·  322.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Upward Bound House |
| Invoice date | 2025-12-03 |
| Billed amount | $101388.00 |
| Deliverables | Base Rate; MH Clinician; Housing Navigation |
| Confidence | high |
| Notes | — |

## Volunteers of America of Los Angeles - Residential - November 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202222_VolunteersofAmericaofLosAngeles-Residential-November2025.pdf`  ·  337.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | VOLUNTEERS OF AMERICA OF LOS ANGELES |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Long Term Residential Day Rate (H0019:U3); Long Term Residential Day Rate (H0019:U1) |
| Confidence | medium |
| Notes | A single 'invoice_date' for the entire document is not present; the document is a detailed report with multiple 'Date of Service' entries. There is also a discrepancy where the report header mentions 'November 2023' while the 'Date of Service' column lists dates in 'November 2024'. The 'billed_amount' (total billed) is not explicitly stated as a grand total sum on the document; only individual line item charges are provided. |

## Volunteers of America of Los Angeles - Residential - October 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1202241_VolunteersofAmericaofLosAngeles-Residential-October2025.pdf`  ·  346.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | VOLUNTEERS OF AMERICA OF LOS ANGELES |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Long Term Residential Day Rate (H0019:U3); Long Term Residential Day Rate (H0019:U1) |
| Confidence | low |
| Notes | The document is a detailed service report listing multiple service dates and charges, not a single summarized invoice. Therefore, a single 'invoice_date' and aggregated 'billed_amount' for the entire document are not present. Only individual service dates and line-item charges are available. |

## Volunteers of America of Los Angeles - Residential - September 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1200975_VolunteersofAmericaofLosAngeles-Residential-September2025.pdf`  ·  327.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | VOLUNTEERS OF AMERICA OF LOS ANGELES |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Long Term Residential Day Rate (H0019:U3) |
| Confidence | high |
| Notes | The document does not specify a single invoice date, only service dates within a reporting period (September 2025). A total billed amount for the entire document is not provided; only individual line-item charges are listed. |
