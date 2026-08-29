---
id: marketing.concepts
kind: concept-registry
domain: marketing
status: active
version: 1
class: "10"
collection: marketing
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - README.md
  - domain.md
sources:
  - ../ONTOLOGY.md
---

# Marketing concepts

Canonical concept registry for the `marketing` domain (see [`domain.md`](domain.md)).

## Campaign
**ID:** `marketing.campaign`

Optional, time-bounded coordination around a goal. Not used for ordinary recurring publishing.

### Relationships
- may group `content.series` (optional, many-to-many)

### Constraints
- A Campaign is not necessarily a Series and does not replace Series or Publication identity.
- Do not create a Campaign for ordinary recurring publishing — only genuinely time-bounded,
  goal-specific coordination.

### Persistence

No Campaign instances exist yet (v1). When the first one is created, this entry gains an entity
contract and, if instances recur, a `_patterns/campaign.md` — per §14.1, a Pattern is added when
instances actually start being created, not merely because the Concept exists.

## No _patterns/ or workflows/

No Campaign instances exist yet, so no local `_patterns/` is warranted (§14.1). No repeatable
multi-step operation on Marketing itself has recurred enough yet to justify a Workflow;
Marketing's scope is applied through Content's own workflows instead.
