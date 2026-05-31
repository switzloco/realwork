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
<<<<<<< Updated upstream
=======

## EXODUS RECOVERY INC - RECOVERY BRIDGE HOUSING- MAY 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164726_EXODUSRECOVERYINC-RECOVERYBRIDGEHOUSING-MAY2024.pdf`  ·  582.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | MAY 2024 |
| Billed amount | $8525.00 |
| Deliverables | Recovery Bridge Housing (H0034) |
| Confidence | high |
| Notes | invoice_date represents a billing period (month/year) rather than a specific invoice issuance date. billed_amount calculated by summing 155 line items, each for 55.00. The vendor name 'EXODUS RECOVERY INC' is identified from the document header, though it also appears in a column labeled 'Client Name'. |

## DIVINE HEALTHCARE SERVICES INC. - RECOVERY BRIDGE HOUSING - MAY.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164725_DIVINEHEALTHCARESERVICESINC.-RECOVERYBRIDGEHOUSING-MAY2024.pdf`  ·  1047.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | DIVINE HEALTHCARE SERVICES INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (P03334) |
| Confidence | medium |
| Notes | The document does not provide a single consolidated 'invoice date' or a grand 'billed_amount' total. 'MAY 2024' is stated as a reporting period, not a specific invoice date. Individual line items each have a 'TOTAL BILLED' amount of $55.00, but no aggregate total for the entire document is present. Extracting a total would require summing these individual amounts, which is an inference not allowed by the instructions. |

## FRED BROWN'S RECOVERY SERVICES INC. - RECOVERY BRIDGE HOUSING - MAY.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164727_FREDBROWN_SRECOVERYSERVICESINC.-RECOVERYBRIDGEHOUSING-MAY2024.pdf`  ·  3520.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | 2024-05-01 |
| Billed amount | $92125.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | Invoice date '2024-05-01' is inferred from the document header 'MAY 2024' and the range of service dates. The total billed amount is calculated by summing all 'Total Disbursed' line items ($55.00 each). There are 1675 line items, resulting in a total of $92125.00. |

## BEIT TSHUVAH - RECOVERY BRIDGE HOUSING - MAY.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164724_BEITTSHUVAH-RECOVERYBRIDGEHOUSING-MAY2024.pdf`  ·  484.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | BEIT TSHUVAH |
| Invoice date | — |
| Billed amount | $9075.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | Invoice date not explicitly stated on the document as a specific issue date. The document title indicates it covers services for 'MAY 2024'. |

## Volunteers of America - Residential - April 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165762_VolunteersofAmerica-Residential-April2024.pdf`  ·  201.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | VOLUNTEERS OF AMERICA OF LOS ANGELES |
| Invoice date | 2024-03-26 |
| Billed amount | $12425.58 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1); Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | high |
| Notes | The document is a summary report of services. The 'invoice_date' is extracted from the 'Data Disclaimer' statement 'accurate as of 3/26/2024' as there is no single explicit invoice date. The 'billed_amount' is the sum of all 'Total Charge' line items. |

## Tarzana Treatment Centers Inc. - Recovery Bridge Housing - Apr. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165761_TarzanaTreatmentCentersInc.-RecoveryBridgeHousing-Apr.2024.pdf`  ·  343.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TARZANA TREATMENT CENTERS INC. |
| Invoice date | April 2024 |
| Billed amount | $9625.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | Invoice date is provided as 'April 2024', lacking a specific day. Billed amount calculated by summing 175 line items, each for $55.00. |

## SRO - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187884_SRO-ICMS-Apr2024.pdf`  ·  962.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SRO Housing |
| Invoice date | 05/03/2024 |
| Billed amount | $309375.00 |
| Deliverables | D7; CFCI 2; D7 Flex; DHS; MHSA |
| Confidence | high |
| Notes | The billed_amount is taken from 'AMOUNT REQUESTED' and confirmed by the 'Total Cost' in the billing summary. The document also states 'net pay $308,925.00' after 'applied disallowed costs $450.00', but 'billed_amount' refers to the gross amount requested. Deliverables are derived from the 'Fund' categories in the 'BILLING SUMMARY' table on page 70, representing the top-level service categories. |

## Safe Refuge - Recovery Bridge Housing - Apr. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165759_SafeRefuge-RecoveryBridgeHousing-Apr.2024.pdf`  ·  2647.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SAFE REFUGE |
| Invoice date | — |
| Billed amount | $6160.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | Invoice date not explicitly stated on the document. The document title indicates 'APRIL 2024' as the service period. Billed amount is calculated by summing 112 line items, each for $55.00, from the provided OCR text. |

## Social Model Recovery Systems Inc. - Recovery Bridge Housing - Apr. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165760_SocialModelRecoverySystemsInc.-RecoveryBridgeHousing-Apr.2024.pdf`  ·  2185.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SOCIAL MODEL RECOVERY SYSTEMS INC. |
| Invoice date | April 2024 |
| Billed amount | $55275.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | Invoice date 'April 2024' is the billing period as printed in the document header, as a specific invoice issuance date (YYYY-MM-DD) is not present. The total billed amount is derived by summing the 'Total Disbursed' amount of $55.00 for each of the 1005 service line items listed in the document (1005 * $55.00 = $55275). |

## Sadler House - Residential Services - Apr.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165757_SadlerHouse-ResidentialServices-Apr.2024.pdf`  ·  2411.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | high |
| Notes | This document is a multi-page service report detailing individual service dates and charges, not a single invoice. A single 'invoice_date' and total 'billed_amount' for the entire document are not present. The 'vendor' and 'deliverables' were extracted directly from the repeating line items. |

## House of Hope Foundation Inc. - Recovery Bridge Housing - Apr. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165752_HouseofHopeFoundationInc.-RecoveryBridgeHousing-Apr.2024.pdf`  ·  676.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOUSE OF HOPE FOUNDATION INC. |
| Invoice date | 2024-04-30 |
| Billed amount | $4125.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a detailed report for services rendered in April 2024. No explicit invoice date is provided, so the last date of service (2024-04-30) in the billing month (April 2024) was used. The billed amount is the sum of all individual service line items ($55.00 per line). The document contains duplicate service entries listed across pages for the same provider program and date, which have been counted as they appear on the document (75 lines total). |

## LA Centers for Alcohol and Drug Abuse - Recovery Bridge Housing - Apr. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165756_LACentersforAlcoholandDrugAbuse-RecoveryBridgeHousing-Apr.2024.pdf`  ·  1129.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA CENTERS FOR ALCOHOL AND DRUG ABUSE |
| Invoice date | — |
| Billed amount | $110610.00 |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034:PG); Recovery Bridge Housing (H2034-C); Recovery Bridge Housing (H2034:HD) |
| Confidence | high |
| Notes | No single "invoice_date" is present as the document is a summary report of services for "April 2024". The "billed_amount" is the sum of "Total Disbursed" for all line items with a "Claim Status" of "Approved". One line item was explicitly "Denied" with a "Total Disbursed" of $0.00 and was excluded from the sum. |

## Healthright 360 - Recovery Bridge Housing - Apr. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165751_Healthright360-RecoveryBridgeHousing-Apr.2024.pdf`  ·  1181.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | April 2024 |
| Billed amount | $29315.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | No single invoice date is present, but the document header indicates 'April 2024' as the billing period. The billed_amount is the sum of all 'Total Disbursed' line items (533 entries * $55.00/entry). All deliverables are identical across all line items. |

## Fred Brown's Recovery Services Inc. - Recovery Bridge Housing - Apr. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165750_FredBrown_sRecoveryServicesInc.-RecoveryBridgeHousing-Apr.2024.pdf`  ·  1149.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | $123860.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | A single specific invoice date (YYYY-MM-DD) for the entire document is not explicitly stated. The document's title indicates 'April 2024' as the period of coverage. The 'Date of Service' column lists dates throughout April 2024. The 'billed_amount' is a sum of 2252 line items, each for $55.00. |

##  Exodus Recovery Inc - Recovery Bridge Housing - Apr. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165749_ExodusRecoveryInc-RecoveryBridgeHousing-Apr.2024.pdf`  ·  580.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | — |
| Billed amount | $22550.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The invoice date is not explicitly stated as a single date on the document; the title indicates 'APRIL 2024' as the service period. The billed_amount was calculated by summing the 'Total Charge' of all 410 line items ($55.00 each) present in the document. |

## CRI-Help Inc. - Recovery Bridge Housing - Apr. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165748_CRI-HelpInc.-RecoveryBridgeHousing-Apr.2024.pdf`  ·  956.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRI-HELP INC. |
| Invoice date | — |
| Billed amount | $24695.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document does not provide a single, specific invoice date (date of issue). It indicates 'April 2024' as the billing period and lists individual 'Date of Service' entries throughout April 2024. Therefore, 'invoice_date' is returned as null. The total billed amount is calculated by summing all 449 'Total Disbursed' line items ($55.00 each). |

## Beit T'Shuvah - Recovery Bridge Housing - Apr. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165747_BeitT_Shuvah-RecoveryBridgeHousing-Apr.2024.pdf`  ·  386.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | BEIT TSHUVAH |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | invoice_date is not explicitly stated; 'April 2024' is a billing period. billed_amount is not explicitly stated as a total; only per-line disbursed amounts are shown, and the visible table is truncated. |

## Volunteers of America - Residential - Apr.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164738_VolunteersofAmerica-Residential-April2024.pdf`  ·  201.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | VOLUNTEERS OF AMERICA OF LOS ANGELES |
| Invoice date | 2024-03-26 |
| Billed amount | $12425.58 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1); Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | medium |
| Notes | The document is a report of approved claims rather than a traditional invoice with a single invoice date and total billed amount. The 'invoice_date' is extracted from the 'Data Disclaimer' statement 'accurate as of 3/26/2024', as there is no explicit 'Invoice Date' field. The 'billed_amount' is the sum of all 'Total Disbursed' amounts listed in the document. All claims were 'Approved' and 'Total Charge' matched 'Total Disbursed'. There were 42 entries for $210.34 and 15 entries for $239.42, summing to (42 * 210.34) + (15 * 239.42) = 8834.28 + 3591.30 = 12425.58. |

## Volunteers of America - Residential - Mar.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165595_VolunteersofAmerica-Residential-Mar.2024.pdf`  ·  120.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | VOLUNTEERS OF AMERICA OF LOS ANGELES |
| Invoice date | — |
| Billed amount | $4497.60 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3); Behavioral Health; Long Term Residential (H0019:U1) |
| Confidence | high |
| Notes | No single 'invoice_date' was present on the document. The 'billed_amount' was calculated by summing all 'Total Disbursed' amounts, as the document appears to be a report of multiple approved and paid services, and 'Total Charge' and 'Total Disbursed' columns had identical values for each line item. |

##  The Beacon House Assc - Recovery Bridge Housing - Mar. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165594_TheBeaconHouseAssc-RecoveryBridgeHousing-Mar.2024.pdf`  ·  1643.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | THE BEACON HOUSE ASSC OF SAN PEDRO |
| Invoice date | March 2024 |
| Billed amount | $35695.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The 'invoice_date' is stated as 'March 2024', indicating the billing period rather than a single specific date. The 'billed_amount' was calculated by summing the 'Total Disbursed' amount ($55.00) for all 649 line items listed in the document. |

## Sadler Healthcare Inc. - Residential Services - Apr.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164737_SadlerHouse-ResidentialServices-Apr.2024.pdf`  ·  2411.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC. |
| Invoice date | — |
| Billed amount | $274419.93 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | high |
| Notes | Invoice date is not explicitly stated; a data accuracy date is present at the top of the document (3/26/2024). The billed amount is calculated by summing the 'Total Charge' column for all 1135 line items across all pages, as no single grand total was provided. Specifically, there are 1127 line items with a Total Charge of $242.97, 6 line items with a Total Charge of $0.00, and 2 line items with a Total Charge of $272.97. |

## Sadler House - Residential Services - Mar.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165593_SadlerHouse-ResidentialServices-Mar.2024.pdf`  ·  179.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | high |
| Notes | The document is a service report with multiple service dates, not a single invoice with an invoice date, so invoice_date is null. A total billed amount for the entire document (sum of all line items) is not explicitly stated, so billed_amount is null. |

##  Volunteer of America - Residential - Mar.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165592_March2024-VolunteerofAmerica-H0019Residential.pdf`  ·  120.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | VOLUNTEERS OF AMERICA OF LOS ANGELES |
| Invoice date | 2024-03-26 |
| Billed amount | $4497.60 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3); Behavioral Health; Long Term Residential (H0019:U1) |
| Confidence | high |
| Notes | The invoice_date was extracted from the 'Data Disclaimer' statement 'accurate as of 3/26/2024' as there is no explicit 'Invoice Date' field. The billed_amount is the sum of all 'Total Disbursed' values. |

## Lake Huges - Residential Services - Mar.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165589_LakeHuges-ResidentialServices-Mar.2024.pdf`  ·  1440.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LAKE HUGHES RECOVERY |
| Invoice date | — |
| Billed amount | $130710.52 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1); Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | high |
| Notes | A single invoice date is not explicitly stated on the document; individual service dates are provided in the 'Date of Service' column. The billed_amount is the sum of all 'Total Disbursed' amounts listed across all pages. |

## House of Hope Foundation Inc. - Recovery Bridge Housing - Mar. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165587_HouseofHopeFoundationInc.-RecoveryBridgeHousing-Mar.2024.pdf`  ·  861.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOUSE OF HOPE FOUNDATION INC. |
| Invoice date | 2024-03-31 |
| Billed amount | $14850.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a monthly summary report for 'March 2024'. The invoice date is set to the last day of the month as no specific invoice date was present. The billed amount was calculated by summing the 'Total Disbursed' column for all 270 line items across all 5 pages, as no grand total was explicitly stated. |

## LA Centers for Alcohol and Drug Abuse - Recovery Bridge Housing - Mar. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165588_LACentersforAlcoholandDrugAbuse-RecoveryBridgeHousing-Mar.2024.pdf`  ·  2676.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA CENTERS FOR ALCOHOL AND DRUG ABUSE |
| Invoice date | — |
| Billed amount | $55585.00 |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034:PG); Recovery Bridge Housing (H2034:HD); Recovery Bridge Housing (H2034-C) |
| Confidence | high |
| Notes | Invoice date is not explicitly stated on the document. The document title "March 2024" refers to the billing period, not a specific invoice date. Therefore, it is returned as null. |

##  Healthright 360 - Recovery Bridge Housing - Mar. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165586_Healthright360-RecoveryBridgeHousing-Mar.2024.pdf`  ·  1217.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | March 2024 |
| Billed amount | $28050.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document serves as a billing statement for services rendered in 'March 2024'. A specific day for the 'invoice_date' (YYYY-MM-DD) is not stated on the document, so 'March 2024' is provided as printed. The 'billed_amount' was calculated by summing the 'Total Disbursed' amount ($55.00) for all 510 line items listed across all pages, as no grand total was explicitly present on the document. |

## Grandview Foundation Inc. - Recovery Bridge Housing - Mar. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165585_GrandviewFoundationInc.-RecoveryBridgeHousing-Mar.2024.pdf`  ·  738.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANDVIEW FOUNDATION INC |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | Invoice date is not explicitly stated. A single total billed amount is not present on the document; only line-item charges are shown. |

## Fred Brown's Recovery Services Inc. - Recovery Bridge Housing - Mar. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165584_FredBrown_sRecoveryServicesInc.-RecoveryBridgeHousing-Mar.2024.pdf`  ·  503.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | $9955.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a multi-page report for 'March 2024' rather than a single invoice with a specific invoice date. 'March 2024' indicates the reporting period, therefore invoice_date is null. The billed_amount is the sum of 181 line items, each for $55.00. |

##  Biet T'Shuvah - Recovery Bridge Housing - Mar. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165580_BietT_Shuvah-RecoveryBridgeHousing-Mar.2024.pdf`  ·  5.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | — |
| Invoice date | — |
| Billed amount | — |
| Deliverables | — |
| Confidence | low |
| Notes | No text was detected in the provided document, so all fields are null. |

## Exodus Recovery Inc - Recovery Bridge Housing - Mar. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165583_ExodusRecoveryInc-RecoveryBridgeHousing-Mar.2024.pdf`  ·  650.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | 2024-03-31 |
| Billed amount | $15950.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The 'invoice_date' is inferred as the last day of the reporting month ('March 2024') as no explicit invoice issue date is present. The 'billed_amount' is calculated by summing the 'Total Charge' for all 290 line items (290 * $55.00), as no overall total is provided on the document. The 'Total Unbilled' column matches 'Total Charge' for all line items, indicating these amounts are likely outstanding. |

## Volunteers of America - Residential - Mar.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164748_VolunteersofAmerica-Residential-Mar.2024.pdf`  ·  120.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | VOLUNTEERS OF AMERICA OF LOS ANGELES |
| Invoice date | 2024-03-26 |
| Billed amount | $4497.60 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3); Behavioral Health; Long Term Residential (H0019:U1) |
| Confidence | high |
| Notes | The document is an overview/report of services, not a traditional invoice. The 'invoice_date' is derived from the 'Data Disclaimer' stating the accuracy date of the report, as no specific invoice date for the entire document was present. |

## CRI-Help Inc. - Recovery Bridge Housing - Mar. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165582_CRI-HelpInc.-RecoveryBridgeHousing-Mar.2024.pdf`  ·  981.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRI-HELP INC. |
| Invoice date | — |
| Billed amount | $5665.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | Invoice date is not explicitly stated as a single date on the document; 'March 2024' is provided as the billing period in the header, so null is returned for invoice_date. The OCR text provided only includes content for 'page 1' and 'page 5' of the full document image. The total billed amount and deliverables list are calculated based solely on the 103 service line items found within these provided OCR blocks. Pages 2, 3, and 4 of the document's OCR were not provided in the prompt. |

## The Beacon House Assc - Recovery Bridge Housing - Feb. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165579_TheBeaconHouseAssc-RecoveryBridgeHousing-Feb.2024.pdf`  ·  4073.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | THE BEACON HOUSE ASSC OF SAN PEDRO - Recovery Bridge Housing |
| Invoice date | February 2024 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The document lists services for 'February 2024' as the billing period, not a specific invoice issue date (YYYY-MM-DD). No total 'billed_amount' is present on the document; only individual line item charges are listed. |

## So Cal Alcohol and Drug Programs - Residential Services - Feb.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165576_SoCalAlcoholandDrugPrograms-ResidentialServices-Feb.2024.pdf`  ·  622.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SO CAL ALCOHOL AND DRUG PROGRAMS INC. |
| Invoice date | — |
| Billed amount | $48282.26 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1); Behavioral Health; Long Term Residential (H0019:U3); Behavioral Health; Long Term Residential (H0019:U1:HD); Behavioral Health; Long Term Residential (H0019:U3:HD) |
| Confidence | high |
| Notes | The document is a report of services billed, not a traditional invoice. Therefore, a single 'invoice_date' is not present. The 'billed_amount' has been calculated by summing all values in the 'Total Charge' column. There are 167 instances of $213.46 and 52 instances of $242.97. Calculation: (167 * 213.46) + (52 * 242.97) = 35647.82 + 12634.44 = 48282.26. |

##  Social Model Recovery Systems Inc. - Recovery Bridge Housing - Feb. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165577_SocialModelRecoverySystemsInc.-RecoveryBridgeHousing-Feb.2024.pdf`  ·  5560.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SOCIAL MODEL RECOVERY SYSTEMS INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | No single 'invoice_date' or 'billed_amount' (grand total) is explicitly stated on the document. The document appears to be a report listing multiple service dates and individual charges. The document title mentions 'February 2024' but includes service dates from 2022, 2023, and 2024, at two different rates ($50.00 and $55.00). |

## Safe Refuge - Recovery Bridge Housing - Feb. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165575_SafeRefuge-RecoveryBridgeHousing-Feb.2024.pdf`  ·  5055.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SAFE REFUGE |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The document is a multi-year report summarizing services for various February months (2022, 2023, 2024), not a single invoice with a specific invoice date. Therefore, 'invoice_date' is null. The document provides individual line item amounts ('Total Disbursed') but no grand total billed amount for the entire document. Summing the line items would be an inference, thus 'billed_amount' is null. |

##  Sadler House - Residential Services - Feb.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165574_SadlerHouse-ResidentialServices-Feb.2024.pdf`  ·  2033.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | high |
| Notes | The document is a multi-page report of individual service entries rather than a single summary invoice. Therefore, a single 'invoice_date' and total 'billed_amount' for the entire document are not present. The 'deliverables' represent the consistent service type listed across all line items. |

## JWCH Institute Inc. - Recovery Bridge Housing - Feb. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165571_JWCHInstituteInc.-RecoveryBridgeHousing-Feb.2024.pdf`  ·  13.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | — |
| Invoice date | — |
| Billed amount | — |
| Deliverables | — |
| Confidence | low |
| Notes | The document is completely blank or unreadable. No information could be extracted. |

##  House of Hope Foundation Inc. - Recovery Bridge Housing - Feb. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165570_HouseofHopeFoundationInc.-RecoveryBridgeHousing-Feb.2024.pdf`  ·  1757.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOUSE OF HOPE FOUNDATION INC. |
| Invoice date | February 2024 |
| Billed amount | $26665.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a multi-page report detailing services, not a single invoice. The 'invoice_date' refers to the period the report covers and cannot be formatted as YYYY-MM-DD. Pages 3, 5, and 8 were not provided in the OCR transcriptions and therefore their data could not be extracted or included in the total billed amount. The billed amount is a summation of 'Total Charge' line items from the available OCR pages. Services span across February of 2024, 2023, and 2022, with daily rates of $55.00 in 2024 and $50.00 in 2023 and 2022. |
>>>>>>> Stashed changes
