# Changelog

Version history. Each entry states **what changed**, **why**, and **what must not change**.
Newest first. Keep entries short; one block per version.

---

## v0.2 — Skeleton (no features)
- **Date:** 07-Oct-2026
- **Status:** Done
- **What changed:** Initialized a Reflex app with the blank template (`reflex==0.9.12`, pinned in `requirements.txt`) and shaped it to the ARCHITECTURE.md structure: `rxconfig.py` (app_name `app`), `app/app.py` (app object + placeholder landing page), `app/styles.py` (all DESIGN_SYSTEM.md tokens), and empty `app/state/`, `app/pages/`, `app/components/` packages. Added `.gitignore` (`.web/`, `.states/`, `__pycache__/`, `*.db`, `venv/`, plus `reflex.lock/`). Confirmed `reflex run` starts (frontend 3000, backend 8000).
- **Why:** Task 2 of the experiment: make the project runnable before any feature work so later tasks start from a stable base.
- **No features:** F1–F10 stay **Planned**. `app/app.py` renders only a placeholder heading; no state classes, models, or feature components exist.
- **What must not change:** `prd.md` remains the source of truth. The pinned Reflex version (0.9.12) is followed by all later code. Design values live only in `app/styles.py`.
- **Follow-ups:** F1–F3 (Task 3), then F4–F6, F7–F10. DB migration commands (`reflex db init/makemigrations/migrate`) get documented in README.md when models are first added.

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
