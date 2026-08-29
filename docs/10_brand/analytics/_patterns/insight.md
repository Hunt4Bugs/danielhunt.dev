---
id: analytics.pattern.insight
kind: pattern
domain: analytics
pattern_for: analytics.insight
status: active
version: 1
class: "10"
collection: analytics
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - ../insights/README.md
  - ../concepts.md
sources:
  - ../../ONTOLOGY.md
---

# Pattern: Insight

What an `analytics.insight` instance document (stored under `insights/`) must contain. See
[`concepts.md`](../concepts.md#insight) for the entity contract this pattern instantiates.

## Required frontmatter

```yaml
id: analytics.insight.<subject-slug>
kind: note
domain: analytics
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
4. **Strategy recommendation (optional)** — a recommendation for Strategy to review, never a
   direct edit to Strategy, Theme, or the controlling editorial plan.
