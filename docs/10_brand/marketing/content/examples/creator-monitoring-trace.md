---
class: "100"
collection: content
type: example
status: active
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - operations
related:
  - ../concepts.md
  - ../_patterns/creator.md
  - ../_patterns/creator-channel.md
  - ../../../channels/README.md
sources:
  - ../../../ONTOLOGY.md
---

# Illustrative creator monitoring trace

> **Simulation only.** This trace validates the Creator and Creator Channel contracts. It does not assert a real Creator, Creator Channel, Publication, Review, or Motif. Nothing here may be promoted without the appropriate Workflow and evidence.

## Subject

An illustrative competitor-and-inspiration account being onboarded into Content's creator-monitoring model: a fictional Creator, "Acme Fictional Fitness Co.", and one Creator Channel it holds on Instagram. This is the seed of a worked example that later slices in this parent extend — capturing a Publication observed from this Creator Channel, then Reviews of that Publication, then a Motif drawn from repeated observation.

## Happy path

| Illustrative Work Item | Workflow | Stage transition | Output |
| --- | --- | --- | --- |
| `WI-20260828-add-creator-acme-fictional-fitness-co` | Add Creator | Capture → Validate | Illustrative Creator `content.creator.acme-fictional-fitness-co`: Creator Type `Brand`, Creator Relationships `Competitor` and `Inspiration`. |
| `WI-20260828-add-creator-channel-acme-fictional-fitness-co-instagram` | Add Creator Channel | Capture → Validate | Illustrative Creator Channel `content.creator-channel.acme-fictional-fitness-co-instagram` belonging to the Creator above, referencing the existing Instagram `channels.channel` value. |

"Add Creator" and "Add Creator Channel" above are illustrative labels for a manual registry addition, not named Workflow documents — Creator and Creator Channel instances are added directly to the registry rather than through a dedicated Workflow contract in this pass. Every later row in this table names a real `workflows/*.md` contract.

This table is the seed of a worked example that later slices extend — a captured Publication, its Reviews, and a derived Motif each add a row here rather than restructuring the table.

## Illustrative records

### Creator

- `id`: `content.creator.acme-fictional-fitness-co`
- `name`: Acme Fictional Fitness Co.
- `creator_type`: Brand
- `relationships`: Competitor, Inspiration — demonstrating that Creator Relationship is multi-valued
- `niches`: Home Gym Equipment, Beginner Strength Training
- `notes`: Illustrative only, invented for contract validation; not a real account or brand.
- `creating_work_item`: `WI-20260828-add-creator-acme-fictional-fitness-co`

### Creator Channel

- `id`: `content.creator-channel.acme-fictional-fitness-co-instagram`
- `creator`: `content.creator.acme-fictional-fitness-co`
- `channel`: Instagram (`channels.channel`, per [Channels](../../../channels/README.md))
- `handle`: @acmefictionalfitnessco
- `url`: https://instagram.com/acmefictionalfitnessco (illustrative, not a real destination)
- `creating_work_item`: `WI-20260828-add-creator-channel-acme-fictional-fitness-co-instagram`

## Validation scenarios

- A Creator with no Creator Relationship value fails validation.
- A Creator Channel that restates a platform type instead of referencing `channels.channel` fails validation.
- Two Creator Relationship values on the same Creator (Competitor and Inspiration) are valid — Creator Relationship is multi-valued.
- A Creator Channel without a `creator` link, or with more than one, fails validation — cardinality is exactly 1.
