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

## LA Centers for Alcohol and Drug Abuse - Recovery Bridge Housing - October 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179559_LACentersforAlcoholandDrugAbuse-RecoveryBridgeHousing-October2024.pdf`  ·  305.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA CENTERS FOR ALCOHOL AND DRUG ABUSE |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (HBISA); Recovery Bridge Housing (HBISD); Recovery Bridge Housing (HBIS HS); Recovery Bridge Housing (HBIS H4); Recovery Bridge Housing (HBIS H5); Recovery Bridge Housing (HBIS H2); Recovery Bridge Housing (HBIS H3); Recovery Bridge Housing (HBIS H6); Recovery Bridge Housing (HBIS H7); Recovery Bridge Housing (HBIS C) |
| Confidence | medium |
| Notes | The document is a data extraction report of multiple service claims, not a single invoice. As such, a single 'invoice_date' for the entire document is not present, nor is a consolidated 'billed_amount'. 'invoice_date' and 'billed_amount' are returned as null as they are not explicitly stated on the document as a total for the entire report. The 'Data period is October 2014' is mentioned, but it's a period, not a specific invoice date. The 'Data extract date: 01/08/2015' is also present, but it refers to the report generation date, not a billing date for services rendered in October 2014. |

## Grandview Foundation Inc. - Recovery Bridge Housing - October 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179555_GrandviewFoundationInc.-RecoveryBridgeHousing-October2024.pdf`  ·  225.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANVIEW FOUNDATION INC. |
| Invoice date | 2025-01-08 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (HDS24) |
| Confidence | medium |
| Notes | The total billed amount is not explicitly stated on the document; individual line item charges are present but no sum. The 'invoice_date' was inferred from the 'Data extraction: 01/08/2025' timestamp as the closest date related to the document's generation, though not explicitly labeled 'Invoice Date'. The document title also indicates 'October 2024' as the service period. |

## Fred Browns Recovery Services Inc. - Residential - October 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179554_FredBrownsRecoveryServicesInc.-Residential-October2024.pdf`  ·  220.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1) |
| Confidence | medium |
| Notes | A specific invoice date is not explicitly stated on the document; 'October 2024' is provided as a billing period in the header, and '11/20/2024' as a data extraction date in the overview. A total billed amount is not present on the document; only individual line item charges are listed. |

##  Fred Browns Recovery Services Inc. - Recovery Bridge Housing - October 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179553_FredBrownsRecoveryServicesInc.-RecoveryBridgeHousing-October2024.pdf`  ·  302.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | $151310.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a multi-page statement or report detailing services provided for October 2024, rather than a single invoice with a distinct, overall invoice date. Therefore, invoice_date is null. All listed services fall within October 2024. The billed_amount was calculated by summing the 'Total Charge' of $60.50 for each of the 2501 line items found across all 20 pages of the document. |

## Exodus Recovery Inc. - Recovery Bridge Housing - October 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179552_ExodusRecoveryInc.-RecoveryBridgeHousing-October2024.pdf`  ·  220.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXCELUS RECOVERY INC |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (HSDM) |
| Confidence | medium |
| Notes | Invoice date is not a single date but a reporting period (October 2024) indicated in the title; individual service dates are present per line item. The total billed amount could not be determined as the provided images do not definitively contain all line items to sum the total charges, and no overall total sum is provided on the document. |

## Beit Tshuvah - Recovery Bridge Housing - Oct 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179550_BeitTshuvah-RecoveryBridgeHousing-October2024.pdf`  ·  213.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Belt Tuvun/AAM |
| Invoice date | October 2024 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (HSDH) |
| Confidence | high |
| Notes | Invoice date is a month/year ('October 2024'), not a specific day, and therefore not in ISO YYYY-MM-DD format. The total billed amount for the entire document is not explicitly stated. While individual line items have a charge of $80.50, and there is a 'TOTALS' row at the bottom with '$80.50', this 'TOTALS' amount is not the sum of all charges listed and is therefore ambiguous or incorrect as a grand total for the document. Per instructions, this field is set to null as a valid grand total is not explicitly stated without inference. |

## Venice Community - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190092_VeniceCommunity-Sep2024.pdf`  ·  214.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Venice Community Housing |
| Invoice date | 2024-10-11 |
| Billed amount | $102292.50 |
| Deliverables | D7 Slot Costs; DHS Slot Costs; MHSA Slot Costs; PHK (D7) Slot Costs |
| Confidence | high |
| Notes | All requested fields were clearly found. |

## Volunteers of America of Los Angeles - Residential - September 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179549_VolunteersofAmericaofLosAngeles-Residential-September2024.pdf`  ·  250.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | VOLUNTEERS OF AMERICA OF LOS ANGELES |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral health, Long Term Residential (H0019)(s) |
| Confidence | high |
| Notes | Invoice date is not present on the document; the document indicates a service period (September 2024) and a data extraction date (December 4, 2024) but no single invoice date. A total billed amount is not present on the document; it lists individual line item charges but no grand total. |

## Tarzana Treatment Centers Inc. - Recovery Bridge Housing - September 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179547_TarzanaTreatmentCentersInc.-RecoveryBridgeHousing-September2024.pdf`  ·  312.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TARZANA TREATMENT CENTERS INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034:HD) |
| Confidence | high |
| Notes | Invoice date and total billed amount are not explicitly stated on the document. The document header indicates 'September 2024' as a reporting period, not a single invoice date. There is no grand total listed, only individual line item charges. |

## The Beacon House Association of San Pedro - Recovery Bridge Housing - September 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179548_TheBeaconHouseAssociationofSanPedro-RecoveryBridgeHousing-September2024.pdf`  ·  251.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | THE BEACON HOUSE ASSOC OF SAN PEDRO |
| Invoice date | 2024-09-30 |
| Billed amount | $45375.00 |
| Deliverables | Recovery Bridge Housing (H323K) |
| Confidence | high |
| Notes | The 'invoice_date' is derived from the 'September 2024' reporting period stated in the document title, interpreted as the end of the month (2024-09-30) to fit the requested ISO YYYY-MM-DD format. The 'billed_amount' is a calculated sum of 750 line items, as a grand total was not explicitly present on the document. |

## Social Model Recovery Systems Inc. - Recovery Bridge Housing - September 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179546_SocialModelRecoverySystemsInc.-RecoveryBridgeHousing-September2024.pdf`  ·  255.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Social Model Recovery Systems Inc. |
| Invoice date | September 2024 |
| Billed amount | $44352.50 |
| Deliverables | Recovery Bridge Housing (HBDA) |
| Confidence | high |
| Notes | Invoice date refers to the billing period stated in the document header. There is no specific invoice issuance date. The billed_amount was calculated by summing 785 individual line items, each for 56.50, as no grand total was explicitly stated on the document. |

## Safe Refuge - Recovery Bridge Housing - September 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179545_SafeRefuge-RecoveryBridgeHousing-September2024.pdf`  ·  258.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SAFE REFUGE |
| Invoice date | September 2024 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (HSDM) |
| Confidence | medium |
| Notes | The document provides a reporting period "September 2024" rather than a single invoice date. A total billed amount for the entire document is not explicitly provided; only individual line item charges are listed without an aggregate sum. |

## Sadler Healthcare Inc. - Residential - September 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179544_SadlerHealthcareInc.-Residential-September2024.pdf`  ·  257.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC. |
| Invoice date | 2024-11-24 |
| Billed amount | $132646.23 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | high |
| Notes | The document is a data extraction report summarizing services rather than a traditional invoice. The 'invoice_date' is derived from the report's data extraction date (11/24/2024), as there is no explicit single invoice date for the services themselves; the report covers services rendered in 'September 2024'. The 'billed_amount' is the sum of the 'Total Charge' for all 537 line items visible in the document (537 * 246.79 = 132646.23). |

## Jwch Institute Inc. - Recovery Bridge Housing - Sept 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179542_JwchInstituteInc.-RecoveryBridgeHousing-September2024.pdf`  ·  232.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | AVOSH INSTITUTE INC. |
| Invoice date | — |
| Billed amount | $55715.00 |
| Deliverables | Recovery Bridge Housing (HSDX4); Recovery Bridge Housing (HSDX4 HO); Recovery Bridge Housing (HSDX4 C); Recovery Bridge Housing (HSDX4 CS) |
| Confidence | medium |
| Notes | The document is a detailed report of services billed for a period (September 2024), not a traditional single invoice with a specific invoice date. Therefore, 'invoice_date' is returned as null. The total 'billed_amount' was calculated by summing all line items from the 'Total Charge' column across all pages of the document. |

## House of Hope Foundation Inc. - Recovery Bridge Housing - Sept 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179541_HouseofHopeFoundationInc.-RecoveryBridgeHousing-September2024.pdf`  ·  223.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOUSE OF HOPE FOUNDATION INC. |
| Invoice date | September 2024 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | invoice_date refers to the billing period stated in the document header, as no specific invoice issuance date is present. billed_amount is null because a grand total billed for the entire document is not explicitly stated; only individual line item charges are provided. |

## LA Centers for Alcohol and Drug Abuse - Recovery Bridge Housing - September 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179543_LACentersforAlcoholandDrugAbuse-RecoveryBridgeHousing-September2024.pdf`  ·  302.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA CENTERS FOR ALCOHOL AND DRUG ABUSE |
| Invoice date | 2024-09-30 |
| Billed amount | $33819.50 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a multi-page report detailing services, not a traditional single invoice with a summary section. The 'vendor' was extracted from the 'Provider Name' column. The 'invoice_date' was inferred as the last day of the reporting period ('September 2024') mentioned in the document title, as no explicit invoice date was provided. The 'billed_amount' was calculated by summing the 'Total Charge' ($60.50) for all 559 line items present across the 20 pages of the document, as a grand total was not explicitly stated. The 'deliverables' were extracted from the 'Service Type' column, which was consistent for all line items. |

## Healthright 360 - Recovery Bridge Housing - Sept 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179540_Healthright360-RecoveryBridgeHousing-September2024.pdf`  ·  211.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | — |
| Billed amount | $242.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | Invoice date is not explicitly stated as a single date; the document refers to a billing period 'September 2024' and a data extraction date of '12/04/2024'. |

## Fred Browns Recovery Services Inc. - Residential - September 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179538_FredBrownsRecoveryServicesInc.-Residential-September2024.pdf`  ·  220.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | September 2024 |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1) |
| Confidence | medium |
| Notes | Invoice date refers to the billing period 'September 2024' as stated in the document title, as no specific single invoice date (YYYY-MM-DD) is present. Total billed amount is not explicitly stated on the document; summing individual line items would be an inference, which is not permitted. |

## Grandview Foundation Inc. - Recovery Bridge Housing - Sept 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179539_GrandviewFoundationInc.-RecoveryBridgeHousing-September2024.pdf`  ·  221.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANDVIEW FOUNDATION INC. |
| Invoice date | September 2024 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (HDSN) |
| Confidence | medium |
| Notes | The total billed amount is not explicitly stated on the document; only individual line items are provided. The invoice date 'September 2024' is stated as printed because a specific day (YYYY-MM-DD) is not determinable from the document. |

## Fred Browns Recovery Services Inc. - Recovery Bridge Housing - Sept 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1179537_FredBrownsRecoveryServicesInc.-RecoveryBridgeHousing-September2024.pdf`  ·  289.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | 2024-09-30 |
| Billed amount | $28737.50 |
| Deliverables | Recovery Bridge Housing (H2DX) |
| Confidence | high |
| Notes | The document is a data extraction report for a billing period rather than a traditional invoice. The invoice date is inferred as the last day of the "September 2024" billing period mentioned in the title. The billed amount is the sum of the "Total Charge" for all 475 line items listed (475 * $60.50). |
