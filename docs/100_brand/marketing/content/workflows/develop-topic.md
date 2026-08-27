---
class: "100"
collection: content
type: workflow
status: active
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-27
facets:
  - operations
related:
  - README.md
  - ../work-items/README.md
sources:
  - ../../../ONTOLOGY.md
---

# Develop Topic

## Work Item contract

- **Primary subject:** the principal Knowledge record from which the Topic is developed.
- **Entry stage:** Validate.
- **Successful exit stage:** Plan.
- **Creates:** one Topic record when no materially equivalent Topic exists.
- **Updates:** an existing Topic when the proposed subject is materially duplicative.
- **Required predecessors:** completed [Capture Knowledge](capture-knowledge.md) Work Items for the supporting Knowledge.
- **Possible next workflows:** [Develop Blueprint](develop-blueprint.md).
- **Validation evidence:** Topic premise, exact Theme and Audience Segment values, Topic Mode, strategic fit, evidence boundary, duplicate check, and output link recorded in the Work Item.
- **Failure and return paths:** return to Capture when support is insufficient; complete without a Topic when the subject is off-strategy or cannot be generalized safely.

## Required references

- [Brand ontology v1](../../../ONTOLOGY.md): Topic, Topic Mode, Knowledge relationships, and the boundary between Topic, Blueprint, and Publication.
- [Topic records](../topics/README.md): reusable-subject and relationship requirements.
- [Strategy](../../../strategy/README.md): primary Themes, positioning, and editorial constraints.
- [Audience](../../../audience/README.md): Audience Segments, needs, problems, and credibility boundaries.
- [Identity](../../../identity/README.md): voice, privacy, scars-not-wounds, and observation-over-preaching boundaries.

## Taxonomy contract

- **Reads:** Topic Mode, the canonical Themes, Audience Segments, and the existing Topic inventory.
- **Writes:** one existing Topic Mode, one primary Theme, and the relevant Audience Segment on the resulting Topic record.
- **Restriction:** use only ontology-defined Topic Modes, Strategy-owned Themes, and Audience-owned Audience Segments. Route a missing controlled value through [Propose Taxonomy Addition](propose-taxonomy-addition.md).

## Input

One or more related Knowledge records with their supporting Sources and evidence boundaries.

## Procedure

1. Identify the smallest reusable subject supported by the Knowledge. Keep channel choice, hook, CTA, publication copy, and treatment decisions out of the Topic.
2. Check the existing Topic inventory. Extend an existing Topic when the proposed subject is materially duplicative.
3. Select one primary Theme and one Topic Mode: Build, Offline, or Bridge.
4. Identify the relevant Audience Segment and the need, problem, curiosity, or tension the Topic addresses.
5. State the Topic premise, why it fits the Brand strategy, and the credibility boundary established by its supporting Knowledge and Sources.
6. Link all supporting Knowledge and retain meaningful open questions that a later Blueprint must not treat as resolved.

## Output

One reusable Topic record with a primary Theme, Topic Mode, relevant Audience Segment name and code, premise, strategic fit, supporting Knowledge, credibility boundary, open questions, and a link to the creating Work Item. A ready Topic may proceed to [Develop Blueprint](develop-blueprint.md).

## Stop conditions

Stop and return to [Capture Knowledge](capture-knowledge.md) when support is insufficient. Stop without creating a Topic when the subject is outside the Brand's strategic constraints, depends on private or customer-sensitive material that cannot be safely generalized, or would publish a wound rather than a scar.
