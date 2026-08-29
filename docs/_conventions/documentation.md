---
id: protocol.conventions.documentation
kind: note
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - README.md
  - identifiers.md
  - ../00_system/010_governance/DOMAIN_PROTOCOL.md
supersedes:
  - ../00_system/010_governance/METADATA.md
---

# Documentation frontmatter contract

This supersedes `00_system/010_governance/METADATA.md` as the repository-wide standard. It merges
this repository's pre-existing physical-placement fields with
[DOMAIN_PROTOCOL.md](../00_system/010_governance/DOMAIN_PROTOCOL.md) §9.1's machine contract, so
neither `LIBRARY_MAP.md` routing nor protocol validation has to be sacrificed for the other.

## Required keys

```yaml
id: <domain>.<kind>.<name>        # protocol identity — see identifiers.md
kind: domain | concept-registry | pattern | workflow | decision | note | protocol
domain: <domain-id>                # e.g. content, ops, protocol
status: draft | active | blocked | superseded | archived
version: 1
class: "00" | "10" | "20" | "30"    # physical placement — see LIBRARY_MAP.md
collection: <collection-name>       # physical placement within the class
```

Plus, when relevant: `owner`, `created`, `updated`, `facets`, `related`, `sources`.

## Two identity systems, one document

- `id` / `kind` / `domain` answer *what is this, semantically, and which model does it belong to.*
  This is what `protocol-lint` and any future skill validate against.
- `class` / `collection` answer *where does this physically live and how do I route to it.* This is
  what `LIBRARY_MAP.md` resolves.

They are independent and both required on any document created or materially revised from this
point forward. A document's `class` does not need to match its `domain` — `10_brand/marketing/
content/` is `class: "10"` but `domain: content`, because one numbered class directory can host
more than one Domain, and a Domain's documents don't have to sit under a single class prefix.

## `kind` values

The protocol (§9.1) allows `domain | concept-registry | pattern | workflow | decision | note`.
This repository adds one exception: **`protocol`**, reserved for
[DOMAIN_PROTOCOL.md](../00_system/010_governance/DOMAIN_PROTOCOL.md) itself. It is not an instance
of any domain's concept — it is the meta-spec that defines what a domain, concept, or pattern *is*
— so forcing it into `kind: domain` or `kind: concept-registry` would misrepresent it. Do not use
`kind: protocol` for anything else; a document that models actual domain content, however
foundational, uses one of the six protocol-defined kinds.

## Migration policy

Existing documents predate this merged standard and retain their canonical placement and existing
frontmatter until they are materially revised — matching the precedent this repository already
set in `METADATA.md`. Do not mass-rewrite frontmatter across files that aren't otherwise being
touched. New documents, and any document whose body is materially rewritten, carry the full
merged contract above.

## Status values

Unchanged from the prior standard: `draft`, `active`, `blocked`, `superseded`, `archived`. Dates
use ISO-8601. Each record distinguishes verified evidence, interpretation, assumptions,
recommendations, and decisions, and uses repository-relative links for `related` and `sources`.
