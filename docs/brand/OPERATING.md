# Brand Operating Plan

**Source strategy:** [`specs/2026-07-22-personal-brand-strategy.md`](specs/2026-07-22-personal-brand-strategy.md)
**Identity:** [`IDENTITY.md`](IDENTITY.md)
**Review cadence:** quarterly

This document holds the revisable operational plan: platform roles, the content system, the competitor-audit program, and editorial rules. Identity-level decisions (positioning, thesis, services, pillars, points of view) live in IDENTITY.md and change rarely. Operating decisions here are expected to evolve as evidence accumulates.

The pre-2026-07-22 operating plan (cinematic-vlog production machinery, 80/20 Life-Sciences content mix, phased YouTube launch criteria, travel batch-shoot logistics) is superseded; it survives in git history for reference.

## Surface map

Five platforms, each with a defined purpose.

| Platform | Purpose |
|---|---|
| **LinkedIn** | Attract clients. Build authority. Share business insights. Publish educational content. The primary client channel. |
| **YouTube** | Tutorials, workflow demonstrations, build in public, technical deep dives, Shorts. |
| **X (Twitter)** | Technical discussions, AI insights, systems thinking, networking with developers and founders. |
| **Instagram** | Travel, lifestyle, build in public, behind the scenes, personal brand. The live-offline half is most visible here. |
| **TikTok** | Short educational videos, automation demos, travel, productivity, build in public. |

The site (danielhunt.dev) is not a content platform. It is the credibility surface and contact path the platforms point to. Platform links are added to the site as each account goes live.

## Cadence

Not set by the 2026-07-22 strategy. Set per-platform when publishing starts, and revisit at the quarterly review.

Rule carried over from the previous plan: whenever a cadence is set, define its fallback cadence at the same time, so a slow month is a defined backup rather than a failure event.

## Content system

Five pillars ([`IDENTITY.md`](IDENTITY.md)) crossed with eleven formats. A piece of content is planned by picking a pillar, a format, and a platform.

### Formats

| Format | Shape / examples |
|---|---|
| **Educational** | "How to automate…", "Beginner's guide to…", "Framework for…", "Checklist for…", "How I built…" |
| **Lists** | "5 workflow mistakes", "7 AI tools I actually use", "3 ways to replace spreadsheets", "Top automations for small businesses", "My development stack" |
| **Before & after** | Spreadsheet → internal app. Manual process → AI workflow. Email chain → automated system. Legacy process → modern software. |
| **Workflow teardowns** | "Here's how I'd redesign this workflow", "If this company hired me…", breaking down inefficient business processes, "How I'd automate this operation" |
| **"What I'd do"** | "If I joined this company tomorrow…", "If I inherited this spreadsheet…", "If I had one week to improve this business…", "If I were the CTO…" |
| **Opinion pieces** | "Why you don't need 20 AI agents", "Documentation beats prompting", "Most automations are over-engineered", "AI should simplify, not complicate" |
| **Build-in-public updates** | What I'm building this week, new feature walkthroughs, lessons learned, challenges I'm solving, architecture decisions |
| **Behind the scenes** | My coding setup, AI workflow, Cursor tips, Claude Code workflow, how I organize projects |
| **Mistakes & lessons** | Biggest automation mistakes, AI implementation mistakes, documentation mistakes, dashboard mistakes, common workflow problems |
| **Storytelling** | "I saw a company wasting 20 hours every week…", how one spreadsheet inspired a product, the problem that led me to build…, lessons from enterprise software |
| **Quick demos** | 30–60 second videos: building software, automating a workflow, replacing a spreadsheet, creating dashboards, AI-assisted development |

## Competitor audit program

A standing research program, not a one-off. Purpose: understand **why** content works rather than copying it.

### Search terms by category

| Category | Terms |
|---|---|
| Workflow automation | workflow automation · business automation · AI workflow · AI automation · process automation · business systems |
| Internal software | internal tools · internal software · business software · operations software · custom software |
| AI development | Cursor AI · Claude Code · MCP · AI coding · AI engineer · software architecture · vibe coding |
| Business operations | operations management · operations optimization · systems thinking · process improvement · RevOps · COO |
| Build in public | build in public · indie hacker · SaaS founder · startup journey · solopreneur |
| Technical creators | AI consultant · automation consultant · workflow consultant · systems consultant · software consultant · technical founder · engineering leader |

### Per-creator checklist

For each creator surfaced, analyze:

- Hook quality
- Storytelling
- Video length
- Visual presentation
- Call to action
- Engagement (comments vs. likes)
- Audience questions
- Posting consistency
- Content pillars
- Topics that perform best

## Editorial rules

1. **The pillars control, not the algorithm.** If one post massively overperforms, that is informative data, not a content commitment. The pillar mix dictates the next post. (Carried over from the previous plan; still load-bearing.)
2. **Lessons are shared retrospectively.** Mistakes-and-lessons content covers what was learned, not live crises. (The substance of the old "scars, not wounds" rule.)
3. **Understand why it works; don't copy it.** Applies to everything the competitor audit surfaces.
4. **Client work is anonymized by default.** Client stories become content as patterns and lessons; naming a client requires their explicit permission.
5. **Model the points of view.** Content should itself be simple, documented, and maintainable — the brand can't argue "most automations are over-engineered" with over-engineered content systems.

More editorial rules accumulate here as content goes live and edge cases surface.

## The flywheel

**Content → Trust → Clients → Experience → Products → More Content**

Every client engagement should:

1. Solve a real business problem.
2. Generate content and lessons to share publicly.
3. Reveal repeatable patterns.
4. Become reusable frameworks or software.
5. Eventually evolve into products.

Services fund the practice, content compounds trust, patterns become products. Engagements that satisfy none of criteria 2–5 are still valid work, but they don't feed the flywheel — notice when that keeps happening.

## Documented brand decisions

Rejections and contrary positions captured here so they are not re-litigated.

### 2026-07-22: Life-Sciences positioning superseded

The brand spine is no longer "SWE walking into life sciences" (Datavial as flagship artifact, GxP contrarians, 80/20 Life-Sciences content mix, cinematic-vlog hero format). The 2026-07-22 strategy replaces it with the services-led positioning in IDENTITY.md. Prior specs, scripts, and plans under `docs/brand/` remain as dated historical snapshots — do not treat them as current strategy, and do not resurrect the old positioning without a new changelog entry.

### Carried forward from the previous plan

- **No metrics theater.** Build in public means real builds, decisions, and lessons — not MRR screenshots and vanity dashboards.
- **The algorithm doesn't steer.** See editorial rule 1.
- **Fallback cadences are defined up front.** See Cadence.
