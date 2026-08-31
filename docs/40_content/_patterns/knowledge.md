---
id: content.pattern.knowledge
kind: pattern
domain: content
pattern_for: content.knowledge
status: active
version: 1
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - analytics
related:
  - ../knowledge/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Pattern: Knowledge

What a `content.knowledge` instance document (stored under `knowledge/`) must contain. See
[`concepts.md`](../concepts.md#knowledge) for the Knowledge entity contract this pattern
instantiates.

## Required body sections

1. **Knowledge Kind** — the one classification (Insight, Observation, Experience, Research,
   Opinion, Idea, Question, Lesson, Process, Framework, or Evidence).
2. **Reusable synthesis** — the smallest reusable synthesis, kept distinct from a Topic, Blueprint,
   claim, or publication draft.
3. **Evidence boundary** — what must not be stated as established fact; the separation of verified
   evidence, firsthand account, interpretation, and unknowns.
4. **Supporting Sources** — links to every Source this Knowledge draws on.
5. **Related Topics and Insights** — links to Topics informed by this Knowledge and any Insights
   that created or revised it (may be empty at creation).
6. **Creating or revising Work Item** — link to the Work Item that created or last revised this
   record.

## Notes

Do not store raw assets in a Knowledge document — link to the Asset instead. The Source record,
not Knowledge, preserves provenance.
