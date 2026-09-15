---
id: protocol.taxonomy.field-store
rdf:type: skos:ConceptScheme
skos:prefLabel: Field Store
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
applies_to:
  - protocol.concept
related:
  - ../concepts/concept.md
sources: []
---

# Field Store

## Definition

Where a property's value physically lives in its instance file. Declared explicitly on every
property and never derived from the range: `name` is a string kept in front matter because the
contract says so, not because of its type.

## Values

| Value | Definition |
| --- | --- |
| frontmatter | The value is a YAML key. Scalars, references and controlled values live here. |
| body | The value is a markdown section named verbatim by `section`. Prose lives here. |
