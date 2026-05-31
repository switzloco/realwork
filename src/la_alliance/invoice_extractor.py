"""
LA Alliance "PDF Black Hole" Parser — unstructured invoice → normalized ledger.

The problem this solves
-----------------------
LA County publishes the "LA Alliance Documents" dataset: raw, scanned,
inconsistently-formatted invoices from homeless-service providers tied to a
large county settlement. State and county auditors can't query it — the
billing detail is locked inside scanned PDFs that no CSV export reaches. A
human has to open each one and read it. That's the black hole.

What this pipeline does
-----------------------
1. DISCOVER  — list the document URLs (Socrata catalog, a manifest file, or a
               local directory of already-downloaded PDFs).
2. FETCH     — pull each PDF's raw bytes through Bright Data's Web Unlocker
               (routes around the portal's anti-bot; binary-safe via
               BrightDataClient.fetch_bytes).
3. EXTRACT   — hand the raw PDF directly to Gemini 2.5 Flash, which reads
               scanned pages natively (vision) and returns structured fields:
               vendor, invoice date, billed amount, stated deliverables.
4. NORMALIZE — validate into an InvoiceRecord (pydantic), coerce the dollar
               amount, keep a confidence + notes trail.
5. REPORT    — write a clean JSON ledger plus a before/after markdown that
               shows the unreadable source next to the structured output.

Why Gemini for extraction: google-generativeai is already a project dep and
Gemini ingests PDFs (including scanned images) inline — no poppler/OCR stack.
An AI/ML API (GPT-4o vision) path is provided as a structurally-different
second extractor for the ensemble/cross-model story.

Budget: Bright Data spend is gated by BrightDataClient's cap + JSONL ledger.

Run examples
------------
    # against a local folder of sample PDFs Antigravity already pulled
    python -m src.la_alliance.invoice_extractor --pdf-dir data/la_alliance/raw --limit 50

    # against a manifest (JSON list of {"title","url"}) fetched via Bright Data
    python -m src.la_alliance.invoice_extractor --manifest data/la_alliance/manifest.json --limit 50

    # discover straight off the county Socrata catalog (confirm dataset id first)
    python -m src.la_alliance.invoice_extractor --dataset <socrata-resource-url> --limit 50

Output:
    data/la_alliance/ledger.json          normalized records
    data/la_alliance/before_after.md      demo-ready before/after
"""

from __future__ import annotations

import argparse
import json
import os
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

import requests
from pydantic import BaseModel, Field, field_validator

from src.bright_data.client import BrightDataClient, BudgetExceeded

OUT_DIR = Path("data/la_alliance")
OUT_DIR.mkdir(parents=True, exist_ok=True)

GEMINI_MODEL = os.environ.get("GEMINI_EXTRACT_MODEL", "gemini-2.5-flash")
AIMLAPI_URL = "https://api.aimlapi.com/v1/chat/completions"

# Inline-data ceiling for Gemini; larger files should go via the File API.
MAX_INLINE_BYTES = 18 * 1024 * 1024

EXTRACTION_PROMPT = """You are an audit data-extraction assistant. The attached
file is a single invoice or billing document from a homeless-service provider
submitted to Los Angeles County. It may be a scanned image, faxed, or poorly
formatted.

Extract ONLY what is stated on the document. Do not infer, guess, or fill in
values that are not present. If a field is missing or unreadable, return null
for it and say so in extraction_notes.

Return a single JSON object, no prose, with exactly these keys:
{
  "vendor": string|null,            // the billing organization / provider name
  "invoice_date": string|null,      // ISO YYYY-MM-DD if determinable, else as printed
  "billed_amount": number|null,     // total billed, numeric only (no $ or commas)
  "deliverables": [string],         // line-item services/deliverables as stated
  "confidence": "high"|"medium"|"low",
  "extraction_notes": string        // what was unclear, ambiguous, or missing
}
Do not wrap the JSON in markdown fences."""


# --------------------------------------------------------------------------- #
# Normalized record
# --------------------------------------------------------------------------- #

class InvoiceRecord(BaseModel):
    source_title: str = ""
    source_url: str = ""
    vendor: Optional[str] = None
    invoice_date: Optional[str] = None
    billed_amount: Optional[float] = None
    deliverables: list[str] = Field(default_factory=list)
    confidence: str = "low"
    extraction_notes: str = ""
    extractor: str = GEMINI_MODEL

    @field_validator("billed_amount", mode="before")
    @classmethod
    def _coerce_amount(cls, v):
        if v is None or v == "":
            return None
        if isinstance(v, (int, float)):
            return float(v)
        cleaned = re.sub(r"[^0-9.\-]", "", str(v))
        try:
            return float(cleaned) if cleaned else None
        except ValueError:
            return None


def _strip_json(text: str) -> dict:
    """Pull a JSON object out of an LLM reply, tolerating ``` fences / stray prose."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.MULTILINE).strip()
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON object in model reply: {text[:200]}")
    return json.loads(text[start:end + 1])


# --------------------------------------------------------------------------- #
# 1. DISCOVER
# --------------------------------------------------------------------------- #

_URL_FIELDS = ["url", "document_url", "file_url", "attachment", "link", "href"]
_TITLE_FIELDS = ["title", "name", "document_name", "description", "label"]


def _pick(row: dict, candidates: list[str]) -> str:
    for c in candidates:
        v = row.get(c)
        if isinstance(v, dict):  # Socrata 'url' columns nest under {"url": ...}
            v = v.get("url")
        if v:
            return str(v)
    return ""


def discover_documents(dataset_url: str = "", manifest: str = "",
                       pdf_dir: str = "", limit: int = 50) -> list[dict]:
    """Return a list of {title, url|path} document references."""
    if pdf_dir:
        files = sorted(Path(pdf_dir).glob("*.pdf"))[:limit]
        return [{"title": f.stem, "path": str(f)} for f in files]

    if manifest:
        rows = json.loads(Path(manifest).read_text())
        out = []
        for row in rows:
            url = row.get("sds_published_url") or row.get("url")
            title = row.get("sds_title") or row.get("title")
            if url:
                out.append({"title": title, "url": url})
        return out[:limit]

    if dataset_url:
        r = requests.get(dataset_url, params={"$limit": limit}, timeout=60)
        r.raise_for_status()
        out = []
        for row in r.json():
            url = _pick(row, _URL_FIELDS)
            if url:
                out.append({"title": _pick(row, _TITLE_FIELDS) or url, "url": url})
        return out[:limit]

    raise SystemExit("Provide one of --pdf-dir, --manifest, or --dataset")


# --------------------------------------------------------------------------- #
# 2. FETCH
# --------------------------------------------------------------------------- #

def fetch_pdf(doc: dict, client: Optional[BrightDataClient]) -> Optional[bytes]:
    """Local path → read; remote URL → Bright Data (binary-safe) fetch."""
    if doc.get("path"):
        return Path(doc["path"]).read_bytes()

    url = doc.get("url")
    if not url:
        return None
    if client is None or "lacounty.gov" in url:
        # no Bright Data creds or it's a known permissive host — try a plain GET
        try:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=60)
            return r.content if r.ok else None
        except Exception:
            return None

    resp = client.fetch_bytes(url)
    if resp.get("status") != 200:
        print(f"fetch fail {resp.get('status')}")
    return resp.get("content") if resp.get("status") == 200 else None


# --------------------------------------------------------------------------- #
# 3. EXTRACT
# --------------------------------------------------------------------------- #

def extract_with_gemini(pdf_bytes: bytes, model: str = GEMINI_MODEL) -> dict:
    """Hand the raw PDF to Gemini and return the parsed JSON dict."""
    if len(pdf_bytes) > MAX_INLINE_BYTES:
        return {"extraction_notes": "PDF exceeds inline limit; use Gemini File API",
                "confidence": "low"}
    try:
        import google.generativeai as genai
    except ImportError:
        return {"extraction_notes": "google-generativeai not installed",
                "confidence": "low"}

    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        return {"extraction_notes": "GEMINI_API_KEY not set", "confidence": "low"}

    genai.configure(api_key=key)
    gm = genai.GenerativeModel(model)
    resp = gm.generate_content([
        EXTRACTION_PROMPT,
        {"mime_type": "application/pdf", "data": pdf_bytes},
    ], request_options={"timeout": 120})
    return _strip_json(resp.text)


def extract_with_aimlapi(image_b64: str, model: str = "gpt-4o") -> dict:
    """Structurally-different second extractor (vision) via AI/ML API.

    image_b64 is a base64 PNG/JPEG data payload of a rendered page. Provided
    for the cross-model ensemble story; Gemini is the default path because it
    accepts PDFs directly without a render step.
    """
    key = os.environ.get("AIMLAPI_KEY", "")
    if not key:
        return {"extraction_notes": "AIMLAPI_KEY not set", "confidence": "low"}
    r = requests.post(
        AIMLAPI_URL,
        headers={"Authorization": f"Bearer {key}"},
        json={
            "model": model,
            "messages": [{
                "role": "user",
                "content": [
                    {"type": "text", "text": EXTRACTION_PROMPT},
                    {"type": "image_url",
                     "image_url": {"url": f"data:image/png;base64,{image_b64}"}},
                ],
            }],
            "temperature": 0,
        },
        timeout=90,
    )
    r.raise_for_status()
    return _strip_json(r.json()["choices"][0]["message"]["content"])


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #

def run(dataset_url: str = "", manifest: str = "", pdf_dir: str = "",
        limit: int = 50, budget: float = 25.0, model: str = GEMINI_MODEL) -> dict:
    docs = discover_documents(dataset_url, manifest, pdf_dir, limit)
    print(f"=== LA Alliance PDF Black Hole Parser ===")
    print(f"{len(docs)} document(s) to process | extractor: {model}\n")

    # Bright Data client only needed for remote fetches
    client = None
    if not pdf_dir:
        try:
            client = BrightDataClient(budget_cap=budget, label="la_alliance")
        except RuntimeError as e:
            print(f"  (no Bright Data client: {e}; will try direct GETs)")

    records: list[InvoiceRecord] = []
    before_after: list[dict] = []
    ok, failed = 0, 0
    budget_stop = False

    ledger_path = OUT_DIR / "ledger.json"
    existing_titles = set()
    if ledger_path.exists():
        try:
            existing_data = json.loads(ledger_path.read_text())
            for row in existing_data:
                existing_titles.add(row.get("source_title"))
                # Also restore them to the current run so we don't lose them on save
                records.append(InvoiceRecord(**row))
                ok += 1
        except Exception as e:
            print(f"Failed to load existing ledger: {e}")

    def process_doc(i, doc):
        title = doc.get("title", f"doc_{i}")
        if title in existing_titles:
            return i, title, None, None, "skipped_cached"

        try:
            pdf = fetch_pdf(doc, client)
        except BudgetExceeded as e:
            return i, title, None, None, f"Budget stop: {e}"
        if not pdf:
            return i, title, None, None, "fetch failed"
        try:
            raw = extract_with_gemini(pdf, model)
        except Exception as e:
            return i, title, None, None, f"extract error: {e}"
        
        rec = InvoiceRecord(
            source_title=title,
            source_url=doc.get("url", doc.get("path", "")),
            extractor=model,
            **{k: raw.get(k) for k in
               ("vendor", "invoice_date", "billed_amount",
                "deliverables", "confidence", "extraction_notes")
               if raw.get(k) is not None},
        )
        return i, title, rec, pdf, None

    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(process_doc, i, doc): doc for i, doc in enumerate(docs, 1)}
        for future in as_completed(futures):
            try:
                i, title, rec, pdf, err = future.result(timeout=120)
            except Exception as e:
                print(f"  [Task Timeout or Error] — {e}")
                failed += 1
                continue

            if err:
                if err == "skipped_cached":
                    pass # Silently skip
                elif "Budget stop" in err:
                    print(f"\n! {err}")
                    budget_stop = True
                else:
                    print(f"  [{i}] {title[:50]} — {err}")
                    failed += 1
                continue
            
            records.append(rec)
            before_after.append({
                "title": title,
                "source": rec.source_url,
                "size_kb": round(len(pdf) / 1024, 1),
                "structured": rec.model_dump(),
            })
            amt = f"${rec.billed_amount:,.2f}" if rec.billed_amount else "?"
            print(f"  [{i}] {title[:45]:45} -> {rec.vendor or '?'} | {amt} | {rec.confidence}")
            ok += 1

            # Intermittent save for live updates
            if ok % 20 == 0:
                ledger_path = OUT_DIR / "ledger.json"
                ledger_path.write_text(json.dumps([r.model_dump() for r in records], indent=2))
                _write_before_after(before_after)

    # write outputs
    # Sort records back into original order by sorting by source_title (or just letting them be unordered)
    records.sort(key=lambda r: r.source_title)
    before_after.sort(key=lambda d: d["title"])
    
    ledger_path = OUT_DIR / "ledger.json"
    ledger_path.write_text(json.dumps([r.model_dump() for r in records], indent=2))
    _write_before_after(before_after)

    if client:
        print(f"\n{client.report()}")
    print(f"Done. extracted={ok} failed={failed}")
    print(f"Ledger        -> {ledger_path}")
    print(f"Before/after  -> {OUT_DIR / 'before_after.md'}")
    return {"extracted": ok, "failed": failed, "ledger": str(ledger_path)}


def _write_before_after(items: list[dict]):
    lines = ["# LA Alliance Invoices — Before / After\n",
             "Left: an unstructured scanned invoice the county published as a PDF.",
             "Right: the normalized ledger row our agent extracted autonomously.\n"]
    for it in items:
        s = it["structured"]
        deliv = "; ".join(s.get("deliverables") or []) or "—"
        lines += [
            f"## {it['title']}\n",
            f"**Source:** `{it['source']}`  ·  {it['size_kb']} KB scanned PDF\n",
            "| Field | Extracted value |",
            "|-------|-----------------|",
            f"| Vendor | {s.get('vendor') or '—'} |",
            f"| Invoice date | {s.get('invoice_date') or '—'} |",
            f"| Billed amount | {('$%0.2f' % s['billed_amount']) if s.get('billed_amount') else '—'} |",
            f"| Deliverables | {deliv} |",
            f"| Confidence | {s.get('confidence')} |",
            f"| Notes | {s.get('extraction_notes') or '—'} |\n",
        ]
    (OUT_DIR / "before_after.md").write_text("\n".join(lines))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    src = ap.add_argument_group("source (pick one)")
    src.add_argument("--dataset", default="", help="Socrata resource URL")
    src.add_argument("--manifest", default="", help="JSON list of {title,url}")
    src.add_argument("--pdf-dir", default="", help="local dir of *.pdf files")
    ap.add_argument("--limit", type=int, default=50)
    ap.add_argument("--budget", type=float, default=25.0,
                    help="Bright Data spend cap in $ for this run")
    ap.add_argument("--model", default=GEMINI_MODEL, help="Gemini extractor model")
    args = ap.parse_args()
    run(dataset_url=args.dataset, manifest=args.manifest, pdf_dir=args.pdf_dir,
        limit=args.limit, budget=args.budget, model=args.model)
