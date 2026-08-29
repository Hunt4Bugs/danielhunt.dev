---
id: protocol.documentation.v0.2
kind: protocol
domain: protocol
status: draft
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-27
version: 0.2
---

# Domain Documentation Protocol v0.2

> **Model the domain. Document the contract. Execute the workflow.**

This is the model-first documentation protocol for describing domains, capturing
reusable structure, and executing workflows consistently across humans, AI agents,
and software. v0.2 merges and reconciles the earlier domain-model work in this
repository with a general, provider-agnostic protocol for defining any domain.

## 1. Purpose

The protocol defines a provider-agnostic way to:

- model a domain,
- document its concepts and relationships,
- capture reusable rules and structures,
- define workflows that operate on the model,
- create instances of modeled concepts,
- and expose enough structure that humans, AI agents, or software can operate
  against the same documentation.

Markdown is the initial representation. **Markdown is not the model itself.**

```text
Domain Model
     ↓
Canonical Documentation
     ↓
Possible Representations
     ├── Markdown
     ├── JSON / YAML
     ├── Database Schema
     ├── JSON Schema
     ├── OWL / RDF
     └── Code
```

The protocol must therefore avoid encoding assumptions that only make sense for
a particular LLM provider.

## 2. Core principles

### 2.1 Model before execution

Define the domain before creating workflows against it.

```text
Model
  ↓
Document
  ↓
Operate
```

Not:

```text
Prompt
  ↓
Hope the model understands the domain
```

### 2.2 Stable semantics, flexible implementation

Every domain follows the same modeling protocol. Domains do **not** need identical
internal structures. Content may contain `Topic / Blueprint / Publication`;
engineering may contain `Service / API / Package`; laboratory operations may
contain `Sample / Test / Method`. The protocol stays constant.

### 2.3 Documentation is the contract

AI skills should contain as little domain knowledge as possible.

```text
Skill
  ↓
load domain
  ↓
resolve workflow
  ↓
resolve concept / pattern
  ↓
execute
  ↓
verify
```

rather than embedding all the domain logic inside the skill. Changing a pattern
or a workflow changes behavior without rewriting every skill.

### 2.4 Humans and machines share the same source

Do not create separate "AI documentation" unless a machine-specific
representation becomes necessary. The canonical material should be useful to both.

### 2.5 Structure only what needs structure

Use formal structure where it creates value. Avoid turning Markdown into a
hand-maintained graph database. The two contracts that get structured frontmatter
in v0.2 — **Workflow** and **Concept/entity** — are the ones that must be
machine-checkable for workflows to gather inputs and validate before transforming.

### 2.6 Mutable state lives in metadata

Anything that changes over the life of a record — document lifecycle, execution
state, current stage — is represented in metadata, never smuggled into prose.

## 3. Meta-model

The structural primitives. These describe how the model is shaped:

```text
Domain
Concept
Relationship
Constraint
Pattern
Workflow
```

### 3.1 Domain

A bounded area of reality being modeled. Examples: `content`, `engineering`,
`brand`, `analytics`, `laboratory-operations`, `commerce`.

A Domain defines its purpose, scope, concepts, relationships, constraints, and
connections to neighboring domains.

### 3.2 Concept

A type of thing that exists or matters within a domain. A Concept describes a
**type**, not a specific instance.

```text
Concept: Topic

Instance:
"Why repository structure improves AI-assisted engineering"
```

### 3.3 Relationship

A directed semantic association between concepts:

```text
Publication -- communicates --> Topic
Service -- exposes --> API
Analyst -- performs --> Test
```

```text
<source concept> <relationship> <target concept>
```

### 3.4 Constraint

An invariant that must or should remain true within the model:

```text
A Publication must reference a Topic.
A Test must use an approved Method.
A Service may expose zero or more APIs.
```

Constraints are what make the model useful for validation, schema generation,
and semantic representations. **Constraint is an invariant rule. It is not a
representation convention.** See §7.

### 3.5 Pattern

A **representation convention**: the shape a document describing an instance of
a Concept takes in this repository.

```text
CONCEPT    What is a Topic?
   ↓
PATTERN    What does a Topic document look like?   (_patterns/topic.md)
   ↓
INSTANCE   Here is one particular Topic.           (topics/<name>.md)
```

A Pattern is documentation infrastructure, not modeled content. See §7 for the
full pattern-vs-constraint distinction.

### 3.6 Workflow

A repeatable, **stateful transformation** that operates on the domain. It
declares what inputs it gathers, what state its subject must already be in
(preconditions), what it creates or updates, and what valid state it must exit in.

```text
develop-topic
create-publication
add-api-endpoint
qualify-sample
review-architecture
```

A Workflow references Concepts and Patterns rather than redefining them.

### 3.7 What is deliberately NOT a structural primitive

**Decision.** A recorded choice whose rationale matters ("Use `uv` for Python
dependency management", "Treat Publication as platform-specific"). A Decision
answers *why is the system this way* and prevents conventions from becoming
unexplained folklore. It is modeled as an ordinary Concept with a Pattern
(`decisions/decision.md`), **not** a peer structural primitive — it is a record
of a past choice (temporal, provenance-bearing), not a shape of the model.

**Artifact.** Deferred. Leave it out of the required meta-model until use proves
it represents something distinct from Concept.

**Domain-specific terms** (`Topic`, `Knowledge`, `Blueprint`, `Service`, `API`,
`Sample`, `Instrument`, `Asset`, `Campaign`) are **not** protocol primitives.
They are domain concepts.

## 4. State model

Three separable kinds of state. Do not conflate them.

| Field | Applies to | Values (domain-definable) | Job |
| --- | --- | --- | --- |
| `status` | any document | `draft`, `active`, `blocked`, `superseded`, `archived` | document/record lifecycle & maintenance |
| `work_state` | a Work Item execution | `queued`, `in_progress`, `blocked`, `completed`, `cancelled` | whether this execution is running |
| `current_stage` | a Work Item execution | domain-defined lifecycle stages (e.g. `Capture → Validate → Plan → Draft → Review → Produce → Publish → Measure → Learn → Reuse/Repurpose`) | where in the lifecycle this execution is |

`status` says "is this document live or retired." `work_state` says "is this
execution running." `current_stage` says "where in the pipeline is it." The
content lifecycle stages are owned by the domain that defines them.

## 5. Stable identifiers

Semantic identifiers:

```text
<domain>.<kind>.<name>
```

Examples at the type level:

```text
content.topic
content.blueprint
content.publication
engineering.service
engineering.api
```

At the instance level:

```text
content.topic.repository-context
content.workflow.develop-topic
engineering.service.billing
engineering.workflow.create-service
```

`content.topic` = concept/type identifier; `content.topic.repository-context` =
instance identifier. This is a lightweight type-instance system.

**Instances that are executed** (Work Items) use a dated scheme so they are unique
and never renamed:

```text
WI-YYYYMMDD-<workflow>-<subject>      # e.g. WI-20260827-develop-topic-ai-repository-guidance
```

`id` is immutable once assigned. Never rename an identifier.

## 6. Relationship notation

Keep it minimal and meaningful.

```text
Publication -- communicates --> Topic
Publication -- uses --> Blueprint
Knowledge -- supports --> Topic
```

Or in Markdown:

```markdown
### Relationships
- `Publication` **communicates** `Topic`
- `Publication` **uses** `Blueprint`
- `Knowledge` **supports** `Topic`
```

This maps directly onto `subject → predicate → object`, a bridge to RDF if it is
ever needed.

## 7. Pattern versus Constraint

Two distinct notions, previously conflated under one word. Name them explicitly:

| Notion | Question it answers | Carries | Lives in |
| --- | --- | --- | --- |
| **Pattern** | What does a document of this Concept look like? | structure, sections, field layout | `_patterns/*.md` |
| **Constraint** | What must remain true about this model? | invariant rules, cardinality, requirements | `concepts.md` (constraint block) |

A Topic Pattern says *write the Proposition, Audience, Value, Evidence, Notes*
sections. A Topic Constraint says *a Topic must reference at least one Knowledge*.
Patterns are representation conventions; Constraints are invariant rules.

## 8. Domain structure contract

Root documentation-system contract:

```text
docs/
├── README.md
├── _conventions/
│   ├── README.md
│   ├── documentation.md
│   ├── identifiers.md
│   └── relationships.md
├── _patterns/            # meta-patterns: what each kind of doc must contain
│   ├── README.md
│   ├── domain.md
│   ├── concept.md
│   ├── workflow.md
│   ├── pattern.md
│   └── decision.md
└── <domains>/
```

The underscore convention marks **documentation-system infrastructure** rather
than modeled domain content. Not security/private.

### 8.1 Required domain structure

Only these roles are standardized:

```text
<domain>/
├── README.md       # routing document: where am I, what is this for, where next
├── domain.md       # boundary + high-level model (kind: domain)
├── concepts.md     # the concept registry + entity contracts (kind: concept-registry)
├── _patterns/      # representation conventions per concept
└── workflows/      # reusable operations on the model
```

Optional, and domain-defined: `decisions/`, `standards/`, `references/`,
`examples/`, plus instance directories justified by the model (e.g. `topics/`,
`publications/`, `services/`). Only `workflows/` is close to universally useful.

## 9. Frontmatter contracts

### 9.1 Common metadata (all documents)

```yaml
id: <domain>.<kind>.<name>
kind: domain | concept-registry | pattern | workflow | decision | note
domain: <domain-id>
status: draft | active | blocked | superseded | archived
version: 1
```

Plus, when relevant: `owner`, `created`, `updated`, `facets`, `related`, `sources`.

### 9.2 `domain.md`

```yaml
id: content
kind: domain
domain: content
status: active
version: 1
```

Body: `Purpose`, `Scope (Includes / Excludes)`, `Model`, `Relationships`,
`Constraints`, `Related Domains`, `Examples`.

### 9.3 `concepts.md` — the concept registry and entity contracts

One canonical registry per domain. Each Concept carries its definition,
relationships, constraints, and an **entity contract** (see §10) when its
instances are persisted.

```markdown
# Concepts

## Topic
**ID:** `content.topic`

A subject, proposition, or idea intended for communication.

### Relationships
- supported by `content.knowledge`
- expressed through `content.blueprint`
- communicated by `content.publication`

### Constraints
- A Topic must reference at least one supporting `content.knowledge`.

### Entity contract
`content.topic`  # field list; see §10
```

Engineering uses the same protocol with different concepts:

```markdown
## Service
**ID:** `engineering.service`

An independently deployable or executable software capability.

### Relationships
- exposes `engineering.api`
- belongs to `engineering.system`
```

Same protocol. Different domain.

### 9.4 `_patterns/<concept>.md`

```yaml
id: content.pattern.topic
kind: pattern
domain: content
pattern_for: content.topic
```

Body: the template sections an instance document must contain. A workflow can then
say "Create a `content.topic` using `_patterns/topic.md`" and the AI does not have
to invent the structure.

### 9.5 `workflows/<name>.md`

This is the centerpiece. See §11.

## 10. The Concept / entity contract

The type system. When a Concept's instances are persisted, define its fields so
workflows can validate inputs and outputs against them.

```yaml
# inside concepts.md, under the Concept heading
entity: content.publication
fields:
  - name: blueprint
    type: ref(content.blueprint)
    required: true
    cardinality: 1
  - name: channel
    type: ref(content.channel)
    required: true
    cardinality: 1
  - name: format
    type: taxonomy(Publication Format)
    required: true
    cardinality: 1
  - name: published_at
    type: date
    required: false
    writable_after: workflow.publish
  - name: dependencies
    type: taxonomy(Production Dependency State)
    required: true
    cardinality: 0..*
```

Field types: `ref(<concept-id>)` (link to an instance of another concept),
`taxonomy(<controlled vocabulary>)` (value drawn from a governed set),
`text`, `date`, `url`, `list` of any of these. `cardinality` states how many
values are valid (`1`, `0..1`, `0..*`, `1..*`).

A controlled vocabulary is owned by exactly one context. Adding a value is
governed (see §13.3); a workflow or skill may propose a value but may not use it
before approval.

## 11. The Workflow contract (centerpiece)

Every Workflow carries its operational contract in structured frontmatter so it
can be validated, chained, and compiled into a runnable skill. The prose body
(`Purpose`, `Procedure`, `Exceptions`, worked examples) stays human-readable; the
machine contract lives in YAML.

```yaml
id: content.workflow.develop-publication
kind: workflow
domain: content
status: active
version: 1
contract:
  subject_type: content.blueprint      # what it operates on
  entry_stage: Draft                   # required current_stage of the Work Item
  exit_stage: Review                   # valid current_stage on success
  requires:                            # PRECONDITIONS — what must already exist
    - id: content.blueprint
      state: completed                 # required predecessor work_state
      optional: false
    - id: content.script
      state: validated
      optional: true                   # only when a primary Script is used
  inputs:                              # data gathered BEFORE transforming
    - name: channel
      type: ref(content.channel)
      required: true
    - name: format
      type: taxonomy(Publication Format)
      required: true
    - name: copy
      type: text
      required: true
  creates:                             # what it produces
    - type: content.publication
      via_pattern: _patterns/publication.md
  updates:                             # what it modifies
    - type: content.publication
  validation:                          # EVIDENCE required to pass
    - subject_blueprint_linked
    - channel_format_compatible
    - dependencies_resolved
    - copy_preserves_blueprint_intent
  next:                                # valid follow-on workflows
    - content.workflow.validate-publication
  failure_paths:                       # valid return routes
    - content.workflow.develop-blueprint
    - content.workflow.revise-script
```

Body sections a workflow must contain: `Purpose`, `Inputs`, `Preconditions`,
`Procedure`, `Outputs`, `Patterns` (which `_patterns/*` to use), `Verification`,
`Exceptions`.

The `requires` block is what makes "gather requirements, inputs, and states
before following the steps" real: an agent checks `requires` (preconditions) and
gathers `inputs` (typed, against entity contracts and controlled vocabularies)
**before** it starts the `Procedure`. `validation` is what it proves to exit.

Workflows reference Concepts and Patterns; they may not redefine an entity or
silently extend a controlled vocabulary.

## 12. Execution model

A skill is little more than orchestration. It loads the domain rather than
embedding it.

```text
User: "Create a topic about schema evolution."

Skill:
1. Determine domain = content
2. Read content/README.md
3. Resolve content.workflow.develop-topic
4. Read its contract (requires, inputs, creates, validation)
5. Resolve content.topic and its entity contract
6. Load content/_patterns/topic.md
7. Check preconditions; gather typed inputs
8. Execute the procedure
9. Validate against `validation` + `exit_stage`
10. Record the Work Item
```

Changing `_patterns/topic.md` or `workflows/develop-topic.md` changes behavior
without rewriting every skill.

A Work Item is one persistent record of one execution of one Workflow against one
subject. It carries `work_state` and `current_stage` in metadata, names its
`Inputs / Decisions and assumptions / Outputs / Validation / Predecessors /
Possible next workflows`, and links every record it creates back to itself.
Work Items are never renamed or deleted after completion.

## 13. Validation and lint

A protocol whose premise is "humans, agents, and software operate against the
same docs" needs an enforcement mechanism. `protocol-lint` checks, per domain:

1. Required structure exists: `README.md`, `domain.md`, `concepts.md`,
   `_patterns/`, `workflows/`.
2. All `id`s are unique and well-formed (`<domain>.<kind>.<name>`).
3. Frontmatter has the required keys (`id`, `kind`, `domain`, `status`, `version`).
4. `status` is in the allowed set.
5. Every `related` / `sources` link resolves to an existing file.
6. Every `ref(<concept>)` in a field or `requires` resolves to a defined Concept.
7. Every `taxonomy(...)` value used in an instance exists in its owning registry.
8. Workflow `next` and `failure_paths` resolve to defined workflows.
9. A Workflow's `creates` entity contract matches its `exit_stage`.
10. Sources back material claims; unknowns are explicitly labeled `draft`/`unknown`.

### 13.2 Validate before use

Run lint before generating a skill, before committing, and after any model change.
A domain that fails lint is not a valid target for skill generation.

### 13.3 Governed taxonomy additions

Adding a controlled value to any owning registry is a governed operation, not a
silent edit. A workflow or skill may create a **proposal** record; the value is
never selectable until approval updates the owning canonical context.

## 14. Instance storage is domain-defined

The protocol does **not** say "every concept gets a folder." A domain determines
whether concept instances require persisted documentation.

If Topic instances matter: `topics/`. If Engineering Services are represented
primarily by source code, you may not need `services/` at all — the Concept still
exists in the model. The documentation model must not force a filesystem
representation of every modeled thing.

### 14.1 When does a Concept get a Pattern?

Create a local Pattern when:

- humans or software repeatedly create instances of the Concept,
- instances require a predictable representation,
- a Workflow produces that Concept,
- or consistent structure materially improves reasoning or validation.

Do not create one merely because the Concept exists.

## 15. Domain creation workflow

A root-level workflow (not inside a domain). Given a domain name and intent:

1. **Identify** — name, `id`, purpose. What bounded area are we trying to
   understand or operate?
2. **Scope** — what belongs, what does not, which neighboring domains exist?
3. **Discover concepts** — what things exist / have identity / change over time /
   are created or consumed / do people act upon / would a database represent?
   Start minimal; do not invent dozens of concepts.
4. **Define relationships** — what can it contain, what creates it, what does it
   depend on, what does it reference, what can act on it?
5. **Define constraints** — what must always be true, what must never happen,
   what is required, what is optional?
6. **Validate the model** — walk real scenarios; if the model cannot describe
   them cleanly, revise it.
7. **Determine persisted representations** — for each Concept, does it need
   independent identity, will workflows create instances, must humans/machines
   reference instances? If yes, decide on a Pattern and/or instance directory.
8. **Generate the structure** — `README.md`, `domain.md`, `concepts.md`,
   `_patterns/`, `workflows/`, plus justified domain-specific structures.
9. **Define initial workflows** — only the highest-value operations first.
10. **Test against real work** — run an actual task through the domain; revise
    the model rather than compensating with increasingly complicated prompts.

## 16. Protocol lifecycle

```text
DEFINE → MODEL → VALIDATE → REPRESENT → OPERATE → OBSERVE → EVOLVE
```

Concretely:

```text
Define Domain
  ↓ Model Concepts
  ↓ Define Relationships
  ↓ Define Constraints
  ↓ Validate with examples
  ↓ Create Patterns where needed
  ↓ Create Workflows
  ↓ Execute
  ↓ Update model when reality changes
```

## 17. What is not universal

The following are **not** protocol primitives:

```text
Topic  Knowledge  Blueprint  Publication  Service  API  Audience  Asset
Campaign  Sample  Instrument
```

They are domain concepts. `Knowledge` may be a useful Concept in Content; in
Engineering you might model `Standard`, `Principle`, `ArchitectureDecision`
instead — or not model knowledge as a concept at all.

## 18. Minimal domain examples

Content:

```text
20-content/
├── README.md
├── domain.md
├── concepts.md
├── _patterns/
│   ├── topic.md
│   ├── blueprint.md
│   └── publication.md
├── topics/
├── blueprints/
├── publications/
└── workflows/
    ├── capture-knowledge.md
    ├── develop-topic.md
    └── create-publication.md
```

Engineering:

```text
30-engineering/
├── README.md
├── domain.md
├── concepts.md
├── _patterns/
│   └── decision.md
├── stack.md
├── architecture.md
├── standards/
├── decisions/
└── workflows/
    ├── create-service.md
    ├── add-endpoint.md
    └── release.md
```

Same protocol. Different implementation.

## 19. v0.2 freeze

```text
META-MODEL
──────────
Domain  Concept  Relationship  Constraint  Pattern  Workflow
(Decision = ordinary concept+pattern, not a primitive; Artifact deferred)

REQUIRED DOMAIN STRUCTURE
─────────────────────────
README.md  domain.md  concepts.md  _patterns/  workflows/

REQUIRED DOCUMENT METADATA
──────────────────────────
id  kind  domain  status  version

EXECUTION STATE
───────────────
status (doc)  work_state (execution)  current_stage (lifecycle)

MACHINE-CONTRACT DOCS
─────────────────────
concept/entity contract (fields, types, cardinality)
workflow contract (subject_type, entry/exit stage, requires, inputs,
                   creates, updates, validation, next, failure_paths)

IDENTIFIERS
───────────
<domain>.<kind>.<name>   (type)     content.topic
<domain>.<kind>.<name>   (instance) content.topic.repository-context
WI-YYYYMMDD-<workflow>-<subject>     (executed instances)

DOMAIN CREATION PROCESS
───────────────────────
Identify → Scope → Discover → Relate → Constrain → Validate →
Represent → Generate → Workflow → Test against real work

EXECUTION MODEL
───────────────
Skill → Domain → Workflow → Concept → Pattern → Instance → Verification

VALIDATION
──────────
protocol-lint (structure, ids, metadata, links, refs, taxonomies,
               workflow chaining, exit_stage vs creates)
```

Do not add more to the protocol yet. Everything else should prove its need
through usage.

## 20. Open questions for v0.3

- **Where does the protocol live?** It is developed inside `danielhunt.dev` but is
  meant to be the cross-brand/company template. Decide whether it graduates to a
  standalone template repo, or stays as a governing standard here with a
  parameterized scaffold stamped out per brand.
- **Artifact**: promote when a distinct role proves itself.
- **Version semantics**: when does `version` bump — on any change, or only on
  breaking contract changes?
- **Numeric class prefixes** (current `00_system` / `10_brand`) vs semantic
  domain folders (`20-content` / `30-engineering`): reconciled in the first real
  migration (see `docs/00_system/010_governance/LIBRARY_MAP.md`) — class prefixes
  stay as the physical top-level layout (shrunk to 2 digits to match this
  section's own examples), and protocol Domains are modeled *within* them rather
  than replacing them. Revisit only if a domain's natural boundary stops fitting
  inside a single numeric class.
- **A single vertical slice** (entity-contract + workflow-contract-as-frontmatter
  + a generated skill) should be built and run before this is handed to any
  wider tooling.
