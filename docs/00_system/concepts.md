---
id: ops.concepts
kind: concept-registry
domain: ops
status: active
version: 1
class: "00"
collection: governance
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - domain.md
  - workflows/README.md
  - 030_operations/TRACKER.md
  - 030_operations/TRIAGE.md
  - 020_agents/TEMPLATES.md
  - 020_agents/AGENTS.md
  - ../_patterns/concept.md
sources:
  - 030_operations/TRACKER.md
  - 030_operations/TRIAGE.md
  - 020_agents/TEMPLATES.md
  - 020_agents/AGENTS.md
  - 020_agents/AUTONOMY.md
  - 020_agents/WORKFLOWS.md
  - 020_agents/VALIDATION.md
  - 020_agents/PLUGIN_POLICY.md
---

# Concepts

Canonical concept registry for the `ops` domain (see [`domain.md`](domain.md)). Every Concept
`ops` models gets one entry here.

## Tracker Item
**ID:** `ops.tracker-item`

One row of incoming or in-progress internal work, tracked in `030_operations/TRACKER.md`. Not an
external issue — an internal planning record.

### Relationships
- classified by `ops.triage-item`
- evidenced by `ops.record`

### Constraints
- `id` must be a stable, unique, never-reused label (e.g. `OPS-001`); once assigned it is never
  renumbered even if the item is later superseded.
- `state` must use the shared document-status vocabulary owned by
  [`_conventions/documentation.md`](../_conventions/documentation.md) — `ops` does not define its
  own status values.
- A new item enters the tracker at `state: draft` before it is classified by a Triage Item.

### Entity contract
```yaml
entity: ops.tracker-item
fields:
  - name: id
    type: text
    required: true
    cardinality: 1
  - name: item
    type: text
    required: true
    cardinality: 1
  - name: state
    type: taxonomy(Document Status)
    required: true
    cardinality: 1
  - name: evidence_next_action
    type: text
    required: true
    cardinality: 1
```

## Triage Item
**ID:** `ops.triage-item`

One routing rule from `030_operations/TRIAGE.md` that classifies a category of incoming work into
a lane with a required response. `TRIAGE.md` persists these as a table of lanes rather than as
individual dated instances; a Tracker Item's classification is recorded inline (in its `Evidence /
next action` cell) rather than as a separate document — see §14 of `DOMAIN_PROTOCOL.md` on
domain-defined persistence.

### Relationships
- classifies `ops.tracker-item`
- governed by `ops.agent-guidance-doc` (`TRIAGE.md` itself)

### Constraints
- `lane` must be one of the four canonical lanes (Brand foundation, Site implementation,
  Delivery, Governance) — a governed vocabulary owned by `TRIAGE.md`; adding a lane is a
  governance change to that file, not a silent extension.
- Any subject matching an escalation trigger (secrets, security concerns, public publication,
  data loss, financial/legal exposure, a brand-strategy-changing decision) must escalate
  immediately instead of being routed through a normal lane.

### Entity contract
```yaml
entity: ops.triage-item
fields:
  - name: lane
    type: taxonomy(Triage Lane)
    required: true
    cardinality: 1
  - name: criteria
    type: text
    required: true
    cardinality: 1
  - name: required_response
    type: text
    required: true
    cardinality: 1
  - name: escalation_trigger
    type: taxonomy(Escalation Trigger)
    required: false
    cardinality: 0..*
```

## Record
**ID:** `ops.record`

One dated, evidence-based document — a decision, audit, setup, or note — capturing what was
found, decided, or learned about the repository, per `020_agents/TEMPLATES.md`'s record template.
Records live in `090_records/` and are never rewritten after the fact; a correction is a new
dated Record.

### Relationships
- evidences `ops.tracker-item`
- governed by `ops.agent-guidance-doc` (`TEMPLATES.md`, `VALIDATION.md`)

### Constraints
- `type` must be one of `decision`, `audit`, `setup`, `note`.
- Must contain the required body sections (`Evidence`, `Interpretation`, `Assumptions`, `Decision
  or recommendation`, `Risks and open questions`, `Next actions`, `Learning update`) unless a
  section is genuinely inapplicable, per `TEMPLATES.md`.
- `created` and `updated` use ISO-8601 dates; `created` is set once and never changed.
- Each Record must distinguish verified evidence from interpretation, assumptions,
  recommendations, and decisions (per `METADATA.md`'s superseded standard, carried forward by
  `_conventions/documentation.md`), and use repository-relative links for `related` and `sources`.
- A Record is historical evidence: once created it is left untouched even when later work
  supersedes part of it (see `090_records/2026-07-28-project-os-bootstrap.md`).

### Entity contract
```yaml
entity: ops.record
fields:
  - name: type
    type: taxonomy(Record Type)
    required: true
    cardinality: 1
  - name: status
    type: taxonomy(Document Status)
    required: true
    cardinality: 1
  - name: owner
    type: text
    required: true
    cardinality: 1
  - name: created
    type: date
    required: true
    cardinality: 1
  - name: updated
    type: date
    required: true
    cardinality: 1
  - name: facets
    type: text
    required: false
    cardinality: 0..*
  - name: related
    type: url
    required: false
    cardinality: 0..*
  - name: sources
    type: url
    required: false
    cardinality: 0..*
```

## Agent Guidance Doc
**ID:** `ops.agent-guidance-doc`

One of the nested `020_agents/` documents (`AGENTS.md`, `AUTONOMY.md`, `PLUGIN_POLICY.md`,
`TEMPLATES.md`, `VALIDATION.md`, `WORKFLOWS.md`) that governs what an agent may do in this
repository and how. The pattern is the nested-guidance-set itself: one short, focused document per
guidance type, all resolved through `AGENTS.md` as the entry point.

### Relationships
- governs `ops.tracker-item`, `ops.triage-item`, `ops.record`

### Constraints
- Exactly one canonical document exists per `doc_type` — guidance is consolidated in one place,
  never forked across files.
- A guidance change is itself a local, reversible documentation edit; it may not authorize
  publishing, deploying, altering GitHub settings or secrets, installing plugins, changing global
  configuration, or making external commitments (see `AUTONOMY.md`, `PLUGIN_POLICY.md`).

### Entity contract
```yaml
entity: ops.agent-guidance-doc
fields:
  - name: doc_type
    type: taxonomy(Agent Guidance Doc Type)
    required: true
    cardinality: 1
  - name: status
    type: taxonomy(Document Status)
    required: true
    cardinality: 1
  - name: owner
    type: text
    required: true
    cardinality: 1
  - name: updated
    type: date
    required: true
    cardinality: 1
```

## Owned vocabularies

`ops` owns these controlled vocabularies (§13.3 — extend only by governed edit to the owning
file, never silently from a workflow or skill):

- **Triage Lane** (`030_operations/TRIAGE.md`): Brand foundation, Site implementation, Delivery,
  Governance.
- **Escalation Trigger** (`030_operations/TRIAGE.md`): secrets, security concerns, public
  publication, data loss, financial/legal exposure, brand-strategy decision.
- **Record Type** (`020_agents/TEMPLATES.md`): decision, audit, setup, note.
- **Agent Guidance Doc Type** (this file): agents-guide (`AGENTS.md`), autonomy-policy
  (`AUTONOMY.md`), plugin-policy (`PLUGIN_POLICY.md`), template-guide (`TEMPLATES.md`),
  validation-guide (`VALIDATION.md`), workflow-guide (`WORKFLOWS.md`).

`ops` references but does not own **Document Status** (`draft`, `active`, `blocked`,
`superseded`, `archived`), which is owned by
[`_conventions/documentation.md`](../_conventions/documentation.md) and shared across every
domain.
