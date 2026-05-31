# LA Alliance Invoices — Before / After

Left: an unstructured scanned invoice the county published as a PDF.
Right: the normalized ledger row our agent extracted autonomously.

## Southern CA Alcohol and Drug Programs Inc. - Residential - March 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187863_SouthernCAAlcoholandDrugProgramsInc.-Residential-March2025.pdf`  ·  240.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SO CAL ALCOHOL AND DRUG PROGRAMS, INC. |
| Invoice date | — |
| Billed amount | $113320.38 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1); Behavioral Health; Long Term Residential (H0019:01) |
| Confidence | high |
| Notes | The document does not provide a single 'invoice_date'. It is a spreadsheet-like summary of services rendered over a period, with individual 'Date of Service' entries ranging from March 1, 2025, to March 31, 2025. The header also states 'March 2025'. The 'billed_amount' is the sum of all values in the 'Total Charge' column across all pages of the document. |

## Exodus Recovery Inc. - Recovery Bridge Housing - November 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179568_ExodusRecoveryInc.-RecoveryBridgeHousing-November2024.pdf`  ·  228.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | — |
| Billed amount | $103217.94 |
| Deliverables | Recovery Bridge Housing (H2018) |
| Confidence | high |
| Notes | invoice_date is null because the document appears to be a service report for a period ('November 2024') rather than a traditional invoice with a single issue date. The document also mentions a 'data extraction date' (03/05/2023), but neither represents a singular invoice date for the entire document as an invoice. The billed_amount was calculated by summing all 'Total Charge' line items visible across the two pages provided. |

## JWCH LAC+USC - Jan 2025

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1192165_JWCHLAC_USC-Jan2025.pdf`  ·  418.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH Institute Inc. |
| Invoice date | 2024-12-31 |
| Billed amount | $520800.00 |
| Deliverables | Recuperative Care |
| Confidence | high |
| Notes | Invoice date derived from the authorization date. The invoice number '01-2025...' and claim period 'Jan-2025' suggest a January 2025 context. 'Interim Housing -IHS' is stated as the general service category, while 'Recuperative Care' is the specific program type detailed in the line items. |

## Jwch Institute Inc. - Recovery Bridge Housing - October 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179558_JwchInstituteInc.-RecoveryBridgeHousing-October2024.pdf`  ·  237.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH INSTITUTE INC. |
| Invoice date | October 2024 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034-C) |
| Confidence | medium |
| Notes | Billed amount is not a single total on the document; individual line item charges are present. Invoice date reflects a billing period as stated in the document title rather than a specific issue date. |

## Healthright 360 - Recovery Bridge Housing - October 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179556_Healthright360-RecoveryBridgeHousing-October2024.pdf`  ·  211.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | — |
| Billed amount | $121.00 |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is an overview/summary for services provided in 'October 2024'. A specific 'invoice_date' in YYYY-MM-DD format for the summary document itself is not present. The data extraction date for the report is 01/08/2025, which is not considered the invoice date for the services. |
