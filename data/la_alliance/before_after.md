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

## Healthright 360 - Recovery Bridge Housing - Feb. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165569_Healthright360-RecoveryBridgeHousing-Feb.2024.pdf`  ·  1604.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | — |
| Billed amount | $39095.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a report of services rendered for multiple periods (February 2024 and February 2023), not a single invoice with one invoice date. 'February 2024' is stated as a general period at the top, but line items cover both 2023 and 2024. Therefore, 'invoice_date' is set to null. The 'billed_amount' is the sum of all 'Total Disbursed' line items across all pages (519 lines at $55.00 and 211 lines at $50.00). |

## Grandview Foundation Inc. - Recovery Bridge Housing - Feb. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165568_GrandviewFoundationInc.-RecoveryBridgeHousing-Feb.2024.pdf`  ·  1312.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANDVIEW FOUNDATION INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The document is a multi-page data extract listing service dates and individual charges, not a single invoice with an overall invoice date or total billed amount. Therefore, 'invoice_date' and 'billed_amount' are null. The earliest service date is 2023-02-01 and the latest is 2024-03-27. The data extraction date is stated as 2024-03-01, but this is not an invoice date. |

## Fred Brown -Residential Services - Feb.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165566_FredBrown-ResidentialServices-Feb.2024.pdf`  ·  640.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | $50347.96 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3); Behavioral Health; Long Term Residential (H0019:U1) |
| Confidence | high |
| Notes | The document is a statement of services over a period (February 2024), not a single invoice with a specific invoice date. The 'invoice_date' field is therefore null. The 'billed_amount' is the sum of all 'Total Disbursed' line items across all pages. |

## Fred Brown's Recovery Services Inc. - Recovery Bridge Housing - Feb. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165567_FredBrown_sRecoveryServicesInc.-RecoveryBridgeHousing-Feb.2024.pdf`  ·  9199.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The document is a multi-page service report covering a period (February 2024 and February 2023), not a single invoice. Therefore, a single 'invoice_date' and 'billed_amount' for the entire document are not explicitly stated. Summation of line items for a total billed amount is not permitted by instructions. |

## February 2024- Fred Brown- H0019 Residential Services

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165563_February2024-FredBrown-H0019ResidentialServices.pdf`  ·  640.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3); Behavioral Health; Long Term Residential (H0019:U1) |
| Confidence | medium |
| Notes | No single invoice date is explicitly stated; the document is a report of services over a period. The date '3/26/2024' is stated as a data accuracy date, not an invoice date. No single total billed amount is explicitly stated for the entire document; only line-item 'Total Disbursed' amounts are provided. |

## Exodus Recovery Inc - Recovery Bridge Housing - Feb. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165561_ExodusRecoveryInc-RecoveryBridgeHousing-Feb.2024.pdf`  ·  668.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | — |
| Billed amount | $29810.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | invoice_date is null as the document is a multi-page report detailing services over a period (February 2023 - February 2024), not a single invoice with a specific date. The title 'February 2024' refers to the reporting period. Pages 2 and 3 appear to be duplicate printouts of the data on page 1, repeating the same line items and date ranges. The billed amount is calculated by summing the unique line items found on page 1 only. |

## So Cal Alcohol and Drug Programs - Residential Services - Feb.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164742_SoCalAlcoholandDrugPrograms-ResidentialServices-Feb.2024.pdf`  ·  622.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SO CAL ALCOHOL AND DRUG PROGRAMS INC. |
| Invoice date | — |
| Billed amount | $52795.43 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1); Behavioral Health; Long Term Residential (H0019:U3); Behavioral Health; Long Term Residential (H0019:U1:HD); Behavioral Health; Long Term Residential (H0019:U3:HD) |
| Confidence | high |
| Notes | The document is a service claim report with multiple service dates, not a single invoice with a specific invoice date, therefore 'invoice_date' is null. The 'billed_amount' was calculated by summing all 'Total Disbursed' values across all pages of the document. |

## CRI-Help Inc. - Recovery Bridge Housing - Feb. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165560_CRI-HelpInc.-RecoveryBridgeHousing-Feb.2024.pdf`  ·  1463.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRI-HELP INC. |
| Invoice date | February 2024 |
| Billed amount | $15360.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The invoice_date is not a single specific date but a period ("February 2024") as stated in the document header. It is returned as printed as no specific day is determinable. The billed_amount was calculated by summing the "Total Disbursed" for all 285 unique line items across the provided document segments, accounting for overlaps between images. The "Total Disbursed" amount per line item varied between $55.00 (for 2024 services) and $50.00 (for 2023 services) depending on the date of service. |

## Sadler Healthcare Inc. - Residential Services - Feb.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164741_SadlerHouse-ResidentialServices-Feb.2024.pdf`  ·  2033.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | medium |
| Notes | The document is a multi-page report detailing numerous service instances, not a single invoice with a singular invoice date or total billed amount. `invoice_date` is null as no overall invoice date is provided. Dates of service are listed per line item. `billed_amount` is null as no overall total billed amount is provided for the entire document. Line-item charges are provided for each service, but summing them would be an inference, which is not permitted. |

## Lake Huges - Residential Services - Feb.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164740_LakeHuges-ResidentialServices-February2024.pdf`  ·  2971.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LAKE HUGHES RECOVERY |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3); Behavioral Health; Long Term Residential (H0019:U1) |
| Confidence | medium |
| Notes | Invoice date is null as the document is a data extraction or report showing services over a period, not a single invoice with a specific issue date. Billed amount is null as there is no overall total amount stated on the document; only individual line item charges are present. |

## Volunteers of America - Residential - Jan.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165504_VolunteersofAmerica-Residential-Jan.2024.pdf`  ·  2126.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | VOLUNTEERS OF AMERICA OF LOS ANGELES |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3); Behavioral Health; Long Term Residential (H0019:U1) |
| Confidence | high |
| Notes | No single 'invoice date' is stated on the document; a range of 'Date of Service' entries is provided. No single 'total billed' amount for the entire document is explicitly stated; individual 'Total Charge' and 'Total Disbursed' amounts are listed per service line item. |

## Tarzana Treatment Centers Inc. - Recovery Bridge Housing - Jan. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165502_TarzanaTreatmentCentersInc.-RecoveryBridgeHousing-Jan.2024.pdf`  ·  3328.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TARZANA TREATMENT CENTERS INC. |
| Invoice date | — |
| Billed amount | $74250.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a detailed report for services rendered during January 2024, not a single invoice with a specific invoice date. Each line item has its own 'Date of Service'. The 'billed_amount' was calculated by summing the 'Total Disbursed' amount for all line items. There are 25 pages, each with 54 line items, totaling 1350 line items. Each line item has a 'Total Disbursed' amount of $55.00, so the total billed amount is 1350 * $55.00 = $74,250.00. |

## Social Model Recovery Systems Inc. - Recovery Bridge Housing - Jan. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165499_SocialModelRecoverySystemsInc.-RecoveryBridgeHousing-Jan.2024.pdf`  ·  1383.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SOCIAL MODEL RECOVERY SYSTEMS INC |
| Invoice date | January 2024 |
| Billed amount | $75350.00 |
| Deliverables | Recovery Bridge Housing (H2024) |
| Confidence | high |
| Notes | Invoice date represents a reporting period (January 2024) as printed, no specific day is provided. Billed amount calculated by summing all 1370 line items, each at $55.00. |

## Sadler House - Residential Services - Jan.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165469_SadlerHouse-ResidentialServices-Jan.2024.pdf`  ·  1936.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | high |
| Notes | This document appears to be a multi-line service report rather than a single summary invoice. Therefore, a single 'invoice_date' and 'billed_amount' for the entire document are not present. The 'Date of Service' column contains multiple dates (from 2024-01-01 to 2024-01-31). The 'Total Charge' and 'Total Disbursed' are listed per line item, but no overall total is provided. The 'Data Disclaimer' mentions 'accurate as of 3/26/2024', which appears to be a report generation date, not an invoice date. |

## Safe Refuge - Recovery Bridge Housing - Jan. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165471_SafeRefuge-RecoveryBridgeHousing-Jan.2024.pdf`  ·  689.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SAFE REFUGE |
| Invoice date | — |
| Billed amount | $64900.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The invoice_date is null because no specific date for the invoice itself is present; 'January 2024' in the title refers to the service reporting period. The billed_amount was calculated by summing the 'Total Charged' for all 1180 line items, as no grand total was explicitly stated. |

## LA Centers for Alcohol and Drug Abuse - Recovery Bridge Housing - Jan. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165468_LACentersforAlcoholandDrugAbuse-RecoveryBridgeHousing-Jan.2024.pdf`  ·  1652.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA CENTERS FOR ALCOHOL AND DRUG ABUSE |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | low |
| Notes | The document is a detailed service log for January 2024, not a single invoice with a specific invoice date. Therefore, 'invoice_date' is null. There is no grand total 'billed_amount' present on the document; only individual line item amounts are listed. Summing these would be an inference, which is explicitly disallowed, so 'billed_amount' is null. |

## JWCH Institute Inc. - Recovery Bridge Housing - Jan. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165467_JWCHInstituteInc.-RecoveryBridgeHousing-Jan.2024.pdf`  ·  879.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH INSTITUTE INC. |
| Invoice date | January 2024 |
| Billed amount | $8660.00 |
| Deliverables | Recovery Bridge Housing (HSDX4); Recovery Bridge Housing (HSDX4-HI); Recovery Bridge Housing (HSDX4-PG); Recovery Bridge Housing (HSDX4-H); Recovery Bridge Housing (HSDX4-I); Recovery Bridge Housing (HSDX4-C); Recovery Bridge Housing (HSDX4-G); Recovery Bridge Housing (HSDX4-M); Recovery Bridge Housing (HSDX4-HS) |
| Confidence | high |
| Notes | The 'invoice_date' was extracted as 'January 2024' as stated in the header, as no specific invoice day was provided. The 'billed_amount' was calculated by summing all 'Total Charge' line items across all 6 pages of the document. |

## Fred Brown - Residential - Jan.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165465_January2024-FredBrown-H0019Residential.pdf`  ·  744.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | 2024-03-26 |
| Billed amount | $63678.45 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1); Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | high |
| Notes | The document is a service report, not a traditional invoice. The 'invoice_date' has been extracted from the 'Data Disclaimer' date (accurate as of) as there is no single invoice date. The 'billed_amount' is the sum of all 'Total Disbursed' line items: (131 * $213.46) + (147 * $242.97). |

##  House of Hope Foundation Inc. - Recovery Bridge Housing - Jan. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165463_HouseofHopeFoundationInc.-RecoveryBridgeHousing-Jan.2024.pdf`  ·  670.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOUSE OF HOPE FOUNDATION INC. |
| Invoice date | — |
| Billed amount | $12980.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | Invoice date is not explicitly stated as a single date for the entire document; rather, the document details services provided across a range of dates in January 2024, as indicated by the 'January 2024 Recovery Bridge Housing' title and 'Date of Service' column. |

## Healthright 360 - Recovery Bridge Housing - Jan. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165462_Healthright360-RecoveryBridgeHousing-Jan.2024.pdf`  ·  673.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | January 2024 |
| Billed amount | $23815.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | invoice_date: The document is a monthly summary for "January 2024" rather than a single invoice date. Dates of service range from 2024-01-01 to 2024-01-31. "January 2024" is used as it is printed at the top of the document. billed_amount: Calculated by summing the "Total Charge" for all 433 line items across all 5 pages (433 * $55.00). |

## Grandview Foundation Inc. - Recovery Bridge Housing - Jan. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165460_GrandviewFoundationInc.-RecoveryBridgeHousing-Jan.2024.pdf`  ·  465.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANVIEW FOUNDATION INC. |
| Invoice date | January 2024 |
| Billed amount | $33715.00 |
| Deliverables | Recovery Bridge Housing (H2024) |
| Confidence | high |
| Notes | Invoice date refers to the reporting period 'January 2024' as stated in the document header. No specific invoice day was present. The billed amount was calculated by summing all 'Total Unburdened' values (613 line items * $55.00 each). |

## Fred Brown's Recovery Services Inc. - Recovery Bridge Housing - Jan. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165458_FredBrown_sRecoveryServicesInc.-RecoveryBridgeHousing-Jan.2024.pdf`  ·  2252.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | $30635.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | A specific invoice date is not present; "January 2024" is stated as the period covered by this report. The billed_amount was calculated by summing the 'Total Billed' for all 557 line items across the 17 pages (557 * $55.00 = $30635.00). |

##  Exodus Recovery Inc - Recovery Bridge Housing - Jan. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165454_ExodusRecoveryInc-RecoveryBridgeHousing-Jan.2024.pdf`  ·  237.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | January 2024 |
| Billed amount | $13000.00 |
| Deliverables | Recovery Bridge Housing (HSDPA) |
| Confidence | medium |
| Notes | The document provides 'January 2024' as a billing period rather than a specific YYYY-MM-DD invoice date. No single specific invoice date is present on the document. The 'billed_amount' was calculated by summing the 'Total Charge' column for all 260 line items ($50.00 per item). |

## Divine Healthcare Services Inc. - Recovery Bridge Housing - Jan. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165453_DivineHealthcareServicesInc.-RecoveryBridgeHousing-Jan.2024.pdf`  ·  201.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | DIVINE HEALTHCARE SERVICES INC. |
| Invoice date | — |
| Billed amount | $3465.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | An explicit 'invoice_date' is not present on the document. The document title indicates 'January 2024' as the service period, and a disclaimer states the data extraction date was 'May 2024'. |

## Fred Brown - Residential Services - Jan.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165456_FredBrown-ResidentialServices-Jan.2024.pdf`  ·  744.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | $65380.37 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1); Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | high |
| Notes | The document is a report compiling multiple service dates for January 2024, not a single invoice with a specific invoice date. Therefore, 'invoice_date' is null. The date '3/26/2024' in the disclaimer is a report generation date, not an invoice date. The 'billed_amount' is the sum of all 'Total Disbursed' values from the provided OCR text across all pages. OCR text for page 6 was missing, so its data could not be included in the total billed amount or deliverables count. |

##  CRI-Help Inc. - Recovery Bridge Housing - Jan. 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1165452_CRI-HelpInc.-RecoveryBridgeHousing-Jan.2024.pdf`  ·  609.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRI-HELP INC. |
| Invoice date | January 2024 |
| Billed amount | $14300.00 |
| Deliverables | Recovery Bridge Housing (H2024) |
| Confidence | high |
| Notes | The invoice date 'January 2024' represents the reporting period as no specific invoice date (YYYY-MM-DD) is present for the entire document. The billed amount is a sum of 260 individual line items, each for 'Recovery Bridge Housing (H2024)' service, charged at $55.00 per item. |

## Fred Brown - Residential Services - Jan.2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1164743_FredBrown-ResidentialServices-Jan.2024.pdf`  ·  744.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | 2024-03-26 |
| Billed amount | $67726.69 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1); Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | high |
| Notes | The invoice date is taken from the 'Data Disclaimer' as the date the data was accurate. The billed amount is the sum of all 'Total Disbursed' entries across all pages (143 instances of $213.46 and 153 instances of $242.97). Deliverables are derived from the distinct 'Service Type' entries. |

## Volunteers of America of Los Angeles - Residential - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162171_DEC2023-VOLUNTEERSOFAMERICAOFLOSANGELES-Residental.pdf`  ·  510.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | VOLUNTEERS OF AMERICA OF LOS ANGELES |
| Invoice date | December 2023 |
| Billed amount | $141514.26 |
| Deliverables | Behavioral Health: Long Term Residential (H0019 U1) |
| Confidence | high |
| Notes | The invoice_date 'December 2023' refers to the period of services billed, as no specific invoice issuance date was present. The billed_amount was calculated by summing all 'Total Charge' entries from the document (441 entries of 239.42 and 156 entries of 230.34), as a grand total was not explicitly stated. |

## The Beacon House Assc of San Pedro - Recovery Bridge Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162167_DEC2023-THEBEACONHOUSEASSCOFSANPEDRO-RecoveryBridgeHousing.pdf`  ·  942.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | THE BEACON HOUSE ASSOC OF SAN PEDRO |
| Invoice date | — |
| Billed amount | $66330.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document specifies 'December 2023' as the reporting period, not a specific invoice date, so invoice_date is null. The billed_amount was calculated by multiplying the consistent 'Total Charge' of 55 by the total number of service line items (1206) found across the document. |

## Tarzana Treatment Centers Inc. - Recovery Bridge Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162166_DEC2023-TARZANATREATMENTCENTERSINC.-RecoveryBridgeHousing.pdf`  ·  3326.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TARZANA TREATMENT CENTERS INC. |
| Invoice date | December 2023 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H3034) |
| Confidence | low |
| Notes | billed_amount is unreadable (appears as '$S' in the document). The invoice_date 'December 2023' refers to the billing period rather than a specific invoice issue date. |

## So Cal Alcohol and Drug Programs Inc. - Residential - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162164_DEC2023-SOCALALCOHOLANDDRUGPROGRAMSINC.-Residental.pdf`  ·  6.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | — |
| Invoice date | — |
| Billed amount | — |
| Deliverables | — |
| Confidence | low |
| Notes | All fields are missing or unreadable as the provided document content is blank. |

## Social Model Recovery Systems Inc. - Recovery Bridge Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162165_DEC2023-SOCIALMODELRECOVERYSYSTEMSINC.-RecoveryBridgeHousing.pdf`  ·  1484.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SOCIAL MODEL RECOVERY SYSTEMS INC. |
| Invoice date | — |
| Billed amount | $146960.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | No single invoice date is present on the document. The document lists services provided during December 2023. The billed amount was calculated by summing the 'Total Charge' of 55 for each of the 2672 line items listed from Data Row Number 8 to 2679. The deliverable 'Recovery Bridge Housing (H2034)' is consistently listed under the 'Service Name' column, and confirmed by the 'Service Type' description on page 11. |

## Safe Refuge - Recovery Bridge Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162163_DEC2023-SAFEREFUGE-RecoveryBridgeHousing.pdf`  ·  1584.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SAFE REFUGE |
| Invoice date | — |
| Billed amount | $18150.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a detailed report for the month of December 2023, listing individual services provided. It does not have a single 'invoice_date' for the entire document; instead, each line item has its own 'Date of Service'. The 'billed_amount' was calculated by summing the 'Total Charge' (55) for all 330 line items across the 11 pages (330 * 55 = 18150). |

## Sadler Healthcare Inc. - Residential - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162162_DEC2023-SADLERHEALTHCAREINC.-Residental.pdf`  ·  1058.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC |
| Invoice date | December 2023 |
| Billed amount | $459197.50 |
| Deliverables | Behavioral Health, Long Term Residential (H0019 U1) |
| Confidence | high |
| Notes | The invoice_date is extracted as the month and year explicitly stated as the reporting period. The billed_amount is calculated by multiplying the consistent 'Total Charge' of 262.97 by the total number of service entries (1750 entries across 7 pages of data). |

## LA Centers for Alcohol and Drug Abuse - Recovery Bridge Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162160_DEC2023-LACENTERSFORALCOHOLANDDRUGABUSE-RecoveryBridgeHousing.pdf`  ·  3267.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA CENTERS FOR ALCOHOL AND DRUG ABUSE |
| Invoice date | — |
| Billed amount | $123200.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a detailed list of services provided in December 2023. No single 'invoice date' is present, only a billing period 'December 2023'. The 'billed_amount' is calculated by summing the 'Total Charge' ($55) for each line item (2240 lines total across all pages). Deliverables are consistently listed as 'Recovery Bridge Housing (H2034)' for all service entries. |

## JWCH Institute Inc. - Recovery Bridge Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162159_DEC2023-JWCHINSTITUTEINC.-RecoveryBridgeHousing.pdf`  ·  959.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH INSTITUTE INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034:HS); Recovery Bridge Housing (H2034:C); Recovery Bridge Housing (H2034-PG); Recovery Bridge Housing (H2034:HD) |
| Confidence | high |
| Notes | The document is a detailed service report listing individual service dates and charges for December 2023. A single 'invoice_date' for the entire document and a 'billed_amount' (total sum) are not explicitly stated on the document. |

## House of Hope Foundation Inc. - Recovery Bridge Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162158_DEC2023-HOUSEOFHOPEFOUNDATIONINC.-RecoveryBridgeHousing.pdf`  ·  708.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOUSE OF HOPE FOUNDATION INC. |
| Invoice date | — |
| Billed amount | $85305.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a report for the period 'December 2023', not a single invoice with a specific issue date. Therefore, 'invoice_date' is null. The 'billed_amount' was calculated by summing the 'Total Charge' column for all line items (1551 lines * 55 per line), as no grand total was explicitly provided on the document. |

## Healthright 360- Recovery Bridge Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162157_DEC2023-HEALTHRIGHT360-RecoveryBridgeHousing.pdf`  ·  682.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | 2023-12-31 |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | Billed amount is null because a total billed amount is not explicitly stated on the document; only individual line item amounts are present. The invoice date is inferred as the end of the month (2023-12-31) from the report title 'December 2023' which indicates the period covered. |

## Fred Brown's Recovery Services Inc. - Residential - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162155_DEC2023-FREDBROWN_SRECOVERYSERVICESINC.-Residental.pdf`  ·  461.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health: Long Term Residential (HDCS U/I); Residential Alcohol and/or Drug Service (HDCS U/I) |
| Confidence | medium |
| Notes | Invoice date is not present. The document refers to a reporting period 'December 2023' and a data extraction date 'March 2024', but no single invoice issuance date. Total billed amount is not present; the document lists individual line item charges but no grand total. |

## Grandview Foundation Inc. - Recovery Bridge Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162156_DEC2023-GRANDVIEWFOUNDATIONINC.-RecoveryBridgeHousing.pdf`  ·  475.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANDVIEW FOUNDATION INC. |
| Invoice date | December 2023 |
| Billed amount | $15895.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The vendor name is stated on page 1 and page 8. The invoice date 'December 2023' is taken from the document title on page 8 as no specific ISO YYYY-MM-DD invoice date is present. The deliverables 'Recovery Bridge Housing (H2034)' are extracted from the 'Service Type' column on pages 8-14. The billed amount is calculated by counting the number of 'Recovery Bridge Housing (H2034)' service lines on pages 8-14 (total 289 lines) and multiplying by the unit charge of 55, which is consistently shown under 'Total Charge' on pages 15-21. The number of lines in the 'Total Charge' section (408 lines) is different from the number of service lines (289 lines), which reduces confidence in directly summing the 'Total Charge' column without explicit context linking it to the specific 'December 2023' services. The billed amount is derived from the explicit service entries and the explicit unit charge. |

## Fred Brown's Recovery Services Inc. - Recovery Bridge Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162154_DEC2023-FREDBROWN_SRECOVERYSERVICESINC.-RecoveryBridgeHousing.pdf`  ·  2380.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | $264770.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | A specific 'invoice_date' field is not present on the document; 'December 2023' is indicated as the billing month in the header. The 'billed_amount' was calculated by summing the 'Total Billed' amount for each of the 4814 line items, where each line item bills 55. |

## Exodus Recovery Inc. - Recovery Bridge Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162153_DEC2023-EXODUSRECOVERYINC-RecoveryBridgeHousing.pdf`  ·  266.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | No single invoice date for the entire document was found; the document indicates a period of December 2023. No grand total billed amount was explicitly stated on the document; only individual line item charges are present. |

## The Beacon House Assc of San Pedro - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162150_NOV2023-THEBEACONHOUSEASSCOFSANPEDRO-RecoveryBridgeHousing.pdf`  ·  893.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | THE BEACON HOUSE ASSOC OF SAN PEDRO |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | low |
| Notes | No single invoice date is explicitly stated; the document covers services for November 2023. The 'Total Charge' column contains 'SS' values, making the total billed amount unreadable or undeterminable. |

## CRI-Help Inc. - Recovery Bridge Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162151_DEC2023-CRI-HELPINC.-RecoveryBridgeHousing.pdf`  ·  545.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRI-HELP INC. |
| Invoice date | December 2023 |
| Billed amount | $19470.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The invoice date is presented as the billing period 'December 2023'. A specific day (DD) was not explicitly stated on the document, so it is provided as printed rather than an ISO YYYY-MM-DD format. |

## Tarzana Treatment Centers Inc. - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162149_NOV2023-TARZANATREATMENTCENTERSINC.-RecoveryBridgeHousing.pdf`  ·  2909.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TARZANA TREATMENT CENTERS INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2016) |
| Confidence | medium |
| Notes | The document is a data extraction report for services provided in November 2023, not a single invoice, so a singular 'invoice_date' is not present. The 'billed_amount' is unreadable/redacted, appearing as '$$' in all entries for 'Total Charge' and 'Total Disbursed'. |

## Social Model Recovery Systems Inc. - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162148_NOV2023-SOCIALMODELRECOVERYSYSTEMSINC.-RecoveryBridgeHousing.pdf`  ·  1319.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SOCIAL MODEL RECOVERY SYSTEMS INC |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | low |
| Notes | No specific invoice date is present; the document indicates a reporting period of 'November 2023'. The 'Total Charge' column, which would determine the billed amount, contains only '$$' for all line items, making the total billed amount unreadable and undeterminable. |

## So Cal Alcohol and Drug Programs Inc. - Resedential - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162146_NOV2023-SOCALALCOHOLANDDRUGPROGRAMSINC.-Residental.pdf`  ·  810.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SO CAL ALCOHOL AND DRUG PROGRAMS INC |
| Invoice date | — |
| Billed amount | $59278.52 |
| Deliverables | Behavioral Health: Long Term Residential (H0019 U1); Behavioral Health: Long Term Residential (H0019 U3); Behavioral Health: Long Term Residential (H0019 H5) |
| Confidence | high |
| Notes | The document is a data extract/report for services rendered in November 2023, with an extraction date of March 2024, rather than a traditional invoice with a single 'invoice_date'. Therefore, 'invoice_date' is returned as null. All other fields were clearly and consistently present. |

## Sadler Healthcare Inc. - Residential - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162142_NOV2023-SADLERHEALTHCAREINC.-Residental.pdf`  ·  855.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC. |
| Invoice date | November 2023 |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3) |
| Confidence | medium |
| Notes | invoice_date refers to the reporting period (November 2023) as a specific invoice date is not present. The total billed_amount is not explicitly stated on the document; only individual line item charges are listed, and calculations are not permitted. |

## Safe Refuge - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162144_NOV2023-SAFEREFUGE-RecoveryBridgeHousing.pdf`  ·  1553.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SAFE REFUGE |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | invoice_date is null because the document provides a processing month ('November 2023') and individual 'Date of Service' values per line item, but no single invoice date for the entire document in YYYY-MM-DD format. billed_amount is null because the document provides a 'Total Charge' for each line item, but no overall total billed amount for the entire spreadsheet/invoice is explicitly stated on the document. Calculating a sum would be an inference. |

## Lake Hughes Recovery - Residential - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162141_NOV2023-LAKEHUGHESRECOVERY-Residental.pdf`  ·  2865.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LAKE HUGHES RECOVERY |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U1); Residential -Alcohol and/or Drug Service (H0019:U1:HA); Subacute Detox Residential (H0019:U1S) |
| Confidence | high |
| Notes | The document is a detailed data extract of services for November 2023, not a single consolidated invoice. As such, a specific 'invoice_date' and a 'billed_amount' (total for the entire document) are not stated explicitly and would require inference or calculation, which is disallowed. Each line item has a 'Date of Service' and 'Total Charge', but no overarching invoice date or grand total is present. |

## LA Centers for Alcohol and Drug Abuse - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162140_NOV2023-LACENTERSFORALCOHOLANDDRUGABUSE-RecoveryBridgeHousing.pdf`  ·  3287.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA CENTERS FOR ALCOHOL AND DRUG ABUSE |
| Invoice date | 2023-11-30 |
| Billed amount | $74415.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a monthly report for November 2023. 'invoice_date' is set to the last day of the reporting month to represent the reporting period. 'billed_amount' is calculated by summing the 'Total Charge' for all 1353 service line items identified across the 23 data pages, where each line item has a stated 'Total Charge' of 55. The grand total is not explicitly printed on the document. |

## House of Hope Foundation Inc. - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162138_NOV2023-HOUSEOFHOPEFOUNDATIONINC.-RecoveryBridgeHousing.pdf`  ·  530.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOUSE OF HOPE FOUNDATION INC. |
| Invoice date | — |
| Billed amount | $15675.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | invoice_date field is null because the document is a service report spanning multiple dates (November 2023), not a single invoice with a specific issue date. billed_amount was calculated by summing the 'Total Charge' of 55.00 for each of the 285 detected service line items, as no grand total was explicitly provided on the document. The document format is a spreadsheet/data export, not a traditional invoice. |

## JWCH Institute Inc. - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162139_NOV2023-JWCHINSTITUTEINC.-RecoveryBridgeHousing.pdf`  ·  925.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCH INSTITUTE INC. |
| Invoice date | — |
| Billed amount | $25940.00 |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034:HD); Recovery Bridge Housing (H2034-C); Recovery Bridge Housing (H2034-D); Recovery Bridge Housing (H2034-PG); Recovery Bridge Housing (H2034-HS) |
| Confidence | high |
| Notes | The document is a detailed service report for November 2023, not a traditional single invoice with a distinct 'invoice date'. Therefore, 'invoice_date' is returned as null, as no single date applies to the entire document. The 'billed_amount' was calculated by summing the 'Total Charge' column for all 384 line items across the 6 pages of the document. |

## Grandview Foundation Inc. - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162136_NOV2023-GRANDVIEWFOUNDATIONINC.-RecoveryBridgeHousing.pdf`  ·  438.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANDVIEW FOUNDATION INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | Invoice date is a report period (November 2023) with multiple service dates; a single invoice date for the entire document is not present. The total billed amount is not explicitly summed on the document, only individual line item charges are listed. |

## Healthright 360 - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162137_NOV2023-HEALTHRIGHT360-RecoveryBridgeHousing.pdf`  ·  589.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | — |
| Billed amount | $2750.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | A single invoice date is not present on the document; service dates range across November 2023. The billed amount is calculated by summing the 'Total Charge' (55) for each of the 50 line items found in the provided OCR data block. It is assumed the provided OCR data block represents the complete list of billed services from the document. |

## Fred Brown's Recovery Services Inc. - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162134_NOV2023-FREDBROWN_SRECOVERYSERVICESINC.-RecoveryBridgeHousing.pdf`  ·  2371.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | $43890.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | A single invoice date is not present. The document is a data extract for services provided in "November 2023", as indicated in the document title. The billed_amount was calculated by summing the 'Total Charge' of $55 for each of the 798 line items found in the document. |

## Exodus Recovery Inc. - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162133_NOV2023-EXODUSRECOVERYINC.-RecoveryBridgeHousing.pdf`  ·  257.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) - daily bundled rate encompassing assessment, counseling, family therapy, medication services, patient education, and intervention services |
| Confidence | medium |
| Notes | A specific invoice date is not present. The document is titled 'November 2023', which indicates the reporting period. The 'Total Charge' and 'Total Disbursed' values are unreadable ('SS') for all line items on the document, and no grand total is provided, so the billed_amount cannot be determined. |

## Divine Healthcare Services Inc. - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162132_NOV2023-DIVINEHEALTHCARESERVICESINC.-RecoveryBridgeHousing.pdf`  ·  646.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | DIVINE HEALTHCARE SERVICES INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | low |
| Notes | Invoice date is not present on the document; the document indicates a billing period (November 2023) and a data extraction date (March 2024). The billed amount is unreadable; the 'Total Charge' column consistently displays 'SS' instead of numeric values. |

## CRI-Help Inc. - Recovery Bridge Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162131_NOV2023-CRI-HELPINC.-RecoveryBridgeHousing.pdf`  ·  505.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRI-HELP INC |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | invoice_date is not explicitly stated; only a billing period (November 2023) and individual service dates are present. A grand total billed_amount for the entire document is not explicitly stated; only line-item charges are provided. |

## The Beacon House Assc of San Pedro - Recovery Bridge Housing - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162130_OCT2023-THEBEACONHOUSEASSCOFSANPEDRO-RecoveryBridgeHousing.pdf`  ·  674.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | THE BEACON HOUSE ASSOC OF SAN PEDRO |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | low |
| Notes | Invoice date is not a specific YYYY-MM-DD, only a month and year range ('October 2023') is present in the document title, and individual service dates are listed in a column. No single overall invoice date is available. The 'billed_amount' could not be determined as the 'Total Charge' column values are all unreadable ('SS'). |

## Tarzana Treatment Centers Inc. - Recovery Bridge Housing - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162129_OCT2023-TARZANATREATMENTCENTERSINC.-RecoveryBridgeHousing.pdf`  ·  3090.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | TARZANA TREATMENT CENTERS INC. |
| Invoice date | 2023-10-31 |
| Billed amount | $20460.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a detailed ledger for services provided in October 2023. The 'invoice_date' is inferred as the last day of the month the services cover (October 2023) based on the document's header. The 'billed_amount' is calculated by summing the 'Total Disbursed' for all line items. There are 12 unique locations, each with 31 daily entries for October, and each entry shows a disbursement of $55. Therefore, 12 locations * 31 days * $55 = $20,460. |

## Social Model Recovery Systems Inc. - Recovery Bridge Housing - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162128_OCT2023-SOCIALMODELRECOVERYSYSTEMSINC.-RecoveryBridgeHousing.pdf`  ·  1241.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SOCIAL MODEL RECOVERY SYSTEMS INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | Invoice date is a billing period 'October 2023' rather than a specific date. No single total billed amount is present; only per-line-item charges are listed. |

## So Cal Alcohol and Drug Programs Inc. - Residential - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162127_OCT2023-SOCALALCOHOLANDDRUGPROGRAMSINC.-Residental.pdf`  ·  852.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SO CAL ALCOHOL AND DRUG PROGRAMS INC. |
| Invoice date | October 2023 |
| Billed amount | $80387.13 |
| Deliverables | Behavioral Health; Long Term Residential (H0019:U3:HD) |
| Confidence | high |
| Notes | The invoice_date 'October 2023' is provided as printed, as a specific YYYY-MM-DD date for the entire document was not determinable. The billed_amount was calculated by summing all individual 'Total Charge' line items across all pages: (166 items * 213.48) + (185 items * 242.97) = 35437.68 + 44949.45 = 80387.13. The deliverables were consistent across all line items. |

## Safe Refuge - Recovery Bridge Housing - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162126_OCT2023-SAFEREFUGE-RecoveryBridgeHousing.pdf`  ·  1443.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SAFE REFUGE |
| Invoice date | 2023-10-31 |
| Billed amount | $95700.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | Invoice date inferred as the last day of the billing period (October 2023) as no specific invoice date was present. The total billed amount was calculated by summing 1740 individual line items, each with a total charge of $55.00. |

## Sadler Healthcare Inc. - Residential - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162125_OCT2023-SADLERHEALTHCAREINC.-Residental.pdf`  ·  631.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SADLER HEALTHCARE INC. |
| Invoice date | October 2023 |
| Billed amount | — |
| Deliverables | Behavioral Health, Long Term Residential (HDDU9 L1) |
| Confidence | medium |
| Notes | Invoice date refers to the billing period 'October 2023' rather than a specific issuance date. Total billed amount is not explicitly stated as a sum on the document; only individual line item charges are present. Returning null as per instructions not to infer or calculate. |

## LA Centers for Alcohol and Drug Abuse - Recovery Bridge Housing - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162123_OCT2023-LACENTERSFORALCOHOLANDDRUGABUSE-RecoveryBridgeHousing.pdf`  ·  3327.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA CENTERS FOR ALCOHOL AND DRUG ABUSE |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | Invoice date is not explicitly stated for the entire document; 'October 2023' refers to the service period. Billed amount is not stated as this is a partial document (page 25 of an unknown total). |

## Lake Hughes Recovery - Residential - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162124_OCT2023-LAKEHUGHESRECOVERY-Residental.pdf`  ·  2701.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LAKE HUGHES RECOVERY |
| Invoice date | — |
| Billed amount | $243513.65 |
| Deliverables | Residential -Alcohol and/or Drug Service (H0019:U1:HA); Behavioral Health, Long Term Residential (H0019:U1); Residential -Alcohol and/or Drug Service (H0019:U3:HA); Behavioral Health, Long Term Residential (H0019:U3); Subacute Detox Residential (H0019:LTF); Subacute Detox Residential (H0019:LTF:HA) |
| Confidence | high |
| Notes | The document indicates a billing period of 'OCTOBER 2023', but a specific invoice date (day) is not determinable from the text, so 'invoice_date' is returned as null. The billed_amount was calculated by summing all 'Total Charge' line items across all 21 pages of the document. |

## Healthright 360. - Recovery Bridge Housing - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162120_OCT2023-HEALTHRIGHT360-RecoveryBridgeHousing.pdf`  ·  671.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HEALTHRIGHT 360 |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The document is a detailed service report listing individual services rendered during October 2023, not a single invoice with a distinct invoice date or a consolidated total billed amount. Therefore, 'invoice_date' and 'billed_amount' are returned as null as they are not explicitly stated on the document. The date 10/31/2023 mentioned in the overview is an extract generation date, not an invoice date. |

## House of Hope Foundation - Recovery Bridge Housing - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162121_OCT2023-HOUSEOFHOPEFOUNDATIONINC.-RecoveryBridgeHousing.pdf`  ·  453.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | HOUSE OF HOPE FOUNDATION INC. |
| Invoice date | — |
| Billed amount | $4840.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | The provided text is OCR for page 3 of a multi-page document. An overall 'invoice_date' for the entire billing document is not present in the provided OCR text; only 'Date of Service' for individual line items (all in October 2023) are available. The billed_amount is calculated by summing the 'Total Billed' for all 88 line items on this page (88 * $55.00). |

## Fred Brown's Recovery Services Inc. - Residential - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162118_OCT2023-FREDBROWN_SRECOVERYSERVICESINC.-Residental.pdf`  ·  509.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Behavioral Health, Long Term Residential (HDDS U1) |
| Confidence | medium |
| Notes | The document is a detailed report rather than a summary invoice. A single 'invoice_date' is not present, though 'October 2023' is indicated as the reporting period. A single 'billed_amount' (grand total) is not present; only line-item 'Total Charge' values are listed. |

## JWCH Institute Inc. - Recovery Bridge Housing - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162122_OCT2023-JWCHINSTITUTEINC.-RecoveryBridgeHousing.pdf`  ·  920.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | JWCW INSTITUTE INC. |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034); Recovery Bridge Housing (H2034-HS); Recovery Bridge Housing (H2034-PG); Recovery Bridge Housing (H2034-C) |
| Confidence | medium |
| Notes | invoice_date is null because no single 'Invoice Date' field is present on the document. 'October 2023' is in the title, referring to the service period, and 'March 2024' is stated as the extraction date in the overview, but neither is an explicit invoice date nor formatted as YYYY-MM-DD with a specific day. billed_amount is null because there is no explicit 'Total Billed Amount' or 'Grand Total' field stated on the document. Individual line item charges are present, but no overall sum. |

## Grandview Foundation Inc. - Recovery Bridge Housing - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162119_OCT2023-GRANDVIEWFOUNDATIONINC.-RecoveryBridgeHousing.pdf`  ·  381.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | GRANDVIEW FOUNDATION INC. |
| Invoice date | — |
| Billed amount | $3465.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | A single 'invoice_date' is not explicitly stated on the document. The document is a report titled 'Recovery Bridge Housing - Recovery Bridge Housing October 2023', and lists individual service entries with specific 'Date Entered' values, primarily within October 2023. These 'Date Entered' values represent service dates rather than a single invoice date. The billed_amount was calculated by summing the 'Total Billed Amount' for all 63 line items ($55.00 each). |

## Exodus Recovery Inc. - Recovery Bridge Housing - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162116_OCT2023-EXODUSRECOVERYINC-RecoveryBridgeHousing.pdf`  ·  184.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | EXODUS RECOVERY INC |
| Invoice date | — |
| Billed amount | — |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | medium |
| Notes | invoice_date is not present as a single date; the document specifies 'October 2023' as a summary period and lists individual 'Date of Service' entries. billed_amount is not present as a grand total; the document lists individual charges per service date without a summed total for the entire document. |

## Fred Brown's Recovery Services Inc. - Recovery Bridge Housing - Oct. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162117_OCT2023-FREDBROWN_SRECOVERYSERVICESINC.-RecoveryBridgeHousing.pdf`  ·  2381.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | FRED BROWN'S RECOVERY SERVICES INC. |
| Invoice date | October 2023 |
| Billed amount | $41855.00 |
| Deliverables | Recovery Bridge Housing (H2034) |
| Confidence | high |
| Notes | The document is a detailed service log/report covering the month of October 2023, rather than a single invoice with a specific invoice date. 'October 2023' is used for invoice_date to represent the billing period indicated in the report header. The billed_amount is calculated by summing all 'Total Charge' line items (761 lines * $55.00/line). |

## WCA - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190094_WCA-Sep2024.pdf`  ·  300.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Weingart Center Association |
| Invoice date | 2024-09-12 |
| Billed amount | — |
| Deliverables | ICMS costs for Permanent Supportive Housing Edition enrollments for August 2024 service month |
| Confidence | high |
| Notes | This document is a 'Notification of Payment Recovery' from Los Angeles County to the vendor (Weingart Center Association), not an invoice from the vendor to the county. The 'billed_amount' field is null because the document does not state a total amount billed by the vendor; instead, it states an amount ($13,972.50) that DHS is recovering due to disallowed costs. |

## VOALA - Sep 2024.pdf

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190093_VOALA-Sep2024.pdf`  ·  1748.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Volunteers of America |
| Invoice date | 2024-10-02 |
| Billed amount | $115440.00 |
| Deliverables | ARPA; ARPA/FHSP; CFCI 2; D7; DHS; HDAP; HDAP (D7); HDAP (GR); MHSA |
| Confidence | high |
| Notes | — |

## The Center in Hollywood - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190090_TheCenterinHollywood-Sep2024.pdf`  ·  326.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The Center in Hollywood |
| Invoice date | 2024-10-01 |
| Billed amount | $144813.75 |
| Deliverables | Vacant Slot Cost - D7; Occupied Slot Cost - D7; Vacant Slot Cost - DHS; Occupied Slot Cost - DHS; Vacant Slot Cost - SAM; Occupied Slot Cost - SAM |
| Confidence | high |
| Notes | All requested fields are clearly stated. The deliverables are extracted from the 'BILLING SUMMARY' on page 29, which consolidates costs by Fund (D7, DHS, SAM) and slot status (Vacant/Occupied). Detailed individual slot and staff listings were not treated as separate line items for the final deliverable list, as their costs are aggregated into these summary categories. |

## Step up on Second - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190089_StepuponSecond-Sep2024.pdf`  ·  615.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Step Up on Second |
| Invoice date | 2024-10-03 |
| Billed amount | $577476.25 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; Housing for Healthy CA; D7 Flex; HFMH (D7); MHSA; SRAP |
| Confidence | high |
| Notes | The invoice date was extracted from 'DATE SUBMITTED'. Deliverables were extracted from the 'BILLING SUMMARY' section on page 101, which categorizes the services/programs being billed. |

## The People Concern - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190091_ThePeopleConcern-Sep2024.pdf`  ·  15211.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The People Concern |
| Invoice date | 2024-10-03 |
| Billed amount | $1662743.75 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; D7 Flex; EWH; HDAP; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA; PHK (D7) |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE SUBMITTED' on page 1. Deliverables are derived from the 'Fund' categories listed in the 'BILLING SUMMARY' table on page 198, representing the high-level services billed. |

## ST JOSEPH CENTER - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190088_STJOSEPHCENTER-Sep2024.pdf`  ·  468.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | St. Joseph's Center |
| Invoice date | 2024-10-09 |
| Billed amount | $501385.00 |
| Deliverables | ARPA; D7; ARPA/FHSP; Housing for Healthy CA; SAM; D7 Flex; DHS; HDAP (D7); HFMH (D7); MHSA; PHK (D7) |
| Confidence | high |
| Notes | — |

## SSG.HOPICS - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190087_SSG.HOPICS-Sep2024.pdf`  ·  1354.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SSG/HOPICS/Project180 |
| Invoice date | 2024-10-07 |
| Billed amount | $464963.75 |
| Deliverables | ARPA: $40,537.50; ARPA/FHSP: $48,903.75; D7: $270,901.25; DHS: $13,800.00; SAM: $3,622.50; D7 Flex: $9,660.00; DHSP (D7): $9,315.00; HDAP: $15,525.00; HDAP (D7): $13,886.25; HFMH (D7): $5,175.00; Housing for Healthy CA: $21,217.50; MHSA: $12,420.00 |
| Confidence | high |
| Notes | Vendor and billed amount found on page 1. Invoice date (date submitted) found on page 1. Deliverables and their costs are extracted from the 'BILLING SUMMARY' table on page 77 under 'Fund' and 'Total Cost'. |

## SROH - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190086_SROH-Sep2024.pdf`  ·  4972.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SRO Housing |
| Invoice date | 2024-10-02 |
| Billed amount | $343706.25 |
| Deliverables | D7; Housing for Healthy CA; SRAP; CFCI 2; D7 Flex; DHS; MHSA |
| Confidence | high |
| Notes | — |

## SFVCMHC - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190085_SFVCMHC-Sep2024.pdf`  ·  260.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | San Fernando Valley Community Mental Health Center |
| Invoice date | 2024-09-12 |
| Billed amount | $258.75 |
| Deliverables | Recovery of disallowed ICMS costs for August 2024 service month due to enrollments flagged for Overdue Documentation |
| Confidence | high |
| Notes | The document is a notification of payment recovery. The 'billed_amount' represents the total amount being recovered from the vendor due to disallowed costs. The 'deliverables' describe the reason for these disallowed costs. |

## PENNY LANE - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190084_PENNYLANE-Sep2024.pdf`  ·  4764.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Penny Lane |
| Invoice date | 2024-10-07 |
| Billed amount | $115316.25 |
| Deliverables | Vacant Slots; Occupied Slots |
| Confidence | high |
| Notes | The invoice date year '24' was inferred to be 2024 based on the 'DATE INVOICE RECIEVED: 10/7/2024' and the footer timestamp 'Run by Rosa Leynes on 10/1/2024'. Deliverables are extracted from the main categories of billed items explicitly named in the document: 'VACANT SLOTS' and 'OCCUPIED SLOTS', which are summarized on page 26. |

## MHALB - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190082_MHALB-Sep2024.pdf`  ·  372.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Mental Health America (MHA), Long Beach |
| Invoice date | 2024-10-07 |
| Billed amount | $273412.50 |
| Deliverables | ARPA/FHSP; D7; DHS; SAM; Housing for Healthy CA; D7 Flex; HFMH (D7); MHSA |
| Confidence | high |
| Notes | — |

## PATH - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190083_PATH-Sep2024.pdf`  ·  283.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | PATH |
| Invoice date | 2024-09-12 |
| Billed amount | $9056.25 |
| Deliverables | ICMS costs billed under Work Order 113-HFH-ICMS |
| Confidence | medium |
| Notes | The document is a 'Notification of Payment Recovery Due to Disallowed Costs' from Los Angeles County Health Services to PATH, rather than a traditional invoice from a homeless-service provider to Los Angeles County. 'vendor' was inferred as 'PATH' because the document explicitly references 'ICMS costs billed under Work Order 113-HFH-ICMS' which were disallowed, indicating PATH as the original billing provider. 'billed_amount' is the 'Total Disallowed Cost Amount' of $9,056.25 being recovered by the county from PATH, which is a negative adjustment to prior billing. 'deliverables' is based on the stated subject of the recovery. |

## LSTEP - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190081_LSTEP-Sep2024.pdf`  ·  710.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Life Skills Training and Educational Programs |
| Invoice date | 2024-10-04 |
| Billed amount | $218677.50 |
| Deliverables | ARPA/FHSP; D7; DHS; HFMH (D7); MHSA |
| Confidence | high |
| Notes | Invoice date formatted to YYYY-MM-DD. Deliverables represent the fund categories from the 'BILLING SUMMARY' on page 39, which detail different types of slots and staffing services. |

## LINC - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190080_LINC-Sep2024.pdf`  ·  426.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LINC |
| Invoice date | 2024-10-03 |
| Billed amount | $259698.75 |
| Deliverables | ARPA/FHSP; D7; D7 Flex; Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | — |

## KYCC - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190078_KYCC-Sep2024.pdf`  ·  2427.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Koreatown Youth and Community Center (KYCC) |
| Invoice date | 2024-10-02 |
| Billed amount | $82627.50 |
| Deliverables | D7; D7 Flex; MHSA |
| Confidence | high |
| Notes | Invoice date '10/2/24' interpreted as YYYY-MM-DD based on FY 24-25 budget period. |

## LAFH - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190079_LAFH-Sep2024.pdf`  ·  1378.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Family Housing (LAFH) |
| Invoice date | 2024-10-03 |
| Billed amount | $497641.25 |
| Deliverables | D7; PHK (D7); SAM; D7 Flex; DHS; MHSA |
| Confidence | high |
| Notes | — |

## Jenesse Solaris - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190077_JenesseSolaris-Sep2024.pdf`  ·  1389.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Jenesse Center, Inc. |
| Invoice date | 2024-10-11 |
| Billed amount | $23977.50 |
| Deliverables | Single Adult High Acuity; Family High Acuity |
| Confidence | high |
| Notes | The date 'Dotober 11, 2024' was interpreted as 'October 11, 2024' for the invoice_date. Deliverables are identified from the categories of 'Occupied Slots' that contributed to the total billed amount, as summarized on pages 8, 9, and 10. |

## Housing Works - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190076_HousingWorks-Sep2024.pdf`  ·  435.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Housing Works (HW) |
| Invoice date | 10/15/2024 |
| Billed amount | $270737.50 |
| Deliverables | ARPA/FHSP; D7; DHS; D7 Flex; DHSP (D7); HFMH (D7); Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | — |

## HHCLA - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190075_HHCLA-Sep2024.pdf`  ·  6326.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Homeless Healthcare Los Angeles (HHCLA) |
| Invoice date | 2024-10-09 |
| Billed amount | $231150.00 |
| Deliverables | ARPA/FHSP; D7; SAM; D7 Flex; DHS; MHSA; SRAP |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE INVOICE RECIEVED'. Deliverables are listed as the 'Fund' categories from the 'BILLING SUMMARY' table on page 42, representing high-level service categories. |

## Exodus - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190073_Exodus-Sep2024.pdf`  ·  401.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Exodus |
| Invoice date | 2024-10-01 |
| Billed amount | $321836.25 |
| Deliverables | ARPA slots; ARPA/FHSP slots; D7 slots; D7 Flex slots; DHS slots; HFMH (D7) slots; PHK (D7) slots; SRAP slots |
| Confidence | high |
| Notes | The deliverables are extracted from the 'BILLING SUMMARY' on the last page, representing the aggregated categories of 'slots' billed. |

## Heritage Clinic - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190074_HeritageClinic-Sep2024.pdf`  ·  14493.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Heritage Clinic |
| Invoice date | 10/11/24 |
| Billed amount | $255127.50 |
| Deliverables | ARPA; CFCI 2; D7; PHK (D7); MHSA; SRAP |
| Confidence | high |
| Notes | — |

## DWC - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190072_DWC-Sep2024.pdf`  ·  292.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Downtown Women's Center |
| Invoice date | 2024-09-12 |
| Billed amount | $8797.50 |
| Deliverables | ICMS costs (Work Order 018-HFH-ICMS) |
| Confidence | high |
| Notes | The document is a notification of payment recovery from Los Angeles County to the provider, Downtown Women's Center, not a traditional invoice from the provider. The 'billed_amount' refers to the total amount being recovered by the County. 'Deliverables' refers to the overarching category of services for which costs were disallowed, as stated in the document. |

## CRCD - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190071_CRCD-Sep2024.pdf`  ·  373.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRCD Coalition for Responsible Community |
| Invoice date | 2024-10-04 |
| Billed amount | $221231.25 |
| Deliverables | ARPA; D7; D7 Flex; MHSA; SRAP |
| Confidence | high |
| Notes | — |

## A Community of Friends - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190069_ACommunityofFriends-Sep2024.pdf`  ·  203.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | — |
| Invoice date | — |
| Billed amount | $212615.00 |
| Deliverables | — |
| Confidence | low |
| Notes | Vendor name is not explicitly stated on the document. The organization "A COMMUNITY OF FRIENDS" is mentioned in a file path related to the contract, but its role as the billing organization is not explicitly stated. Invoice date is not present; only email communication dates are available. No line-item services or deliverables are listed. |

## American Family Housing - Sep 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1190070_AmericanFamilyHousing-Sep2024.pdf`  ·  172.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | American Family Housing |
| Invoice date | 2024-10-11 |
| Billed amount | $78573.75 |
| Deliverables | STAFFING; INVALID SLOTS; NEW SLOTS; RESERVED SLOTS; VACANT SLOTS; OCCUPIED SLOTS |
| Confidence | high |
| Notes | Invoice date '10.11.24' on page 1 was interpreted as YYYY-MM-DD based on the footer timestamp '10/11/2024'. Deliverables are extracted from the main section headers that describe the services and reporting categories within the document. |

## The People Concern - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189822_ThePeopleConcern-Aug2024.pdf`  ·  916.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The People Concern |
| Invoice date | 2024-09-09 |
| Billed amount | $1647877.50 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; Housing for Healthy CA; D7 Flex; EWH; HDAP; HDAP (D7); HFMH (D7); MHSA; PHK (D7) |
| Confidence | high |
| Notes | — |

## SSG - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189820_SSG-Aug2024.pdf`  ·  1693.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SSG/HOPICS/Project180 |
| Invoice date | 2024-09-05 |
| Billed amount | $342240.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; D7 Flex; DHSP (D7); HDAP; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | — |

## The Center in Hollywood - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189821_TheCenterinHollywood-Aug2024.pdf`  ·  308.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The Center in Hollywood |
| Invoice date | 9/9/2024 |
| Billed amount | $142916.25 |
| Deliverables | Vacant Slot Cost; Occupied Slot Cost |
| Confidence | high |
| Notes | Invoice date taken from 'DATE SUBMITTED'. Deliverables are derived from the aggregated categories in the 'BILLING SUMMARY' on page 27, representing the types of services for which costs were incurred. 'New Slot Cost' was $0.00 and therefore not included. |

## SRO - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189819_SRO-Aug2024.pdf`  ·  762.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SRO Housing |
| Invoice date | 2024-09-05 |
| Billed amount | $340860.00 |
| Deliverables | D7; Housing for Healthy CA; SRAP; CFCI 2; D7 Flex; DHS; MHSA |
| Confidence | high |
| Notes | — |

## Penny Lane - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189818_PennyLane-Aug2024.pdf`  ·  3735.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Penny Lane |
| Invoice date | 2024-09-05 |
| Billed amount | $113418.75 |
| Deliverables | D7 slots; D7 Flex slots; MHSA slots |
| Confidence | high |
| Notes | — |

## PATH - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189817_PATH-Aug2024.pdf`  ·  975.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | PATH |
| Invoice date | 2024-09-10 |
| Billed amount | $934296.25 |
| Deliverables | ARPA; ARPA/FHSP; D7; D7 Flex; DHS; SAM; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA; PHK (D7); SRAP |
| Confidence | high |
| Notes | Invoice date taken from 'DATE SUBMITTED'. Deliverables extracted from the 'BILLING SUMMARY' table on page 149. |

## LST and E - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189816_LSTandE-Aug2024.pdf`  ·  757.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Life Skills Training and Educational Programs |
| Invoice date | 2024-09-10 |
| Billed amount | $208552.50 |
| Deliverables | ARPA/FHSP; D7; DHS; HFMH (D7); MHSA |
| Confidence | high |
| Notes | — |

## LINC - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189815_LINC-Aug2024.pdf`  ·  431.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LINC |
| Invoice date | 2024-09-03 |
| Billed amount | $253402.50 |
| Deliverables | ARPA/FHSP; D7; D7 Flex; Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | — |

## LAFH - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189814_LAFH-Aug2024.pdf`  ·  1964.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Family Housing (LAFH) |
| Invoice date | 2024-09-03 |
| Billed amount | $444618.75 |
| Deliverables | D7; PHK (D7); SAM; D7 Flex; DHS; MHSA |
| Confidence | high |
| Notes | — |

## KYCC - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189813_KYCC-Aug2024.pdf`  ·  2094.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Koreatown Youth and Community Center (KYCC) |
| Invoice date | 2024-09-06 |
| Billed amount | $82627.50 |
| Deliverables | D7 Slots; D7 Flex Slots; MHSA Slots |
| Confidence | high |
| Notes | — |

## HHCLA - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189812_HHCLA-Aug2024.pdf`  ·  6204.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Homeless Healthcare Los Angeles (HHCLA) |
| Invoice date | 2024-09-09 |
| Billed amount | $233057.50 |
| Deliverables | ARPA/FHSP; D7; SAM; D7 Flex; DHS; MHSA; SRAP |
| Confidence | high |
| Notes | — |

## Exodus - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189810_Exodus-Aug2024.pdf`  ·  421.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Exodus |
| Invoice date | 2024-09-01 |
| Billed amount | $316537.50 |
| Deliverables | ARPA; ARPA/FHSP; D7; D7 Flex; DHS; HFMH (D7); PHK (D7); SRAP |
| Confidence | high |
| Notes | — |

## CRCD - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189809_CRCD-Aug2024.pdf`  ·  430.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRCD Coalition for Responsible Community Development |
| Invoice date | 2024-08-05 |
| Billed amount | $223905.00 |
| Deliverables | ARPA services; D7 services; D7 Flex services; MHSA services; SRAP services |
| Confidence | high |
| Notes | — |

## Heritage Clinic - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189811_HeritageClinic-Aug2024.pdf`  ·  12892.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Heritage Clinic |
| Invoice date | 2024-09-03 |
| Billed amount | $255127.50 |
| Deliverables | ARPA; CFCI 2; D7; PHK (D7); MHSA; SRAP |
| Confidence | high |
| Notes | All requested values were extracted directly from the document. The invoice date was taken from 'DATE SUBMITTED'. The deliverables are the 'Fund' categories listed in the 'BILLING SUMMARY' on page 42, representing the types of projects/services. |

## A Community of Friends - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189807_ACommunityofFriends-Aug2024.pdf`  ·  509.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | A Community of Friends |
| Invoice date | 2024-09-12 |
| Billed amount | $187766.25 |
| Deliverables | D7; D7 Flex; MHSA |
| Confidence | high |
| Notes | Invoice date taken from 'DATE SUBMITTED'. Deliverables are extracted from the 'Fund' categories listed in the 'BILLING SUMMARY' on page 42, as these represent the main service categories billed. |

## American Family Housing - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189808_AmericanFamilyHousing-Aug2024.pdf`  ·  163.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | American Family Housing |
| Invoice date | 2024-09-03 |
| Billed amount | $76417.50 |
| Deliverables | American Family Housing EHV (D7); American Family Housing FUP (D7); American Family Housing Scattered 1 (D7); American Family Housing Scattered 2 (D7); American Family Housing Scattered 3 (ARPA/FHSP) |
| Confidence | high |
| Notes | Deliverables were extracted from the 'Project' names listed under 'VACANT SLOTS' and 'OCCUPIED SLOTS' sections, as these represent the specific services/projects for which costs are incurred. The total billed amount is clearly stated on page 1 ('AMOUNT REQUESTED') and confirmed in the 'BILLING SUMMARY' on page 18. |

## WCA - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1189805_WCA-Aug2024.pdf`  ·  16355.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Weingart Center Association |
| Invoice date | 2024-09-09 |
| Billed amount | $228735.00 |
| Deliverables | D7; D7 Flex; DHS |
| Confidence | high |
| Notes | — |

## WCA - Aug 24

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183590_REDACTEDWCAWO_395Aug24Reviewed.pdf`  ·  16355.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Weingart Center Association |
| Invoice date | 2024-09-09 |
| Billed amount | $228735.00 |
| Deliverables | D7 Services; D7 Flex Services; DHS Services |
| Confidence | high |
| Notes | Invoice date was extracted from 'DATE SUBMITTED'. Deliverables are derived from the 'Fund' categories in the 'BILLING SUMMARY' which represent distinct service types being billed. |

## The Center in Hollywood - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183587_REDACTEDTheCenterinHollywoodWO_279Aug24Reviewed.pdf`  ·  308.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The Center in Hollywood |
| Invoice date | 2024-09-09 |
| Billed amount | $142916.25 |
| Deliverables | The Center CoC (D7); The Center CoC (DHS); The Center CoC DMH (D7); The Center CoC DMH (DHS); The Center FHSP TBV (DHS); The Center LACDA HCV 2021 (D7); The Center DHS/DMH (D7); The Center Pre-Housing Resource Unsubsidized (D7); The Center Scattered 1 (D7); The Center EHV (D7); The Center FHSP TBV (D7); The Center Scattered 2 (DHS); The Center TBSH (D7); The Center TBSH DMH (D7) |
| Confidence | high |
| Notes | — |

## The People Concern - Aug 2024 

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183588_REDACTEDThePeopleConcernWO110Aug24Reviewed.pdf`  ·  916.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The People Concern |
| Invoice date | — |
| Billed amount | $1647877.50 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; Housing for Healthy CA; D7 Flex; EWH; HDAP; HDAP (D7); HFMH (D7); MHSA; PHK (D7) |
| Confidence | medium |
| Notes | A specific 'invoice_date' field was not found. The 'CLAIM PERIOD' is stated as '08 / 2024', and the 'DATE INVOICE RECIEVED' is '9/9/2024'. The 'DATE SUBMITTED' is blank. |

## SSG - Aug 2024 

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183586_REDACTEDSSGWO_022Aug24Reviewed.pdf`  ·  1693.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SSG/HOPICS/Project180 |
| Invoice date | 2024-09-05 |
| Billed amount | $342240.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; D7 Flex; DHSP (D7); HDAP; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | — |

## SRO - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183585_REDACTEDSROWO_021Aug24Reviewed.pdf`  ·  762.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SRO Housing |
| Invoice date | 2024-09-05 |
| Billed amount | $340860.00 |
| Deliverables | D7; Housing for Healthy CA; SRAP; CFCI 2; D7 Flex; DHS; MHSA |
| Confidence | high |
| Notes | — |

## Penny Lane - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183584_REDACTEDPennyLaneWO075Aug24Reviewed.pdf`  ·  3735.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Penny Lane |
| Invoice date | 2024-09-05 |
| Billed amount | $113418.75 |
| Deliverables | D7 services; D7 Flex services; MHSA services |
| Confidence | high |
| Notes | — |

## LST and E - Aug 2024 

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183582_REDACTEDLSTandEWO_115Aug24Reviewed.pdf`  ·  757.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Life Skills Training and Educational Programs |
| Invoice date | 2024-09-10 |
| Billed amount | $208552.50 |
| Deliverables | ARPA/FHSP; D7; DHS; HFMH (D7); MHSA |
| Confidence | high |
| Notes | — |

## PATH - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183583_REDACTEDPATHWO_113Aug24Reviewed.pdf`  ·  975.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | PATH |
| Invoice date | 2024-09-10 |
| Billed amount | $934296.25 |
| Deliverables | ARPA; ARPA/FHSP; D7; D7 Flex; DHS; SAM; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA; PHK (D7); SRAP |
| Confidence | high |
| Notes | — |

## LINC - Aug 24

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183581_REDACTEDLINCWO_114Aug24Reviewed.pdf`  ·  431.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LINC |
| Invoice date | 2024-09-03 |
| Billed amount | $253402.50 |
| Deliverables | ARPA/FHSP; D7; D7 Flex; Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | All requested fields were clearly found on the document. Invoice date was converted to ISO YYYY-MM-DD format. |

## KYCC - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183578_REDACTEDKYCCWO_095Aug24Reviewed.pdf`  ·  2094.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Koreatown Youth and Community Center (KYCC) |
| Invoice date | 2024-09-06 |
| Billed amount | $82627.50 |
| Deliverables | D7; D7 Flex; MHSA |
| Confidence | high |
| Notes | — |

## LAFH - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183579_REDACTEDLAFHWO012Aug24Reviewed.pdf`  ·  1964.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Family Housing (LAFH) |
| Invoice date | 2024-09-03 |
| Billed amount | $444618.75 |
| Deliverables | New Slot Cost; Vacant Slot Cost; Occupied Slot Cost |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE SUBMITTED'. Deliverables are derived from the cost categories listed in the 'BILLING SUMMARY' that sum up to the total billed amount. |

## HHCLA WO - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183577_REDACTEDHHCLAWO_104Aug24Reviewed.pdf`  ·  6204.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Homeless Healthcare Los Angeles (HHCLA) |
| Invoice date | 2024-09-09 |
| Billed amount | $233057.50 |
| Deliverables | ARPA/FHSP; D7; SAM; D7 Flex; DHS; MHSA; SRAP |
| Confidence | high |
| Notes | — |

## Exodus - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183574_REDACTEDExodusWO_070Aug24Reviewed.pdf`  ·  421.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Exodus |
| Invoice date | 2024-09-01 |
| Billed amount | $316537.50 |
| Deliverables | ARPA; ARPA/FHSP; D7; D7 Flex; DHS; HFMH (D7); PHK (D7); SRAP |
| Confidence | high |
| Notes | All requested fields were clearly present on the document. The total billed amount was found on page 1 as 'AMOUNT REQUESTED' and confirmed in the 'BILLING SUMMARY' table on page 55 as 'Total Cost'. |

## Heritage Clinic - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183575_REDACTEDHeritageClinicWO_087Aug24Reviewed.pdf`  ·  12892.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Heritage Clinic |
| Invoice date | 2024-09-03 |
| Billed amount | $255127.50 |
| Deliverables | ARPA; CFCI 2; D7; PHK (D7); MHSA; SRAP |
| Confidence | high |
| Notes | — |

## CRCD - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183573_REDACTEDCRCDWO_076Aug24Reviewed.pdf`  ·  430.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRCD - Coalition for Responsible Community Development |
| Invoice date | 2024-08-05 |
| Billed amount | $223905.00 |
| Deliverables | ARPA; D7; D7 Flex; MHSA; SRAP |
| Confidence | high |
| Notes | — |

## American Family Housing - Aug 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183571_REDACTEDAmericanFamilyHousingWO_096Aug24Reviewed.pdf`  ·  163.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | American Family Housing |
| Invoice date | 2024-09-03 |
| Billed amount | $76417.50 |
| Deliverables | Vacant Slots: American Family Housing EHV (D7); Vacant Slots: American Family Housing FUP (D7); Vacant Slots: American Family Housing Scattered 1 (D7); Occupied Slots: American Family Housing EHV (D7); Occupied Slots: American Family Housing FUP (D7); Occupied Slots: American Family Housing Scattered 1 (D7); Occupied Slots: American Family Housing Scattered 2 (D7); Occupied Slots: American Family Housing Scattered 3 (ARPA/FHSP) |
| Confidence | high |
| Notes | All requested fields were clearly present and readable on the document. |

##  Housing Works - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1177434_HousingWorks-ICMS-Jul2024.pdf`  ·  378.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Housing Works (HW) |
| Invoice date | 08/16/2024 |
| Billed amount | $208035.00 |
| Deliverables | ARPA/FHSP; D7; DHS; D7 Flex; DHSP (D7); HFMH (D7); Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | — |

## A Community of Friends - Aug 24 

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1183570_REDACTEDACommunityofFriendsWO_090Aug24Reviewed.pdf`  ·  509.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | A Community of Friends |
| Invoice date | 2024-09-12 |
| Billed amount | $187766.25 |
| Deliverables | D7; D7 Flex; MHSA |
| Confidence | high |
| Notes | — |

## HHCLA - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1177432_HHCLA-ICMS-Jul2024.pdf`  ·  6187.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Homeless Healthcare Los Angeles (HHCLA) |
| Invoice date | 2024-08-12 |
| Billed amount | $223646.25 |
| Deliverables | ARPA/FHSP; D7; SAM; D7 Flex; DHS; MHSA; SRAP |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE SUBMITTED'. Deliverables are extracted from the 'Fund' categories in the 'BILLING SUMMARY' as they represent distinct service types billed. |

## Downtown Women Center - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1177429_DowntownWomenCenter-ICMS-Jul2024.pdf`  ·  214.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Downtown Women's Center |
| Invoice date | 8/6/2024 |
| Billed amount | $108330.00 |
| Deliverables | ARPA; D7; DHS; SAM; MHSA |
| Confidence | high |
| Notes | Deliverables are identified from the 'Fund' categories in the billing summary, which represent distinct housing/service programs. No further detailed descriptions of individual services per fund are provided on the document. |

## CRCD - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1177428_CRCD-ICMS-Jul2024.pdf`  ·  247.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRCD - Coalition for Responsible Community |
| Invoice date | 08/05/2024 |
| Billed amount | $223905.00 |
| Deliverables | ARPA: $15,783.75; D7: $129,978.75; D7 Flex: $11,126.25; MHSA: $21,476.25; SRAP: $45,540.00 |
| Confidence | high |
| Notes | — |

## Heritage Clinic - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1177431_HeritageClinic-ICMS-Jul2024.pdf`  ·  12210.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Heritage Clinic |
| Invoice date | 2024-08-08 |
| Billed amount | $254092.50 |
| Deliverables | ARPA; CFCI 2; D7; PHK (D7); MHSA; SRAP |
| Confidence | high |
| Notes | — |

## American Family Housing - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1177427_AmericanFamilyHousing-ICMS-Jul2024.pdf`  ·  165.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | American Family Housing |
| Invoice date | 2024-08-01 |
| Billed amount | $78401.25 |
| Deliverables | ARPA/FHSP Vacant Slot Costs; ARPA/FHSP Occupied Slot Costs; D7 Vacant Slot Costs; D7 Occupied Slot Costs |
| Confidence | high |
| Notes | The invoice date is extracted from 'DATE SUBMITTED'. The billed amount is confirmed by 'AMOUNT REQUESTED' and 'BILLING SUMMARY TOTAL Cost'. Deliverables are derived from the aggregate categories and their costs as listed in the 'BILLING SUMMARY' table on page 18, representing the highest-level breakdown of services. |

## A Community of Friends - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1177426_ACommunityofFriends-ICMS-Jul2024.pdf`  ·  545.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | A Community of Friends |
| Invoice date | 8/12/2024 |
| Billed amount | $188887.50 |
| Deliverables | New Slot Cost; Vacant Slot Cost; Occupied Slot Cost |
| Confidence | high |
| Notes | — |

## KYCC - Jul 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1177425_KYCC-ICMS-Jul2024.pdf`  ·  2181.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Koreatown Youth and Community Center (KYCC) |
| Invoice date | 2024-08-08 |
| Billed amount | $81075.00 |
| Deliverables | D7 services (Housing/Service Slots); D7 Flex services (Housing/Service Slots); MHSA services (Housing/Service Slots) |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE SUBMITTED'. Deliverables are categorized by 'Fund' types from the 'BILLING SUMMARY' which details 'Vacant Slot Cost' and 'Occupied Slot Cost' for each category. |

## VOALA - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187891_VOALA-ICMS-Apr2024.pdf`  ·  1954.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Volunteers of America |
| Invoice date | 2024-05-06 |
| Billed amount | $105750.00 |
| Deliverables | ARPA/FHSP Slot Costs; D7 Slot Costs; DHS Slot Costs; HDAP Slot Costs; HDAP (D7) Slot Costs; HDAP (GR) Slot Costs; MHSA Slot Costs; PHK (D7) Slot Costs |
| Confidence | high |
| Notes | The 'billed_amount' is taken from 'AMOUNT REQUESTED' on page 1 and confirmed by 'Total Cost' in the 'BILLING SUMMARY' on page 25. The 'deliverables' are derived from the 'Fund' categories and their associated 'Slot Costs' in the 'BILLING SUMMARY' on page 25, as these represent the line-item services being billed. The 'invoice_date' is taken from 'DATE SUBMITTED' on page 1. |

## Venice community Housing - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187890_VenicecommunityHousing-ICMS-Apr2024.pdf`  ·  2328.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Venice Community Housing |
| Invoice date | 2024-05-06 |
| Billed amount | $88350.00 |
| Deliverables | D7; DHS; MHSA; PHK (D7) |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE SUBMITTED'. Deliverables are derived from the 'Fund' categories listed in the 'BILLING SUMMARY' on page 20, as these represent the aggregated services billed. |

## WCA - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187892_WCA-ICMS-Apr2024.pdf`  ·  11798.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Weingart Center Association |
| Invoice date | 2024-05-01 |
| Billed amount | $207450.00 |
| Deliverables | ICMS costs under Work Order 395-HFH-ICMS; D7 Fund Slot Costs; D7 Flex Fund Slot Costs; DHS Fund Slot Costs |
| Confidence | high |
| Notes | The 'invoice_date' is extracted from 'DATE SUBMITTED' on page 1. The 'billed_amount' reflects the 'AMOUNT REQUESTED' on page 1 and 'TOTAL Cost' from the 'BILLING SUMMARY' on page 37 ($207,450.00), which is the gross amount before disallowed costs ($900.00) were applied, as opposed to the 'net pay' ($206,550.00). The deliverables are based on the description of 'ICMS costs' on page 38 and the breakdown by 'Fund' (D7, D7 Flex, DHS) for 'Slot Costs' in the 'BILLING SUMMARY' on page 37. |

## TPC - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187889_TPC-ICMS-Apr2024.pdf`  ·  1172.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The People Concern |
| Invoice date | 2024-05-06 |
| Billed amount | $1399600.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; D7 Flex; EWH; HDAP; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA; PHK (D7) |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE SUBMITTED' on page 1, as it represents the submission date of this report. The billed amount is confirmed by 'AMOUNT REQUESTED' on page 1 and 'Total Cost' in the 'BILLING SUMMARY' on page 188. Deliverables are extracted from the 'Fund' column in the 'BILLING SUMMARY' on page 188. |

## The Center In Hollywood - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187888_TheCenterInHollywood-ICMS-Apr2024.pdf`  ·  1610.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The Center in Hollywood |
| Invoice date | 2024-05-02 |
| Billed amount | $130050.00 |
| Deliverables | D7 Vacant Slot Cost; D7 Occupied Slot Cost; DHS Vacant Slot Cost; DHS Occupied Slot Cost; SAM Occupied Slot Cost |
| Confidence | high |
| Notes | — |

## Step Up on Second - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187887_StepUponSecond-ICMS-Apr2024.pdf`  ·  965.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Step Up on Second |
| Invoice date | 2024-05-14 |
| Billed amount | $516375.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; Housing for Healthy CA; D7 Flex; HFMH (D7); MHSA; SRAP |
| Confidence | high |
| Notes | The billed amount is the 'AMOUNT REQUESTED' before 'applied disallowed costs' were deducted. The 'Deliverables' are derived from the 'Fund' categories in the 'BILLING SUMMARY' table on page 93. |

## SSG.HOPICS.P180 - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187885_SSG.HOPICS.P180-ICMS-Apr2024.pdf`  ·  484.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SSG/HOPICS/Project180 |
| Invoice date | 2024-05-07 |
| Billed amount | $299100.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; D7 Flex; DHSP (D7); HDAP; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | — |

## SJC - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187883_SJC-ICMS-Apr2024.pdf`  ·  507.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | St. Joseph's Center |
| Invoice date | 2024-05-02 |
| Billed amount | $423575.00 |
| Deliverables | ARPA; D7; ARPA/FHSP; Housing for Healthy CA; SAM; D7 Flex; DHS; HDAP (D7); HFMH (D7); MHSA; PHK (D7) |
| Confidence | high |
| Notes | — |

## SFVCMHC - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187882_SFVCMHC-ICMS-Apr2024.pdf`  ·  710.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | San Fernando Valley Community Mental Health Center (SFVCMHC) |
| Invoice date | 2024-05-13 |
| Billed amount | $88350.00 |
| Deliverables | D7 Slots; DCFS/HSSP Slots; HFMH (D7) Slots |
| Confidence | high |
| Notes | The billed_amount of 88350.00 is taken from 'AMOUNT REQUESTED' on page 1 and is confirmed by the 'TOTAL Cost' in the 'BILLING SUMMARY' on page 19. The document also mentions 'applied disallowed costs $22,800.00' and 'net pay $65,550.00', but the request is for the total billed amount, which is the higher figure before disallowances. Deliverables are identified from the 'BILLING SUMMARY' on page 19, detailing costs by fund type (D7, DCFS/HSSP, HFMH (D7)) which correspond to different categories of 'slots' (new, vacant, occupied) detailed throughout the report. |

## Penny Lane - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187881_PennyLane-ICMS-Apr2024.pdf`  ·  9620.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Penny Lane |
| Invoice date | 2024-05-08 |
| Billed amount | $115500.00 |
| Deliverables | D7 project services; D7 Flex project services; MHSA project services |
| Confidence | high |
| Notes | — |

## LSTEP - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187879_LSTEP-ICMS-Apr2024.pdf`  ·  526.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Life Skills Training and Educational Programs |
| Invoice date | 2024-05-06 |
| Billed amount | $145200.00 |
| Deliverables | ARPA/FHSP; D7; DHS; HFMH (D7); MHSA |
| Confidence | high |
| Notes | — |

## PATH - ICMS - Apr 2024.pdf

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187880_PATH-ICMS-Apr2024.pdf`  ·  1297.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | PATH |
| Invoice date | 2024-05-09 |
| Billed amount | $829175.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; D7 Flex; DHS; SAM; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA; PHK (D7); SRAP |
| Confidence | high |
| Notes | The document includes a 'NOTIFICATION OF PAYMENT RECOVERY DUE TO DISALLOWED COSTS' on page 142, indicating a disallowance of $20,850 from the total requested, which will be deducted from a *next* submitted ICMS invoice. The 'billed_amount' extracted reflects the 'AMOUNT REQUESTED' on page 1 and the 'Total Cost' in the 'BILLING SUMMARY' on page 141, which is the total amount billed *prior* to this disallowance being applied to the current invoice. |

## KYCC - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187876_KYCC-ICMS-Apr2024.pdf`  ·  1301.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Koreatown Youth and Community Center (KYCC) |
| Invoice date | 2024-05-13 |
| Billed amount | $96150.00 |
| Deliverables | D7; D7 Flex; MHSA |
| Confidence | high |
| Notes | — |

## LINC - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187878_LINC-ICMS-Apr2024.pdf`  ·  795.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LINC |
| Invoice date | 2024-05-06 |
| Billed amount | $246000.00 |
| Deliverables | ARPA/FHSP Slot Costs (Occupied and Vacant); D7 Slot Costs (Occupied and Vacant); DHS Slot Costs (Occupied); D7 Flex Slot Costs (Occupied); Housing for Healthy CA Slot Costs (Occupied and Vacant); MHSA Slot Costs (Occupied) |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE SUBMITTED'. Billed amount confirmed from 'AMOUNT REQUESTED' and 'TOTAL' in billing summary. Deliverables are derived from the 'BILLING SUMMARY' table on page 49, representing various slot costs by fund type for Housing for Health services and ICMS. |

## LAFH - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187877_LAFH-ICMS-Apr2024.pdf`  ·  792.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Family Housing (LAFH) |
| Invoice date | 2024-05-03 |
| Billed amount | $406200.00 |
| Deliverables | Vacant Slots; Occupied Slots |
| Confidence | medium |
| Notes | The 'DATE SUBMITTED: 5/3/21' on page 1 appears to be an error, as other dates such as 'CLAIM PERIOD: 04 / 2024' and the preparer's signature date '5/3/24' (Nicholas Kimble) indicate a 2024 date. The `invoice_date` is extracted from the preparer's signature date (Nicholas Kimble's signature on page 1), as it represents the date the report was signed by the vendor's representative. Deliverables are identified as the categories that contribute to the total billed amount: 'Vacant Slots' and 'Occupied Slots', as shown in the 'BILLING SUMMARY' on page 58 and detailed in the respective sections. Other slot categories ('Invalid Slots', 'New Slots', 'Reserved Slots') and 'Staffing' show zero cost in their respective summary totals. |

## Housing Works - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187875_HousingWorks-ICMS-Apr2024.pdf`  ·  893.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Housing Works (HW) |
| Invoice date | 2024-05-15 |
| Billed amount | $205050.00 |
| Deliverables | ARPA/FHSP; D7; DHS; D7 Flex; ARPA; DHSP (D7); HFMH (D7); Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | The billed_amount is taken from 'AMOUNT REQUESTED' and confirmed by the 'TOTAL Cost' in the Billing Summary. The invoice also notes 'applied disallowed costs' and 'net pay', but these are not the total billed amount. The invoice_date is taken from 'DATE SUBMITTED' on page 1, as there is no explicit 'Invoice Date' field, but this is the date the document was created and submitted by the vendor. Deliverables are derived from the 'Fund' categories listed in the 'BILLING SUMMARY' section on page 33, as these represent the breakdown of services provided. |

## HHCLA - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187874_HHCLA-ICMS-Apr2024.pdf`  ·  8027.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Homeless Healthcare Los Angeles (HHCLA) |
| Invoice date | 2024-05-10 |
| Billed amount | $198375.00 |
| Deliverables | ARPA/FHSP; D7; SAM; D7 Flex; DHS; MHSA; SRAP |
| Confidence | high |
| Notes | Invoice date '5/10/24' interpreted as 2024-05-10. Deliverables are identified from the 'Fund' categories in the 'BILLING SUMMARY' table on page 43. |

## Heritage Clinic - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187873_HeritageClinic-ICMS-Apr2024.pdf`  ·  5723.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Heritage Clinic |
| Invoice date | 2024-05-10 |
| Billed amount | $170925.00 |
| Deliverables | ARPA; D7; PHK (D7); MHSA; SRAP |
| Confidence | high |
| Notes | The billed amount is taken from 'AMOUNT REQUESTED' on the first page, which matches the 'Total Cost' in the 'BILLING SUMMARY' on page 35. This is the total billed before any 'applied disallowed costs' ($450.00) mentioned in 'AGENCY COMMENTS' on page 1 and the 'Disallowed Cost Amount' on page 37. Deliverables are identified from the 'Fund' types listed in the 'BILLING SUMMARY' on page 35, which categorize the various slots being billed. |

## Exodus - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187872_Exodus-ICMS-Apr2024.pdf`  ·  401.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Exodus |
| Invoice date | 2024-05-02 |
| Billed amount | $281625.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; D7 Flex; DHS; HFMH (D7); PHK (D7); SRAP |
| Confidence | high |
| Notes | None |

## DWC - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187871_DWC-ICMS-Apr2024.pdf`  ·  725.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Downtown Women's Center |
| Invoice date | 2024-05-21 |
| Billed amount | $112950.00 |
| Deliverables | ARPA Slots; D7 Slots; DHS Slots; SAM Slots; MHSA Slots |
| Confidence | high |
| Notes | The billed_amount of $112,950.00 is the 'AMOUNT REQUESTED' and 'TOTAL Cost' from the Billing Summary, which is the gross amount before the stated 'applied disallowed costs' of $3,600.00, resulting in a 'net pay' of $109,350.00. |

## American Family Housing - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187869_AmericanFamilyHousing-ICMS-Apr2024.pdf`  ·  610.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | American Family Housing |
| Invoice date | 2024-05-03 |
| Billed amount | $80175.00 |
| Deliverables | Vacant Slot Cost; Occupied Slot Cost |
| Confidence | high |
| Notes | — |

## A Community of Friends - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187868_ACommunityofFriends-ICMS-Apr2024.pdf`  ·  426.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | A Community of Friends |
| Invoice date | 5/6/2024 |
| Billed amount | $169650.00 |
| Deliverables | D7; D7 Flex; MHSA |
| Confidence | high |
| Notes | The total billed amount on page 1 and the Billing Summary (page 41) aligns to $169,650.00. Page 40 shows a total of $165,900.00 which corresponds to the 'Occupied Slot Cost' in the summary. Deliverables are derived from the 'Fund' categories in the 'BILLING SUMMARY' section. |

## CRCD - ICMS - Apr 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1187870_CRCD-ICMS-Apr2024.pdf`  ·  688.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRCD - Coalition for Responsible Community Development |
| Invoice date | 05/02/2024 |
| Billed amount | $179700.00 |
| Deliverables | ARPA - Vacant Slot Costs; ARPA - Occupied Slot Costs; D7 - Vacant Slot Costs; D7 - Occupied Slot Costs; D7 Flex - Occupied Slot Costs; MHSA - Vacant Slot Costs; MHSA - Occupied Slot Costs |
| Confidence | high |
| Notes | The billed_amount is taken from 'AMOUNT REQUESTED' on page 1 and confirmed by 'Total Cost' in the 'BILLING SUMMARY' on page 33. The 'net pay' figure reflects a $450.00 disallowance, which is an adjustment after billing, as detailed on page 34. Deliverables are derived from the categories and non-zero costs listed in the 'BILLING SUMMARY' on page 33, as these provide a high-level overview of services billed. |

## SFVCMHC - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186929_WO141SFVCMHCMar24__Redacted.pdf`  ·  627.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | San Fernando Valley Community Mental Health Center (SFVCMHC) |
| Invoice date | 04/02/2024 |
| Billed amount | $87900.00 |
| Deliverables | D7 Vacant Slot Cost; D7 Occupied Slot Cost; DCFS/HSSP Vacant Slot Cost; DCFS/HSSP Occupied Slot Cost; HFMH (D7) Vacant Slot Cost; HFMH (D7) Occupied Slot Cost |
| Confidence | high |
| Notes | The document presents 'AMOUNT REQUESTED' as $87,900.00 on page 1. On the same page, 'net pay' is $62,400.00 after 'applied disallowed costs' of $25,500.00. The 'Total Cost' in the billing summary on page 19 matches the 'AMOUNT REQUESTED'. The billed_amount is taken as the total amount requested/billed, which is $87,900.00. Deliverables are derived from the 'BILLING SUMMARY' on page 19, which breaks down costs by fund and slot status. |

## TCH - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186930_WO279TCHMar24__Redacted.pdf`  ·  3736.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The Center in Hollywood |
| Invoice date | 2024-04-04 |
| Billed amount | $130050.00 |
| Deliverables | New Slot Cost; Vacant Slot Cost; Occupied Slot Cost |
| Confidence | high |
| Notes | — |

## SUS - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186928_WO117SUSMar24__Redacted.pdf`  ·  1165.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Step Up on Second |
| Invoice date | 2024-04-09 |
| Billed amount | $517300.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; Housing for Healthy CA; D7 Flex; HFMH (D7); MHSA; SRAP |
| Confidence | high |
| Notes | The 'DATE SUBMITTED' (4/9/2024) on page 1 was used for 'invoice_date'. The 'AMOUNT REQUESTED' ($517,300.00) on page 1 was used for 'billed_amount' as it represents the total billed amount before any disallowed costs or net pay adjustments. Deliverables were extracted from the 'BILLING SUMMARY' table on page 94, representing the aggregated line-item services by fund type. |

## LSTE - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186927_WO115LSTEMar24__Redacted.pdf`  ·  698.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Life Skills Training and Educational Programs |
| Invoice date | 2024-04-10 |
| Billed amount | $145650.00 |
| Deliverables | ARPA/FHSP; D7; DHS; HFMH (D7); MHSA |
| Confidence | high |
| Notes | — |

## LINC - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186926_WO114LINCMar24__Redacted.pdf`  ·  2664.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LINC |
| Invoice date | April 1, 2024 |
| Billed amount | $246000.00 |
| Deliverables | ARPA/FHSP; D7; DHS; D7 Flex; Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | The billed_amount is taken from 'AMOUNT REQUESTED' on page 1, which matches the 'Total Cost' in the 'BILLING SUMMARY' on page 49. The 'deliverables' are extracted from the 'Fund' categories listed in the 'BILLING SUMMARY' on page 49, as these represent the line-item service types. |

## The People Concern - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186924_WO110TPCMar24__Redacted.pdf`  ·  5114.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The People Concern |
| Invoice date | 2024-04-16 |
| Billed amount | $1391800.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; Housing for Healthy CA; D7 Flex; EWH; HDAP; HDAP (D7); HFMH (D7); MHSA; PHK (D7) |
| Confidence | high |
| Notes | — |

## HHCLA - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186923_WO104HHCLAMar24__Redacted.pdf`  ·  518.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Watts Labor CAC |
| Invoice date | 2024-04-09 |
| Billed amount | $108525.00 |
| Deliverables | ARPA services; D7 services; DHS services; SAM services; D7 Flex services |
| Confidence | high |
| Notes | — |

## PATH - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186925_WO113PATHMar24__Redacted.pdf`  ·  2031.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | PATH |
| Invoice date | — |
| Billed amount | $825825.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; D7 Flex; DHS; SAM; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA; PHK (D7); SRAP |
| Confidence | medium |
| Notes | Invoice date is not explicitly stated as a single date (e.g., YYYY-MM-DD) on the provided image (page 1 of 145). The 'CLAIM PERIOD: 03 / 2024' indicates the month/year of services. 'DATE INVOICE RECEIVED: 4/10/2024' is a receipt date, not an invoice date. |

## KYCC - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186921_WO095KYCCMar24__Redacted.pdf`  ·  2203.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Koreatown Youth and Community Center (KYCC) |
| Invoice date | 2024-04-02 |
| Billed amount | $95850.00 |
| Deliverables | D7 Vacant Slot Cost; D7 Occupied Slot Cost; D7 Flex Occupied Slot Cost; MHSA Occupied Slot Cost |
| Confidence | high |
| Notes | — |

## A Community of Friends - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186920_WO090ACommunityofFriendsMarch24__Redacted.pdf`  ·  647.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | A Community of Friends |
| Invoice date | 04/15/2024 |
| Billed amount | $168975.00 |
| Deliverables | D7 slots (Vacant and Occupied); D7 Flex slots (Vacant and Occupied); MHSA slots (Vacant and Occupied) |
| Confidence | high |
| Notes | — |

## American Family Housing - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186922_WO096AmericanFamilyHousingMar24__Redacted.pdf`  ·  164.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | American Family Housing |
| Invoice date | 04/05/2024 |
| Billed amount | $80325.00 |
| Deliverables | ARPA/FHSP - 15 Single Adult High Acuity Slots; D7 - 1 Single Adult Low Acuity Slot; D7 - 87 Single Adult High Acuity Slots; D7 - 57 Family High Acuity Slots; D7 - 2 Family High Acuity Vacant Slots |
| Confidence | high |
| Notes | — |

## CRCD - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186915_WO076CRCDMar24__Redacted.pdf`  ·  349.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRCD - Coalition for Responsible Community Development |
| Invoice date | 04/01/2024 |
| Billed amount | $178200.00 |
| Deliverables | ARPA; D7; D7 Flex; MHSA |
| Confidence | high |
| Notes | The deliverables are derived from the 'Fund' categories in the 'BILLING SUMMARY' on page 34, representing the primary service types billed for. Individual slot details are summarized by these funds. |

## Heritage Clinic - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186917_WO087HeritageClinicMar24__Redacted.pdf`  ·  11138.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Heritage Clinic |
| Invoice date | 4/9/2024 |
| Billed amount | $174925.00 |
| Deliverables | ARPA New Slot Cost; ARPA Vacant Slot Cost; ARPA Occupied Slot Cost; D7 New Slot Cost; D7 Vacant Slot Cost; D7 Occupied Slot Cost; PHK (D7) New Slot Cost; PHK (D7) Vacant Slot Cost; PHK (D7) Occupied Slot Cost; MHSA New Slot Cost; MHSA Vacant Slot Cost; MHSA Occupied Slot Cost; SRAP New Slot Cost; SRAP Vacant Slot Cost; SRAP Occupied Slot Cost |
| Confidence | high |
| Notes | Invoice date was extracted from 'DATE SUBMITTED' on page 1, which matches 'DATE INVOICE RECIEVED'. The billed amount is from 'AMOUNT REQUESTED' on page 1, which matches 'TOTAL Cost' in the 'BILLING SUMMARY' on page 37. Deliverables are derived from the 'BILLING SUMMARY' table on page 37, combining the 'Fund' with 'New Slot Cost', 'Vacant Slot Cost', and 'Occupied Slot Cost' categories, as these represent the line-item services being billed. |

## Penny Lane - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186914_WO075PennyLaneMar24__Redacted.pdf`  ·  9196.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Penny Lane |
| Invoice date | 2024-04-04 |
| Billed amount | $115200.00 |
| Deliverables | D7 Slots; D7 Flex Slots; MHSA Slots |
| Confidence | high |
| Notes | The 'billed_amount' is taken from 'AMOUNT REQUESTED' on page 1 and confirmed by 'Total Cost' in the 'BILLING SUMMARY' on page 25. This reflects the total amount billed before any applied disallowed costs or net pay adjustments mentioned in the 'AGENCY COMMENTS' on page 1 or the 'NOTIFICATION OF PAYMENT RECOVERY' on page 26. Deliverables are derived from the categories in the 'BILLING SUMMARY' on page 25, which break down the total billed amount into different types of 'slots' (Vacant and Occupied) under specific funding mechanisms (D7, D7 Flex, MHSA). |

## Exodus Recovery Inc. - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186913_WO070ExodusMar24__Redacted.pdf`  ·  3171.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Exodus |
| Invoice date | 2024-04-01 |
| Billed amount | $276650.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; D7 Flex; DHS; HFMH (D7); PHK (D7); SRAP |
| Confidence | high |
| Notes | The document is a multi-page 'HFH Project Invoice Report'. The 'invoice_date' is taken from the report generation date stated in the footer. The 'billed_amount' is the 'Total Cost' from the 'BILLING SUMMARY' on page 29. The 'deliverables' are the distinct 'Fund' categories listed in the 'BILLING SUMMARY' table. A separate notification regarding disallowed costs was present, but it explicitly states these costs will be recovered from a 'next submitted ICMS invoice' and is not part of the current invoice total. |

## VOALA - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186911_WO036VOALAMar24__Redacted.pdf`  ·  1948.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Volunteers of America |
| Invoice date | 2024-04-02 |
| Billed amount | $106350.00 |
| Deliverables | ARPA/FHSP; D7; DHS; HDAP; HDAP (D7); HDAP (GR); MHSA; PHK (D7) |
| Confidence | high |
| Notes | Invoice date inferred from 'DATE SUBMITTED' and 'DATE INVOICE RECIEVED' fields on page 1. Billed amount derived from 'AMOUNT REQUESTED' on page 1, which matches 'Total Cost' in the 'BILLING SUMMARY' on page 25. 'Net pay' was identified as a post-disallowance amount and not used for total billed. Deliverables are derived from the 'Fund' categories listed in the 'BILLING SUMMARY' on page 25. |

## HW - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186912_WO067HWMar24__Redacted.pdf`  ·  1114.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Housing Works (HW) |
| Invoice date | 2024-04-16 |
| Billed amount | $205050.00 |
| Deliverables | ARPA/FHSP Slots; D7 Slots; DHS Slots; D7 Flex Slots; ARPA Slots; DHSP (D7) Slots; HFMH (D7) Slots; Housing for Healthy CA Slots; MHSA Slots |
| Confidence | high |
| Notes | The billed_amount is taken from 'AMOUNT REQUESTED' on page 1 and confirmed by 'TOTAL Cost' in the 'BILLING SUMMARY' on page 33. The 'net pay' mentioned in agency comments reflects a deduction for disallowed costs, not the original billed amount. Deliverables are summarized by the 'Fund' categories from the 'BILLING SUMMARY' table on page 33, as these represent the distinct service categories with associated total costs. |

## SJC - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186910_WO023SJCMar24__Redacted.pdf`  ·  506.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | St. Joseph's Center |
| Invoice date | 2024-04-04 |
| Billed amount | $422950.00 |
| Deliverables | ARPA; D7; ARPA/FHSP; Housing for Healthy CA; SAM; D7 Flex; DHS; HDAP (D7); HFMH (D7); MHSA; PHK (D7) |
| Confidence | high |
| Notes | — |

## SRO Housing - ICMS - Mar 2024 - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186908_WO021SROHousingMar24__Redacted.pdf`  ·  549.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SRO Housing |
| Invoice date | 2024-04-05 |
| Billed amount | $308625.00 |
| Deliverables | New Slot Costs; Vacant Slot Costs; Occupied Slot Costs |
| Confidence | high |
| Notes | — |

## SSG HOPICS P180 - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186909_WO022SSG.HOPICS.P180Mar24__Redacted.pdf`  ·  1110.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SSG/HOPICS/Project180 |
| Invoice date | 2024-04-05 |
| Billed amount | $299025.00 |
| Deliverables | ARPA slots; ARPA/FHSP slots; D7 slots; DHS slots; SAM slots; D7 Flex slots; DHSP (D7) slots; HDAP slots; HDAP (D7) slots; HFMH (D7) slots; Housing for Healthy CA slots; MHSA slots |
| Confidence | high |
| Notes | — |

## DWC - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186906_WO018DWCMar24__Redacted.pdf`  ·  438.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Downtown Women's Center |
| Invoice date | 2024-04-24 |
| Billed amount | $114150.00 |
| Deliverables | ARPA services; D7 services; DHS services; SAM services; MHSA services |
| Confidence | high |
| Notes | The invoice date is taken from 'DATE SUBMITTED' on page 1, which also matches 'DATE INVOICE RECIEVED'. The billed amount is 'AMOUNT REQUESTED' from page 1, which matches 'TOTAL Cost' in the 'BILLING SUMMARY' on page 17. The deliverables are the line items from the 'BILLING SUMMARY' on page 17, representing services billed under different fund categories. |

## VOALA - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186707_VOALA-ICMS-Jan2024.pdf`  ·  2019.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Volunteers of America |
| Invoice date | 2024-02-06 |
| Billed amount | $105750.00 |
| Deliverables | ARPA/FHSP; D7; DHS; HDAP; HDAP (D7); HDAP (GR); MHSA; PHK (D7) |
| Confidence | high |
| Notes | none |

## LAFH - ICMS - Mar 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186899_WO012LAFHMar24__Redacted.pdf`  ·  3831.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Family Housing (LAFH) |
| Invoice date | 2024-04-04 |
| Billed amount | $420500.00 |
| Deliverables | D7 - New Slot Cost; D7 - Vacant Slot Cost; D7 - Occupied Slot Cost; PHK (D7) - Occupied Slot Cost; SAM - Occupied Slot Cost; D7 Flex - Vacant Slot Cost; D7 Flex - Occupied Slot Cost; DHS - Vacant Slot Cost; DHS - Occupied Slot Cost; MHSA - Occupied Slot Cost |
| Confidence | high |
| Notes | Invoice date inferred from 'DATE SUBMITTED' and 'DATE INVOICE RECIEVED' fields on page 1. Deliverables are extracted from the 'BILLING SUMMARY' table on page 59, combining the 'Fund' and 'Slot Cost' categories as presented. |

## WCA - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186709_WCA-ICMS-Jan2024.pdf`  ·  14425.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Weingart Center Association |
| Invoice date | 2024-02-01 |
| Billed amount | $232800.00 |
| Deliverables | Intensive Case Management Services (ICMS) - New Slots; Intensive Case Management Services (ICMS) - Vacant Slots; Intensive Case Management Services (ICMS) - Occupied Slots |
| Confidence | high |
| Notes | The invoice date was extracted from 'DATE SUBMITTED'. The billed amount was extracted from 'AMOUNT REQUESTED' and verified with the 'Total Cost' in the Billing Summary. Deliverables were identified from the document title 'HFH Project Invoice Report', the mention of 'ICMS' throughout, and the billing categories 'New Slots', 'Vacant Slots', and 'Occupied Slots'. |

## Venice Community Housing - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186705_VeniceCommunityHousing-ICMS-Jan2024.pdf`  ·  720.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Venice Community Housing |
| Invoice date | 2024-02-14 |
| Billed amount | $70275.00 |
| Deliverables | D7 - Vacant Slots; D7 - Occupied Slots; DHS - Vacant Slots; DHS - Occupied Slots; MHSA - Occupied Slots; PHK (D7) - Vacant Slots; PHK (D7) - Occupied Slots |
| Confidence | high |
| Notes | — |

## The People Concern - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186704_ThePeopleConcern-ICMS-Jan2024.pdf`  ·  2475.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The People Concern |
| Invoice date | 2024-02-06 |
| Billed amount | $1309175.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; Housing for Healthy CA; D7 Flex; EWH; HDAP; HDAP (D7); HFMH (D7); MHSA; PHK (D7) |
| Confidence | high |
| Notes | — |

## The Center of Hollywood - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186703_TheCenterofHollywood-ICMS-Jan2024.pdf`  ·  3607.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The Center in Hollywood |
| Invoice date | 2024-02-01 |
| Billed amount | $130050.00 |
| Deliverables | Vacant Slot Cost; Occupied Slot Cost |
| Confidence | high |
| Notes | — |

## STEP UP ON SECOND - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186702_STEPUPONSECOND-ICMS-Jan2024.pdf`  ·  711.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Step Up on Second |
| Invoice date | 2024-02-02 |
| Billed amount | $495675.00 |
| Deliverables | ARPA: $18,900.00; ARPA/FHSP: $2,700.00; D7: $327,525.00; DHS: $26,625.00; SAM: $5,400.00; Housing for Healthy CA: $450.00; D7 Flex: $41,625.00; HFMH (D7): $14,400.00; MHSA: $17,550.00; SRAP: $40,500.00 |
| Confidence | high |
| Notes | — |

## ST Josephs - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186701_STJosephs-ICMS-Jan2024.pdf`  ·  808.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | St. Joseph's Center |
| Invoice date | 2024-02-02 |
| Billed amount | $392250.00 |
| Deliverables | ARPA; D7; ARPA/FHSP; Housing for Healthy CA; SAM; D7 Flex; DHS; HDAP (D7); HFMH (D7); MHSA; PHK (D7) |
| Confidence | high |
| Notes | Vendor and invoice date extracted from Page 1. Billed amount is the 'AMOUNT REQUESTED' from Page 1, which matches the 'Total Cost' in the 'BILLING SUMMARY' on Page 74. Deliverables are the 'Fund' types listed in the 'BILLING SUMMARY' table on Page 74. |

## SSG HOPICS - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186698_SSGHOPICS-ICMS-Jan2024.pdf`  ·  2274.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SSG/HOPICS/Project180 |
| Invoice date | 2024-02-05 |
| Billed amount | $298575.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; D7 Flex; DHSP (D7); HDAP; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | The "billed_amount" is taken from "AMOUNT REQUESTED" on page 1 and confirmed by "Total Cost" in the billing summary on page 65. The document also states an "applied disallowed costs" and a "net pay" after these costs, but the "AMOUNT REQUESTED" represents the total billed prior to these adjustments. The invoice date is taken from "DATE SUBMITTED" on page 1. |

## SRO HOUSING - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186697_SROHOUSING-ICMS-Jan2024.pdf`  ·  791.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SRO Housing |
| Invoice date | 2024-02-06 |
| Billed amount | $299400.00 |
| Deliverables | Housing Services (D7 Fund); Housing Services (D7 Flex Fund); Housing Services (DHS Fund); Housing Services (MHSA Fund) |
| Confidence | high |
| Notes | — |

## SFVCMHC - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186694_SFVCMHC-ICMS-Jan2024.pdf`  ·  630.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | San Fernando Valley Community Mental Health Center (SFVCMHC) |
| Invoice date | 2024-02-13 |
| Billed amount | $93550.00 |
| Deliverables | D7 - New Slot Cost; D7 - Vacant Slot Cost; D7 - Occupied Slot Cost; DCFS/HSSP - Vacant Slot Cost; DCFS/HSSP - Occupied Slot Cost; HFMH (D7) - Vacant Slot Cost; HFMH (D7) - Occupied Slot Cost |
| Confidence | high |
| Notes | The billed_amount is taken from 'AMOUNT REQUESTED' on page 1 and confirmed by 'TOTAL Cost' in the 'BILLING SUMMARY' on page 20. The 'applied disallowed costs' and 'net pay' figures mentioned on page 1 and the notification letter on page 21 refer to a payment recovery to be deducted from a *future* invoice, not a reduction in the billed amount of this specific invoice. Deliverables are extracted from the 'BILLING SUMMARY' table on page 20, listing fund types combined with non-zero slot costs as stated line-items. |

## PATH - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186692_PATH-ICMS-Jan2024.pdf`  ·  2331.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | PATH |
| Invoice date | 2024-02-13 |
| Billed amount | $772725.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; D7 Flex; DHS; SAM; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA; PHK (D7); SRAP |
| Confidence | high |
| Notes | Invoice date was extracted from 'DATE INVOICE RECIEVED' which appeared to be the most relevant date for the overall invoice submission. Total billed amount is consistent across the first page summary and the billing summary table. |

## Penny Lane - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186693_PennyLane-ICMS-Jan2024.pdf`  ·  10145.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Penny Lane |
| Invoice date | 2024-02-05 |
| Billed amount | $118050.00 |
| Deliverables | Fund D7 services; Fund D7 Flex services; Fund MHSA services |
| Confidence | high |
| Notes | — |

## LST&E - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186691_LST_E-ICMS-Jan2024.pdf`  ·  973.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Life Skills Training and Educational Programs |
| Invoice date | 2024-02-08 |
| Billed amount | $144975.00 |
| Deliverables | Intensive Case Management Services (ICMS) - ARPA/FHSP Fund; Intensive Case Management Services (ICMS) - D7 Fund; Intensive Case Management Services (ICMS) - DHS Fund; Intensive Case Management Services (ICMS) - HFMH (D7) Fund; Intensive Case Management Services (ICMS) - MHSA Fund |
| Confidence | high |
| Notes | — |

## LINC - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186690_LINC-ICMS-Jan2024.pdf`  ·  2690.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LINC |
| Invoice date | 2024-02-07 |
| Billed amount | $245700.00 |
| Deliverables | ARPA/FHSP; D7; DHS; D7 Flex; Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | The invoice shows an 'AMOUNT REQUESTED' of $245,700.00 and a 'Total Cost' of $245,700.00 in the billing summary. There is a separate note regarding 'applied disallowed costs $450.00' resulting in 'net pay $245,250.00'. The disallowed costs are explicitly stated as a 'payment recovery' for a previous service month, to be recovered via deduction from the current invoice, therefore the billed amount for this invoice is the original total requested. |

## KYCC - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186688_KYCC-ICMS-Jan2024.pdf`  ·  2294.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Koreatown Youth and Community Center (KYCC) |
| Invoice date | 2024-02-06 |
| Billed amount | $95850.00 |
| Deliverables | D7; D7 Flex; MHSA |
| Confidence | high |
| Notes | Deliverables extracted from 'Fund' categories in the Billing Summary on page 21, as they represent the itemized services/costs contributing to the total billed amount. |

## LAFH - ICMS - Jan 2024.pdf

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186689_LAFH-ICMS-Jan2024.pdf`  ·  4252.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Family Housing (LAFH) |
| Invoice date | 2024-02-07 |
| Billed amount | $361500.00 |
| Deliverables | D7; SAM; D7 Flex; DHS; MHSA |
| Confidence | high |
| Notes | — |

## HW - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186687_HW-ICMS-Jan2024.pdf`  ·  962.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Housing Works |
| Invoice date | 02/15/2024 |
| Billed amount | $204525.00 |
| Deliverables | ARPA/FHSP; D7; DHS; D7 Flex; DHSP (D7); HFMH (D7); Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | The billed_amount is taken from 'AMOUNT REQUESTED' on page 1, which matches 'TOTAL Total Cost' in the Billing Summary on page 33, representing the original amount billed before any disallowed costs were applied. Deliverables are derived from the 'Fund' categories in the 'BILLING SUMMARY' on page 33, as these represent the main service/program categories for which costs are incurred. |

## HHCLA - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186686_HHCLA-ICMS-Jan2024.pdf`  ·  3056.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Homeless Healthcare Los Angeles (HHCLA) |
| Invoice date | 2024-02-12 |
| Billed amount | $196275.00 |
| Deliverables | ARPA/FHSP; D7; SAM; D7 Flex; DHS; MHSA; SRAP |
| Confidence | high |
| Notes | Deliverables are extracted from the 'Fund' categories in the 'BILLING SUMMARY' table on page 43, which represent the different types of projects/services contributing to the total cost. |

## Heritage Clinic - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186685_HeritageClinic-ICMS-Jan2024.pdf`  ·  477.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Heritage Clinic |
| Invoice date | 2024-02-15 |
| Billed amount | $152925.00 |
| Deliverables | ARPA; D7; PHK (D7); MHSA; SRAP |
| Confidence | high |
| Notes | The billed_amount is taken from 'AMOUNT REQUESTED' on page 1 and corroborated by 'Total Cost' in the 'BILLING SUMMARY' on page 32. The document mentions 'applied disallowed costs' and 'net pay', but the request is for the 'total billed' which is the amount before these deductions. Deliverables are identified as the 'Fund' categories listed in the 'BILLING SUMMARY' on page 32. |

## Exodus - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186684_Exodus-ICMS-Jan2024.pdf`  ·  747.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Exodus |
| Invoice date | 2024-02-14 |
| Billed amount | $245700.00 |
| Deliverables | ARPA slots; ARPA/FHSP slots; D7 slots; D7 Flex slots; DHS slots; HFMH (D7) slots; PHK (D7) slots |
| Confidence | high |
| Notes | The billed_amount is taken from 'AMOUNT REQUESTED' on page 1, which matches the 'TOTAL Cost' in the 'BILLING SUMMARY' on page 48. The document also mentions 'applied disallowed costs $450.00' and a 'net pay $245,250.00' on page 1, and a 'NOTIFICATION OF PAYMENT RECOVERY DUE TO DISALLOWED COSTS' on page 49; however, the prompt asks for the total billed amount, which is the requested amount before any recovery/deduction. Deliverables are identified from the distinct fund categories listed in the 'BILLING SUMMARY' table on page 48, representing the various types of slots for which costs are itemized. |

## DWC - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186683_DWC-ICMS-Jan2024.pdf`  ·  523.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Downtown Women's Center |
| Invoice date | 2024-02-07 |
| Billed amount | $120150.00 |
| Deliverables | ARPA - Occupied Slot Cost; D7 - Vacant Slot Cost; D7 - Occupied Slot Cost; DHS - Occupied Slot Cost; SAM - Occupied Slot Cost; MHSA - Occupied Slot Cost |
| Confidence | high |
| Notes | The invoice_date is extracted from 'DATE SUBMITTED' on page 1. The billed_amount is from 'AMOUNT REQUESTED' on page 1 and confirmed by 'TOTAL Cost' on the Billing Summary (page 27). Deliverables are extracted from the 'BILLING SUMMARY' table on page 27, specifically the cost categories that have non-zero amounts. |

## CRCD - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186682_CRCD-ICMS-Jan2024.pdf`  ·  1313.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRCD - Coalition for Responsible Community Development |
| Invoice date | 2024-02-02 |
| Billed amount | $180700.00 |
| Deliverables | ARPA New Slot Cost; ARPA Vacant Slot Cost; ARPA Occupied Slot Cost; D7 New Slot Cost; D7 Vacant Slot Cost; D7 Occupied Slot Cost; D7 Flex New Slot Cost; D7 Flex Vacant Slot Cost; D7 Flex Occupied Slot Cost; MHSA New Slot Cost; MHSA Vacant Slot Cost; MHSA Occupied Slot Cost |
| Confidence | high |
| Notes | — |

## Community of friends - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186680_Communityoffriends-ICMS-Jan2024.pdf`  ·  846.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | A Community of Friends |
| Invoice date | 2/13/2024 |
| Billed amount | $167475.00 |
| Deliverables | Integrated Case Management Services (D7); Integrated Case Management Services (D7 Flex); Integrated Case Management Services (MHSA) |
| Confidence | high |
| Notes | The invoice date is taken from 'DATE SUBMITTED'. The billed amount is from 'AMOUNT REQUESTED' and confirmed by the 'TOTAL Cost' in the billing summary. Deliverables are derived from the 'Fund' categories in the 'BILLING SUMMARY' section, representing different types of Integrated Case Management Services as mentioned in the disallowance notice. |

## American Family Housing - ICMS - Jan 2024

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1186679_AmericanFamilyHousing-ICMS-Jan2024.pdf`  ·  167.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | American Family Housing |
| Invoice date | 2024-02-02 |
| Billed amount | $82425.00 |
| Deliverables | ARPA/FHSP New Slot Cost; ARPA/FHSP Vacant Slot Cost; ARPA/FHSP Occupied Slot Cost; D7 New Slot Cost; D7 Vacant Slot Cost; D7 Occupied Slot Cost |
| Confidence | high |
| Notes | Invoice date taken from 'DATE SUBMITTED'. Deliverables are extracted from the 'BILLING SUMMARY' section on the last page, representing the categories of costs that sum up to the total billed amount. |

## Volunteers of America - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162179_VolunteersofAmerica-Dec.2023.pdf`  ·  2145.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Volunteers of America |
| Invoice date | 2024-01-05 |
| Billed amount | $105750.00 |
| Deliverables | ARPA/FHSP; D7; DHS; HDAP; HDAP (D7); HDAP (GR); MHSA; PHK (D7) |
| Confidence | high |
| Notes | — |

## SSG HOPICS Project180 - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162176_SSGHOPICSProject180-Dec.2023.pdf`  ·  883.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SSG/HOPICS/Project180 |
| Invoice date | 2024-01-10 |
| Billed amount | $299100.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; D7 Flex; DHSP (D7); HDAP; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | The billed_amount is taken from 'AMOUNT REQUESTED' on page 1, which aligns with the 'Total Cost' in the Billing Summary on page 64. This is the total billed before the application of disallowed costs of $18,900.00, which result in a 'net pay' of $280,200.00 as noted on page 1 and explained on page 65. The invoice date is taken from 'DATE INVOICE RECIEVED'. |

## SRO Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162174_SROHousing-Dec.2023.pdf`  ·  832.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SRO Housing |
| Invoice date | 2024-01-04 |
| Billed amount | $301800.00 |
| Deliverables | D7 Fund Slots for Housing and Integrated Case Management Services; D7 Flex Fund Slots for Housing and Integrated Case Management Services; DHS Fund Slots for Housing and Integrated Case Management Services; MHSA Fund Slots for Housing and Integrated Case Management Services |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE SUBMITTED'. Billed amount confirmed by 'AMOUNT REQUESTED' on page 1 and 'TOTAL Cost' in the billing summary on page 70. Deliverables are identified from the 'BILLING SUMMARY' section on page 70, categorized by fund type (D7, D7 Flex, DHS, MHSA) which represent the billing units ('slots') for Housing for Health and Integrated Case Management Services (ICMS) as referenced in the document (pages 1 and 71). |

## Weingart Center Association - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162170_WeingartCenterAssociation-Dec.2023.pdf`  ·  2628.4 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Weingart Center Association |
| Invoice date | 1/2/2024 |
| Billed amount | $101925.00 |
| Deliverables | D7 Slots; D7 Flex Slots; DHS Slots |
| Confidence | high |
| Notes | Invoice date extracted as printed as it is not in ISO format. The deliverables are derived from the 'BILLING SUMMARY' on page 25, which categorizes costs by 'Fund' type (D7, D7 Flex, DHS) and includes both 'Vacant Slot Cost' and 'Occupied Slot Cost' under these categories. The 'STAFFING' section (pages 2-10) provides details but does not present a separate billed amount for 'staffing' as a distinct deliverable; rather, staffing supports the 'slots'. |

## Life Skills Training and Educational Programs - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162113_LifeSkillsTrainingandEducationalPrograms-Dec.2023.pdf`  ·  583.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Life Skills Training and Educational Programs |
| Invoice date | 2024-01-11 |
| Billed amount | $144975.00 |
| Deliverables | ARPA/FHSP; D7; DHS; HFMH (D7); MHSA |
| Confidence | high |
| Notes | — |

## LINC - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162110_LINC-Dec.2023.pdf`  ·  425.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LINC |
| Invoice date | 2024-01-05 |
| Billed amount | $245775.00 |
| Deliverables | ARPA/FHSP; D7; DHS; D7 Flex; Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | Invoice date '1/5/24' was converted to ISO YYYY-MM-DD format. Deliverables are derived from the 'Fund' categories in the 'BILLING SUMMARY' on page 29, which represent the major service programs billed. |

## Homeless Healthcare Los Angeles (HHCLA) - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162106_HomelessHealthcareLosAngeles_HHCLA_-Dec.2023.pdf`  ·  1144.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Homeless Healthcare Los Angeles (HHCLA) |
| Invoice date | 2024-01-11 |
| Billed amount | $196500.00 |
| Deliverables | ARPA/FHSP; D7; SAM; D7 Flex; DHS; MHSA; SRAP |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE SUBMITTED'. Billed amount extracted from 'AMOUNT REQUESTED'. Deliverables are based on the 'Fund' categories in the 'BILLING SUMMARY' section on the last page, as these represent the high-level services being billed. |

## The Center in Hollywood - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162147_TheCenterinHollywood-Dec.2023.pdf`  ·  9715.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The Center in Hollywood |
| Invoice date | 2024-01-04 |
| Billed amount | $130050.00 |
| Deliverables | D7 Vacant Slot Cost; DHS Vacant Slot Cost; SAM Vacant Slot Cost; D7 Occupied Slot Cost; DHS Occupied Slot Cost; SAM Occupied Slot Cost |
| Confidence | high |
| Notes | The invoice date is derived from the 'DATE SUBMITTED' on page 1, which represents the submission date of this Project Invoice Report. The 'CLAIM PERIOD' for this report is 12/2023. 'New Slot Cost' line item was excluded from deliverables as its value was $0.00 across all funds in the billing summary. |

## Venice Community Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162096_VeniceCommunityHousing-Dec.2023.pdf`  ·  189.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Venice Community Housing |
| Invoice date | 2024-01-05 |
| Billed amount | $70275.00 |
| Deliverables | D7; DHS; MHSA; PHK (D7) |
| Confidence | high |
| Notes | — |

## Koreatown Youth and Community Center (KYCC) - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162100_KoreatownYouthandCommunityCenter_KYCC_-Dec.2023.pdf`  ·  5613.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Koreatown Youth and Community Center (KYCC) |
| Invoice date | 1/9/24 |
| Billed amount | $100050.00 |
| Deliverables | D7 - New Slot Cost; D7 - Vacant Slot Cost; D7 - Occupied Slot Cost; D7 Flex - Occupied Slot Cost; MHSA - Occupied Slot Cost |
| Confidence | high |
| Notes | — |

## Penny Lane - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162088_PennyLane-Dec.2023.pdf`  ·  22944.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | — |
| Invoice date | — |
| Billed amount | — |
| Deliverables | — |
| Confidence | low |
| Notes | PDF exceeds inline limit; use Gemini File API |

## Housing Works (HW) - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1161941_HousingWorks_HW_-Dec.2023.pdf`  ·  941.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Housing Works (HW) |
| Invoice date | 01/16/2024 |
| Billed amount | $202425.00 |
| Deliverables | ARPA/FHSP; D7; DHS; D7 Flex; DHSP (D7); HFMH (D7); Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | Billed amount is the 'AMOUNT REQUESTED' from page 1, which matches the 'Total Cost' in the 'BILLING SUMMARY' on page 33. This is the total amount before accounting for applied disallowed costs. Deliverables are derived from the 'Fund' categories in the 'BILLING SUMMARY' table on page 33, as these are the most granular breakdown of billed services provided within the document. |

## CRCD - Coalition for Responsible Community Development - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162032_CRCD-CoalitionforResponsibleCommunityDevelopment-Dec.2023.pdf`  ·  1883.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | CRCD - Coalition for Responsible Community Development |
| Invoice date | 01/04/2024 |
| Billed amount | $166500.00 |
| Deliverables | Staffing; Invalid Slots; New Slots; Reserved Slots; Vacant Slots; Occupied Slots |
| Confidence | high |
| Notes | The billed amount is derived from 'AMOUNT REQUESTED' on page 1 and confirmed by the 'TOTAL Total Cost' in the 'BILLING SUMMARY' on page 30. The invoice date is 'DATE SUBMITTED' on page 1, which aligns with the report run date. Deliverables are identified from the major sections of the 'HFH Project Invoice Report' (pages 2-29) which categorize the services being billed. |

## San Fernando Valley Community Mental Health - Dec. 2023.pdf

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1159832_SanFernandoValleyCommunityMentalHealth-Dec.2023.pdf`  ·  608.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | San Fernando Valley Community Mental Health Center (SFVCMHC) |
| Invoice date | 2024-01-25 |
| Billed amount | $42525.00 |
| Deliverables | D7; DCFS/HSSP; HFMH (D7) |
| Confidence | high |
| Notes | — |

## PATH Dec. 2023.pdf

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1160006_PATH-Dec.2023.pdf`  ·  1243.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | PATH |
| Invoice date | 2024-01-10 |
| Billed amount | $760050.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; D7 Flex; DHS; SAM; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA; PHK (D7); SRAP |
| Confidence | high |
| Notes | Invoice date extracted from 'DATE SUBMITTED' on page 1. Billed amount extracted from 'AMOUNT REQUESTED' on page 1, which matches the 'Total Cost' in the 'BILLING SUMMARY' on page 133. Deliverables are listed as the 'Fund' categories from the 'BILLING SUMMARY' table on page 133, which represent the line-item services/programs being billed. |

## American Family Housing - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1159822_AmericanFamilyHousing-Dec.2023.pdf`  ·  210.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | American Family Housing |
| Invoice date | 2024-01-03 |
| Billed amount | $80175.00 |
| Deliverables | ARPA/FHSP Vacant Slot Cost; D7 Vacant Slot Cost; D7 Occupied Slot Cost |
| Confidence | high |
| Notes | — |

## Step Up on Second - Dec. 2023.pdf

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1159829_StepUponSecond-Dec.2023.pdf`  ·  1186.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Step Up on Second |
| Invoice date | 2024-01-08 |
| Billed amount | $494475.00 |
| Deliverables | SUOS (HFMH); SUOS 2nd Street (D7 Flex); SUOS 5th Street (D7 Flex); SUOS EHV (ARPA/EHV); SUOS HUD VASH CCM HACLA (D7); SUOS HUD VASH CCM LACDA (D7); SUOS Scattered 2 (D7); SUOS Scattered 3 (ARPA); SUOS Scattered 4 (SRAP); SUOS Scattered 5 (ARPA/FHSP); SUOS Step Up On 3rd (D7); SUOS Step Up On 3rd DMH (D7); SUOS Step Up On Broadway (D7); SUOS Stepping Up LA County TBRA (D7); SUOS Stepping Up Pasadena TBRA (D7); SUOS Tammy (D7 Flex); SUOS Daniel's Village (MHSA); SUOS DMH HACLA TBSH (D7); SUOS EHV (D7); SUOS Scattered 1 (D7); SUOS Step Up on Colorado (DHS); SUOS Step Up On Vine (MHSA) |
| Confidence | high |
| Notes | Vendor name, invoice date, and billed amount are explicitly stated on page 1. The billed amount is taken from 'AMOUNT REQUESTED: $494,475.00' on page 1, which matches the 'TOTAL' 'Total Cost' on page 90. Disallowed costs mentioned on page 1 and in the attached letters (pages 91, 93) are noted as deductions from payment/recoveries, not affecting the 'total billed' amount requested. Deliverables are identified as the unique 'Project' names listed under 'VACANT SLOTS' (pages 46-48) and 'OCCUPIED SLOTS' (pages 49-89), as these represent the line-item services with associated costs before being summarized by Fund on page 90. |

## A Community of Friends - Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1159819_ACommunityofFriends-Dec.2023.pdf`  ·  358.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | A Community of Friends |
| Invoice date | 2024-01-11 |
| Billed amount | $167100.00 |
| Deliverables | New Slots; Vacant Slots; Occupied Slots |
| Confidence | high |
| Notes | — |

## Exodus - Dec. 2023.pdf

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1159816_Exodus-Dec.2023.pdf`  ·  562.3 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Exodus |
| Invoice date | 2024-01-03 |
| Billed amount | $245250.00 |
| Deliverables | Staffing; Exodus Culver City (PHK); Exodus EHV (ARPA/EHV); Exodus EHV (D7); Exodus New Carver (D7 Flex); Exodus New Carver (D7); Exodus Produce Apartments (D7 Flex); Exodus Scattered 1 (D7); Exodus Scattered 2 (D7); Exodus Scattered 3 DMH (D7); Exodus Scattered 4 (ARPA/FHSP); Exodus SPA 6 (HFMH); Exodus SPA 8 (HFMH); Exodus Hope on Broadway (ARPA/FHSP); Exodus New Carver (DHS); Exodus Produce Apartments (D7); Exodus SPA 4 (HFMH); Exodus Studio 6 (PHK); Applied disallowed costs |
| Confidence | high |
| Notes | — |

## St. Joseph's Center - Dec. 2023.pdf

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1159813_St.Joseph_sCenter-Dec.2023.pdf`  ·  823.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | St. Joseph's Center |
| Invoice date | 2024-01-11 |
| Billed amount | $391950.00 |
| Deliverables | ARPA; D7; ARPA/FHSP; Housing for Healthy CA; SAM; D7 Flex; DHS; HDAP (D7); HFMH (D7); MHSA; PHK (D7) |
| Confidence | high |
| Notes | The invoice date was taken from 'DATE SUBMITTED'. 'Amount Requested' was used for the billed amount, as it represents the total billed before any disallowed costs. |

## Downtown Women's Center - Dec. 2023.pdf

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1159810_DowntownWomen_sCenter-Dec.2023.pdf`  ·  691.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Downtown Women's Center |
| Invoice date | 2024-01-10 |
| Billed amount | $121800.00 |
| Deliverables | Vacant Slot Cost; Occupied Slot Cost |
| Confidence | high |
| Notes | — |

## SFV Community Mental Health Dec. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1159267_122023WO141.pdf`  ·  793.7 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | San Fernando Valley Community Mental Health Center (SFVCMHC) |
| Invoice date | 2024-01-25 |
| Billed amount | $42525.00 |
| Deliverables | Vacant Slots - SFVCMHC (HFMH); Vacant Slots - SFVCMHC EHV (D7); Vacant Slots - SFVCMHC FUP TAY FYI (DCFS/HSSP); Vacant Slots - SFVCMHC Scattered 1 (D7); Vacant Slots - SFVCMHC Welcome Home (D7); Occupied Slots - SFVCMHC (HFMH); Occupied Slots - SFVCMHC DMH (HFMH); Occupied Slots - SFVCMHC EHV (D7); Occupied Slots - SFVCMHC FUP TAY FYI (DCFS/HSSP); Occupied Slots - SFVCMHC Welcome Home (D7) |
| Confidence | high |
| Notes | The billed_amount is the 'AMOUNT REQUESTED' ($42,525.00) as stated on page 1 and confirmed by the 'BILLING SUMMARY' total on page 14, before any 'disallowed costs' ($8,925.00) are applied. The invoice_date is the 'DATE SUBMITTED' on page 1. |

## LA Family Housing (LAFH) - Dec. 2023.pdf

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1159806_LAFamilyHousing_LAFH_-Dec.2023.pdf`  ·  760.8 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | LA Family Housing (LAFH) |
| Invoice date | 2023-01-16 |
| Billed amount | $361500.00 |
| Deliverables | Vacant Slot Cost; Occupied Slot Cost |
| Confidence | medium |
| Notes | The stated 'DATE SUBMITTED' and 'DATE' for authorized signature on page 1 is '01/16/23', which is inconsistent with the 'CLAIM PERIOD: 12 / 2023' and 'DATE INVOICE RECIEVED: 1/18/2024'. The billed amount reflects the 'AMOUNT REQUESTED' (gross amount) as stated on page 1 and confirmed in the 'BILLING SUMMARY' on page 49, prior to the 'applied disallowed costs' mentioned on page 1. |

## PATH Nov.2023.pdf

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1160007_PATH-Nov.2023.pdf`  ·  711.2 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | PATH |
| Invoice date | 2023-12-07 |
| Billed amount | $717975.00 |
| Deliverables | Intensive Case Management Services (ICMS); ARPA Slot Costs; ARPA/FHSP Slot Costs; D7 Slot Costs; D7 Flex Slot Costs; DHS Slot Costs; SAM Slot Costs; HDAP (D7) Slot Costs; HFMH (D7) Slot Costs; Housing for Healthy CA Slot Costs; MHSA Slot Costs; PHK (D7) Slot Costs |
| Confidence | high |
| Notes | — |

## Volunteers of America - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162178_VolunteersofAmerica-Nov.2023.pdf`  ·  2176.6 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Volunteers of America |
| Invoice date | 2023-12-06 |
| Billed amount | $105750.00 |
| Deliverables | ARPA/FHSP; D7; DHS; HDAP; HDAP (D7); HDAP (GR); MHSA; PHK (D7) |
| Confidence | high |
| Notes | — |

## SSG HOPICS Project180 - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162175_SSGHOPICSProject180-Nov.2023.pdf`  ·  2558.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SSG/HOPICS/Project180 |
| Invoice date | 12/07/2023 |
| Billed amount | $298050.00 |
| Deliverables | ARPA; ARPA/FHSP; D7; DHS; SAM; D7 Flex; DHSP (D7); HDAP; HDAP (D7); HFMH (D7); Housing for Healthy CA; MHSA |
| Confidence | high |
| Notes | — |

## SRO Housing - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162173_SROHousing-Nov.2023.pdf`  ·  843.5 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | SRO Housing |
| Invoice date | 2023-12-07 |
| Billed amount | $303150.00 |
| Deliverables | D7; D7 Flex; DHS; MHSA |
| Confidence | high |
| Notes | The invoice date is taken from 'DATE SUBMITTED'. The billed amount is taken from 'AMOUNT REQUESTED' on page 1 and confirmed by 'TOTAL Cost' in the 'BILLING SUMMARY' on page 71. The document also mentions 'applied disallowed costs $10,800.00' and 'net pay $292,350.00', but the total billed is $303,150.00. Deliverables are extracted from the 'Fund' categories in the 'BILLING SUMMARY' table on page 71, representing the categories of services billed. |

## Weingart Center Association - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162169_WeingartCenterAssociation-Nov.2023.pdf`  ·  3339.1 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Weingart Center Association |
| Invoice date | 2023-12-04 |
| Billed amount | $138600.00 |
| Deliverables | D7 Vacant Slot Cost; D7 Occupied Slot Cost; D7 Flex Vacant Slot Cost; D7 Flex Occupied Slot Cost; DHS Vacant Slot Cost; DHS Occupied Slot Cost |
| Confidence | high |
| Notes | Invoice date converted to ISO YYYY-MM-DD from 'December 4, 2023'. Deliverables are extracted from the 'BILLING SUMMARY' section on page 31, combining fund types with 'Vacant Slot Cost' and 'Occupied Slot Cost' as line items. |

## Life Skills Training and Educational Programs - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162112_LifeSkillsTrainingandEducationalPrograms-Nov.2023.pdf`  ·  546.0 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | Life Skills Training and Educational Programs |
| Invoice date | 2023-12-07 |
| Billed amount | $144825.00 |
| Deliverables | ARPA/FHSP; D7; DHS; HFMH (D7); MHSA |
| Confidence | high |
| Notes | The invoice date was chosen as 'DATE SUBMITTED' (12/7/23) as it represents the submission date of this invoice report. Deliverables were extracted from the 'BILLING SUMMARY' on page 34, specifically the 'Fund' categories, as these represent the primary service groupings detailed in the report. |

## The Center in Hollywood - Nov. 2023

**Source:** `https://file.lacounty.gov/SDSInter/ceo/asp/1162145_TheCenterinHollywood-Nov.2023.pdf`  ·  9295.9 KB scanned PDF

| Field | Extracted value |
|-------|-----------------|
| Vendor | The Center in Hollywood |
| Invoice date | 2023-12-05 |
| Billed amount | $130350.00 |
| Deliverables | New Slot Cost; Vacant Slot Cost; Occupied Slot Cost |
| Confidence | high |
| Notes | — |
