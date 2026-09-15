---
id: protocol.note
rdf:type: owl:Class
rdfs:label: Note
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
properties: []
related:
  - concept.md
sources: []
---

# Note

## Definition

A prose document that carries no modelled properties of its own: a routing `README.md`, a
guidance page, a strategy document, a dated record's narrative. A Note is still a typed, linted
file — it carries the record properties every file carries, its links are resolved, its id is
checked — but its body is free.

## Constraints

- A Note declares no properties, so the rule that every H2 must map to a declared `section`
  holds vacuously and its headings are unconstrained. This is the only reason that rule can be
  absolute everywhere else.
- A Note may not live in a directory named by another concept's `persistence.path`. That
  directory holds instances of that concept and its `README.md`, and nothing else — which is what
  stops `protocol.note` from becoming an escape hatch for material that should have been
  modelled.

## Notes

Reach for a Note when a document genuinely has no repeatable shape. If two of them start growing
the same headings, that is a concept waiting to be declared, not a Note.
