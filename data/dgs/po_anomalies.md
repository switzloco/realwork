# DGS Purchase Order Anomalies

- Records analyzed: 50,000
- Total value: $30,152,656,435

## Buyer-Vendor Concentration (>=75% of buyer's spend)

| Buyer | Vendor | POs | Total | Share |
|-------|--------|-----|-------|-------|
| High Speed Rail Authority, Cal | California Department of Trans | 3 | $228,419,658 | 94% |
| Conservation, Department of | California Department of Conse | 14 | $6,683,993 | 85% |

## Just-Under-Threshold Clusters (split-contract pattern)

| Vendor | Threshold | Count | Example amounts |
|--------|-----------|-------|-----------------|
| McKesson Medical - Surgical Minneso | $4,999 | 7 | $4,943, $4,957, $4,949 |
| Panini Time | $49,999 | 7 | $49,950, $49,950, $49,950 |
| Prison Industry Authority | $4,999 | 6 | $4,999, $4,961, $4,905 |
| Airgas USA LLC | $4,999 | 4 | $4,999, $4,999, $4,999 |
| California Veteran Supply Inc. | $4,999 | 4 | $4,917, $4,907, $4,997 |
| Sharp Electronics Corporation | $4,999 | 4 | $4,984, $4,932, $4,932 |
| Bay Medical Co., Inc | $4,999 | 4 | $4,988, $4,931, $4,966 |
| Fastenal | $4,999 | 3 | $4,941, $4,953, $4,965 |
| Progressive Medical, Inc. | $4,999 | 3 | $4,999, $4,999, $4,999 |
| Falcon Fuels Inc | $4,999 | 3 | $4,919, $4,975, $4,963 |
| Taborda Solutions | $4,999 | 3 | $4,929, $4,963, $4,912 |
| River City Office Supply | $4,999 | 3 | $4,989, $4,970, $4,995 |
| National Office Solutions | $4,999 | 3 | $4,959, $4,947, $4,996 |
| San Joaquin Distributors, Inc. | $4,999 | 3 | $4,928, $4,999, $4,973 |
| Unknown | $4,999 | 3 | $4,999, $4,999, $4,900 |
| Adolph Inc. | $9,999 | 3 | $9,995, $9,975, $9,920 |
| Battery Systems | $4,999 | 2 | $4,997, $4,997 |
| DirectGov Source | $4,999 | 2 | $4,989, $4,920 |
| Department of Justice | $4,999 | 2 | $4,907, $4,967 |
| Adolph Inc. | $4,999 | 2 | $4,960, $4,948 |
| Celle Brite USA, Corp. | $4,999 | 2 | $4,998, $4,998 |
| PROVISTA SOFTWARE INTL INC | $4,999 | 2 | $4,922, $4,922 |
| Life Technologies Corp | $4,999 | 2 | $4,995, $4,995 |
| PACIFIC INDUSTRIAL | $4,999 | 2 | $4,945, $4,937 |
| Pinnacle Petroleum | $4,999 | 2 | $4,968, $4,900 |
| Siemens Healthcare Diagnostics | $4,999 | 2 | $4,927, $4,913 |
| Sacramento Technology Group | $4,999 | 2 | $4,999, $4,999 |
| PC Specialist Inc dba TIG (Technolo | $4,999 | 2 | $4,966, $4,937 |
| Food Service Systems Inc | $4,999 | 2 | $4,961, $4,990 |
| Glacier Laboratories, Inc | $4,999 | 2 | $4,980, $4,930 |

## Repeating Exact-Amount POs (round-tripping pattern)

| Vendor | Amount | Count | Total |
|--------|--------|-------|-------|
| Telecare Corporation | $4,883,437 | 3 | $14,650,311 |
| CONFIDENTIAL - Information Withheld | $50,000 | 65 | $3,250,000 |
| Global Environmental Products, Inc | $939,200 | 3 | $2,817,600 |
| CONFIDENTIAL - Information Withheld | $75,000 | 34 | $2,550,000 |
| EXPRESS Office Products, Inc. | $500,000 | 5 | $2,500,000 |
| JLS ENVIRONMENTAL SERVICES, INC | $500,000 | 5 | $2,500,000 |
| Northpointe Inc. | $821,250 | 3 | $2,463,750 |
| CONFIDENTIAL - Information Withheld | $40,000 | 36 | $1,440,000 |
| CONFIDENTIAL - Information Withheld | $30,000 | 39 | $1,170,000 |
| US FOODSERVICE | $390,000 | 3 | $1,170,000 |
| CONFIDENTIAL - Information Withheld | $25,000 | 45 | $1,125,000 |
| CONFIDENTIAL - Information Withheld | $60,000 | 17 | $1,020,000 |
| United Rentals (North America), Inc | $305,719 | 3 | $917,157 |
| CONFIDENTIAL - Information Withheld | $100,000 | 9 | $900,000 |
| ICL Performance Products | $81,273 | 10 | $812,729 |
| US FOODSERVICE | $200,000 | 4 | $800,000 |
| CONFIDENTIAL - Information Withheld | $150,000 | 5 | $750,000 |
| CONFIDENTIAL - Information Withheld | $35,000 | 19 | $665,000 |
| ICL Performance Products LP | $162,317 | 4 | $649,266 |
| CONFIDENTIAL - Information Withheld | $20,000 | 31 | $620,000 |
| Stepp Manufacturing Co., Inc. | $171,349 | 3 | $514,048 |
| CONFIDENTIAL - Information Withheld | $15,000 | 33 | $495,000 |
| CONFIDENTIAL - Information Withheld | $45,000 | 11 | $495,000 |
| Newton Construction & Management, I | $116,000 | 4 | $464,000 |
| ICL Performance Products LP | $81,158 | 5 | $405,791 |
| US FOODSERVICE | $45,000 | 9 | $405,000 |
| US FOODSERVICE | $100,000 | 4 | $400,000 |
| CONFIDENTIAL - Information Withheld | $10,000 | 34 | $340,000 |
| California State University, Sacram | $100,000 | 3 | $300,000 |
| Pinnacle Petroleum | $100,000 | 3 | $300,000 |

## Vague High-Value POs (no real deliverable)

| Vendor | Buyer | Amount | Description |
|--------|-------|--------|-------------|
| County of Contra Costa | State Hospitals, Departme | $83,824,316 | County Mental Health Specialty Services |
| CENTRAL CALIFORNIA TECHNO | Employment Development De | $40,500,000 | IT technogy support services |
| Monterey County Health De | State Hospitals, Departme | $31,208,974 | Specialty Mental Health Services |
| AMERICAN CORRECTIONAL PAR | Correctional Health Care  | $29,516,987 | Temporary/Relief Psychiatry Services |
| Neelam Sachdev, MD PC | Correctional Health Care  | $27,549,188 | Temporary/Relief Psychiatry Services |
| glenn vega, md inc | Correctional Health Care  | $23,613,590 | Temporary/Relief Psychiatry Services |
| ABM Industries | California Technology Age | $21,780,625 | engineering services |
| Community Hospital of San | State Hospitals, Departme | $20,000,000 | Acute hospital care and related services for PSH p |
| COUNTY OF HUMBOLDT | State Hospitals, Departme | $19,771,129 | County Mental Health Plan specialty services. |
| Lead Staffing Corporation | Mental Health, Department | $16,864,056 | Temp/Relief Psychologist Services |
| BAY AREA DOCTORS INC. | Correctional Health Care  | $15,742,393 | Temporary/Relief Psychiatry Services |
| COUNTY OF MARIN | State Hospitals, Departme | $13,215,983 | Specialty Mental Health Services |
| COUNTY OF MERCED | State Hospitals, Departme | $12,819,547 | Mental Health Specialty Services |
| CALTROP Corporation | Transportation, Departmen | $11,700,000 | Structural materials inspection services |
| Fugro Consultants, Inc. | Transportation, Departmen | $9,800,000 | Pavement Structure Data Collection and Inventory S |
| Strumwasser & Woocher LLP | Insurance, Department of | $9,541,474 | Legal Services. |
| Pinnacle Health Services, | Correctional Health Care  | $7,871,197 | Temporary/Relief Psychiatry Services |
| County of Riverside | Aging, Department of | $7,663,782 | Area Plan Services |
| Madera County Behavioral  | State Hospitals, Departme | $7,052,983 | Specialty Mental Health Services |
| County of San Diego | Public Health, Department | $6,794,632 | Provide Immunization Services to the General Publi |
| COUNCIL ON AGING SILICON  | Aging, Department of | $6,730,063 | Area Plan Services |
| Visionary Integration Pro | Health Care Services, Dep | $6,451,200 | Project Management SErvices |
| County of Riverside | Public Health, Department | $6,322,887 | Local Assistance for HIV/AIDS Services |
| County of Lake | State Hospitals, Departme | $6,288,495 | Specialty Mental Health Services |
| FFF ENTERPRISES INC | Public Health, Department | $6,054,229 | Various Influenza Vaccines:Flumist, Fluvirin and F |
| Registry of Physician Spe | Correctional Health Care  | $5,903,398 | Temporary/Relief Psychiatry Services |
| County of Alameda | Aging, Department of | $5,754,422 | Title III, VII Services |
| ATHALYE CONSULTING ENGINE | Transportation, Departmen | $5,450,000 | Construction Inspection Services in District 4 |
| Clean Seas | Fish and Wildlife, Depart | $5,000,000 | Orphan oil spill response services. |
| Community Regional Hospit | State Hospitals, Departme | $5,000,000 | Hospital Services |