# 135/137 Union Avenue — Plan Retrieval Packet

**Goal:** Obtain copies of the original 1983 building plans for 135 Union Avenue
(architect Michael Moyer / Union Avenue Associates) and any alteration plans for
**137 Union Ave Unit E, Campbell, CA 95008** — specifically to determine whether
a post in Unit E is structural (load-bearing).

**City index handle we already have:** `Union 135`, microfiche filename **11512**
(Campbell Planning microfiche system). We viewed the digitized scan at the city
but were not given copies.

**Status notes:**
- HOA asked — they do **not** have a copy.
- This is a condominium (common-interest development), so under H&S Code §19851
  the HOA board *or* the owner can supply the owner-side permission; the city
  must still seek the architect's permission via certified letter.

---

## 1. Email to Campbell Building / Planning (records + duplication)

> **To:** building@campbellca.gov; planning@campbellca.gov
> **Subject:** Plan duplication request — 137 Union Ave Unit E (microfiche "Union 135" / file 11512)
>
> Hello,
>
> I am the owner of **137 Union Avenue, Unit E, Campbell, CA 95008** (part of the
> 135 Union Avenue condominium development, built 1983, architect Michael Moyer /
> Union Avenue Associates). I am requesting **copies** of:
>
> 1. The original 1983 building/architectural plans for the development — your
>    microfiche index lists these under **"Union 135," filename 11512**;
> 2. Any building permits and associated plan sets for **alterations to Unit E**
>    (any year);
> 3. The recorded **condominium plan** for the development if held in your files.
>
> I understand that under **Health & Safety Code §19851** the city may duplicate
> plans with (a) the written permission of the licensed professional who signed
> them — or their successor — and (b) the permission of the current owner, or for
> a common-interest development, the HOA board. As the **current owner of Unit E**,
> I am providing my permission, and I can supply HOA board authorization for the
> common structure. Please send me your **plan-duplication affidavit / indemnity
> form**, and please initiate the §19851 **certified-letter request to the
> architect of record (Michael Moyer)** so duplication can proceed; that
> permission "shall not be unreasonably withheld" under the statute.
>
> Purpose: I need to confirm whether a specific post in my unit is load-bearing
> before any work, and to support a future building permit.
>
> Proof of ownership (grant deed / tax bill) attached. Happy to pay copy fees.
> Thank you,
> Nicholas Switzer — [phone]

**Campbell contacts:** Planning (408) 866-2140 · planning@campbellca.gov ·
Building Division page: https://campbellca.gov/1458/Building-Division ·
Forms: https://www.campbellca.gov/1135/Building-Handouts-and-Forms

---

## 2. Direct note to the architect (parallel path, speeds §19851)

The architect of record is almost certainly **Michael D. Moyer**. Two practices,
very likely the same person across time:
- **Michael D. Moyer Associates Architects** — formerly 430 Sherman Ave, Palo
  Alto (now closed). Right era/region for the 1983 stamp.
- **Michael Moyer Architecture** — Mill Valley (5 Manor Ter / 239 Miller Ave),
  operating since 1976. Likely his current/successor practice.

> Dear Mr. Moyer,
>
> I own Unit E at 137 Union Avenue, Campbell — part of the 135 Union Avenue
> condominiums you designed (Union Avenue Associates, ~1983). The City of Campbell
> holds your plans on microfiche ("Union 135," file 11512) but under H&S Code
> §19851 needs your written permission to release copies to me. Would you provide
> a brief signed authorization (or reply to the city's forthcoming certified
> letter)? I only need to confirm structural framing for a small interior project.
> If you still have the drawing set, I'd gladly pay for a copy directly. Thank you.

---

## 3. Records that may answer the post question *without* the microfiche

- **Recorded Condominium Plan** (SCC Clerk-Recorder) — public; often delineates
  unit boundaries and bearing walls. Search by address/APN:
  https://clerkrecorder.santaclaracounty.gov/services/search-assessor-property-address
- **Assessor parcel record** (APN, year built, building sketch):
  https://www.sccassessor.org/index.php/online-services/property-search/real-property
- **Prior Unit E remodel permits** — a past permit's plan set may already mark
  the post.
- **Definitive answer:** a licensed structural engineer can confirm load-bearing
  status on a site visit (≈$300–600) and you'll need their stamp for a permit
  anyway. The plans are corroboration, not a prerequisite, for that question.

---

## 4. Automated sweep (run locally where the Bright Data key lives)

```
python -m src.property.union_ave_hunt --budget 15          # full SERP + unlock
python -m src.property.union_ave_hunt --budget 15 --resume # continue a run
python -m src.property.union_ave_hunt --no-unlock          # discovery only
```

Outputs ranked leads to `data/property/union_ave_findings.json` and saves any
retrieved PDFs/pages to `data/property/`. The Web Unlocker is needed because
CAB, the Assessor, and the city site all return **403** to plain fetchers.
