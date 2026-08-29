---
id: protocol.pattern.decision
kind: pattern
domain: protocol
pattern_for: protocol.decision
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - README.md
  - ../00_system/010_governance/DOMAIN_PROTOCOL.md
---

# Pattern: `decisions/<name>.md`

A Decision is an ordinary Concept with a Pattern (§3.7) — not a structural primitive. It records a
past choice whose rationale matters, so conventions don't calcify into unexplained folklore.

## Frontmatter

```yaml
id: <domain>.decision.<name>
kind: decision
domain: <domain-id>
status: active | superseded
version: 1
created: YYYY-MM-DD
```

## Required body sections

- **Context** — the situation that forced a choice. What problem, constraint, or conflicting goal
  made the default approach insufficient?
- **Decision** — the choice, stated plainly in one or two sentences.
- **Rationale** — *why* this option over the alternatives. This is the part a Decision exists to
  preserve; don't let it decay into "because we said so."
- **Alternatives considered** — what else was on the table and why it lost, briefly.
- **Consequences** — what this commits the domain to, and what it forecloses.

A superseded Decision is not deleted — set `status: superseded` and add `related:` pointing to the
Decision that replaced it. Git history is not a substitute for this: the point of a Decision
record is that its rationale is discoverable without archaeology.
