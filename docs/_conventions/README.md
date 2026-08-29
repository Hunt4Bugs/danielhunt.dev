---
id: protocol.conventions
kind: note
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - ../README.md
  - ../_patterns/README.md
  - documentation.md
  - identifiers.md
  - relationships.md
  - ../00_system/010_governance/DOMAIN_PROTOCOL.md
---

# Conventions

Standing rules every document in `docs/` follows, regardless of which domain it belongs to. These
implement [DOMAIN_PROTOCOL.md](../00_system/010_governance/DOMAIN_PROTOCOL.md) §8's root contract.

- [documentation.md](documentation.md) — the frontmatter contract: required keys, allowed `kind`
  and `status` values, and how the protocol's fields (`id`, `kind`, `domain`, `version`) coexist
  with this repository's pre-existing physical-placement fields (`class`, `collection`).
- [identifiers.md](identifiers.md) — the `<domain>.<kind>.<name>` scheme for types and instances,
  and the `WI-YYYYMMDD-<workflow>-<subject>` scheme for executed Work Items.
- [relationships.md](relationships.md) — how to state a directed relationship between two
  concepts, in prose and in Markdown.

A domain may add its own stricter rules (an entity contract, a controlled vocabulary) but may not
contradict what's here.
