---
id: protocol.taxonomy.body-format
rdf:type: skos:ConceptScheme
skos:prefLabel: Body Format
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

# Body Format

## Definition

How a `store: body` property is written inside its section. Mandatory on every body property, so
that the two halves of the old `text` type — *it is a string* and *it is prose* — can never drift
apart across the two lines that now carry them.

## Values

| Value | Definition |
| --- | --- |
| prose | One value: the section's paragraphs, taken whole. Requires `sh:maxCount: 1`. |
| list | One value per `- ` bullet. A reference bullet is written a bullet written as `- [Label](path.md)`. |
| table | A markdown table, read row-per-record. Used by taxonomy values and derived indexes. |
