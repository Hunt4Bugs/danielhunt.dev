---
id: content.pattern.series
kind: pattern
domain: content
pattern_for: content.series
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - editorial
related:
  - ../series/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Pattern: Series

What a `content.series` instance document (stored under `series/`) must contain. See
[`concepts.md`](../concepts.md#series) for the Series entity contract this pattern instantiates.

## Required body sections

1. **Continuing premise** — the recurring editorial premise that ties member Topics and/or
   Publications together.
2. **Inclusion boundary** — the rule for what belongs in this Series and what does not.
3. **Related Topics** — links to member Topics (may be empty at creation).
4. **Related Publications** — links to member Publications (may be empty at creation).
5. **Campaign references** — optional links to Campaigns this Series participates in.
6. **Creating Work Item** — link to the Work Item that created this Series.

## Notes

A Series is not necessarily a Campaign, and grouping Topics or Publications into a Series does not
replace their own identity or record contract.
