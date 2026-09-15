---
id: content.note.concepts-readme
rdf:type: protocol.note
domain: content
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
related:
  - ../domain.md
  - ../taxonomies/README.md
  - ../../_protocol/concepts/concept.md
sources: []
---

# Content concepts

One file per concept. Each carries its definition, its constraints, its property contract, and
where its instances live — so there is one place to read what a Creator *is* and one place to
change it.

- [Creator](creator.md) — a person, company, brand, or organization.
- [Creator Channel](creator-channel.md) — one account a Creator controls on one Channel.
- [Work Item](work-item.md) — one execution of one workflow.

Controlled values live in [`../taxonomies/`](../taxonomies/README.md), not here.

```bash
uv run dh concepts --domain content
uv run dh get content.creator
```

This directory replaces the former single `concepts.md`. The remaining concepts are being moved
across in waves; until each lands, `concepts.md` is still the source for it.
