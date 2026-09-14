---
id: protocol.taxonomy
rdf:type: owl:Class
rdfs:label: Taxonomy
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
title_field: skos:prefLabel
instance_rdf_type: skos:ConceptScheme
persistence:
  mode: directory
  path: taxonomies
  scope: all-domains
properties:
  - id: skos:prefLabel
    rdf:type: owl:DatatypeProperty
    rdfs:label: Preferred label
    rdfs:comment: >-
      The vocabulary's name, exactly as properties reference it through skos:inScheme. Unique
      across the repository — a vocabulary is owned by the file that defines it.
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: applies_to
    rdf:type: owl:DatatypeProperty
    rdfs:label: Applies to
    rdfs:comment: Concept ids whose properties draw on this scheme. Advisory, not enforced.
    rdfs:range: xsd:string
    store: frontmatter
  - id: columns
    rdf:type: owl:DatatypeProperty
    rdfs:label: Columns
    rdfs:comment: >-
      Maps a Values-table header to the term it carries. Column 1 is always skos:prefLabel and is
      never declared. Headers covered by the default mapping need no entry; any other header
      must have one, and lint fails on an unmapped header rather than dropping the column.
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: frontmatter
  - id: definition
    rdf:type: owl:DatatypeProperty
    rdfs:label: Definition
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: body
    section: Definition
    format: prose
  - id: values
    rdf:type: owl:DatatypeProperty
    rdfs:label: Values
    rdfs:comment: The vocabulary itself, as a row-per-value markdown table.
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: body
    section: Values
    format: table
related:
  - concept.md
  - ../taxonomies/vocabulary-term.md
sources: []
---

# Taxonomy

## Definition

A controlled vocabulary: a `skos:ConceptScheme` whose values are the rows of a single markdown
table. One file per vocabulary, so a vocabulary's owner is structurally the file that defines
it — ownership stops being a prose policy anything has to reason about.

## Constraints

- `skos:prefLabel` is unique across the repository. Two files declaring the same vocabulary name
  is an error.
- The `## Values` table is row-per-value. Column 1 holds the value and maps to `skos:prefLabel`
  implicitly.
- Every other column maps by header name: `Definition` / `Meaning` / `Use` / `Description` to
  `skos:definition`; `Stable code` / `Code` / `Notation` to `skos:notation`; `Broader` / `Parent`
  to `skos:broader`; `Note` / `Notes` to `skos:scopeNote`; `Example` to `skos:example`;
  `Alias` / `Aliases` / `Also known as` to `skos:altLabel`. Anything else requires a `columns`
  entry.
- A literal `|` inside a cell is written `\|`.
- `skos:broader` cells hold a value from column 1 of the same table. Cross-scheme hierarchy is
  not expressible; a grouping that spans two vocabularies is a third vocabulary plus a column.
- Renaming a value is governed: mint the new value and mark the old `owl:deprecated`. Values are
  never edited in place, because slugs are computed from them.

## Notes

A value's IRI is the scheme IRI plus a slug of its `skos:prefLabel` — NFKC, lowercased, every run
outside `[a-z0-9]` collapsed to `-`. `skos:prefLabel` keeps the exact original string, so
flattening `→`, `/` and `+` loses nothing, and lint checks slug uniqueness within the scheme.

A column may point into another vocabulary by carrying `rdfs:range: skos:Concept` and
`skos:inScheme`. That is what makes a compatibility table checkable rather than aspirational.
