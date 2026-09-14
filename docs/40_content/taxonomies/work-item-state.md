---
id: content.taxonomy.work-item-state
rdf:type: skos:ConceptScheme
skos:prefLabel: Work Item State
domain: content
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
applies_to:
  - content.work-item
related:
  - ../concepts/work-item.md
  - workflow-stage.md
sources:
  - ../../00_system/010_governance/ONTOLOGY.md
---

# Work Item State

## Definition

The execution state of one Work Item, independent of where it sits in the content lifecycle. A
Work Item may be Blocked at any stage; state and stage are separate axes and must never be
conflated.

## Values

| Value | Definition |
| --- | --- |
| Queued | Accepted but not started. |
| In Progress | Actively being worked. |
| Blocked | Stopped pending evidence, approval, or a dependency named in the record. |
| Completed | Finished, having reached its workflow's exit stage. |
| Cancelled | Abandoned deliberately. Not a failure, and not resumable. |
