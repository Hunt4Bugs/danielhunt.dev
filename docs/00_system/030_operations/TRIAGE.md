---
class: "00"
collection: operations
type: triage-policy
status: active
owner: Daniel Hunt
updated: 2026-07-28
---

# Triage

Capture incoming work in `TRACKER.md` as `draft`, then classify it:

| Lane | Use when | Required response |
| --- | --- | --- |
| Brand foundation | Voice, audience, positioning, visual direction | Read the relevant canonical brand documents before proposing a change. |
| Site implementation | Public HTML, CSS, JS, assets, SEO | Validate locally; do not deploy without approval. |
| Delivery | GitHub Actions, pages, secret-dependent behavior | Diagnose and recommend; external configuration changes require approval. |
| Governance | Process, templates, tracker, or guidance | Update class 000 after evidence review. |

Escalate immediately for secrets, security concerns, public publication, data loss, financial/legal exposure, or a decision that changes brand strategy.
