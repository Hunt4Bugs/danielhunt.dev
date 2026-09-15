---
id: content.taxonomy.channel
rdf:type: skos:ConceptScheme
skos:prefLabel: Channel
domain: content
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
applies_to:
  - content.creator-channel
columns:
  Status: skos:scopeNote
  Compatible Publication Formats:
    rdfs:range: skos:Concept
    skos:inScheme: content.taxonomy.publication-format
    format: list
  Role: skos:definition
related:
  - ../concepts/creator-channel.md
  - ../channels.md
  - publication-format.md
sources:
  - ../channels.md
---

# Channel

## Definition

A distribution surface where a Publication appears. Channel is a controlled vocabulary rather
than a modelled class: a channel has attributes but no independent identity to track, and
nothing is ever stored per channel beyond the row below.

`Compatible Publication Formats` is a cross-scheme column. It is what makes the standing rule —
a workflow must reject an incompatible Channel and Publication Format pair — checkable rather
than aspirational.

## Values

| Value | Status | Compatible Publication Formats | Role |
| --- | --- | --- | --- |
| X | Active | Text Post, Thread | Optional reuse, build-journal fragments, and personal observations; no posting quota. |
| Instagram | Active | Carousel, Short-form Video | Optional reuse or personal expression through movement, food, culture, and relevant build observations. |
| LinkedIn | Active | Text Post, Carousel, Article | Priority technical teaching channel: worked lessons and shorter engineering observations. |
| YouTube | Planned | Short-form Video, Long-form Video | Future cinematic storytelling if readiness gates and capacity support a separately chosen launch. |
| Newsletter | Future | Newsletter | A future owned editorial channel; not part of the current cadence. |
