---
id: protocol.pattern.domain
kind: pattern
domain: protocol
pattern_for: protocol.domain-doc
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - README.md
  - ../00_system/010_governance/DOMAIN_PROTOCOL.md
---

# Pattern: `domain.md`

Every domain's `domain.md` (DOMAIN_PROTOCOL.md §9.2) states its boundary. It does not enumerate
concepts in detail — that's `concepts.md` — and it does not define workflows — that's
`workflows/`.

## Frontmatter

```yaml
id: <domain-id>
kind: domain
domain: <domain-id>
status: draft | active | blocked | superseded | archived
version: 1
class: "<class>"        # this repository's physical-placement addition
collection: <collection>
```

## Required body sections

- **Purpose** — one paragraph: what bounded area of reality does this domain model, and why does
  it exist as its own domain rather than folding into a neighbor?
- **Scope** — `Includes` and `Excludes` as two short lists. Be explicit about what looks related
  but is deliberately out of scope (this is what keeps domains from sprawling into each other).
- **Model** — the domain's Concepts, named but not fully specified (full specification is
  `concepts.md`'s job). A short sentence per Concept is enough here.
- **Relationships** — the domain's own top-level relationships, in the notation from
  [`_conventions/relationships.md`](../_conventions/relationships.md).
- **Constraints** — the domain's invariants (§3.4): what must always be true, stated as rules, not
  representation conventions.
- **Related Domains** — which neighboring domains this one depends on, references, or is
  referenced by, and which context owns which shared taxonomy.
- **Examples** — one or two concrete, real instances (not illustrative placeholders) that make the
  model legible.
