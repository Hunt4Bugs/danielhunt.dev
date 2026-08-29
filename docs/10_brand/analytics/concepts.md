---
id: analytics.concepts
kind: concept-registry
domain: analytics
status: active
version: 1
class: "10"
collection: analytics
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - README.md
  - domain.md
  - measurements/README.md
  - insights/README.md
sources:
  - ../ONTOLOGY.md
  - measurement-plan.md
---

# Analytics concepts

Canonical concept registry for the `analytics` domain (see [`domain.md`](domain.md)). Each
Concept's document shape lives in [`_patterns/`](_patterns/) (`measurement.md`, `insight.md`)
rather than in the record type's own `README.md`, which is a routing document only — the same
convention `content` uses.

## Measurement
**ID:** `analytics.measurement`

A dated observed metric for one Publication on one Channel.

### Relationships
- attached to `content.publication`
- informs `analytics.insight`
- created by `content.work-item`

### Constraints
- A Measurement is evidence, not an explanation or strategic instruction.
- Simulated values are permitted only in explicitly illustrative examples, never in this record
  collection.
- Compare Measurements only when Metric Name, unit, Format, Channel, and observation window are
  meaningfully compatible; missing platform data remains unknown rather than recorded as zero.
- Use cumulative observations at approximately 24 hours, 7 days, and 30 days after publication
  when the Channel exposes the metric, per [`measurement-plan.md`](measurement-plan.md).

### Entity contract
```yaml
entity: analytics.measurement
fields:
  - name: publication
    type: ref(content.publication)
    required: true
    cardinality: 1
  - name: channel
    type: ref(channels.channel)
    required: true
    cardinality: 1
  - name: metric_name
    type: taxonomy(Metric Name)
    required: true
    cardinality: 1
  - name: value
    type: text
    required: true
    cardinality: 1
  - name: unit
    type: text
    required: true
    cardinality: 1
  - name: observation_time
    type: date
    required: true
    cardinality: 1
  - name: period_start
    type: date
    required: true
    cardinality: 1
  - name: period_end
    type: date
    required: true
    cardinality: 1
  - name: collection_method
    type: text
    required: true
    cardinality: 1
  - name: verification_limits
    type: text
    required: true
    cardinality: 1
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1
```

## Insight
**ID:** `analytics.insight`

An interpretation of one or more Measurements that creates or revises Knowledge.

### Relationships
- interprets `analytics.measurement` (1..*)
- creates or revises `content.knowledge`
- may recommend a Strategy review (never changes Strategy directly)
- created by `content.work-item`

### Constraints
- Must separate observed Measurement values from explanations.
- Must record limitations and plausible competing explanations.
- Must not infer causation from one Publication, and must not compare unlike Formats, Channels, or
  observation windows as though equivalent.
- May recommend later work or a Strategy review; may not silently change Strategy, taxonomy, or
  the controlling editorial plan.

### Entity contract
```yaml
entity: analytics.insight
fields:
  - name: measurements
    type: ref(analytics.measurement)
    required: true
    cardinality: 1..*
  - name: interpretation
    type: text
    required: true
    cardinality: 1
  - name: limitations
    type: text
    required: true
    cardinality: 1
  - name: competing_explanations
    type: text
    required: false
    cardinality: 0..*
  - name: knowledge_created_or_revised
    type: ref(content.knowledge)
    required: false
    cardinality: 0..*
  - name: strategy_recommendation
    type: text
    required: false
    cardinality: 0..1
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1
```

## Owned vocabularies

`analytics` owns one controlled vocabulary (§13.3 — extend only by governed edit here, never
silently from a workflow or skill):

- **Metric Name** ([`ONTOLOGY.md`](../ONTOLOGY.md) Supporting taxonomy, applied to Measurement) —
  Impressions, Views, Watch Time, Completion Rate, Likes, Comments, Saves, Shares, Clicks.
