# Decisions

Architecture Decision Records (ADRs) for TaskFlow. Each entry states **what**, **why**, and **what must not change**.
Add an entry for any non-obvious choice (AGENTS.md). Newest first.

---

## D-005 — Mock auth with cookie/local-storage session
- **What:** Login is fake (any email + password of 6+ chars) and the "session" is stored in a browser cookie / local storage, rehydrated on load.
- **Why:** Reflex State resets on page refresh, so F1's "login survives page refresh" needs a persistent client-side marker. Real auth is out of scope (prd.md §1.3).
- **Must not change:** No real credentials, tokens, or personal data are stored. The session is a mock flag only.

## D-004 — One state class per domain
- **What:** Separate `AuthState`, `TaskState`, `ProjectState`, `SettingsState` instead of one global state.
- **Why:** Keeps each domain's data and handlers isolated, which makes tasks small and reduces the chance the AI edits unrelated features.
- **Must not change:** Data changes happen only inside event handlers of the owning state. Rendering reads state; it never mutates it.

## D-003 — Filters stored in URL query params
- **What:** Search text, status filter, priority filter, and sort live in the URL query string (F5, F6).
- **Why:** The user flow "open task → change status → back (filter preserved)" requires the filtered view to survive navigation. URL params are the natural store.
- **Must not change:** This is the v1.0 behavior. A later "changed behavior" task may move filters into State (see PROMPTS.md), at which point this entry is superseded, not deleted.

## D-002 — Pure-Python Reflex UI; no JavaScript
- **What:** Build the entire UI with Reflex Python components.
- **Why:** AGENTS.md and prd.md fix the stack as Python + Reflex. It is also part of the experiment: can a doc-driven AI avoid reaching for React.
- **Must not change:** Do not introduce React/JS. If a Reflex-native way genuinely does not exist, log a new ADR explaining the exception before writing JS.

## D-001 — Docs-first workflow; prd.md is the source of truth
- **What:** Requirements and design are written/updated in `prd.md` and `docs/` before code, and docs are updated after every change.
- **Why:** This is the core experiment (prd.md §1.1): can structured `.md` memory keep an AI from losing context or drifting across versions.
- **Must not change:** `prd.md` wins any conflict with other docs. Code follows docs, not the other way around.
