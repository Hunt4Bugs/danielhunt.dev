---
id: protocol.pattern.workflow
kind: pattern
domain: protocol
pattern_for: protocol.workflow-doc
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - README.md
  - ../00_system/010_governance/DOMAIN_PROTOCOL.md
---

# Pattern: `workflows/<name>.md`

The centerpiece contract (DOMAIN_PROTOCOL.md §11). A workflow document carries a structured
machine contract in frontmatter and a human-readable body. Neither substitutes for the other.

## Frontmatter

```yaml
id: <domain>.workflow.<name>
kind: workflow
domain: <domain-id>
status: draft | active | blocked | superseded | archived
version: 1
contract:
  subject_type: <domain>.<concept>     # what it operates on
  entry_stage: <Stage>                 # required current_stage of the Work Item
  exit_stage: <Stage>                  # valid current_stage on success
  requires:                            # preconditions — what must already exist
    - id: <domain>.<concept>
      state: <work_state>
      optional: true | false
  inputs:                              # data gathered before transforming
    - name: <field-name>
      type: ref(<domain>.<concept>) | taxonomy(<vocabulary>) | text | date | url | list
      required: true | false
  creates:
    - type: <domain>.<concept>
      via_pattern: _patterns/<concept>.md
  updates:
    - type: <domain>.<concept>
  validation:                          # evidence required to pass
    - <named check>
  next:                                 # valid follow-on workflows
    - <domain>.workflow.<name>
  failure_paths:                        # valid return routes
    - <domain>.workflow.<name>
```

## Required body sections

`Purpose`, `Inputs`, `Preconditions`, `Procedure`, `Outputs`, `Patterns` (which `_patterns/*.md`
files this workflow's `Procedure` uses), `Verification`, `Exceptions`.

## Rules

- The `contract:` block is what a future skill or `protocol-lint` checks mechanically; the body is
  what a human or an agent actually follows step by step. Keep them consistent — if the
  `Procedure` changes what the workflow creates or requires, update `contract:` in the same edit.
- `requires` and `inputs` are gathered *before* `Procedure` starts — a workflow does not discover
  a missing precondition midway through executing.
- `next` and `failure_paths` must resolve to other workflow files that actually exist in this
  domain (or an explicitly named neighboring domain). Don't reference an aspirational workflow.
