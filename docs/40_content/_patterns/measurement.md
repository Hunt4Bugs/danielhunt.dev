---
id: content.pattern.measurement
kind: pattern
domain: content
pattern_for: content.measurement
status: active
version: 1
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-09-07
related:
  - ../measurements/README.md
  - ../concepts.md
sources:
  - ../../00_system/010_governance/ONTOLOGY.md
---

# Pattern: Measurement

What a `content.measurement` instance document (stored under `measurements/`) must contain. See
[`concepts.md`](../concepts.md#measurement) for the entity contract this pattern instantiates.

## Required frontmatter

```yaml
id: content.measurement.<publication-slug>-<observation-window>
kind: note
domain: content
status: active
owner: Daniel Hunt
created: YYYY-MM-DD
updated: YYYY-MM-DD
publication: ../publications/<publication>.md
channel: <channel>
metric_name: <Metric Name>
creating_work_item: WI-YYYYMMDD-record-measurements-<subject>
```

## Required body sections

1. **Value and unit** — the observed value and its unit.
2. **Observation window** — observation time, period start, period end.
3. **Collection method** — how the value was obtained (platform analytics export, manual count,
   and so on).
4. **Verification limits** — what this Measurement cannot verify (for example, platform-reported
   figures that cannot be independently audited).
