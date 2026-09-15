---
id: protocol.taxonomy.persistence-mode
rdf:type: skos:ConceptScheme
skos:prefLabel: Persistence Mode
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

# Persistence Mode

## Definition

Whether a concept's instances are stored, and if so how. The documentation model must not force a
filesystem representation of every modelled thing, so a concept that is real but unstored says so
rather than growing an empty directory.

## Values

| Value | Definition |
| --- | --- |
| directory | One file per instance, at `<domain-root>/<path>/*.md`, excluding `README.md`. |
| registry | Instances are rows in a table or a single named file; `path` names it. |
| external | Instances live outside `docs/`; `path` is a repo-relative glob. Listed, not validated. |
| none | Modelled but not persisted. The concept exists; nothing is stored for it. |
