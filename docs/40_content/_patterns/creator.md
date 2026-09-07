---
id: content.pattern.creator
kind: pattern
domain: content
pattern_for: content.creator
status: active
version: 2
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-09-06
related:
  - ../creators/README.md
  - ../concepts.md
sources:
  - ../../00_system/010_governance/ONTOLOGY.md
---

# Pattern: Creator

What a `content.creator` instance document (stored under `creators/`) must contain. See
[`concepts.md`](../concepts.md#creator) for the Creator entity contract this pattern instantiates.

## Required body sections

1. **Name** — the Creator's name.
2. **Creator Type** — the one classification of what this Creator is (Person, Company, Brand,
   Organization, or Other).
3. **Relationships** — one or more Creator Relationship classifications (Competitor, Inspiration,
   Peer, Reference, Self) describing our stance toward this Creator; a Creator may hold more than
   one simultaneously.
4. **Niches** — free-text list of the subject areas or niches this Creator operates in (optional).
5. **Notes** — free-text observations (optional).
6. **Creator Channels** — links to this Creator's `content.creator-channel` records (may be empty
   at creation).
7. **Registration Provenance** — link to the Work Item that created this record when one exists;
   otherwise identify the manual addition date and the source evidence.
8. **Identity** (optional; present only when `relationships` includes `Self`, or another record
   genuinely warrants a fuller narrative) — subsections: Thesis, Current professional context,
   Brand Statement, Contrarians, Persona, The Toggle, Public Referral Sentences, Service
   expression, Signature phrases, References we borrow from, Aesthetic tie-break, Guiding
   principles, Brand role, Mission. Absent entirely for an ordinary monitored Creator — do not add
   empty Identity subsections to a record that doesn't need them.

## Notes

`creator_type` (what the Creator is) and `relationships` (our stance toward it) must never be
conflated into one field — keep them as separate sections. Niches and notes are free text, not
controlled vocabulary. Creator covers Daniel Hunt himself (`Self`), an external creator monitored
for competitor, inspiration, peer, or reference intelligence, and a general person or organization
worth recording (see `concepts.md` and [`ONTOLOGY.md`](../../00_system/010_governance/ONTOLOGY.md)'s
V1 boundary). The Identity section (8) is the only body section unique to a `Self`-relationship
record; every other Creator record uses sections 1–7 only.

Direct manual registry additions are permitted. They must preserve their source evidence and
explicitly state that no creation workflow exists, rather than inventing a Work Item reference.
