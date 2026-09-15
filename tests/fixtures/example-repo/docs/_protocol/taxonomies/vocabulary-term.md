---
id: protocol.taxonomy.vocabulary-term
rdf:type: skos:ConceptScheme
skos:prefLabel: Vocabulary Term
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
columns:
  Prefix: skos:notation
  Value kind: skos:scopeNote
  Appears on: skos:example
related:
  - ../PROTOCOL.md
  - ../concepts/concept.md
sources: []
---

# Vocabulary Term

## Definition

Every standard term this repository writes into a file, and how to read it. Registering the
vocabulary as an ordinary taxonomy rather than a paragraph in the spec means lint can reject an
unbound prefix or an unknown key by consulting a file, and means the vocabulary is itself
queryable.

**Colons are theirs. Dots are ours.** A colon in a key or a value names a term defined by the
W3C. A dot names something defined here. A bare key is protocol-local. Export turns dots into
IRIs; nothing else changes.

*Value kind* says how to read what follows the key: `literal` is text, `iri` is a term or an id
that must resolve.

## Values

| Value | Prefix | Value kind | Appears on |
| --- | --- | --- | --- |
| rdf:type | rdf | iri | every file; every property |
| rdfs:label | rdfs | literal | concept, property, domain, workflow, skill |
| rdfs:comment | rdfs | literal | property |
| rdfs:range | rdfs | iri | property |
| owl:inverseOf | owl | iri | property, inside `derived` |
| owl:deprecated | owl | literal | any file; any taxonomy value |
| skos:prefLabel | skos | literal | taxonomy file; column 1 of Values, implicitly |
| skos:inScheme | skos | iri | property whose range is `skos:Concept`; column mapping |
| skos:definition | skos | literal | column mapping |
| skos:notation | skos | literal | column mapping |
| skos:broader | skos | iri | column mapping |
| skos:altLabel | skos | literal | column mapping |
| skos:scopeNote | skos | literal | column mapping |
| skos:example | skos | literal | column mapping |
| sh:minCount | sh | literal | property; workflow input; column mapping |
| sh:maxCount | sh | literal | property; workflow input; column mapping |
| sh:pattern | sh | literal | property |
| owl:Class | owl | iri | value of `rdf:type` on a concept |
| owl:ObjectProperty | owl | iri | value of `rdf:type` on a property whose range is an id |
| owl:DatatypeProperty | owl | iri | value of `rdf:type` on a property whose range is `xsd:` |
| skos:Concept | skos | iri | value of `rdfs:range` on a controlled property |
| skos:ConceptScheme | skos | iri | value of `rdf:type` on a taxonomy file |
| xsd:string | xsd | iri | value of `rdfs:range` |
| xsd:integer | xsd | iri | value of `rdfs:range` |
| xsd:date | xsd | iri | value of `rdfs:range` |
| xsd:anyURI | xsd | iri | value of `rdfs:range` |
