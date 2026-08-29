---
class: "10"
collection: brand
type: domain-map
status: active
owner: Daniel Hunt
updated: 2026-08-26
---

# Brand domain map

`Brand` is the root domain for the personal-brand corpus. This index names the canonical bounded contexts and routes work to the smallest authoritative document.

## Contexts

| Context | Owns | Canonical reference |
| --- | --- | --- |
| Identity | Meaning, voice, principles, public language | [identity](identity/README.md) |
| Strategy | Positioning, goals, themes, differentiation, narrative | [strategy](strategy/README.md) |
| Audience | Segments, needs, problems, and audience relationship | [audience](audience/README.md) |
| Offers | Service and product offers | [offers](offers/README.md) |
| Assets | Reusable media, design, brand assets, and templates | [assets](assets/README.md) |
| Channels | Distribution destinations, roles, and constraints | [channels](channels/README.md) |
| Marketing | Campaigns, distribution, growth, funnel, and Content | [marketing](marketing/README.md) |
| Analytics | Measurements, insights, and learning feedback | [analytics](analytics/README.md) |
| Relationships | Future people and organization boundary | [relationships](relationships/README.md) |

The v1 entity model, terminology, and relationship rules live in [ONTOLOGY.md](ONTOLOGY.md). Historical plans, specifications, and the [changelog](CHANGELOG.md) remain dated evidence rather than active sources of truth.

## Source ownership

When a decision spans contexts, update the context that owns the decision and link to it from the related contexts. Do not duplicate operational rules across documents. Identity and visual direction remain mandatory context for public brand-shaped work; implementation details remain in [CLAUDE.md](../../CLAUDE.md).
