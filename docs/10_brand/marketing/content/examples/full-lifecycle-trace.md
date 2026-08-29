---
class: "100"
collection: content
type: example
status: active
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-27
facets:
  - operations
  - analytics
related:
  - ../workflows/README.md
  - short-form-stop-hook-payoff.md
sources:
  - ../sources/colin-and-samir-short-form-anatomy.md
  - ../knowledge/short-form-anatomy.md
---

# Illustrative full lifecycle trace

> **Simulation only.** This trace validates contracts and transitions. It does not assert a real Topic, Blueprint, Script, Publication, publish event, Measurement, Insight, or performance result. Nothing here may be promoted without the appropriate Workflow and evidence.

## Subject

Use the illustrative subject from the [short-form Script path](short-form-stop-hook-payoff.md): how repository guidance makes AI-assisted coding changes easier to review. The existing short-form Source and Knowledge support only the communication method, not the illustrative repository claim. A real execution requires separate evidence for that claim.

## Happy path

| Illustrative Work Item | Workflow | Stage transition | Output |
| --- | --- | --- | --- |
| `WI-20260827-capture-knowledge-ai-repository-guidance` | Capture Knowledge | Capture → Validate | Illustrative Knowledge with provenance and an evidence boundary. |
| `WI-20260827-develop-topic-ai-repository-guidance` | Develop Topic | Validate → Plan | Topic using `Systems and Observation`, `Build`, and `Primary Editorial Audience (B2)`. |
| `WI-20260827-develop-blueprint-ai-repository-guidance` | Develop Blueprint | Plan → Draft | Educational Blueprint with a supported promise and short-form structure. |
| `WI-20260827-generate-hook-options-ai-repository-guidance` | Generate Hook Options | Plan → Draft | Close-Up Shot plus Opinion selected; rejected pairs remain in the Work Item. |
| `WI-20260827-generate-script-ai-repository-guidance` | Generate Short-Form Script | Draft → Review | Script for Short-form Video. Each beat has a dependency state. |
| `WI-20260827-validate-script-ai-repository-guidance` | Validate Script | Review → Produce | Script passes format, evidence, Blueprint, hook, and dependency checks without selecting a Channel. |
| `WI-20260827-develop-publication-ai-repository-guidance` | Develop Publication | Draft → Review | Instagram Short-form Video Publication with channel-specific copy and the validated Script. |
| `WI-20260827-validate-publication-ai-repository-guidance` | Validate Publication | Review → Produce | Instagram and Short-form Video compatibility, copy, privacy, evidence, and dependencies pass. |
| `WI-20260827-produce-publication-ai-repository-guidance` | Produce Publication | Produce → Publish | Planned screen capture becomes an Existing Asset and the final expression passes preflight. |
| `WI-20260827-publish-publication-ai-repository-guidance` | Publish Publication | Publish → Measure only after authorization | Dry run stops before external action because this example grants no authorization. |

## Simulated learning continuation

The following rows test downstream contracts only. They assume a hypothetical authorized publication and use no real values.

| Illustrative Work Item | Workflow | Stage transition | Simulated output |
| --- | --- | --- | --- |
| `WI-20260827-record-measurements-ai-repository-guidance` | Record Measurements | Measure → Learn | Separate simulated records for Views and Completion Rate with explicit 7-day period fields. |
| `WI-20260827-derive-insight-ai-repository-guidance` | Derive Insight | Learn → Reuse / Repurpose | A simulated interpretation with limitations and no automatic Strategy change. |
| `WI-20260827-repurpose-publication-ai-repository-guidance` | Repurpose Publication | Reuse / Repurpose → Draft | A derived X Thread when promise, angle, proof, and structure remain valid. |

If the repurposed expression changes the promise or angle, the same workflow creates no Publication and exits to Plan for Develop Blueprint.

## Validation scenarios

- Missing claim evidence returns work to Capture or Validate.
- An undefined taxonomy value creates a Propose Taxonomy Addition Work Item and remains unavailable until approval updates the owning context.
- An Unresolved production dependency prevents Script or Publication validation.
- Instagram plus Thread fails Channel compatibility; Instagram plus Short-form Video passes.
- Script validation does not require a Channel.
- Publish Publication stops at Publish without explicit authorization and leaves durable publication facts empty.
- Measurements remain evidence; the Insight contains interpretation and limitations.
- Repurposing preserves `derives from` and creates a separate Publication.
