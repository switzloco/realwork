# Risk Analyst — Detection Capabilities

The risk analyst is a Gemini 2.5 Pro agent with Google Search grounding that
reads each normalized invoice from `ledger.json` and reasons about it against
public context: contracted rates, federal/state coverage rules, and provider
corporate history. It does **not** make legal determinations. Every output is a
*candidate for investigation* — an anomaly a human auditor should look at — not
an accusation.

> **Language discipline (project rule):** findings are framed as "anomaly,"
> "discrepancy," or "warrants investigation." Never as "fraud." The tool builds
> the audit queue; humans and counsel decide what it means.

## Why grounding matters

Most "anomaly detection" hallucinates a baseline. This agent looks the baseline
up. Before flagging an amount as high, it searches for the actual contracted
rate in public MOU documents. Before flagging a billing code, it searches for
what that code means in the relevant program. The flag is only as strong as the
public source behind it, and the source is cited.

## Anomaly classes the agent surfaces

These are the *categories* of pattern the system is built to catch. Examples
are illustrative and generic — real entity-level findings are never published
here (see "What we deliberately do not publish" below).

### 1. Regulatory-exclusion conflict
A billed service category is cross-referenced against the coverage rules of the
program that ultimately funds it. When a line item appears to bill for a service
type that a federal or state rule excludes from coverage, the agent flags the
conflict and cites the controlling rule. This is the highest-value class because
it connects a single local line item to a codified statute — something a CSV
scan can never do.

### 2. Resource double-counting
The agent checks whether the *same underlying resource* (e.g., a single staff
hour at a single site) appears to be billed under two different unit categories
in the same period. Charging one resource twice under different labels has no
administrative justification, so this pattern is a strong candidate for review.

### 3. Temporal anomaly ("payment before service")
Invoice dates and service windows are compared against payment dates. A payment
that lands *before* the service window it covers is a control-failure signal in
municipal accounting — public funds generally cannot prepay a per-unit rate
before the units are delivered. The agent flags the timeline inversion.

### 4. Entity-existence / address anomalies
Provider names are searched for an independent public footprint. A vendor billing
large amounts with no verifiable business presence, or billing from an
unverified residential address, is flagged for identity verification.

## Output

Per invoice: decoded deliverables, any contracted rate found (with source), a
list of flags with severity and reasoning, and the grounding sources used.
Resumable via a checkpoint; rate-limited to respect grounding quota.

## What we deliberately do not publish

Entity-level risk assessments — anything that names a specific provider next to
an asserted violation — are **never committed to this repository.** They are
written to a gitignored private directory by design.

Two reasons:

1. **Defamation.** Naming a real organization alongside an asserted violation,
   based on automated inference that has not been verified against primary
   service records, is a legal exposure we don't take on.
2. **Whistleblower protection.** Under the federal and California False Claims
   Acts, a qui tam claim's value depends on filing *under seal before public
   disclosure*. Publishing a specific allegation forfeits that position. If a
   real finding surfaces, the correct path is a qui tam attorney (contingency),
   not a public post. We do not contact the entity, the funding agency, or the
   press.

The published dataset (`ledger.json`) is restructured **public record** — the
county already published these invoices. Turning unqueryable PDFs into a clean,
queryable ledger is the contribution. The interpretation that points at a named
party stays private until counsel decides otherwise.
