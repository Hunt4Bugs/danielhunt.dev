---
id: protocol.note.documentation
rdf:type: protocol.note
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
protocol_version: "1.0"
previous_id: protocol.documentation.v0.2
supersedes:
  - ../00_system/010_governance/DOMAIN_PROTOCOL.md
related:
  - README.md
  - domain.md
  - concepts/concept.md
  - ../ROUTER.md
sources:
  - ../00_system/010_governance/DOMAIN_PROTOCOL.md
---

# Domain Documentation Protocol v1.0

A lightweight, domain-driven standard for documentation that humans read and software operates
on. It supersedes v0.2, whose freeze clause is retired.

Its own `id` carries no version. v0.2's id was `protocol.documentation.v0.2`, which made every
version bump an illegal rename under the identifier rule below; the version lives in
`protocol_version` and in `version`, where it belongs. The old id is kept in `previous_id`.

## 1. Purpose

One source of truth, readable two ways. A person reads the prose; `uv run dh` reads the front
matter. Neither is generated from the other, and neither is allowed to drift from it, because
lint checks that the same file satisfies both.

## 2. Reading the vocabulary

> **Colons are theirs. Dots are ours.**
>
> A colon in a key (`rdfs:range`) or a value (`owl:Class`, `xsd:string`) names a term defined by
> the W3C. A dot (`content.creator`) names something defined in this repository. A bare key
> (`store`, `section`) is protocol-local. Export turns dots into IRIs; nothing else changes.

And the rule that decides what gets a standard name:

> **A standard term is written in the file when the engine reads it. Everything the engine does
> not read is mapped at export.**

Every term the repository writes is registered in
[`taxonomies/vocabulary-term.md`](taxonomies/vocabulary-term.md), so the vocabulary is a file
that lint consults rather than a paragraph anyone has to remember.

## 3. Meta-model

Domain, Concept, Taxonomy, Workflow, Router, Note, Skill. Each is declared in
[`concepts/`](concepts/) and each is an ordinary record the engine can read.

`Pattern` is **not** a primitive. A concept's property contract — `store`, `section`, `format`,
and declaration order — *is* the representation convention, so a separate pattern document would
restate it in prose and drift. v0.2's `_patterns/` and the content templates are retired for
this reason.

## 4. State

Three separable kinds, never conflated: `status` (documentary state, from the
[Status](taxonomies/status.md) vocabulary), `work_state` (execution), and `current_stage`
(lifecycle position). Only `status` is universal.

## 5. Identifiers

```text
slug     := [a-z0-9]+(-[a-z0-9]+)*
domain   := <slug>                            content, ops, site, delivery, protocol
class    := <domain>.<slug>                   content.creator          — a class id IS its name
resource := <domain>.<class-slug>.<slug>      content.creator.alex-xu
```

For a resource, `<domain>` MUST equal the `domain` key and `<class-slug>` MUST equal the last
segment of `rdf:type`. That binding is what makes the identifier check decidable: under v0.2,
`content.note.themes` and `content.creator.alex-xu` were structurally indistinguishable, so
nothing could tell a correct id from a coincidence.

`id` is immutable. A file whose id changed under the v1.0 grammar carries `previous_id`.

## 6. Document classes

Every file under `docs/` is an instance of exactly one concept, named by its `rdf:type`. A file
with no repeatable shape is a [Note](concepts/note.md) — still typed, still linted, but with a
free body. That is the only reason the "every heading is declared" rule can be absolute
everywhere else.

## 7. Front matter

`id`, `rdf:type`, `domain`, `status`, `version` are required on every file. The record
properties every file may carry — `owner`, `created`, `updated`, `facets`, `related`, `sources`,
`previous_id` — are declared once in [`domain.md`](domain.md) and belong to *being a file in this
repository*, not to being any particular concept. That is why the model needs no class
hierarchy.

Serialization order is fixed, so two agents writing the same values produce identical bytes:
`id`, `rdf:type`, `domain`, `status`, `version`, `owner`, `created`, `updated`, the concept's own
properties in declaration order, then `facets`, `related`, `sources`, `previous_id`.

## 8. Domain structure

```text
<domain>/
├── README.md        # routing document
├── domain.md        # boundary and root
├── concepts/        # >= 1 concept                       [required]
├── taxonomies/      # 0..n vocabularies                  [if the domain owns any]
└── workflows/       # 0..n operations                    [if the domain defines any]
```

`concepts.md` and `_patterns/` are gone. The structure check is unconditional because there is
nothing left to opt out of: an absent `taxonomies/` means the domain owns no vocabulary, which
is a fact about the domain rather than a gap in it.

## 9. The property contract

See [`concepts/concept.md`](concepts/concept.md), which declares it and is an instance of it.
In brief: each property states `rdf:type` (`owl:ObjectProperty` or `owl:DatatypeProperty`),
`rdfs:range`, its cardinality as `sh:minCount` / `sh:maxCount`, and `store` — `frontmatter` or
`body`, always explicit, never derived from the range. A body property names its heading
verbatim in `section` and its rendering in `format`.

`rdfs:domain` is never written; containment states it. See §17 for why that is correctness and
not convenience.

A relationship **is** a property. v0.2 kept `relationships` and `fields` as separate blocks that
restated each other — `controls content.creator-channel` was the `creator_channels` field — and
nothing checked that they agreed.

## 10. Types and cardinality

| Meaning | `rdf:type` | `rdfs:range` |
| --- | --- | --- |
| reference to a record | `owl:ObjectProperty` | a concept id |
| controlled value | `owl:ObjectProperty` | `skos:Concept` plus `skos:inScheme` |
| text | `owl:DatatypeProperty` | `xsd:string` |
| date | `owl:DatatypeProperty` | `xsd:date` |
| url | `owl:DatatypeProperty` | `xsd:anyURI` |

There is no list type. Multi-valued is the default, exactly as in RDF: absent `sh:maxCount` means
unbounded, absent `sh:minCount` means optional. v0.2's `type: list` plus `cardinality: 0..*` said
the same thing twice.

Omit what does not constrain. `sh:minCount: 1` with `sh:maxCount: 1` is exactly one;
`sh:minCount: 1` alone is one or more; neither is optional and unbounded.

This collapse removes a contradiction that sat in v0.2's own worked example, which declared a
field `required: true` *and* `cardinality: 0..*` — required, but zero values legal. Under
`sh:minCount` the question cannot be asked.

## 11. Taxonomies

One file per vocabulary, so a vocabulary's owner is structurally the file that defines it. See
[`concepts/taxonomy.md`](concepts/taxonomy.md).

## 12. Persistence

A concept declares whether and how its instances are stored: `directory`, `registry`, `external`
(a glob outside `docs/` — listed, not validated) or `none`. The documentation model must not
force a filesystem representation of every modelled thing.

## 13. Workflows

See [`concepts/workflow.md`](concepts/workflow.md). The contract's keys stay protocol-local
because OWL, RDFS and SKOS have no process vocabulary; its values are ontology-typed and are
resolved by lint.

## 14. Execution

Skill → Router → Domain → Concept → contract → instance → `uv run dh lint`.

## 15. Derived values

A property carrying `derived` is computed and written by `dh index`, never by hand. Lint
verifies that the stored value equals the recomputed one.

## 16. Governed vocabulary additions

Adding a value to any vocabulary is a governed operation. A skill may propose a value; it may
never write one that has not been approved. `uv run dh taxonomy check` exits non-zero on an
unknown value precisely so that a skill can route to approval instead of inventing.

## 17. Validation

> **These are shapes, not axioms.**
>
> Every `sh:` key is a **constraint**: a condition a file must already satisfy, checked against
> the file as written, where anything not stated is false. Every `owl:` and `rdfs:` key is a
> **description** — a name, a type, a range. It carries no obligation and can never fail.
>
> The two must never be traded for one another. `sh:minCount: 1` means *lint fails if this value
> is missing*. `owl:minCardinality 1` means *a value exists; if the file does not state it, infer
> one anyway*. Under OWL's open-world assumption an unsatisfied cardinality is not an error, it
> is a new inferred fact — so **a check rewritten as an OWL axiom can never fail.** It would not
> break loudly. Every rule in the repository would quietly become a rubber stamp, and lint would
> keep reporting success.
>
> Therefore cardinality, value sets, datatypes, patterns and closedness are written **only** with
> `sh:` terms. Lint rejects these by name: `owl:Restriction`, `owl:minCardinality`,
> `owl:maxCardinality`, `owl:cardinality`, `owl:someValuesFrom`, `owl:allValuesFrom`,
> `owl:FunctionalProperty`, `owl:disjointWith`, `owl:equivalentClass`, `rdfs:domain`,
> `rdfs:subClassOf`.
>
> `owl:` earns four terms here: `owl:Class`, `owl:ObjectProperty`, `owl:DatatypeProperty`, and
> `owl:inverseOf`. The first three name things and infer nothing.
>
> `owl:inverseOf` is the single exception, and it is deliberate: it is the one inference this
> repository performs. It is performed by `dh index` — deterministically, at a known time,
> writing a visible result into a file — not by a reasoner over a graph. Because a derived value
> is computed rather than authored, **a derived property carries no `sh:` constraints**: there is
> no authored value to constrain, and a constraint there would be vacuous or would fail on
> correct data.
>
> `sh:closed` deserves its own line, because it is the emblem of this stance: it is the one thing
> SHACL has that OWL has no equivalent for at any price. OWL cannot say "and nothing else" — in
> an open world there is always something else.
>
> This repository has no reasoner, no triple store, and no inference at query time. The files are
> the source of truth. `uv run dh lint` is the only authority.

**Severity is scoped by status.** A missing required value is an `error` on an `active` record
and a `warn` on a `draft`, `blocked`, `superseded` or `archived` one — because those statuses are
already honest labels for incompleteness, and because forcing a value onto an archived record
would mean inventing one.

**The `sources` check is advisory only.** "Sources back material claims" is not mechanically
decidable. What the code does is narrower and says so: it flags an `active` record with
substantial prose and no `sources`, and an `active` record containing an unfilled placeholder. A
`draft` record produces no finding at all, because `draft` *is* the explicit unknown label the
rule asks for. Do not read a green lint as "claims are sourced."

## 18. Adding a domain

Write `domain.md`, at least one concept, and a skill file. Nothing else is edited — not the
router, which is generated, and not the engine, which names no domain. That property is enforced
by a test.

## 19. Conformance

A document conforms to v1.0 when `uv run dh lint` reports zero errors against it. There is no
freeze clause: the protocol changes when the model needs it to, and `version` bumps on a change
to a contract, not on a prose edit.
