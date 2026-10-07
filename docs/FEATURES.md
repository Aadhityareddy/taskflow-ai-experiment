# Features

Source of truth: `prd.md` §4.1. This file tracks feature status.
Status values: **Planned** (approved, not built), **In Progress**, **Done**.
Rule (AGENTS.md): implement only features marked **Planned** or explicitly requested. Never modify a **Done** feature unless the task names it.

All v1.0 features are **Planned**. No code exists yet (Task 1 is docs-only).

## v1.0

| ID | Feature | Status | Acceptance criteria |
|---|---|---|---|
| F1 | Mock login | Planned | Email + password (min 6 chars); inline errors; redirect to Dashboard; protected routes; login survives page refresh |
| F2 | App shell & navigation | Planned | Responsive sidebar, active-link highlight, logout |
| F3 | Task CRUD | Planned | Create/edit via dialog form; delete with confirm dialog |
| F4 | Task fields | Planned | Title, description, priority (Low/Medium/High), due date, status (Todo/In Progress/Done) |
| F5 | Search & filter | Planned | Search by title; filter by status and priority; filters kept in URL query params |
| F6 | Sort | Planned | By due date, priority, created date; ascending/descending |
| F7 | Projects | Planned | CRUD projects (name + color); assign a task to a project |
| F8 | Dashboard | Planned | Cards for total, completed, overdue; list of next 5 due tasks |
| F9 | Dark/light theme | Planned | Toggle in Settings; persisted; respects system default |
| F10 | Empty/loading/error states | Planned | Every list/screen has all three states |

## Later versions (add here as **Planned** before writing code)

| ID | Feature | Status | Notes |
|---|---|---|---|
| F11 | _to be defined_ | Not started | Added in the F11/F12 round (see PROMPTS.md) |
| F12 | _to be defined_ | Not started | Added in the F11/F12 round (see PROMPTS.md) |
| F13 | Task tags | Not started | Cold-start task (see PROMPTS.md) |

## Feature-to-doc map
| Feature | Primary docs |
|---|---|
| F1 | ARCHITECTURE.md §4 (AuthState, session persistence) |
| F2 | COMPONENTS.md §1 (AppShell, Sidebar, Topbar) |
| F3, F4 | COMPONENTS.md §2; ARCHITECTURE.md §5 (Task model) |
| F5 | ARCHITECTURE.md §4.3 (URL filters) |
| F6 | ARCHITECTURE.md §4 (TaskState sort) |
| F7 | COMPONENTS.md §3; ARCHITECTURE.md §5 (Project model) |
| F8 | COMPONENTS.md §4 |
| F9 | DESIGN_SYSTEM.md §1 (light/dark tokens); ARCHITECTURE.md §8 |
| F10 | COMPONENTS.md §5 |

## Status change log
| Date | Feature | From → To | Reason |
|---|---|---|---|
| 06-Oct-2026 | F1–F10 | (new) → Planned | Defined in prd.md v1.0 |
