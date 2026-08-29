---
id: analytics.readme
kind: note
domain: analytics
class: "10"
collection: analytics
type: analytics
status: active
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-29
facets:
  - content
related:
  - domain.md
  - concepts.md
  - measurements/README.md
  - insights/README.md
  - measurement-plan.md
sources:
  - ../ONTOLOGY.md
---

# Analytics

Analytics turns observed results into learning without allowing short-term engagement to replace strategy. [`domain.md`](domain.md) states this domain's boundary and [`concepts.md`](concepts.md) is its concept registry (Measurement, Insight) with entity contracts, per the [Domain Documentation Protocol](../../00_system/010_governance/DOMAIN_PROTOCOL.md).

## Core concepts

- **Measurement:** a dated value for a Publication on a Channel, such as impressions, views, watch time, completion rate, likes, comments, saves, shares, or clicks.
- **Insight:** an interpretation of one or more Measurements.
- **Knowledge feedback:** an Insight may create or revise Knowledge, which can inform later Topics.

Measurements are evidence, not direction by themselves. The Build/Offline toggle and strategic Themes govern editorial choices; an overperforming item is informative data, not a commitment to repeat that subject.

Store canonical [Measurement records](measurements/README.md) and [Insight records](insights/README.md) in their respective collections. Evaluation windows, operating success criteria, and review rules live in the [measurement plan](measurement-plan.md).

An Insight may recommend a strategic review, but only an explicit update to [Strategy](../strategy/README.md) changes Themes, positioning, or content weighting.
