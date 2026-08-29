---
id: ops.workflow.create-domain
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
  - maintain-record.md
  - ../010_governance/LIBRARY_MAP.md
  - ../../_patterns/README.md
  - ../../_patterns/domain.md
  - ../../_patterns/concept.md
  - ../../_patterns/pattern.md
  - ../../_patterns/workflow.md
  - ../../_conventions/documentation.md
sources:
  - ../010_governance/DOMAIN_PROTOCOL.md
contract:
  subject_type: text
  entry_stage: Identify
  exit_stage: Test
  requires:
    - id: ops.tracker-item
      state: draft
      optional: true
  inputs:
    - name: domain_name
      type: text
      required: true
    - name: domain_id
      type: text
      required: true
    - name: intent
      type: text
      required: true
    - name: class
      type: taxonomy(Library Map Class)
      required: true
    - name: collection
      type: taxonomy(Library Map Collection)
      required: false
    - name: neighboring_domains
      type: list
      required: false
  creates:
    - type: domain
      via_pattern: ../../_patterns/domain.md
    - type: concept-registry
      via_pattern: ../../_patterns/concept.md
    - type: pattern
      via_pattern: ../../_patterns/pattern.md
    - type: workflow
      via_pattern: ../../_patterns/workflow.md
    - type: ops.record
      via_pattern: ../020_agents/TEMPLATES.md
  updates:
    - type: ops.tracker-item
  validation:
    - domain_id_unique_and_well_formed
    - scope_includes_and_excludes_stated
    - concepts_discovered_and_minimal
    - relationships_and_constraints_defined
    - model_validated_against_real_scenarios
    - required_structure_present
    - initial_workflows_defined_and_resolve
    - tested_against_one_real_task
  next:
    - ops.workflow.maintain-record
  failure_paths:
    - ops.workflow.create-domain
---

# Create Domain

Implements [`DOMAIN_PROTOCOL.md`](../010_governance/DOMAIN_PROTOCOL.md) §15's domain creation
workflow as a real, runnable workflow document rather than prose a session has to re-derive each
time. This is the workflow a future session runs against each of the seven remaining thin Brand
contexts — Identity, Strategy, Audience, Offers, Assets, Channels, Analytics, Relationships — once
one of them has enough real material to justify full modeling. It works the same way for any other
future domain.

## Purpose

Take a proposed domain name and intent and produce a protocol-conformant domain: a bounded scope,
a minimal set of Concepts with relationships and constraints, a validated model, and the required
file structure (`README.md`, `domain.md`, `concepts.md`, `_patterns/`, `workflows/`) — without
skipping the modeling steps that keep the domain from sprawling or duplicating a neighbor.

## Inputs

- `domain_name` (text, required) — the human-readable name (e.g. "Identity").
- `domain_id` (text, required) — the short lowercase identifier used in `<domain>.<kind>.<name>`
  (e.g. `identity`). Must not collide with an existing domain id (`content`, `ops`, `protocol`,
  …).
- `intent` (text, required) — what bounded area of reality this domain models and why it needs to
  exist separately from a neighboring domain.
- `class` (taxonomy(Library Map Class), required) — which numbered class directory will host the
  domain's files, resolved via [`LIBRARY_MAP.md`](../010_governance/LIBRARY_MAP.md).
- `collection` (taxonomy(Library Map Collection), optional) — the collection within that class,
  if the class already defines one that fits; otherwise the domain may need its own root-level
  placement (as `ops` itself does).
- `neighboring_domains` (list, optional) — other domains this one is likely to reference or be
  referenced by (e.g. a new `identity` domain neighboring `content`).

## Preconditions

- None strictly required — this is a root-level workflow, not scoped inside any one domain
  (`DOMAIN_PROTOCOL.md` §15 opening line). If a Tracker Item already proposed the new domain
  (`state: draft`), this workflow resolves it; otherwise it may create one as part of `Identify`.
- The subject is *not* yet a modeled Concept when this workflow starts — that's the point of the
  workflow — so `subject_type` above is `text` (a proposed name + intent), not a `ref(...)` to an
  existing concept.

## Procedure

Follow `DOMAIN_PROTOCOL.md` §15's ten steps in order. Do not skip a step to get to the file
scaffold faster — a domain generated without steps 3–6 done honestly reproduces the sprawl the
protocol exists to prevent.

1. **Identify.** Name the domain, assign its `id`, and state its purpose in one paragraph: what
   bounded area are we trying to understand or operate? Write this as the `domain_id` and the
   first paragraph of the future `domain.md`.
2. **Scope.** List what belongs and what does not, and name every neighboring domain. Be explicit
   about anything that looks related but is deliberately excluded — this is what keeps domains
   from absorbing each other (see `ops`'s own `domain.md` §Excludes for the shape this should
   take).
3. **Discover concepts.** Ask: what things exist, have identity, change over time, are created or
   consumed, are acted upon, or would need a database table? Start minimal. For a Brand context
   like Identity, this might be `Trait`, `Value`, `Voice Rule` — not dozens of concepts invented
   up front.
4. **Define relationships.** For each Concept: what can it contain, what creates it, what does it
   depend on, what does it reference, what can act on it? Write these in the notation from
   [`_conventions/relationships.md`](../../_conventions/relationships.md).
5. **Define constraints.** What must always be true, what must never happen, what is required,
   what is optional? State each as an invariant rule, not a formatting instruction (§7's
   Pattern-vs-Constraint distinction).
6. **Validate the model.** Walk two or three real scenarios from the actual domain material. If
   the model cannot describe them cleanly, revise steps 3–5 before moving on — do not patch the
   gap with a more complicated workflow later.
7. **Determine persisted representations.** For each Concept: does it need independent identity,
   will a workflow create instances of it, must humans or machines reference specific instances?
   If yes, decide on a `_patterns/<concept>.md` and/or an instance directory (§14, §14.1). If no,
   leave it modeled in `concepts.md` without a Pattern or directory — do not create one "because
   the Concept exists."
8. **Generate the structure.** Produce `README.md` (routing), `domain.md` (via
   [`_patterns/domain.md`](../../_patterns/domain.md)), `concepts.md` (via
   [`_patterns/concept.md`](../../_patterns/concept.md)), a `_patterns/` directory for any
   Concepts from step 7 that need one (via
   [`_patterns/pattern.md`](../../_patterns/pattern.md)'s shape), and a `workflows/` directory,
   plus any domain-specific structures step 7 justified. Carry the merged frontmatter contract
   (`id`/`kind`/`domain`/`status`/`version` alongside `class`/`collection`) on every file, per
   [`_conventions/documentation.md`](../../_conventions/documentation.md).
9. **Define initial workflows.** Write only the highest-value operations first (via
   [`_patterns/workflow.md`](../../_patterns/workflow.md)'s `contract:` shape) — typically the
   workflow that creates the domain's primary Concept and the workflow that most commonly updates
   it. Resist writing a workflow for every Concept before any of them has been run.
10. **Test against real work.** Run one actual task through the new domain end to end. If the
    model can't describe it cleanly, revise the model — do not compensate with an increasingly
    complicated prompt or a workflow exception.

Record the outcome as an `ops.record` (`type: setup`) via
[Maintain Record](maintain-record.md)'s pattern, and update the originating Tracker Item.

## Outputs

- A protocol-conformant domain directory (or root-level scaffold, if it doesn't fit inside a
  single existing collection) containing `README.md`, `domain.md`, `concepts.md`, `_patterns/`
  (where step 7 justified one), and `workflows/` with at least one workflow.
- One `ops.record` (`type: setup`) documenting the decisions made at each of the ten steps —
  especially step 2's exclusions and step 7's persistence calls, which are the easiest to
  second-guess later without a record.
- An updated Tracker Item reflecting that the domain now exists.

## Patterns

- [`_patterns/domain.md`](../../_patterns/domain.md) — for the generated `domain.md`.
- [`_patterns/concept.md`](../../_patterns/concept.md) — for the generated `concepts.md`.
- [`_patterns/pattern.md`](../../_patterns/pattern.md) — for any `_patterns/<concept>.md` files
  step 7 decides the domain needs.
- [`_patterns/workflow.md`](../../_patterns/workflow.md) — for each file under the generated
  `workflows/`.
- [`020_agents/TEMPLATES.md`](../020_agents/TEMPLATES.md) — for the closing `ops.record`.

## Verification

- `protocol-lint`'s checks (`DOMAIN_PROTOCOL.md` §13), applied by hand until a lint tool exists:
  required structure present; every `id` unique and well-formed; required frontmatter keys
  present; every `related`/`sources` link resolves; every `ref(...)` resolves to a defined
  Concept; every `taxonomy(...)` resolves to an owning registry; every workflow `next` /
  `failure_paths` resolves to a workflow file that exists.
- Step 10's real task actually completed using only the new domain's documents — not evidence
  that the documents merely look complete.

## Exceptions

- If step 6 (validate the model) fails against real scenarios, do not proceed to step 8 —
  return to step 3 and revise the concept list (`failure_paths: ops.workflow.create-domain`).
- If the "domain" turns out to be a single Concept that fits cleanly inside an existing domain's
  `concepts.md`, stop here and add it there instead — per `DOMAIN_PROTOCOL.md` §2.2, domains do
  not need identical structures, but they also should not be created for something a neighbor
  already models.
- If the new domain's natural boundary does not fit inside any existing numbered class, that is
  itself a decision to record (`ops.record`, `type: decision`) before generating files, per
  `DOMAIN_PROTOCOL.md` §20's open question on class prefixes versus domain folders.
- Publishing, deploying, or otherwise exposing the new domain's content externally stops here and
  requires explicit user authorization, per [`AUTONOMY.md`](../020_agents/AUTONOMY.md) — this
  workflow only ever produces local, reversible documentation.
