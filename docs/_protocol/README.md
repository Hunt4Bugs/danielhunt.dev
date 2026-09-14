---
id: protocol.note.readme
rdf:type: protocol.note
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
related:
  - domain.md
  - PROTOCOL.md
  - ../ROUTER.md
sources: []
---

# Protocol

You are in the meta-domain: the shapes every other domain is written in.

- **What the model is and why** — [`PROTOCOL.md`](PROTOCOL.md).
- **The boundary, the prefix binding, and the record properties every file carries** —
  [`domain.md`](domain.md).
- **The shapes themselves** — [`concepts/`](concepts/): Concept, Domain, Taxonomy, Workflow,
  Router, Note, Skill.
- **The protocol's own vocabularies** — [`taxonomies/`](taxonomies/): Status, Field Store, Body
  Format, Persistence Mode, and the Vocabulary Term registry that lists every standard term this
  repository writes.
- **Which domain owns a subject** — [`../ROUTER.md`](../ROUTER.md).
- **Where a file physically lives** —
  [`../00_system/010_governance/LIBRARY_MAP.md`](../00_system/010_governance/LIBRARY_MAP.md).

## Reading the vocabulary

**Colons are theirs. Dots are ours.** `rdfs:range` and `owl:Class` are W3C terms;
`content.creator` is defined here; a bare key like `store` is protocol-local.

The model adopts OWL/RDFS/SKOS **vocabulary** and SHACL **semantics**. The distinction is
load-bearing, not stylistic: `sh:minCount: 1` fails when a value is missing, while
`owl:minCardinality 1` would *infer* the missing value into existence and could never fail.
PROTOCOL.md §17 says so at length, and lint rejects the OWL constraint terms by name.

## Operating on it

```bash
uv run dh concepts --domain protocol
uv run dh get protocol.concept
uv run dh lint docs/_protocol --strict
```

`docs/_protocol/concepts/concept.md` is the engine's one bootstrap axiom: it is an instance of
itself, read by a minimal parser and then re-validated against the contract it defines.
