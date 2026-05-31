# LA Alliance Invoices — Before / After

Left: an unstructured scanned invoice the county published as a PDF.
Right: the normalized ledger row our agent extracted autonomously.

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
