---
id: ops.readme
kind: note
domain: ops
class: "00"
collection: governance
type: domain-reference
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - domain.md
  - concepts.md
  - workflows/README.md
  - 010_governance/LIBRARY_MAP.md
  - 020_agents/AGENTS.md
sources:
  - 010_governance/DOMAIN_PROTOCOL.md
---

# ops

`ops` is this repository's own project-operations domain: how work on this repository is
tracked, triaged, guided, and recorded. [`domain.md`](domain.md) states its boundary and
[`concepts.md`](concepts.md) is its concept registry with entity contracts, per the
[Domain Documentation Protocol](010_governance/DOMAIN_PROTOCOL.md).

## Records

- [Tracker](030_operations/TRACKER.md): the internal planning tracker — one row per Tracker Item.
- [Triage](030_operations/TRIAGE.md): the routing rules that classify incoming work into a lane
  with a required response.
- [Records](090_records/): dated, evidence-based decisions, audits, setups, and notes. Never
  rewritten after the fact — a correction is a new dated Record.
- [Agent guidance](020_agents/AGENTS.md) and its nested documents (`AUTONOMY.md`,
  `PLUGIN_POLICY.md`, `TEMPLATES.md`, `VALIDATION.md`, `WORKFLOWS.md`): what an agent may do in
  this repository and how.

## Operations

- [Workflows](workflows/README.md) define reusable operations against this model — the default
  [Maintain Record](workflows/maintain-record.md) loop and [Create Domain](workflows/create-domain.md).
- [`010_governance/LIBRARY_MAP.md`](010_governance/LIBRARY_MAP.md) resolves physical placement
  (class and collection) across the whole repository, including root-level domains that have
  outgrown a single class.
- [`010_governance/METADATA.md`](010_governance/METADATA.md) is superseded by
  [`../_conventions/documentation.md`](../_conventions/documentation.md) as the repository-wide
  frontmatter standard; it remains for historical reference.

There is no local `_patterns/` directory: `ops`'s one concept whose instances need a predictable
shape — Record — already has exactly one canonical template in
[`020_agents/TEMPLATES.md`](020_agents/TEMPLATES.md), and `ops.workflow.maintain-record`'s
`via_pattern` points there directly rather than forking a second copy under `_patterns/`. Tracker
Item and Triage Item are persisted as table rows inline in `TRACKER.md` / `TRIAGE.md`, not as
separate instance documents, per [`DOMAIN_PROTOCOL.md`](010_governance/DOMAIN_PROTOCOL.md) §14 on
domain-defined persistence.
