---
id: content.pattern.source
kind: pattern
domain: content
pattern_for: content.source
status: active
version: 1
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - provenance
related:
  - ../sources/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Pattern: Source

What a `content.source` instance document (stored under `sources/`) must contain. See
[`concepts.md`](../concepts.md#source) for the Source entity contract this pattern instantiates.

## Required body sections

1. **Title** — a short, identifying name for the source material.
2. **Origin** — the provider, author, or firsthand context the material comes from.
3. **Source format** — what kind of material this is (document, dataset, recording, interview,
   firsthand context, or similar).
4. **Date or timeframe** — when the material was produced or observed, when known.
5. **Access conditions** — how the material can be accessed or re-verified, and by whom.
6. **Scope** — what this Source does and does not cover.
7. **Verification limits** — what cannot be independently confirmed from this Source alone.
8. **Creating Work Item** — link to the Work Item that created this record.

## Notes

A Source is not automatically an approved brand claim. Preserve the distinction between accessible
source material, attributed firsthand context, and an unsupported assertion — that distinction is
a Constraint (see `concepts.md`), not just a formatting convention here.
