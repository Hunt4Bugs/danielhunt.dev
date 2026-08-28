---
id: ops.workflow.maintain-record
kind: workflow
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
  - ../domain.md
  - ../concepts.md
  - ../020_agents/WORKFLOWS.md
  - ../020_agents/TEMPLATES.md
  - ../020_agents/VALIDATION.md
  - ../030_operations/TRACKER.md
  - ../030_operations/TRIAGE.md
sources:
  - ../020_agents/WORKFLOWS.md
contract:
  subject_type: ops.tracker-item
  entry_stage: Orient
  exit_stage: Verify
  requires:
    - id: ops.tracker-item
      state: draft
      optional: true
  inputs:
    - name: subject
      type: text
      required: true
    - name: primary_class
      type: taxonomy(Library Map Class)
      required: true
    - name: collection
      type: taxonomy(Library Map Collection)
      required: true
    - name: record_type
      type: taxonomy(Record Type)
      required: false
  creates:
    - type: ops.record
      via_pattern: ../020_agents/TEMPLATES.md
  updates:
    - type: ops.tracker-item
  validation:
    - primary_class_and_collection_resolved
    - evidence_interpretation_assumptions_separated
    - mutable_state_recorded_in_metadata_not_prose
    - tracker_or_triage_updated
    - smallest_durable_learning_recorded
  next:
    - ops.workflow.create-domain
  failure_paths:
    - ops.workflow.maintain-record
---

# Maintain Record

Formalizes `020_agents/WORKFLOWS.md`'s existing Orient → Classify → Work → Verify loop as a
runnable workflow document. This is the default `ops` workflow: almost every internal task —
reading, classifying, and recording a piece of repository work — runs through this loop.

## Purpose

Give any piece of internal work (a question, a task, a review, a fix) a consistent path from
"something needs attention" to "a Tracker Item and, where warranted, a Record exist that
correctly describe it." Without this loop, agents re-derive an ad hoc process each time and
mutable state (what's done, what's still open) drifts out of the documents that are supposed to
carry it.

## Inputs

- `subject` (text, required) — what the work is about, in enough detail to classify it.
- `primary_class` (taxonomy(Library Map Class), required) — one of `00`, `10`, `20`, `30`,
  resolved via [`010_governance/LIBRARY_MAP.md`](../010_governance/LIBRARY_MAP.md).
- `collection` (taxonomy(Library Map Collection), required) — the collection within that class
  (e.g. `governance`, `agent-guidance`, `operations`, `records` within class `00`).
- `record_type` (taxonomy(Record Type), optional) — set only if the work will produce a Record
  (`decision`, `audit`, `setup`, `note`); a small fix that only updates the Tracker may not need
  one.

## Preconditions

- None are strictly required to start — this is the entry-point workflow for internal work with
  no other precondition. If a Tracker Item already exists for the subject (`state: draft`), this
  workflow operates on it rather than creating a duplicate (`requires.optional: true`).

## Procedure

1. **Orient.** Read the root and nearest `AGENTS.md`, resolve the subject in
   [`LIBRARY_MAP.md`](../010_governance/LIBRARY_MAP.md), and load only the canonical sources that
   are actually relevant. Do not read the whole corpus speculatively.
2. **Classify.** Select exactly one primary `class` and `collection` per `LIBRARY_MAP.md`; if the
   subject spans more than one, record the others in `facets` / `related` rather than duplicating
   the artifact into a second class. If the subject is genuinely new incoming work, capture it in
   `TRACKER.md` as a Tracker Item with `state: draft`, then apply `030_operations/TRIAGE.md`'s
   lane and required response to it.
3. **Work.** Do the work, keeping evidence, interpretation, assumptions, recommendations, and
   decisions distinguishable from each other as you go. Keep any mutable state (what stage this
   is at, whether it's resolved) in metadata (the Tracker Item's `state`, a Record's frontmatter)
   — never smuggled into prose where it can't be checked mechanically.
4. **Verify.** Apply [`VALIDATION.md`](../020_agents/VALIDATION.md): confirm one primary class, a
   mapped collection, valid metadata, resolved relative links, sources for material claims, and
   clearly labeled unknowns. Update the Tracker Item's `state` (and, if warranted, produce a
   Record using [`TEMPLATES.md`](../020_agents/TEMPLATES.md)) to reflect the outcome. Record the
   smallest durable learning — a note future work can act on without re-deriving it.

## Outputs

- An updated Tracker Item (new or existing) whose `state` accurately reflects where the work
  landed.
- Optionally, one new Record (`decision`, `audit`, `setup`, or `note`) in `090_records/`, created
  via the `TEMPLATES.md` pattern, evidencing the Tracker Item.

## Patterns

- [`020_agents/TEMPLATES.md`](../020_agents/TEMPLATES.md) — the Record frontmatter and body-section
  template used when this workflow's `Work` step produces a Record.

## Verification

- [`020_agents/VALIDATION.md`](../020_agents/VALIDATION.md)'s checklist passes: resolved class and
  collection, valid metadata, resolved links, sourced claims, labeled unknowns.
- The Tracker Item's `state` matches reality at the moment `Verify` completes — not what was true
  when the task started.

## Exceptions

- If verification fails (the classification was wrong, evidence doesn't support the claimed
  state, a link doesn't resolve), do not force an exit — return to `Orient` (`failure_paths:
  ops.workflow.maintain-record`) rather than recording a state the evidence doesn't support.
- If the work's conclusion is "this subject deserves its own modeled domain" rather than a single
  record, hand off to [Create Domain](create-domain.md) instead of forcing the result into a
  Tracker Item and Record alone.
- External writes, deployments, publication, approvals, and destructive actions stop here and
  require explicit user authorization, per [`AUTONOMY.md`](../020_agents/AUTONOMY.md) — this
  workflow only ever produces local, reversible documentation changes.
