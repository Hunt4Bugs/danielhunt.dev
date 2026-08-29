---
id: assets.concepts
kind: concept-registry
domain: assets
status: active
version: 1
class: "10"
collection: assets
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - README.md
  - domain.md
sources:
  - ../ONTOLOGY.md
---

# Assets concepts

Canonical concept registry for the `assets` domain (see [`domain.md`](domain.md)). Script
(`content.script`) and Script Template (`content.script-template`) are Asset subtypes but are
defined in [`content/concepts.md`](../../content/concepts.md), not here — see
[`domain.md`](domain.md)'s Excludes.

## Asset
**ID:** `assets.asset`

A reusable media, design, brand, or knowledge resource — the general (non-Script, non-Template)
Asset subtypes.

### Relationships
- used by `content.publication` (`related_assets`)
- resolves through `taxonomy(Production Dependency State)` when named as a production requirement

### Constraints
- Each Asset carries exactly one `asset_type` from the four general subtypes: Media, Design,
  Brand, Knowledge Asset.
- Raw asset files are not stored inside a Knowledge record; a Knowledge record links to the Asset
  instead (constraint mirrored from `content.knowledge`).

### Entity contract
```yaml
entity: assets.asset
fields:
  - name: asset_type
    type: taxonomy(Asset Type)
    required: true
    cardinality: 1
  - name: title
    type: text
    required: true
    cardinality: 1
  - name: media_type
    type: taxonomy(Media Type)
    required: false   # applies when asset_type is Media
    cardinality: 0..1
  - name: source_or_location
    type: text
    required: true
    cardinality: 1
  - name: licensing_or_access_constraint
    type: text
    required: false
    cardinality: 0..1
```

## Template
**ID:** `assets.template`

Reusable fill-in-the-blank scaffolding for Blueprint, post, carousel, video, and prompt templates
— not itself a content record and not a substitute for evidence or editorial judgment. Script
Template is a related but separately owned concept (`content.script-template`, see
[`domain.md`](domain.md)'s Excludes).

### Relationships
- scaffolds the domain record it targets (e.g. a Blueprint Template scaffolds `content.blueprint`)
- supports `taxonomy(Content Pattern)`
- follows `taxonomy(Narrative Structure)`
- targets `taxonomy(Publication Format)`

### Constraints
- A Template must name its supported Content Pattern, Narrative Structure, and Publication
  Format.
- A Template does not contain publication-specific copy and does not replace the record it
  scaffolds.

### Entity contract
```yaml
entity: assets.template
fields:
  - name: template_kind
    type: taxonomy(Asset Type)   # the Template-family values: Template (Blueprint, post,
                                  # carousel, video, prompt)
    required: true
    cardinality: 1
  - name: supported_content_pattern
    type: taxonomy(Content Pattern)
    required: true
    cardinality: 1..*
  - name: supported_narrative_structure
    type: taxonomy(Narrative Structure)
    required: true
    cardinality: 1..*
  - name: target_publication_format
    type: taxonomy(Publication Format)
    required: true
    cardinality: 1..*
```

## Owned vocabularies

`assets` owns two controlled vocabularies (§13.3 — extend only by governed edit here, never
silently from a workflow or skill):

- **Asset Type** ([`ONTOLOGY.md`](../ONTOLOGY.md) Supporting taxonomy) — Media, Design, Brand,
  Knowledge Asset, Script, Template, Script Template. `assets.asset` and `assets.template` use the
  general values; Script and Script Template name Content-owned concepts hosted here.
- **Media Type** ([`ONTOLOGY.md`](../ONTOLOGY.md) Supporting taxonomy, applied to Media Asset) —
  Image, Video, Audio, Screenshot, Recording, B-roll.

## No _patterns/ or workflows/ in this pass

No local `_patterns/` directory is added in this pass: the one real recurring instance kind
(Blueprint Template) has exactly one instance so far, not yet a proven repeating shape, and no
workflow currently produces one. Script and Script Template already have their document shape
governed by `content/concepts.md` (they are Content-owned concepts hosted here) rather than a
local pattern. No repeatable multi-step operation on Assets itself has recurred enough yet to
justify a Workflow.
