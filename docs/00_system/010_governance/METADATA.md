---
class: "000"
collection: governance
type: standard
status: active
owner: Daniel Hunt
updated: 2026-07-28
---

# Metadata standard

New Project OS records use YAML frontmatter with: `class`, `collection`, `type`, `status`, `owner`, `created`, `updated`, `facets`, `related`, and `sources`. Dates use ISO-8601. `status` is mutable and must be represented in metadata.

Allowed status values are `draft`, `active`, `blocked`, `superseded`, and `archived`. Existing documents predate this standard and retain their canonical placement until they are materially revised; their absence of frontmatter is not evidence that they are non-canonical.

Each record must distinguish verified evidence, interpretation, assumptions, recommendations, and decisions. Use repository-relative links for `related` and `sources`.
