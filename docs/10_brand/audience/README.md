---
id: audience.readme
kind: note
domain: audience
class: "10"
collection: audience
type: audience
status: active
owner: Daniel Hunt
created: 2026-06-01
updated: 2026-09-06
facets:
  - content
related:
  - domain.md
  - concepts.md
  - ../identity/README.md
  - ../strategy/README.md
sources:
  - ../plans/2026-09-06-technical-authority-alignment.md
  - ../specs/2026-06-01-personal-brand-workbook.md
version: 1
---

# Daniel Hunt — Brand Audience

[Identity](../identity/README.md) owns voice and meaning; [Strategy](../strategy/README.md) owns positioning and Themes. This document owns audience definitions, problems, credibility, and the evidence boundaries for teaching.

The September 2026 direction supersedes the audience assumptions in the dated June workbook. Historical snapshots remain evidence of earlier planning, not current career facts.

## Audience tiers

### Audience Segment registry

| Segment | Stable code | Audience Relationship | Use |
| --- | --- | --- | --- |
| Primary Editorial Audience | B2 | Addressed | Working data and software engineers across industries seeking reliability, better modeling, maintainability, and practical AI workflows. |
| Life Sciences Founder Peers | B1 | Spoken-with | Founders building life-sciences software; domain peers whose experience can inform exploration. |
| Lab Operations and Scientists | A | Spoken-about | End users whose workflows provide concrete context and whose needs should be represented accurately. |
| Commercial Services Audience | SERVICES | Addressed | Organizations with a concrete website, automation, integration, or custom-software need; a separate commercial route. |

Names, codes, and relationships are preserved. A proposed new Segment still requires the governed taxonomy-addition workflow.

### (B2) Primary. Working data and software engineers

Engineers building, operating, or improving real systems. They want to understand failures, choose useful abstractions, model data clearly, and apply AI without losing the ability to verify behavior. Their domain may be life sciences, marketing, legal analytics, or another industry.

Content should help them make a better engineering decision. Prior life-sciences knowledge, founder ambitions, and plans to leave employment are not prerequisites. Industry examples provide depth while explaining vocabulary and constraints unfamiliar to other engineers.

### (B1) Life Sciences Founder Peers

A domain peer network, not Daniel's claimed employment status or the default reader of every technical lesson. Conversations can inform Datavial exploration without implying design-partner agreements or customers.

### (A) Lab Operations and Scientists

Describe scientific workflows with empathy and evidence. Do not assume that all lab professionals have the same purchasing authority, software needs, or content habits. Their role here is domain context; it does not make every post an end-user sales message.

### Commercial services audience

The Services route addresses local businesses in Simi Valley and Ventura County, larger organizations, and remote teams with active technology needs. The five offers remain defined in [Offers](../offers/README.md). Client acquisition is secondary to the primary technical-reputation goal.

## Painful Problems v1

These are editorial hypotheses grounded in the work described below, not validated audience research. Refine them through substantive reader exchanges and the [measurement plan](../analytics/measurement-plan.md).

1. My pipeline succeeds, but I cannot tell whether its output is correct.
2. Retries and backfills produce duplicates, gaps, or more manual repair.
3. Our models make every new analytics or application requirement harder.
4. Our framework removes boilerplate but hides behavior developers need to debug.
5. Legacy code is poorly documented, and nobody knows which behavior must survive a refactor.
6. AI produces plausible code, but I need a reliable way to review and verify it.
7. Extracting structured data from documents is easier than evaluating whether it is trustworthy.
8. I want to understand another industry's workflows without pretending to be a domain expert.
9. I want to share useful engineering lessons without exposing private work or exaggerating outcomes.
10. I want meaningful technical work without deferring movement, relationships, and life outside the screen.

## Ideation Table v1

| Problem | Teaching approach | Supporting experience / boundary |
| --- | --- | --- |
| Correctness and silent failures | Explain validation, anomaly detection, and the limits of a successful job status. | W4; demonstrate with synthetic input and expected output. |
| Retries and backfills | Work through recovery behavior and show how to test repeated execution. | W4; an illustrative example is not an employer architecture disclosure. |
| Data modeling | Compare models for a pipeline, API, and analytics consumer. | W1; explain the intended consumer and tradeoff. |
| Framework complexity | Show what a decorator abstracts and what must remain visible. | W1c; no unsupported speed or productivity claim. |
| Legacy modernization | Establish context and behavior checks before AI-assisted changes. | W1b; distinguish the observed work from a newly proposed demonstration. |
| Trustworthy extraction | Explain entity extraction, evaluation, and ground-truth limitations. | W5 and W6; old NLP experience is not proof of current LLM product performance. |
| Domain learning | Explain scientific workflows and state open questions. | W1 / W3; regulatory interpretation, procurement, and product-market fit remain exploratory. |
| Sharing lessons | Use an attributable lesson and a clearly labeled synthetic example when needed. | Evidence discipline below; do not invent an incident. |
| Remaining human | Share a specific personal observation without prescribing universal life advice. | Firsthand personal experience; no performance or health promises. |

## Credibility Bank

**Evidence status:** The implementation-session record links the [observed LinkedIn profile and user confirmations](../plans/2026-09-06-technical-authority-alignment.md#evidence-and-confirmed-decisions). LinkedIn role descriptions are self-reported professional experience, not independently measured project outcomes. Daniel confirmed current Amgen employment and exploratory Datavial status on 2026-09-06.

### Wins

Stable W1/W1b/W2/W3 identifiers are retained for existing references. New identifiers extend the bank without rewriting historical provenance.

- **W1. Amgen modeling and pipelines.** Profile describes data modeling for legacy and new features of a Node.js API serving internal analytics dashboards. Earlier workbook material reports refactoring pharma R&D data models and pipelines and shorter time-to-data; that improvement remains unquantified and unverified.
- **W1b. Amgen documentation and modernization.** Automated documentation across systems to support developer onboarding and AI-assisted coding/troubleshooting; used AI tools to document, refactor, and optimize a large legacy Oracle package. This replaces the vague historical phrase “AI skills.” It does not establish autonomous self-refactoring.
- **W1c. Amgen developer tooling.** Designed a Python decorator framework aligned with Databricks environment, catalog, and database naming structures to simplify pipeline development and maintenance. No measured productivity result is available.
- **W2. Datavial outcome.** Deferred. Datavial is exploratory; no customer result, revenue, compliance status, or product-market fit is established. Capture a verified outcome if one occurs. Technical publishing does not depend on W2.
- **W3. Life-sciences observation.** Earlier workbook material reports fragmented data and constraints on internal software work as motivation to explore Datavial. Treat this as attributed firsthand recollection, not evidence of having left employment or of industry-wide conditions.
- **W4. Realtor.com production data systems.** Built marketing pipelines with Python, Airflow, and Snowflake; validation/anomaly detection using SQL and dbt; recovery and backfill mechanisms; and observability using InfluxDB and Grafana. The profile's “99% reliability” and “billions of impressions” are not supported by definitions, scope, or measurement records here and are omitted from revised public copy.
- **W5. Gavelytics legal analytics.** Built NLP/ML pipelines to extract entities and outcomes from legal text using Keras, Word2Vec, and SciPy; delivered judge/case analytics with Pandas and NumPy. This is prior professional work, not merely a possible future vertical.
- **W6. HRL Laboratories engineering.** Implemented and compared computer-vision saliency methods; built a video annotation tool incorporating translation/rotation detection; performed CAN-bus message analysis and security testing with Python tooling. Claimed annotation-speed benefits remain unmeasured here.

### Scars

- **S1. Fragmented data and excess integration work.** A firsthand observation in the earlier workbook. Use a concrete example or qualify the scope; do not turn it into a universal claim about pharma.
- **S2. Changed assumption.** Deferred until a specific, attributable example exists. It may arise from engineering work or Datavial exploration. Do not invent a failure to fill a narrative slot.

### Evidence discipline

Teach established experience confidently and state the limits of applicability. Label proposed designs, synthetic examples, experiments, personal recollections, and measured outcomes distinctly. A self-reported career bullet supports attribution; it does not independently prove its impact. Quantified results require a metric definition, timeframe, scope, and supporting evidence. Customer stories require verified facts and publication authorization.

## Interest Bank v1

These are candidate investigations, not claims of completed experiments or existing artifacts:

- Safe recovery and backfill demonstrations using synthetic records.
- Models serving both operational APIs and analytics consumers.
- Developer-friendly abstractions that preserve inspectable execution behavior.
- Context preparation and behavior verification for AI-assisted legacy refactoring.
- Evaluation of structured extraction from heterogeneous documents.
- Datavial's scientific workflow and data-container ideas, at exploratory maturity.
- Movement, food, culture, and relationships alongside employed engineering work.

Procurement, regulatory interpretation, and product-market fit remain open learning areas. Production-craft learning is optional and stays backstage unless it yields a useful, evidence-backed lesson.

## Differentiation Breakdown

| Dimension | Brand approach |
| --- | --- |
| Engineering judgment | Explain the problem, alternatives, tradeoff, and verification rather than recommend tools by popularity. |
| Evidence | Make examples inspectable and label their limits; confidence follows demonstrated experience. |
| Domain depth | Use life sciences, marketing infrastructure, and legal analytics to make transferable lessons specific. |
| AI | Teach concrete AI-assisted documentation and modernization workflows while retaining human review and behavior checks. |
| Human life | Preserve presence and curiosity without turning overwork into a credential. |

## Desired Associations

- Reliable data systems, clear models, and maintainable engineering.
- Practical AI-assisted modernization with explicit verification.
- Industry depth that helps engineers across domains learn.
- Build in public. Live offline. as a lived philosophy compatible with technical authority.

Avoid unsupported certainty, generic hype, invented outcomes, and claims that professional learning requires leaving a job.

## Historical context

The [June workbook](../specs/2026-06-01-personal-brand-workbook.md) and its [design rationale](../specs/2026-06-01-workbook-docs-design.md) preserve earlier assumptions. Current audience direction and career facts are stated above; do not reuse the historical departure narrative as fact.
