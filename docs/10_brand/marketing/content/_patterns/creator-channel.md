---
id: content.pattern.creator-channel
kind: pattern
domain: content
pattern_for: content.creator-channel
status: active
version: 1
class: "10"
collection: content
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - marketing
related:
  - ../creator-channels/README.md
  - ../concepts.md
  - ../../../channels/README.md
sources:
  - ../../../ONTOLOGY.md
---

# Pattern: Creator Channel

What a `content.creator-channel` instance document (stored under `creator-channels/`) must
contain. See [`concepts.md`](../concepts.md#creator-channel) for the Creator Channel entity
contract this pattern instantiates.

## Required body sections

1. **Creator** — link to the owning `content.creator` record.
2. **Channel** — the `channels.channel` platform type this account is on (reference the existing
   [Channels](../../../channels/README.md) registry; do not restate what the platform is).
3. **Handle** — the account handle or username on that platform, when known (optional).
4. **URL** — the canonical URL for this account.
5. **Creating Work Item** — link to the Work Item that created this record.

## Notes

"Creator Channel" is named to avoid colliding with `channels.channel`, which means the platform
type (for example, Instagram) — a different granularity than one Creator's specific account on
that platform. Do not duplicate the platform-type registry Channels already owns.
