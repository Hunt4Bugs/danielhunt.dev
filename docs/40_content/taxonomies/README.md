---
id: content.note.taxonomies-readme
rdf:type: protocol.note
domain: content
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
related:
  - ../domain.md
  - ../concepts/README.md
  - ../../_protocol/concepts/taxonomy.md
sources: []
---

# Content vocabularies

One file per controlled vocabulary, so a vocabulary's owner is structurally the file that
defines it.

- [Creator Type](creator-type.md), [Creator Relationship](creator-relationship.md)
- [Channel](channel.md), [Publication Format](publication-format.md)
- [Workflow Stage](workflow-stage.md), [Work Item State](work-item-state.md)

```bash
uv run dh taxonomy list
uv run dh taxonomy values "Creator Relationship"
uv run dh taxonomy check "Creator Relationship" Collaborator   # exits non-zero
```

Adding a value is governed. Propose it; never write one that has not been approved.
