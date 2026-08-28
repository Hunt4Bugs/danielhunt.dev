---
id: protocol.conventions.relationships
kind: note
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - README.md
  - ../00_system/010_governance/DOMAIN_PROTOCOL.md
---

# Relationship notation

Restates [DOMAIN_PROTOCOL.md](../00_system/010_governance/DOMAIN_PROTOCOL.md) §6 as a standalone
reference. Keep relationship statements minimal and meaningful — this is documentation, not a
hand-maintained graph database (§2.5).

## Notation

```text
<source concept> -- <relationship> --> <target concept>
```

Example:

```text
Publication -- communicates --> Topic
Publication -- uses --> Blueprint
Knowledge -- supports --> Topic
```

## In Markdown

```markdown
### Relationships
- `Publication` **communicates** `Topic`
- `Publication` **uses** `Blueprint`
- `Knowledge` **supports** `Topic`
```

This maps directly onto `subject → predicate → object`, so it can bridge to RDF/OWL later if that
representation is ever needed (see DOMAIN_PROTOCOL.md §1's representation diagram) — but nothing
here requires adopting RDF now.

## Where relationships are declared

A Concept's relationships live under its own `### Relationships` heading in the owning domain's
`concepts.md` (§9.3). A Workflow's relationship to other workflows (`next`, `failure_paths`) is
declared in its `contract:` YAML block (§11), not restated in prose form here.
