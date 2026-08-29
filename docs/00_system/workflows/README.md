---
id: ops.workflows
kind: note
domain: ops
status: active
version: 1
class: "00"
collection: governance
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - ../domain.md
  - ../concepts.md
  - ../020_agents/WORKFLOWS.md
  - ../010_governance/DOMAIN_PROTOCOL.md
---

# Workflows

Reusable operations on the `ops` domain model (see [`domain.md`](../domain.md) and
[`concepts.md`](../concepts.md)). Store executions of these against real subjects as Tracker Items
and, where warranted, Records — not as new files under this directory.

Every Workflow here carries a `contract:` block (subject, entry/exit stage, preconditions,
inputs, what it creates or updates, validation evidence, and next/failure paths) per
[`DOMAIN_PROTOCOL.md`](../010_governance/DOMAIN_PROTOCOL.md) §11, plus the human-readable
`Purpose`, `Inputs`, `Preconditions`, `Procedure`, `Outputs`, `Patterns`, `Verification`, and
`Exceptions` sections. A workflow consumes the concepts and patterns defined elsewhere; it does
not redefine an entity or silently extend a controlled vocabulary.

- [Maintain Record](maintain-record.md) — the default Orient → Classify → Work → Verify loop for
  any internal task: classify the work, do it, and leave an accurate Tracker Item and (where
  warranted) Record behind.
- [Create Domain](create-domain.md) — the root-level procedure for standing up a new
  protocol-conformant domain from a name and an intent. This is the workflow to run against each
  of the seven remaining thin Brand contexts (Identity, Strategy, Audience, Offers, Assets,
  Channels, Analytics, Relationships) once one has enough material to justify full modeling.

[Maintain Record](maintain-record.md) is the everyday loop; [Create Domain](create-domain.md) is
what you reach for when a Maintain Record task concludes that the subject deserves its own
modeled domain rather than another Tracker Item and Record.
