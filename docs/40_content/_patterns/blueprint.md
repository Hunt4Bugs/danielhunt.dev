---
id: content.pattern.blueprint
kind: pattern
domain: content
pattern_for: content.blueprint
status: active
version: 1
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - strategy
  - audience
related:
  - ../blueprints/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Pattern: Blueprint

What a `content.blueprint` instance document (stored under `blueprints/`) must contain. See
[`concepts.md`](../concepts.md#blueprint) for the Blueprint entity contract this pattern
instantiates.

## Required body sections

1. **Primary Topic** — the one Topic this Blueprint communicates.
2. **Objective and audience** — the objective and the primary Audience Segment.
3. **Angle and audience promise** — the angle taken and the promise made to the audience.
4. **Classification** — Content Pattern, primary Content Purpose (plus any supporting purposes),
   and Narrative Structure.
5. **Hook selections** — Visual Hook Type and Verbal Hook Type, when the Blueprint targets
   short-form video. Mark explicitly when hook selection is still pending
   [Generate Hook Options](../workflows/generate-hook-options.md).
6. **CTA** — the call to action.
7. **Proof** — linked Sources for every factual claim, statistic, quotation, or outcome.
8. **Constraints** — any planning constraints (production, editorial, or otherwise).
9. **Related Scripts and Publications** — links to Scripts and Publications this Blueprint has
   produced (may be empty at creation).
10. **Creating Work Item** — link to the Work Item that created this Blueprint.

## Notes

A short-form Blueprint is script-ready only once section 5's hook selection is complete — that
readiness condition is a Constraint (see `concepts.md`), restated here only as a reminder of where
it shows up in the document. Reusable production scaffolding is a Template (an Asset), never
folded into a Blueprint document.
