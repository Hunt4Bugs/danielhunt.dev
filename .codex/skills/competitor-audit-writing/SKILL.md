---
name: competitor-audit-writing
description: Use when creating competitor audits, competitive research, TikTok reference analysis, short-form market research, or Notta transcript-based audit docs.
---

# Competitor Audit Writing

## Overview

Use this skill to create competitor audit folders under `docs/products/audits/competitive/`. Each audit should separate the human-readable analysis from raw source files and transcripts.

## When To Use

- Creating a new competitor or competitive audit.
- Reviewing TikTok videos for content, positioning, offers, or CTAs.
- Turning Notta.ai transcripts into market research.
- Comparing short-form content patterns across a competitor or niche.

## Inputs Needed

- Audit title in kebab-case.
- Competitor name, handle, product, or niche.
- TikTok URLs and capture dates.
- Downloaded reference video filenames, when available.
- Notta.ai transcript text files, when available.

## Folder Shape

Create each audit at:

```text
docs/products/audits/competitive/<audit_title>/
  AUDIT.md
  references/
    .gitkeep
    MANIFEST.md
  transcripts/
    .gitkeep
```

`references/` is for local TikTok video downloads and the tracked source manifest. Video files are intentionally ignored by git.

`transcripts/` is for Notta.ai transcript `.txt` files and should be committed.

## Naming

- Audit folders: `kebab-case`, such as `acme-ai-content-audit`.
- Transcript files: `YYYY-MM-DD-source-title.txt` when the date is known.
- Transcript fallback: `source-title.txt` when the date is unknown.
- Video filenames should match the manifest entry closely enough to identify the source.

## MANIFEST.md Template

```markdown
# Reference Manifest

| Source | URL | Captured | Local File | Transcript |
| --- | --- | --- | --- | --- |
| TikTok |  |  |  |  |
```

## AUDIT.md Template

```markdown
# Audit Title

## Competitor Profile

## Positioning

## Content Patterns

## Offer And CTA Patterns

## Strengths

## Gaps

## Reusable Ideas

## Action Recommendations
```

## Workflow

1. Create the audit folder using the required folder shape.
2. Add TikTok sources to `references/MANIFEST.md`.
3. Place Notta.ai transcripts in `transcripts/`.
4. Use transcripts and source notes to write `AUDIT.md`.
5. Keep claims tied to observed sources.
6. Convert observations into concrete recommendations.

## Output Checklist

- The audit lives under `docs/products/audits/competitive/<audit_title>/`.
- `AUDIT.md`, `references/MANIFEST.md`, `references/.gitkeep`, and `transcripts/.gitkeep` exist.
- Video files are not committed.
- Transcript text files use the naming convention.
- Recommendations are specific enough to act on.

## Common Mistakes

- Creating a parallel `competitor/` folder instead of using `competitive/`.
- Mixing raw transcripts into the audit report.
- Making claims that are not supported by references or transcripts.
- Tracking downloaded videos in git.
