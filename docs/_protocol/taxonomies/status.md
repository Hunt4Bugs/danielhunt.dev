---
id: protocol.taxonomy.status
rdf:type: skos:ConceptScheme
skos:prefLabel: Status
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
applies_to:
  - protocol.concept
  - protocol.domain
  - protocol.taxonomy
  - protocol.workflow
  - protocol.note
related:
  - ../concepts/concept.md
sources: []
---

# Status

## Definition

The documentary state of a file: how much it should be relied on, independent of any execution
state. Every file in the repository carries exactly one.

`status` is not a type. A file that is reference material says so through its `rdf:type`, not by
inventing a status value.

Severity is scoped by this vocabulary: a missing required value is an **error** on an `active`
record and a **warning** on any other, because `draft`, `blocked`, `superseded` and `archived`
are already honest labels for incompleteness.

## Values

| Value | Definition |
| --- | --- |
| draft | Written but not yet reliable. Gaps are expected and are not errors. |
| active | Current and relied upon. Required values must be present. |
| blocked | Work stopped pending evidence, approval, or a dependency named in the record itself. |
| superseded | Replaced by a named successor, kept so inbound links and provenance survive. |
| archived | Retained as history. Not current, not maintained, and not brought to contract. |
