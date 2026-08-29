---
id: offers
kind: domain
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
  - concepts.md
  - ../identity/README.md
sources:
  - ../specs/2026-05-28-brand-refinement-design.md
---

# Offers domain

## Purpose

Offers owns the products or services the Brand can credibly introduce or support. It exists as its
own domain, distinct from Identity and Marketing, because an Offer is a concrete
product-or-service commitment — what can actually be delivered — not brand meaning or coordinated
promotional activity.

## Scope

### Includes

- **Service Offer** — a public-facing service the commercial Services page can credibly present
  (Workflow automation, Lead management, Business websites, CRM and tool integrations, Custom
  software builds).
- **Product Offer** — a Brand-adjacent product, currently Datavial.
- The internal service taxonomy (Sales Systems, Marketing Systems, Operations Systems, Custom
  Software) that groups Service Offers for internal organization, distinct from the public offer
  names.

### Excludes

- Public-facing service language and public copy rules — owned by
  [Identity](../identity/README.md) (Service expression section); Offers owns *what* is offered,
  Identity owns *how it is said*.
- The commercial services audience itself — owned by [Audience](../audience/README.md)
  (`SERVICES` segment); Offers references it without owning audience truth.
- Marketing and promotional coordination of an Offer — owned by
  [Marketing](../marketing/README.md); Offers is not interchangeable with Marketing's Campaign
  concept.

## Model

- **Service Offer** — a public-facing service offer with an internal service-taxonomy grouping.
- **Product Offer** — a Brand-adjacent product the personal brand indirectly supports.

Full definitions and relationships live in [`concepts.md`](concepts.md).

## Relationships

- `Service Offer` **is classified by** the internal service taxonomy (Sales Systems, Marketing
  Systems, Operations Systems, Custom Software).
- `Product Offer` **is referenced by** Marketing where relevant, without becoming Datavial's
  direct go-to-market motion.

## Constraints

- Public language for a Service Offer uses the concrete public name, never the internal
  service-taxonomy category name (do not lead a service card with "Sales Systems").
- A Product Offer and a Service Offer are not interchangeable; the personal brand remains an
  indirect credibility moat rather than a Product Offer's direct GTM motion.

## Related Domains

- **[Identity](../identity/README.md)** — owns the public language and copy rules Offers'
  Service Offers are presented through.
- **[Audience](../audience/README.md)** — owns the commercial services audience Service Offers
  are presented to.
- **[Marketing](../marketing/README.md)** — may reference an Offer where relevant without owning
  Offer definitions.

## Examples

- `Workflow automation` (Service Offer, active, Sales Systems / Operations Systems grouping): the
  broadest entry point among the five public offers.
- `Datavial` (Product Offer, active): the flagship Life Sciences product; the personal brand is an
  indirect credibility moat for it, not its GTM motion.
