# Architecture

Source of truth: `prd.md`. This doc describes stack, structure, and patterns for the TaskFlow Reflex app.
It is a plan for the code that Tasks 2+ will build. No application code exists yet.

## 1. Stack

| Layer | Choice | Notes |
|---|---|---|
| Language | Python 3.10+ | prd.md §6 |
| UI framework | Reflex (pure Python) | No React/JS unless unavoidable, logged in DECISIONS.md |
| Storage | SQLite | Local, single user |
| Auth | Mock login | No real credentials, no multi-user |
| Version control | Git + GitHub | Docs and version history |

Reflex version must be pinned in `requirements.txt` (created in Task 2). Follow the pinned version's API.

## 2. Target directory structure

```
rxconfig.py            # Reflex app config (app_name = taskflow)
requirements.txt       # pinned reflex version
.gitignore             # .web, .states, __pycache__, *.db, venv
app/
  app.py               # rx.App, routes, theme wiring
  models.py            # Task, Project (SQLite / rx.Model)
  styles.py            # design tokens + shared style helpers
  state/
    __init__.py
    auth_state.py      # AuthState
    task_state.py      # TaskState
    project_state.py   # ProjectState
    settings_state.py  # SettingsState
  pages/
    __init__.py
    login.py           # /login
    dashboard.py       # /
    tasks.py           # /tasks
    task_detail.py     # /tasks/[task_id]
    projects.py        # /projects
    settings.py        # /settings
  components/
    __init__.py
    layout.py          # app shell: sidebar, topbar, drawer
    task_card.py       # task row/card
    task_form.py       # create/edit dialog
    confirm_dialog.py  # delete confirmation
    stat_card.py       # dashboard metric card
    state_views.py     # empty / loading / error states
```

Rules (from AGENTS.md): state classes in `app/state/`, pages in `app/pages/`, reusable components in `app/components/`.

## 3. Routing

| Route | Page | Access |
|---|---|---|
| `/login` | Login | Public |
| `/` | Dashboard | Protected |
| `/tasks` | Task List | Protected |
| `/tasks/[task_id]` | Task Detail | Protected |
| `/projects` | Projects | Protected |
| `/settings` | Settings | Protected |

Protected routes: an unauthenticated user is redirected to `/login`. Guarding is done on load (e.g. in the page's `on_load` event handler), not with Python `if` at render time.

## 4. State design

One state class per domain. All data changes happen inside event handlers.

| State | Owns | Key actions |
|---|---|---|
| `AuthState` | session flag, email, login/logout | `login`, `logout`, `check_session` |
| `TaskState` | task list, filters, sort, form state | `add_task`, `update_task`, `delete_task`, `set_filter`, `set_sort` |
| `ProjectState` | project list, form state | `add_project`, `update_project`, `delete_project` |
| `SettingsState` | theme preference | `toggle_theme`, `set_theme` |

### 4.1 Reflex rules
- Use `rx.cond` (not Python `if`) and `rx.foreach` (not Python loops) when rendering over State Vars.
- Change state only inside event handlers (never during render).
- Cross-state access uses `self.get_state(...)` or direct subclassing when a state needs another state's data (see DECISIONS.md D-004).

### 4.2 Session persistence
Reflex State resets on page refresh, so the mock login session is stored in a browser cookie / local storage and rehydrated on load via a `check_session` handler (prd.md §14). This is the single mechanism that makes login survive a refresh.

### 4.3 Filters in URL
F5 requires search/filter state to live in URL query params so a filtered view survives navigation. `TaskState` reads query params on load and writes them on change (see DECISIONS.md D-003).

## 5. Data model (SQLite)

Planned models in `app/models.py` (fields finalized when Task 2/3 build them):

**Task**
| Field | Type | Rules |
|---|---|---|
| `id` | int (PK) | auto |
| `title` | str | required, 3–80 chars |
| `description` | str | optional |
| `priority` | str | `Low` / `Medium` / `High` |
| `due_date` | date | today or later |
| `status` | str | `Todo` / `In Progress` / `Done` |
| `project_id` | int (FK, nullable) | assigned project |
| `created_at` | datetime | set on create |

**Project**
| Field | Type | Rules |
|---|---|---|
| `id` | int (PK) | auto |
| `name` | str | required, unique, max 30 chars |
| `color` | str | a token value from DESIGN_SYSTEM.md |

## 6. Rendering & performance
- Target: pages respond in under 1 second with up to 500 tasks (local).
- Lists render with `rx.foreach`; avoid recomputing derived lists inside loops.
- Dashboard shows 4 metrics + next 5 due tasks; keep that query bounded.

## 7. Error / loading / empty states
Every list or data screen must render all three states (F10) using the shared `state_views` components. No page should render a bare list without an empty-state fallback.

## 8. Theming
Light and dark themes are both defined as tokens (DESIGN_SYSTEM.md). `SettingsState` toggles between them, the choice is persisted, and the system default is respected on first run (F9).

## 9. What must not change
- Stack stays Python + Reflex + SQLite. Adding a separate backend API is out of scope.
- No real authentication, multi-user support, notifications, or deployment.
- Design values come only from tokens in `app/styles.py`; pages must not hardcode colors or spacing.
