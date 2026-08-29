---
id: content.pattern.topic
kind: pattern
domain: content
pattern_for: content.topic
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - strategy
  - audience
related:
  - ../topics/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Pattern: Topic

What a `content.topic` instance document (stored under `topics/`) must contain. See
[`concepts.md`](../concepts.md#topic) for the Topic entity contract this pattern instantiates.

## Required body sections

1. **Premise** — the reusable subject or idea in one or two sentences. Never a post, hook, or CTA.
2. **Classification** — the one primary Theme, one Topic Mode (Build, Offline, or Bridge), and the
   relevant Audience Segment name and code.
3. **Strategic fit** — why this Topic fits the Brand's strategic constraints.
4. **Supporting Knowledge** — links to every Knowledge record this Topic draws on.
5. **Credibility boundary** — what the supporting Knowledge and Sources do and do not establish.
6. **Open questions** — meaningful unknowns a later Blueprint must not treat as resolved.
7. **Related Blueprints** — links to any Blueprints this Topic has produced (may be empty at
   creation).
8. **Creating Work Item** — link to the Work Item that created this Topic.

## Notes

Keep Channel, hook, CTA, treatment, and publication copy out of the Topic document — those belong
to Blueprint or Publication instances. This is a representation convention; the underlying rule
("a Topic must reference at least one supporting Knowledge") is a Constraint and lives in
`concepts.md`, not here.
