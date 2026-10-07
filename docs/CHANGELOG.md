# Changelog

Version history. Each entry states **what changed**, **why**, and **what must not change**.
Newest first. Keep entries short; one block per version.

---

## v0.1 — Supporting docs (docs only)
- **Date:** 06-Oct-2026
- **Status:** Done
- **What changed:** Created `docs/ARCHITECTURE.md`, `docs/DESIGN_SYSTEM.md`, `docs/COMPONENTS.md`, `docs/FEATURES.md`, `docs/DECISIONS.md`, `docs/CHANGELOG.md`, `docs/BUGS.md` from `prd.md`. Defined design tokens (colors, spacing, radius, typography) in DESIGN_SYSTEM.md.
- **Why:** Task 1 of the experiment: give the AI a documented context before any code, so later sessions can build v1.0 (F1–F10) without drift.
- **No code:** This version adds no application code, `requirements.txt`, or config. The app is not runnable yet; Task 2 creates the skeleton.
- **What must not change:** `prd.md` remains the source of truth. Tokens in DESIGN_SYSTEM.md are the only source of design values. F1–F10 stay **Planned** until built.
- **Follow-ups:** Task 2 (skeleton), then F1–F3, F4–F6, F7–F10.

---

## Planned versions (from prd.md §11 / PROMPTS.md)
| Version | Change | Status |
|---|---|---|
| v1.0 | Build F1–F10 | Planned |
| v1.1 | Add F11, F12 via docs | Planned |
| v1.2 | Design change | Planned |
| v1.3 | Bug fix | Planned |
| v1.4 | Refactor | Planned |
| v1.5 | Changed behavior (F5 filters) | Planned |
| v1.6 | Cold-start F13 | Planned |
