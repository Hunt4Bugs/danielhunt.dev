---
name: sop-writing
description: Use when creating or revising standard operating procedures, repeatable workflows, process docs, or SOP files for this repo.
---

# SOP Writing

## Overview

Use this skill to create one clear operating procedure per file under `docs/products/sop/`. A good SOP lets a human repeat the process without asking what "done" means.

## When To Use

- Creating a new SOP from a recurring workflow.
- Turning scattered notes into a repeatable procedure.
- Revising an SOP after the process changes.
- Clarifying ownership, quality standards, exceptions, or review cadence.

## Inputs Needed

- SOP title and intended owner.
- The trigger for running the process.
- Required inputs, accounts, assets, or source docs.
- The exact steps a human should follow.
- How to verify the result is acceptable.

## Workflow

1. Create one focused markdown file in `docs/products/sop/`.
2. Use a kebab-case filename, such as `publish-short-form-script.md`.
3. Write for a human operator, not for an implementation log.
4. Keep steps concrete and ordered.
5. Separate normal procedure from exceptions.
6. Include the review cadence so stale processes get revisited.

## SOP Template

```markdown
# SOP Title

## Purpose

## Owner

## When To Run

## Inputs

## Procedure

## Quality Bar

## Exceptions

## Review Cadence
```

## Output Checklist

- The filename is kebab-case and scoped to one process.
- The purpose states the business outcome.
- The owner is named by role or person.
- The procedure is ordered and repeatable.
- The quality bar says how to verify the work.
- Exceptions explain when to stop, escalate, or use judgment.

## Common Mistakes

- Combining multiple workflows into one SOP.
- Writing goals without executable steps.
- Omitting the owner or review cadence.
- Hiding exceptions inside the main procedure.
