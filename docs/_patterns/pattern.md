---
id: protocol.pattern.pattern
kind: pattern
domain: protocol
pattern_for: protocol.pattern-doc
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - README.md
  - ../00_system/010_governance/DOMAIN_PROTOCOL.md
---

# Pattern: a domain's `_patterns/<concept>.md`

This governs the files inside a *domain's own* `_patterns/` directory (e.g.
`content/_patterns/topic.md`) — not the meta-patterns in this directory. A
domain-level pattern is a representation convention: what does one instance document of this
Concept actually look like (§3.5, §7).

## Frontmatter

```yaml
id: <domain>.pattern.<concept>
kind: pattern
domain: <domain-id>
pattern_for: <domain>.<concept>
status: draft | active | blocked | superseded | archived
version: 1
```

## Required body

The template sections an instance document must contain — named, in order, with a one-line note
on what belongs in each. Nothing more: a Pattern carries structure, not the invariant rules that
belong in `concepts.md`'s Constraints block (§7's distinction — don't restate a Constraint here as
if it were a formatting rule).

## When to create one

Per DOMAIN_PROTOCOL.md §14.1: when humans or software repeatedly create instances of the Concept,
instances need a predictable shape, a Workflow produces that Concept, or consistent structure
materially improves reasoning or validation. Not merely because the Concept exists in
`concepts.md` — a Concept with no repeated, persisted instances doesn't need one.
