---
id: content.pattern.insight
kind: pattern
domain: content
pattern_for: content.insight
status: active
version: 1
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-09-07
related:
  - ../insights/README.md
  - ../concepts.md
sources:
  - ../../00_system/010_governance/ONTOLOGY.md
---

# Pattern: Insight

What a `content.insight` instance document (stored under `insights/`) must contain. See
[`concepts.md`](../concepts.md#insight) for the entity contract this pattern instantiates.

## Required frontmatter

```yaml
id: content.insight.<subject-slug>
kind: note
domain: content
status: active
owner: Daniel Hunt
created: YYYY-MM-DD
updated: YYYY-MM-DD
measurements: []
creating_work_item: WI-YYYYMMDD-derive-insight-<subject>
```

## Required body sections

1. **Interpretation** — the reading of the linked Measurements, kept distinguishable from the raw
   values themselves.
2. **Limitations and competing explanations** — what this interpretation cannot rule out.
3. **Knowledge created or revised** — links to any `content.knowledge` this Insight produced or
   updated.
4. **Positioning recommendation (optional)** — a recommendation to revisit Theme priorities or
   positioning in [`themes.md`](../themes.md), never a direct edit to Theme or the controlling
   editorial plan from within the Insight itself.
