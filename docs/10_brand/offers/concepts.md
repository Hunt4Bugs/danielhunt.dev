---
id: offers.concepts
kind: concept-registry
domain: offers
status: active
version: 1
class: "10"
collection: offers
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - README.md
  - domain.md
sources:
  - ../specs/2026-05-28-brand-refinement-design.md
---

# Offers concepts

Canonical concept registry for the `offers` domain (see [`domain.md`](domain.md)).

## Service Offer
**ID:** `offers.service-offer`

A public-facing service the commercial Services page can credibly present.

### Relationships
- classified by the internal service taxonomy (Sales Systems, Marketing Systems, Operations
  Systems, Custom Software)
- presented to `audience.segment` (`SERVICES`)

### Constraints
- Public copy uses the concrete public offer name, never the internal service-taxonomy category
  name.
- Each Service Offer uses one plain-language description of what is connected or produced.

### Persistence

Persisted as a list in [`README.md`](README.md#current-service-offers), not as individual
documents — domain-defined persistence (§14). No entity contract is defined per §10.

## Product Offer
**ID:** `offers.product-offer`

A Brand-adjacent product the personal brand indirectly supports as a credibility moat, not a
direct go-to-market motion.

### Relationships
- may be referenced by `marketing.campaign` where relevant

### Constraints
- Not interchangeable with a Service Offer.
- The personal brand remains an indirect credibility moat for a Product Offer, not its GTM
  motion.

### Persistence

Persisted as prose in [`README.md`](README.md#product-offers) — currently one instance (Datavial).
No entity contract is defined per §10; a contract is added if a second Product Offer with distinct
tracked fields emerges.

## No _patterns/ or workflows/

Service Offer and Product Offer instances are a list and prose in README.md, not individual
documents, so no local `_patterns/` is warranted (§14.1). No repeatable multi-step operation on
Offers has recurred enough yet to justify a Workflow.
