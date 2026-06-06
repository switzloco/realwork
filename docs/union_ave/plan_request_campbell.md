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

Polite, specific, and pre-loaded so the clerk can act in one pass: we name the
exact microfiche frame (file 11512), state the legal basis, and attach the
owner paperwork up front so nobody has to ask for it.

> **To:** building@campbellca.gov; planning@campbellca.gov
> **Subject:** Owner request to copy one microfiche frame — file 11512 (137 Union Ave Unit E, APN 412-14-028)
>
> Hello, and thank you in advance for your help.
>
> I'm the owner of **137 Union Avenue, Unit E, Campbell, CA 95008**
> (**APN 412-14-028**, Tract 7304, Bldg 4), and I'm trying to make this as quick
> as possible on your end. I viewed our building's plans on your digitized
> microfiche at the counter — they're indexed as **"Union 135," file 11512**. I'd
> like a copy of **that specific frame** (the Plan B / Building 4 floor and
> structural sheets), plus, if it's easy to pull at the same time, **any permit
> on record for alterations to Unit E**.
>
> I know that under **Health & Safety Code §19851** plans can be copied with the
> owner's permission and the design professional's (or for a common-interest
> development, the HOA board's). To save a round-trip, I've attached:
>
> - my **grant deed** (Doc #22684526) as proof I'm the current owner,
> - a signed **owner authorization / indemnity** for the copy, and
> - **HOA board authorization** for the common structure.
>
> If your policy is to release to the owner on the indemnity affidavit, I believe
> that covers it — please just let me know your copy fee and how you'd like
> payment. If you also need the architect's permission, I'm happy to have you send
> the §19851 certified letter to the architect of record (Michael Moyer), and I'll
> chase his sign-off in parallel so it doesn't hold you up; the statute notes that
> permission "shall not be unreasonably withheld."
>
> Purpose is simple: my structural engineer needs to confirm whether one interior
> post is load-bearing before a small project, and for the eventual permit.
>
> Truly appreciate it — happy to come to the counter if that's easier for you.
> Thank you,
> Nicholas Switzer — [phone]

*Attach before sending:* grant deed (#22684526), the city's signed affidavit/
indemnity form (request it first if you don't have the blank), and a one-line
HOA board authorization. Leading with all three is what turns this from a
multi-week back-and-forth into a single reply.

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
