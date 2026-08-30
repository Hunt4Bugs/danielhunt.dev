---
id: ops
kind: domain
domain: ops
status: active
version: 1
class: "00"
collection: governance
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - README.md
  - 010_governance/LIBRARY_MAP.md
  - 010_governance/METADATA.md
  - concepts.md
  - workflows/README.md
  - ../_conventions/documentation.md
  - ../_patterns/domain.md
sources:
  - 010_governance/DOMAIN_PROTOCOL.md
  - 020_agents/WORKFLOWS.md
  - 030_operations/TRACKER.md
  - 030_operations/TRIAGE.md
  - 020_agents/TEMPLATES.md
---

# Domain: `ops`

## Purpose

`ops` is this repository's own project-operations domain: how work on this repository is
tracked, triaged, guided, and recorded. It exists as its own domain — rather than folding into
`content`, `site`, or `delivery` — because it governs the *process* of operating on this
repository (what an agent may do, how incoming work is classified, how decisions get evidenced),
not the substance of any one deliverable. Brand, site, and delivery domains describe what this
repository *produces*; `ops` describes how the repository *runs itself*.

## Scope

### Includes

- Agent guidance documents in `020_agents/` (`AGENTS.md`, `AUTONOMY.md`, `PLUGIN_POLICY.md`,
  `TEMPLATES.md`, `VALIDATION.md`, `WORKFLOWS.md`) — the Agent Guidance Doc concept.
- The internal planning tracker, `030_operations/TRACKER.md` — the Tracker Item concept.
- The triage policy, `030_operations/TRIAGE.md` — the Triage Item concept.
- Dated historical records in `090_records/` — the Record concept.
- `010_governance/LIBRARY_MAP.md` and `010_governance/METADATA.md`, insofar as they route and
  govern this domain's own physical placement and metadata standard.

### Excludes

- **`010_governance/DOMAIN_PROTOCOL.md` itself.** The protocol specification is cross-cutting
  infrastructure that `010_governance/` happens to host, not an instance of an `ops` concept. It
  is classified `kind: protocol`, `domain: protocol` — its own domain, not this one. `ops` is a
  *consumer* of the protocol (it models itself using the protocol's meta-model), not the
  protocol's home.
- The root `docs/_conventions/` and `docs/_patterns/` meta-infrastructure. These apply across
  every domain in the repository; they are not `ops`-owned content even though `ops` (like every
  other domain) must conform to them.
- Brand, site, and delivery substantive content (`10_brand/`, `20_site/`, `30_delivery/`) — each
  is its own domain or class, out of scope here even where an `ops` record references it.

## Model

- **Tracker Item** — one row of incoming or in-progress work in `TRACKER.md`, carrying an ID,
  description, state, and evidence.
- **Triage Item** — one routing rule that classifies incoming work into a lane with a required
  response, per `TRIAGE.md`.
- **Record** — one dated, evidence-based document (decision, audit, setup, or note) capturing
  what was found, decided, or learned, per the `TEMPLATES.md` shape.
- **Agent Guidance Doc** — one of the nested `020_agents/` documents that governs what an agent
  may do and how.

Full field-level specification lives in [`concepts.md`](concepts.md).

## Relationships

- `Triage Item` **classifies** `Tracker Item` — incoming work is captured in the tracker as
  `draft` first, then a Triage Item's lane and required response are applied to it.
- `Record` **evidences** `Tracker Item` — a Record's Evidence and Decision sections are what
  justify moving a Tracker Item's state forward (e.g. `draft` → `active`).
- `Agent Guidance Doc` **governs** `Tracker Item`, `Triage Item`, `Record` — `WORKFLOWS.md`,
  `VALIDATION.md`, `AUTONOMY.md`, `PLUGIN_POLICY.md`, and `TEMPLATES.md` define how an agent may
  create or update instances of the other three concepts.

## Constraints

- A Tracker Item's `state` must use the shared document-status vocabulary from
  [`_conventions/documentation.md`](../_conventions/documentation.md) (`draft`, `active`,
  `blocked`, `superseded`, `archived`); `ops` does not define a competing status vocabulary.
- Incoming work must be captured in `TRACKER.md` as `draft` before it is classified by a Triage
  Item — triage does not classify work that has no tracker entry.
- Any subject matching an escalation trigger (secrets, security concerns, public publication,
  data loss, financial/legal exposure, a decision that changes brand strategy) must be escalated
  immediately rather than routed through a normal lane, per `TRIAGE.md`.
- A Record's `type` must be one of `decision`, `audit`, `setup`, `note`; it must carry the seven
  template body sections (`Evidence`, `Interpretation`, `Assumptions`, `Decision or
  recommendation`, `Risks and open questions`, `Next actions`, `Learning update`) unless a
  section is genuinely inapplicable, per `TEMPLATES.md`.
- A Record is historical evidence once created: correct it with a new dated Record rather than
  rewriting the original (see `090_records/2026-07-28-project-os-bootstrap.md`, which stays
  untouched even as later records supersede parts of it).
- Exactly one canonical Agent Guidance Doc exists per guidance type (`AGENTS.md`, `AUTONOMY.md`,
  `PLUGIN_POLICY.md`, `TEMPLATES.md`, `VALIDATION.md`, `WORKFLOWS.md`) — guidance is consolidated,
  not forked.
- Changes within `ops` are local and reversible; external writes, deployments, publication,
  approvals, and destructive actions require explicit user authorization, per `AUTONOMY.md`.

## Related Domains

- **`protocol`** — `ops` conforms to `DOMAIN_PROTOCOL.md` and the root `_conventions/` /
  `_patterns/` it defines; `protocol` does not depend on `ops`.
- **`content`** (`docs/40_content/`) — the first domain fully modeled under this protocol; briefly
  a root-level domain, now its own numbered class. `ops.workflow.create-domain` is the general
  procedure that produced `content`'s scaffold in spirit and is the general procedure behind every
  domain's scaffold since.
- **`identity`, `strategy`, `audience`, `marketing`, `offers`, `assets`, `channels`,
  `relationships`, `analytics`** (`docs/10_brand/*/`), **`site`** (`docs/20_site/`), and
  **`delivery`** (`docs/30_delivery/`) — modeled as protocol domains nested inside their numbered
  class, each with a `domain.md` and `concepts.md` per §8.1. `relationships` is `status: draft`
  and intentionally carries no Concepts yet; `ops` may record decisions about any of these domains
  (as Records) without owning their content.

## Examples

- `OPS-001` (Tracker Item, `active`): "Project OS baseline" — evidenced by
  `090_records/2026-07-28-project-os-bootstrap.md` (Record, `type: setup`), which documents the
  decisions that created class `00` and its four collections.
- `OPS-002` (Tracker Item, `draft`): "README accuracy" — an example of a Tracker Item still
  awaiting a Record that resolves it; per `TRIAGE.md`'s Governance lane, resolving it requires
  updating class `00` after evidence review.
