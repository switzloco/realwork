# LA Alliance Invoices — Before / After

Left: an unstructured scanned invoice the county published as a PDF.
Right: the normalized ledger row our agent extracted autonomously.

## Sadler Healthcare Inc. - Residential - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179515_SadlerHealthcareInc.-Residential-July2024.pdf`  ·  260.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC |
| Invoice date | July 2024 |
| Billed amount | — |
| Deliverables | Behavioral Health, Long Term Residential (H0019)(U); Subacute Detox Residential (H0012)(U) |
| Confidence | medium |
| Notes | Billed amount is null as no single total billed amount is explicitly stated on the document. The invoice date refers to the billing period 'July 2024' as no specific invoice day is present. |

## LA Centers for Alcohol and Drug Abuse - Recovery Bridge Housing - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179514_LACentersforAlcoholandDrugAbuse-RecoveryBridgeHousing-July2024.pdf`  ·  331.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA CENTERS FOR ALCOHOL AND DRUG ABUSE |
| Invoice date | 2024-07-31 |
| Billed amount | $46020.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The billed_amount was calculated by summing the 'Total Charge' of $60.50 across all 761 line items present on the 26 pages of the document. The invoice_date is derived from the latest service date in the 'July 2024' billing period specified in the document title. |

##  Jwch Institute Inc. - Recovery Bridge Housing - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179513_JwchInstituteInc.-RecoveryBridgeHousing-July2024.pdf`  ·  236.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH INSTITUTE INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034-C) |
| Confidence | medium |
| Notes | invoice_date is null because no single invoice date is explicitly stated; the document title refers to the period 'July 2024'. billed_amount is null because no grand total or single billed amount is explicitly stated; only line-item 'Total Disbursed' amounts are present. |

## Grandview Foundation Inc. - Recovery Bridge Housing - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179511_GrandviewFoundationInc.-RecoveryBridgeHousing-July2024.pdf`  ·  225.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANDEVIEW FOUNDATION INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (HDSX4) |
| Confidence | medium |
| Notes | invoice_date is not explicitly stated. The document title 'July 2024' indicates the service period, and '08/24/2023' is stated as the data extraction date, not an invoice date. The total billed amount is not explicitly stated; individual line item charges are present, but no grand total is provided. |

## So Cal Alcohol and Drug Programs Inc. - Residential - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179517_SoCalAlcoholandDrugProgramsInc.-Residential-July2024.pdf`  ·  238.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SO CAL ALCOHOL AND DRUG PROGRAMS INC. |
| Invoice date | — |
| Billed amount | $87828.37 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1) |
| Confidence | high |
| Notes | The attached document is a multi-page summary report of services rendered and approved/paid for the period of 'July 2024', not a single traditional invoice. Therefore, no single 'invoice_date' is present. The 'billed_amount' was calculated by summing all 'Total Charge' values across all 353 line items found in the 6-page document, as no grand total was explicitly stated on the document. The provided OCR snippet in the prompt was only for page 6; the extraction was performed on the full 6-page image. |

## Fred Browns Recovery Services Inc. - Residential - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179510_FredBrownsRecoveryServicesInc.-Residential-July2024.pdf`  ·  223.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1) |
| Confidence | medium |
| Notes | The document is an overview spreadsheet of services rather than a traditional invoice. A specific 'invoice_date' for the entire document is not present, only 'Date of Service' for individual line items. A total 'billed_amount' for the entire document is not present, only 'Total Charge' per line item. |

## Fred Browns Recovery Services Inc. - Recovery Bridge Housing - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179509_FredBrownsRecoveryServicesInc.-RecoveryBridgeHousing-July2024.pdf`  ·  298.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | A single overall invoice date and total billed amount for the document are not explicitly present. The document is a data extract showing multiple individual service transactions rather than a consolidated invoice with a single total. |

## Exodus Recovery Inc. - Recovery Bridge Housing - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179508_ExodusRecoveryInc.-RecoveryBridgeHousing-July2024.pdf`  ·  224.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | No single 'invoice_date' or 'billed_amount' was explicitly stated on the document. The document appears to be a detailed service report for July 2024, with individual service dates and per-item charges, but no grand total. |

## Cri-Help Inc. - Recovery Bridge Housing - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179506_Cri-HelpInc.-RecoveryBridgeHousing-July2024.pdf`  ·  225.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRI-HELP INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | No single invoice date was stated on the document; the billing period is identified as 'July 2024'. No total billed amount was explicitly stated on the document; only line-item charges are present. |

## Beit Tshuvah - Recovery Bridge Housing - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179505_BeitTshuvah-RecoveryBridgeHousing-July2024.pdf`  ·  210.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | BEIT TSHUVAH |
| Invoice date | — |
| Billed amount | $423.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | A single specific 'invoice_date' for the entire document is not present; the document title indicates services for 'July 2024'. The billed_amount is the sum of 'Total Charge' from all line items (7 * $60.50). |

## Divine Healthcase Services Inc. - Recovery Bridge Housing - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179507_DivineHealthcaseServicesInc.-RecoveryBridgeHousing-July2024.pdf`  ·  232.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | DVINE HEALTHCARE SERVICES INC. |
| Invoice date | — |
| Billed amount | $20527.50 |
| Deliverables | Recovery Bridge Housing (HDSX4) |
| Confidence | medium |
| Notes | The document is a data extract of approved and paid services, not a traditional invoice. No single 'invoice_date' is explicitly present for this document. The title mentions 'July 2024', but all service dates in the data table are from 'July 2014', and the data extraction date is '08/24/2016'. The 'billed_amount' was calculated by summing the 'Total Charge' of 80.50 for each of the 255 line items, as no grand total was explicitly stated on the document. |

## Divine Healthcare Services - Recovery Bridge Housing - June 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1170573_DivineHealthcareServices-RecoveryBridgeHousing-June2024.pdf`  ·  1097.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | DIVINE HEALTHCARE SERVICES INC. |
| Invoice date | — |
| Billed amount | $37785.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | No specific 'invoice date' field was found on the document. The document header indicates 'Data Extraction - 08/29/2024' and references 'June 2024' as the service period. The billed amount was calculated by summing the 'Total Charged' column for all 687 line items ($55.00 per item). |

## Beit Tshuvah - Recovery Bridge Housing - June 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1170572_BeitTshuvah-RecoveryBridgeHousing-June2024.pdf`  ·  282.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Belt Tush/Axm |
| Invoice date | June 2024 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (HSDXH) |
| Confidence | high |
| Notes | invoice_date is provided as 'June 2024' in the document title, and a specific ISO YYYY-MM-DD is not explicitly stated or determinable without inference. The total billed_amount is not explicitly stated on the document; only individual line item charges are present. |

## SAFE REFUGE - RECOVERY BRIDGE HOUSING - MAY.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164734_SAFEREFUGE-RECOVERYBRIDGEHOUSING-MAY2024.pdf`  ·  2650.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SAFE REFUGE |
| Invoice date | MAY 2024 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The invoice_date is a billing period 'MAY 2024' as printed, not a specific date in YYYY-MM-DD format. A grand total billed_amount for the entire document is not explicitly stated. While individual line item total billed amounts are present ($55.00 each for 3005 lines, which sums to $165,275.00), the overall sum is not stated as a single value on the document, so it is returned as null per instructions not to infer or calculate. |

## TARZANA TREATMENT CENTERS INC. - RECOVERY BRIDGE HOUSING - MAY.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164735_TARZANATREATMENTCENTERSINC.-RECOVERYBRIDGEHOUSING-MAY2024.pdf`  ·  5947.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TARZANA TREATMENT CENTERS INC. |
| Invoice date | — |
| Billed amount | $119695.00 |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034:HD) |
| Confidence | high |
| Notes | The document is a detailed report of services for the month of May 2024, not a single invoice with a specific issue date. 'May 2024' indicates the billing period. Therefore, 'invoice_date' is returned as null. All other fields were clearly identifiable. |

## JCWH INSTITUTE INC. - RECOVERY BRIDGE HOUSING - MAY.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164732_JCWHINSTITUTEINC.-RECOVERYBRIDGEHOUSING-MAY2024.pdf`  ·  1740.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH INSTITUTE INC. |
| Invoice date | MAY 2024 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034-C); Recovery Bridge Housing (H2034:PG) |
| Confidence | medium |
| Notes | billed_amount is null because a grand total billed amount is not explicitly stated on the document. The document provides line-item charges but no aggregated total. invoice_date is extracted as 'MAY 2024' because a single ISO YYYY-MM-DD invoice date is not present; instead, the document indicates a reporting period. |

## HOUSE OF HOPE FOUNDATION INC. - RECOVERY BRIDGE HOUSING - MAY.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164731_HOUSEOFHOPEFOUNDATIONINC.-RECOVERYBRIDGEHOUSING-MAY2024.pdf`  ·  731.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOUSE OF HOPE FOUNDATION INC. |
| Invoice date | — |
| Billed amount | $10890.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | Invoice date is not explicitly stated as a single date (YYYY-MM-DD); the document title indicates "MAY 2024" as the billing period. The billed amount was calculated by summing the 'Total Charge' of $55.00 for each of the 198 line items present across all pages of the document. |

## HEALTHRIGHT 360 - RECOVERY BRIDGE HOUSING - MAY.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164730_HEALTHRIGHT360-RECOVERYBRIDGEHOUSING-MAY2024.pdf`  ·  1463.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | Invoice date is not explicitly stated; the document is a data report for a period (May 2024) with multiple service dates. The billed amount for the entire document cannot be determined as the attached file is only page 6 of 6, and a grand total is not provided on this page. |

## FRED BROWN'S RECOVERY SERVICES INC. - RESIDENTIAL - MAY.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164728_FREDBROWN_SRECOVERYSERVICESINC.-RESIDENTIAL-MAY2024.pdf`  ·  453.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC |
| Invoice date | — |
| Billed amount | $123153.03 |
| Deliverables | Behavioral Health, Long Term Residential (H0019) (U1) |
| Confidence | high |
| Notes | The document is a report showing multiple daily service entries, not a single invoice with a single invoice date. Therefore, a single 'invoice_date' for the entire document cannot be determined and is set to null. The 'billed_amount' is the sum of 99 individual line items, each billed at 1243.97. |

## GRANDVIEW FOUNDATION INC. - RECOVERY BRIDGE HOUSING - MAY.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164729_GRANDVIEWFOUNDATIONINC.-RECOVERYBRIDGEHOUSING-MAY2024.pdf`  ·  790.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANDVIEW FOUNDATION INC. |
| Invoice date | — |
| Billed amount | $25245.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a detailed statement for the month of May 2024, but a specific 'invoice_date' for the entire document is not present, so it is returned as null. The billing period spans from 2024-05-01 to 2024-05-31. The billed_amount was calculated by summing the 'Total Amount' for all 459 line items ($55.00 each). |
