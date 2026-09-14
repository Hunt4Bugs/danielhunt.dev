---
id: protocol
rdf:type: protocol.domain
rdfs:label: Protocol
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
root: _protocol
base_iri: https://danielhunt.dev/ns/
vocab_iri: https://danielhunt.dev/ns/protocol#
prefixes:
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  owl: http://www.w3.org/2002/07/owl#
  skos: http://www.w3.org/2004/02/skos/core#
  sh: http://www.w3.org/ns/shacl#
  xsd: http://www.w3.org/2001/XMLSchema#
record_properties:
  - id: status
    rdf:type: owl:ObjectProperty
    rdfs:label: Status
    rdfs:range: skos:Concept
    skos:inScheme: protocol.taxonomy.status
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: version
    rdf:type: owl:DatatypeProperty
    rdfs:label: Version
    rdfs:range: xsd:integer
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: owner
    rdf:type: owl:DatatypeProperty
    rdfs:label: Owner
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: frontmatter
  - id: created
    rdf:type: owl:DatatypeProperty
    rdfs:label: Created
    rdfs:range: xsd:date
    sh:maxCount: 1
    store: frontmatter
  - id: updated
    rdf:type: owl:DatatypeProperty
    rdfs:label: Updated
    rdfs:range: xsd:date
    sh:maxCount: 1
    store: frontmatter
  - id: facets
    rdf:type: owl:DatatypeProperty
    rdfs:label: Facets
    rdfs:range: xsd:string
    store: frontmatter
  - id: related
    rdf:type: owl:DatatypeProperty
    rdfs:label: Related
    rdfs:range: xsd:anyURI
    store: frontmatter
  - id: sources
    rdf:type: owl:DatatypeProperty
    rdfs:label: Sources
    rdfs:range: xsd:anyURI
    store: frontmatter
  - id: previous_id
    rdf:type: owl:DatatypeProperty
    rdfs:label: Previous id
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: frontmatter
related:
  - README.md
  - PROTOCOL.md
sources: []
---

# Protocol

## Purpose

The meta-model every other domain conforms to, as used by the test fixture.

## Scope

Includes the meta-concepts and the protocol's own vocabularies. Excludes any domain's own model.
