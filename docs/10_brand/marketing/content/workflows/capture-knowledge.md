---
id: content.workflow.capture-knowledge
kind: workflow
domain: content
class: "10"
collection: content
type: workflow
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-28
facets:
  - operations
related:
  - README.md
  - ../work-items/README.md
  - ../concepts.md
sources:
  - ../../../ONTOLOGY.md
contract:
  subject_type: content.knowledge   # judgment call: the raw material has no persisted concept type of its own; modeled as the Knowledge-in-formation. See report.
  entry_stage: Capture
  exit_stage: Validate
  requires: []
  inputs:
    - name: material
      type: text
      required: true
    - name: origin
      type: text
      required: false
  creates:
    - type: content.knowledge
      via_pattern: ../_patterns/knowledge.md
    - type: content.source
      via_pattern: ../_patterns/source.md
  updates:
    - type: content.knowledge
  validation:
    - provenance_recorded
    - evidence_boundary_stated
    - knowledge_kind_selected
    - duplicate_check_performed
    - output_links_recorded
  next:
    - content.workflow.develop-topic
    - content.workflow.capture-knowledge
  failure_paths:
    - content.workflow.capture-knowledge
---

# Capture Knowledge

## Work Item contract

- **Primary subject:** the raw material being evaluated.
- **Entry stage:** Capture.
- **Successful exit stage:** Validate.
- **Creates:** one Knowledge record and any reusable Source records that do not already exist.
- **Updates:** an existing materially duplicative Knowledge or Source record when appropriate.
- **Required predecessors:** none.
- **Possible next workflows:** [Develop Topic](develop-topic.md) after the Knowledge is usable; this workflow again after verification when material remains unknown.
- **Validation evidence:** provenance, evidence boundary, selected Knowledge Kind, duplicate check, and output links recorded in the Work Item.
- **Failure and return paths:** remain at Capture when origin, privacy, or verification limits prevent honest reusable synthesis.

## Required references

- [Brand ontology v1](../../../ONTOLOGY.md): Knowledge, Source, Knowledge Kind, and their relationships.
- [Source records](../sources/README.md): provenance and verification-boundary requirements.
- [Knowledge records](../knowledge/README.md): reusable synthesis and relationship requirements.
- [Identity](../../../identity/README.md): truthfulness, evidence, privacy, and scars-not-wounds boundaries.

## Taxonomy contract

- **Reads:** Knowledge Kind and the existing Knowledge inventory.
- **Writes:** one existing Knowledge Kind on the resulting Knowledge record.
- **Restriction:** use only ontology-defined values. Route a missing value through [Propose Taxonomy Addition](propose-taxonomy-addition.md).

## Input

Raw material with its available context and provenance. The material may be an observation, experience, research finding, opinion, idea, question, lesson, process, framework, or evidence.

## Procedure

1. Preserve the material's origin, date or timeframe when known, access conditions, and relevant context.
2. Create or link a Source record when the origin has value beyond this capture. For firsthand material, identify the firsthand context and its verification limits.
3. Extract the smallest reusable synthesis without converting it into a Topic, Blueprint, claim, or publication draft.
4. Select one Knowledge Kind and link the supporting Sources.
5. Separate verified evidence, firsthand account, interpretation, and unknowns. Record an evidence boundary for anything that must not be stated as established fact.
6. Check the existing Knowledge inventory and extend an existing record when the material is materially duplicative.

## Output

One reusable Knowledge record with a Knowledge Kind, provenance, synthesis, evidence boundary, links to supporting Sources, and a link to the creating Work Item. The workflow may also produce one or more Source records when reusable provenance does not already exist.

## Stop conditions

Stop without creating Knowledge when the origin cannot be represented honestly, the material is only an unsupported claim, or privacy and confidentiality constraints prevent safe internal capture. Preserve material as an explicitly labeled unknown when it may become usable after verification.
