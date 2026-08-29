---
id: content.pattern.creator
kind: pattern
domain: content
pattern_for: content.creator
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - marketing
related:
  - ../creators/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Pattern: Creator

What a `content.creator` instance document (stored under `creators/`) must contain. See
[`concepts.md`](../concepts.md#creator) for the Creator entity contract this pattern instantiates.

## Required body sections

1. **Name** — the Creator's name.
2. **Creator Type** — the one classification of what this Creator is (Person, Company, Brand,
   Organization, or Other).
3. **Relationships** — one or more Creator Relationship classifications (Competitor, Inspiration,
   Peer, Reference) describing our stance toward this Creator; a Creator may hold more than one
   simultaneously.
4. **Niches** — free-text list of the subject areas or niches this Creator operates in (optional).
5. **Notes** — free-text observations (optional).
6. **Creator Channels** — links to this Creator's `content.creator-channel` records (may be empty
   at creation).
7. **Creating Work Item** — link to the Work Item that created this record.

## Notes

`creator_type` (what the Creator is) and `relationships` (our stance toward it) must never be
conflated into one field — keep them as separate sections. Niches and notes are free text, not
controlled vocabulary. A Creator is not a general Person or Organization record; it exists only to
support content-intelligence monitoring (see `concepts.md` and [`10_brand/ONTOLOGY.md`](../../10_brand/ONTOLOGY.md)'s
V1 boundary).
