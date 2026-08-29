---
id: protocol.pattern.concept
kind: pattern
domain: protocol
pattern_for: protocol.concept-registry-doc
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - README.md
  - ../00_system/010_governance/DOMAIN_PROTOCOL.md
---

# Pattern: `concepts.md`

One canonical registry per domain (DOMAIN_PROTOCOL.md §9.3). Every Concept the domain models gets
one entry, in one place — never split the same Concept's definition across multiple files.

## Frontmatter

```yaml
id: <domain-id>.concepts
kind: concept-registry
domain: <domain-id>
status: draft | active | blocked | superseded | archived
version: 1
```

## Per-concept entry shape

```markdown
## <Concept Name>
**ID:** `<domain>.<concept>`

One or two sentences: what is this, in plain language.

### Relationships
- <verb phrase> `<domain>.<other-concept>`

### Constraints
- An invariant that must remain true, stated as a rule (§3.4) — not a formatting instruction.

### Entity contract
entity: <domain>.<concept>
fields:
  - name: <field-name>
    type: ref(<domain>.<concept>) | taxonomy(<vocabulary>) | text | date | url | list
    required: true | false
    cardinality: 1 | 0..1 | 0..* | 1..*
```

## Rules

- Only add an **Entity contract** when the Concept's instances are actually persisted as
  documents — a Concept can exist in the model without one (§10, §14).
- A `ref(...)` type must resolve to a Concept defined *somewhere* in the repository's domains
  (its own registry or another domain's); a `taxonomy(...)` type must resolve to a controlled
  vocabulary owned by exactly one context (§10, §13.3). Don't invent either inline.
- If a domain's model is authored at a higher level (e.g. a brand-root ontology spanning several
  contexts), the domain-scoped `concepts.md` cross-references that source rather than re-deriving
  it — see `10_brand/marketing/content/concepts.md`'s relationship to `10_brand/ONTOLOGY.md` once
  it exists.
