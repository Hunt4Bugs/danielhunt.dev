---
id: content.creator-channel
rdf:type: owl:Class
rdfs:label: Creator Channel
domain: content
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-09-14
previous_id: content.creator-channel
title_field: name
persistence:
  mode: directory
  path: creator-channels
  scope: own
properties:
  - id: name
    rdf:type: owl:DatatypeProperty
    rdfs:label: Name
    rdfs:comment: How this account is referred to, usually "<Creator> on <Channel>".
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: creator
    rdf:type: owl:ObjectProperty
    rdfs:label: Creator
    rdfs:comment: The Creator that controls this account.
    rdfs:range: content.creator
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: channel
    rdf:type: owl:ObjectProperty
    rdfs:label: Channel
    rdfs:range: skos:Concept
    skos:inScheme: content.taxonomy.channel
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: handle
    rdf:type: owl:DatatypeProperty
    rdfs:label: Handle
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: frontmatter
  - id: url
    rdf:type: owl:DatatypeProperty
    rdfs:label: URL
    rdfs:range: xsd:anyURI
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: creating_work_item
    rdf:type: owl:ObjectProperty
    rdfs:label: Creating Work Item
    rdfs:range: content.work-item
    sh:maxCount: 1
    store: frontmatter
  - id: registration_provenance
    rdf:type: owl:DatatypeProperty
    rdfs:label: Registration Provenance
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: body
    section: Registration Provenance
    format: prose
related:
  - README.md
  - creator.md
  - ../creator-channels/README.md
  - ../taxonomies/channel.md
sources:
  - ../../00_system/010_governance/ONTOLOGY.md
---

# Creator Channel

## Definition

One account a Creator controls on one Channel. A Creator may control several; each is its own
record, so a handle, a URL and a provenance can be tracked per account rather than crammed into
the Creator.

## Constraints

- A Creator Channel belongs to exactly one Creator and sits on exactly one Channel.
- `url` is the account's canonical public address. It is not a post, a profile screenshot, or a
  search result.
- A Creator Channel records that an account exists and who controls it. It is not evidence of
  reach, performance, or current activity; establishing those is a Review.

## Notes

This concept is the inverse side of `content.creator.creator_channels`. That property is derived
from these records by `uv run dh index`, so the link is maintained in one direction only and the
other is computed — which is why neither side can go stale against the other.
