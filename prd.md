# TaskFlow – Project Requirements Document (PRD)

> **`PRD.md` is the only documentation file and the single source of truth.** AI tools must read the whole file before any work and update the relevant sections after any work (rules in Section 21).

| Section | Contents |
|---|---|
| 1–13 | Project requirements (mentor's PRD template) |
| 14 | Frontend architecture |
| 15 | Design system (tokens) |
| 16 | Component catalog |
| 17 | Feature status (Planned / Done) |
| 18 | Decisions log |
| 19 | Version history |
| 20 | Bug log |
| 21 | AI working rules |
| 22 | Screenshot index |

---

## 1. Project Overview
| Field | Value |
|---|---|
| Project Name | TaskFlow |
| Project ID | TF-001 |
| Date | 06-Oct-2026 |
| Version | 1.0 (planned); current build v0.2 (skeleton) |
| Prepared By | Aadhitya Reddy Seelam |
| Approved By | Siddhid Gopujkar |

### 1.1 Purpose of the Project
Build a task and project manager web app, using AI for the whole frontend lifecycle. The real goal is an experiment: can one `.md` file act as persistent memory so an AI can build and evolve a UI app across many versions without losing context?

### 1.2 Project Background
AI coding tools forget earlier decisions between sessions and may drift or break existing features. This project tests whether a well-structured single PRD (requirements, architecture, design system, components, decisions, history) prevents that, and records what works.

### 1.3 Scope of the Project
**In-Scope**
- A Reflex (Python) web app with features F1–F10 (v1.0), then F11+ added through this PRD
- Multiple tagged versions, enhancements, bug fixes, refactors
- Final recommendations on keeping AI context during UI development

**Out-of-Scope**
Real authentication, multi-user support, a separate backend API, notifications, deployment/hosting.

## 2. Stakeholders
**Primary:** Aadhitya Reddy Seelam (Developer) builds and runs the experiment. Siddhid Gopujkar (Approver) reviews the approach and results.
**Secondary:** The AI coding tool (implementer); future readers of the recommendations.
**Communication Plan:** Record observations after every iteration in the experiment log (kept outside the repo); share a short status with the mentor weekly.

## 3. Objectives and Goals
**Key Objectives**
1. Deliver a working app with ~10 features from this PRD.
2. Add features in later versions by editing this PRD first, and check the AI changes only what was asked.
3. Test design changes, bug fixes, refactors, and changed behavior.
4. Produce recommendations for long-term AI context.

**Success Criteria**
- App starts with `reflex run` in the chosen environment and every v1.0 feature meets its acceptance criteria.
- New features do not break old ones (no regressions).
- This PRD matches the code after each version.
- A fresh AI session can add a feature correctly using only this PRD.

## 4. Functional Requirements

### 4.1 Features (v1.0)
| ID | Feature | Acceptance criteria |
|---|---|---|
| F1 | Mock login | Email + password (min 6 chars); inline errors; redirect to Dashboard; protected routes; login survives page refresh |
| F2 | App shell & navigation | Responsive sidebar, active-link highlight, logout |
| F3 | Task CRUD | Create/edit via dialog form; delete with confirm dialog |
| F4 | Task fields | Title, description, priority (Low/Medium/High), due date, status (Todo/In Progress/Done) |
| F5 | Search & filter | Search by title; filter by status and priority; filters kept in URL query params |
| F6 | Sort | By due date, priority, created date; ascending/descending |
| F7 | Projects | CRUD projects (name + color); assign a task to a project |
| F8 | Dashboard | Cards for total, completed, overdue; list of next 5 due tasks |
| F9 | Dark/light theme | Toggle in Settings; persisted; respects system default |
| F10 | Empty/loading/error states | Every list/screen has all three states |

Later features (F11, F12, F13...) are added here and in Section 17 as **Planned** before any code is written.

### 4.2 Screens & Navigation
| Route | Screen | Purpose |
|---|---|---|
| /login | Login | Mock auth |
| / | Dashboard | Stats + next 5 due tasks |
| /tasks | Task List | Search, filter, sort, CRUD |
| /tasks/[task_id] | Task Detail | View/edit one task |
| /projects | Projects | Manage projects |
| /settings | Settings | Theme, profile |

Sidebar on desktop, drawer/hamburger on mobile. Unauthenticated users go to /login.

### 4.3 Validations and Business Rules
- Title: required, 3–80 characters.
- Due date: today or later. Checked only when the date is set or changed, so other fields of an overdue task can still be edited.
- Project name: required, unique, max 30 characters.
- Errors show inline under the field using the `color_danger` token.
- Priority sorts by rank (Low=1, Medium=2, High=3), not alphabetically.
- Deleting a project keeps its tasks; their project is cleared (set to null).
- A project's color is stored as a design token name (for example `color_success`), so it adapts to the dark theme.

### 4.4 User Flows
1. Login → Dashboard → "Add task" → fill dialog → save → toast → task appears in list.
2. Tasks → filter "High" → open task → change status → back (filter preserved).

### 4.5 UI Requirements
- **Layout:** persistent sidebar on desktop, collapsed sidebar on tablet, drawer/hamburger on mobile.
- **Theme:** light and dark themes, both readable; every value comes from the tokens in Section 15.
- **Responsive:** single column on mobile, multi-column on desktop.
- **Feedback:** toast after save/delete, inline validation errors, and an empty, loading and error state on every list.
- **Accessibility basics:** labeled inputs, visible keyboard focus, readable contrast.

## 5. Non-Functional Requirements
- **Performance:** Pages respond in under 1 second for up to 500 tasks (local use).
- **Security:** Mock auth only; no real credentials or personal data stored.
- **Usability:** Responsive; readable contrast in both themes; consistent components and tokens.
- **Availability:** Development and demo use only.
- **Compliance:** None required.

## 6. Assumptions
- The app is built by an AI coding platform (OpenHands Cloud) working on this GitHub repository.
- How the app is run and viewed (cloud workspace, Codespaces, or a computer with Python 3.10+) is to be confirmed with the mentor.
- Reflex may download extra tooling (such as Node.js) on first run, so internet access is needed.
- One user, one browser.

## 7. Constraints
- Zero budget: only free AI tools and free tiers.
- Stack fixed: Python + Reflex, SQLite for storage.
- Free-tier AI limits (for example, 20 OpenHands conversations per day) may slow progress.

## 8. Dependencies
- GitHub (repo and version history).
- Reflex framework, pinned to `0.9.12` in `requirements.txt`.
- OpenHands Cloud as the AI coding tool (tool and model are recorded in the experiment log).

## 9. Risks
| Risk | Mitigation |
|---|---|
| AI is less familiar with Reflex's API | Pin the version, keep tasks small, paste real errors back to the AI |
| AI changes unrelated features | State "implement only X" in every task; review the diff before merging |
| AI ignores this PRD | Start every task with "Read PRD.md first and follow Section 21"; log failures |
| AI-written content contains mistakes | Review every AI change to this PRD before merging; log what was fixed |
| One long file gets skimmed | Stable section numbers, short tables, logs at the end; record file length per version |
| Free-tier limits reached | Split work into small tasks; continue next day or switch tools |

## 10. Deliverables
1. This PRD (`PRD.md`), the only documentation file
2. v1.0 working app (F1–F10)
3. v1.1+ with new features, design change, bug fix, refactor, changed behavior
4. Experiment log with observations (kept outside the repo)
5. Final recommendations for long-term AI context

## 11. Timeline
| Milestone | Target |
|---|---|
| Setup (repo, AI tool, PRD) | Week 1 |
| Skeleton running (v0.2) | Week 1 |
| v1.0 (F1–F10) | Week 2 |
| v1.1 (F11, F12) | Week 3 |
| v1.2–v1.6 (design, bug fix, refactor, changed behavior, cold-start F13) | Week 3–4 |
| Final recommendations | Week 4 |

## 12. Budget
**Estimated Budget:** ₹0. **Breakdown:** free AI tool tier, free GitHub, free tools. **Constraint:** free-tier usage limits.

## 13. Approval & Sign-off
| Name | Role | Signature | Date |
|---|---|---|---|
| Aadhitya Reddy Seelam | Developer | | |
| Siddhid Gopujkar | Approver | | |

---

## 14. Frontend Architecture

### 14.1 Stack
| Layer | Choice | Notes |
|---|---|---|
| Language | Python 3.10+ | |
| UI framework | Reflex 0.9.12 (pure Python) | No React/JS unless unavoidable; log it in Section 18 |
| Storage | SQLite | Local, single user |
| Auth | Mock login | No real credentials, no multi-user |
| Version control | Git + GitHub | |

### 14.2 Directory structure
```
rxconfig.py            # app_name = "app"
requirements.txt       # reflex==0.9.12
.gitignore             # .web, .states, __pycache__, *.db, venv, reflex.lock
app/
  app.py               # rx.App, routes, theme wiring
  models.py            # Task, Project (SQLite / rx.Model)
  styles.py            # design tokens (Section 15) + shared style helpers
  state/
    auth_state.py      # AuthState
    task_state.py      # TaskState
    project_state.py   # ProjectState
    settings_state.py  # SettingsState
  pages/
    login.py           # /login
    dashboard.py       # /
    tasks.py           # /tasks
    task_detail.py     # /tasks/[task_id]
    projects.py        # /projects
    settings.py        # /settings
  components/
    layout.py          # AppShell, Sidebar, Topbar
    task_card.py       # TaskCard
    task_form.py       # TaskForm
    confirm_dialog.py  # ConfirmDialog
    project_card.py    # ProjectCard
    project_form.py    # ProjectForm
    stat_card.py       # StatCard, UpcomingTasks
    state_views.py     # EmptyState, LoadingState, ErrorState
    form_field.py      # FormField
```
Rules: state classes in `app/state/`, pages in `app/pages/`, reusable components in `app/components/`.

### 14.3 Routing
All routes in Section 4.2 are protected except `/login`. An unauthenticated user is redirected to `/login`. Guarding runs on page load (the page's `on_load` event handler), not with a Python `if` at render time.

### 14.4 State design
One state class per domain. All data changes happen inside event handlers.
| State | Owns | Key actions |
|---|---|---|
| `AuthState` | session flag, email | `login`, `logout`, `check_session` |
| `TaskState` | task list, filters, sort, form state | `add_task`, `update_task`, `delete_task`, `set_filter`, `set_sort` |
| `ProjectState` | project list, form state | `add_project`, `update_project`, `delete_project` |
| `SettingsState` | theme preference | `toggle_theme`, `set_theme` |

- Use `rx.cond` (not Python `if`) and `rx.foreach` (not Python loops) on State Vars.
- Change state only inside event handlers, never during render.
- Cross-state access uses `self.get_state(...)` or subclassing when one state needs another's data.
- **Session persistence:** Reflex state resets on refresh, so the mock login is stored in a cookie/local storage and restored on load by `check_session`.
- **Filters in URL:** search, status filter, priority filter and sort live in URL query params; `TaskState` reads them on load and writes them on change.

### 14.5 Data model (SQLite)
**Task:** `id` (int, PK), `title` (str, 3–80), `description` (str, optional), `priority` (Low/Medium/High), `due_date` (date), `status` (Todo/In Progress/Done), `project_id` (int, nullable FK), `created_at` (datetime).
**Project:** `id` (int, PK), `name` (str, unique, max 30), `color` (token name from Section 15.1).
Business rules are in Section 4.3. Tables are created with Reflex migration commands (`reflex db init`, `reflex db makemigrations`, `reflex db migrate`); record the exact commands here when models are first added.

### 14.6 Rendering, states and theming
- Lists render with `rx.foreach`; the dashboard query stays bounded (3 metrics + next 5 tasks).
- Every list or data screen renders loading, empty and error states using the components in Section 16 (F10).
- Light and dark themes are both defined as tokens (Section 15). `SettingsState` toggles them, the choice is persisted, and the system default is respected on first run (F9).

### 14.7 What must not change
- Stack stays Python + Reflex + SQLite. No separate backend API.
- No real authentication, multi-user support, notifications, or deployment.
- Design values come only from `app/styles.py`; pages never hardcode colors or spacing.

## 15. Design System

Tokens are `snake_case` constants in `app/styles.py`. A token value changed here is the only sanctioned way to change the visual design.

### 15.1 Colors (light / dark)
| Role | Light token = value | Dark token = value | Use |
|---|---|---|---|
| Primary | `color_primary` `#4F46E5` | `color_primary_dark` `#818CF8` | Primary actions, active nav, links |
| Primary hover | `color_primary_hover` `#4338CA` | `color_primary_hover_dark` `#A5B4FC` | Hover/pressed |
| Primary soft | `color_primary_soft` `#EEF2FF` | `color_primary_soft_dark` `#312E81` | Tint backgrounds |
| Accent | `color_accent` `#0EA5E9` | `color_accent_dark` `#38BDF8` | Secondary highlight |
| Background | `color_bg` `#F8FAFC` | `color_bg_dark` `#0B1120` | App background |
| Surface | `color_surface` `#FFFFFF` | `color_surface_dark` `#111827` | Cards, dialogs, sidebar |
| Border | `color_border` `#E2E8F0` | `color_border_dark` `#1F2937` | Borders, dividers |
| Text | `color_text` `#0F172A` | `color_text_dark` `#F1F5F9` | Primary text |
| Muted text | `color_text_muted` `#64748B` | `color_text_muted_dark` `#94A3B8` | Labels, secondary text |
| Success | `color_success` `#16A34A` | `color_success_dark` `#4ADE80` | Done status, positive metric |
| Warning | `color_warning` `#D97706` | `color_warning_dark` `#FBBF24` | Overdue, medium priority |
| Danger | `color_danger` `#DC2626` | `color_danger_dark` `#F87171` | Errors, delete, high priority, inline validation |
| Info | `color_info` `#2563EB` | `color_info_dark` `#60A5FA` | In-progress status, info |

Contrast: use warning, success and accent for icons, badges on tinted backgrounds, or large text, not small body text on white.

**Priority/status mapping:** Low and Todo use `color_text_muted`; Medium uses `color_warning`; High uses `color_danger`; In Progress uses `color_info`; Done uses `color_success`.
**Project colors** come from this fixed set: `color_primary`, `color_accent`, `color_success`, `color_warning`, `color_danger`, `color_info`.

### 15.2 Spacing (4px scale)
`space_0` 0, `space_1` 4px, `space_2` 8px, `space_3` 12px, `space_4` 16px, `space_5` 20px, `space_6` 24px, `space_8` 32px, `space_10` 40px, `space_12` 48px.
Common uses: card padding `space_6`; gap between form fields `space_4`; section separation `space_8`; page padding `space_6` (mobile) and `space_8` (desktop).

### 15.3 Radius
`radius_sm` 4px (inputs, chips), `radius_md` 8px (buttons, badges), `radius_lg` 12px (cards, dialogs), `radius_full` 9999px (pills, avatars).

### 15.4 Typography
Font family `font_family`: `Inter, system-ui, sans-serif`.
| Token | Size / line height | Weight | Use |
|---|---|---|---|
| `text_xs` | 12 / 16 | 400 | Captions, helper text |
| `text_sm` | 14 / 20 | 400 | Body small, labels |
| `text_base` | 16 / 24 | 400 | Body |
| `text_lg` | 18 / 28 | 500 | Card titles |
| `text_xl` | 20 / 28 | 600 | Section headings |
| `text_2xl` | 24 / 32 | 600 | Page titles |
| `text_3xl` | 30 / 36 | 700 | Dashboard metric values |

Weights: `weight_regular` 400, `weight_medium` 500, `weight_semibold` 600, `weight_bold` 700.

### 15.5 Elevation, borders, breakpoints
- `shadow_sm` `0 1px 2px rgba(15,23,42,0.06)` (inputs, subtle cards); `shadow_md` `0 4px 12px rgba(15,23,42,0.10)` (cards, dropdowns); `shadow_lg` `0 12px 32px rgba(15,23,42,0.16)` (dialogs, drawer); `border_width` 1px.
- `bp_mobile` 0–767px (drawer nav, single column); `bp_tablet` 768–1023px (collapsed sidebar); `bp_desktop` 1024px+ (persistent sidebar, multi-column).

### 15.6 Usage rules
- Reference tokens only. No raw hex, px or font sizes in pages or components.
- Theme-dependent UI uses the light/dark pair selected by `SettingsState`.
- A new token means editing this section first, then `app/styles.py`, then the code that uses it.

## 16. Component Catalog

Status: **Planned** (designed, not built) or **Done** (built). Reuse a listed component before creating a new one, and add every new component here.

| Component | File (`app/components/`) | Purpose | Key tokens | Status |
|---|---|---|---|---|
| `AppShell` | `layout.py` | Frame for every protected screen; contains Sidebar, Topbar (hamburger + theme toggle), mobile Drawer, content slot (F2) | `color_surface`, `color_border`, `space_*`, `bp_*` | Planned |
| `Sidebar` | `layout.py` | Navigation (Dashboard, Tasks, Projects, Settings), active-link highlight, logout | `color_primary`, `color_primary_soft`, `color_text_muted` | Planned |
| `Topbar` | `layout.py` | Mobile hamburger, page title, theme toggle shortcut | `color_surface`, `shadow_sm` | Planned |
| `TaskCard` | `task_card.py` | One task: title, priority badge, status badge, due date, project dot; actions open/edit/delete (F3, F4). The Refactor round extracts duplicated markup into this | `radius_lg`, `shadow_sm`, priority/status tokens | Planned |
| `TaskForm` | `task_form.py` | Create/edit dialog: title, description, priority, due date, status, project; validation per Section 4.3 | `radius_lg`, `shadow_lg`, `color_danger` | Planned |
| `ConfirmDialog` | `confirm_dialog.py` | Confirm delete of task or project (F3, F7) | `shadow_lg`, `color_danger` | Planned |
| `ProjectCard` | `project_card.py` | Project with color swatch and task count (F7) | project colors, `radius_lg` | Planned |
| `ProjectForm` | `project_form.py` | Create/edit project (name + color); validation per Section 4.3 | project colors, `radius_sm` | Planned |
| `StatCard` | `stat_card.py` | One dashboard metric (total, completed, overdue); used three times (F8) | `text_3xl`, `color_success`, `color_warning` | Planned |
| `UpcomingTasks` | `stat_card.py` | Next 5 tasks due, with empty state (F8) | `space_4`, `text_lg` | Planned |
| `EmptyState` | `state_views.py` | Message + optional action for an empty list (F10) | `color_text_muted`, `space_8` | Planned |
| `LoadingState` | `state_views.py` | Loading indicator (F10) | `color_primary` | Planned |
| `ErrorState` | `state_views.py` | Error message + retry (F10) | `color_danger` | Planned |
| `FormField` | `form_field.py` | Label + input + inline error wrapper for all forms | `color_border`, `color_danger`, `space_2` | Planned |

Component rules:
- Interactive components have label/aria text for accessibility.
- Components receive data via props/State Vars and never mutate state directly.
- Collections render with `rx.foreach`; conditions use `rx.cond`.
- Style only with tokens from Section 15.

## 17. Feature Status

Values: **Planned**, **In Progress**, **Done**. Implement only features that are **Planned** or explicitly requested; never modify a **Done** feature unless the task names it.

| ID | Feature | Status | Version | Notes |
|---|---|---|---|---|
| F1 | Mock login | Planned | | Architecture 14.4 (AuthState, session persistence) |
| F2 | App shell & navigation | Planned | | Components `AppShell`, `Sidebar`, `Topbar` |
| F3 | Task CRUD | Planned | | `TaskCard`, `TaskForm`, `ConfirmDialog` |
| F4 | Task fields | Planned | | Data model 14.5 |
| F5 | Search & filter | Planned | | URL query params (D-003) |
| F6 | Sort | Planned | | Priority rank rule in 4.3 |
| F7 | Projects | Planned | | `ProjectCard`, `ProjectForm` |
| F8 | Dashboard | Planned | | `StatCard`, `UpcomingTasks`; 3 metrics |
| F9 | Dark/light theme | Planned | | Tokens 15.1; `SettingsState` |
| F10 | Empty/loading/error states | Planned | | `EmptyState`, `LoadingState`, `ErrorState` |
| F11 | _to be defined_ | Not started | | Added in the F11/F12 round |
| F12 | _to be defined_ | Not started | | Added in the F11/F12 round |
| F13 | _to be defined_ | Not started | | Cold-start round |

| Date | Feature | From → To | Reason |
|---|---|---|---|
| 06-Oct-2026 | F1–F10 | (new) → Planned | Defined in this PRD v1.0 |

## 18. Decisions Log

Add an entry for any non-obvious choice. Newest first. Each states what, why, and what must not change.

**D-007 — Single `PRD.md`, no other documentation files (07-Oct-2026)**
- **What:** All requirements, architecture, design system, components, decisions, history, bugs and AI rules live in this file.
- **Why:** The team lead asked for one `.md` file, and it tests whether one file can carry all the context.
- **Must not change:** Do not create other `.md` files. Update only the sections affected by a change.

**D-006 — Reflex blank template, app_name `app`, version 0.9.12 (07-Oct-2026)**
- **What:** The skeleton is a Reflex blank template with `app_name = "app"`, so imports are `from app import ...`. Reflex is pinned to `0.9.12`. `app/styles.py` holds all tokens from Section 15.
- **Why:** Section 14.2 fixes the package name as `app`. Pinning follows the working rules. Creating `styles.py` early gives later tasks one place for design values.
- **Must not change:** Later code follows the 0.9.12 API. The package stays `app/`. No React/JS. Design values stay only in `app/styles.py`.

**D-005 — Mock auth with cookie/local-storage session**
- **What:** Login is fake (any email + password of 6+ chars); the session is a cookie/local-storage flag restored on load.
- **Why:** Reflex state resets on refresh, so F1's "login survives refresh" needs a client-side marker. Real auth is out of scope.
- **Must not change:** No real credentials, tokens or personal data are stored.

**D-004 — One state class per domain**
- **What:** Separate `AuthState`, `TaskState`, `ProjectState`, `SettingsState`.
- **Why:** Isolates each domain, keeps tasks small, and reduces the chance the AI edits unrelated features.
- **Must not change:** Data changes only inside event handlers of the owning state.

**D-003 — Filters stored in URL query params**
- **What:** Search, status filter, priority filter and sort live in the URL query string (F5, F6).
- **Why:** The flow "open task → change status → back (filter preserved)" needs the filtered view to survive navigation.
- **Must not change:** This is v1.0 behavior. A later "changed behavior" round may move filters into State; the entry is then superseded, not deleted.

**D-002 — Pure-Python Reflex UI; no JavaScript**
- **What:** The entire UI is built with Reflex Python components.
- **Why:** The stack is fixed as Python + Reflex, and avoiding React is part of the experiment.
- **Must not change:** Do not introduce React/JS. If no Reflex-native way exists, log a new decision explaining the exception first.

**D-001 — PRD-first workflow**
- **What:** Requirements and design are written or updated in this PRD before code, and the PRD is updated after every change.
- **Why:** This is the core experiment (Section 1.1).
- **Must not change:** Code follows the PRD, not the other way around.

## 19. Version History

Newest first. Each entry states what changed, why, and what must not change.

**v0.3 — Single PRD (docs only), 07-Oct-2026**
- **What changed:** Merged the separate docs and AGENTS.md into this one file (Sections 14–22). Added UI requirements, business rules and component summary to Section 4.
- **Why:** Team lead asked for a single `.md` file.
- **Must not change:** Requirements and tokens carry over unchanged from v0.1/v0.2. F1–F10 stay **Planned**.

**v0.2 — Skeleton (no features), 07-Oct-2026**
- **What changed:** Initialized a Reflex app with the blank template (`reflex==0.9.12`) shaped to Section 14.2: `rxconfig.py` (app_name `app`), `app/app.py` (app object + placeholder page), `app/styles.py` (all Section 15 tokens), empty `app/state/`, `app/pages/`, `app/components/` packages. Added `.gitignore`. Confirmed `reflex run` starts (frontend 3000, backend 8000).
- **Why:** Make the project runnable before any feature work.
- **Must not change:** The pinned Reflex version. Design values only in `app/styles.py`. No features exist; `app/app.py` renders only a placeholder heading.
- **Follow-ups:** F1–F3, then F4–F6, F7–F10. Database migration commands are recorded in Section 14.5 when models are first added.

**v0.1 — Supporting docs (docs only), 06-Oct-2026**
- **What changed:** Created architecture, design system, components, features, decisions, changelog and bug documents from the PRD, with design tokens defined.
- **Why:** Give the AI a documented context before any code.
- **Must not change:** The PRD is the source of truth. Tokens are the only source of design values.

| Planned version | Change |
|---|---|
| v1.0 | Build F1–F10 |
| v1.1 | Add F11, F12 via this PRD |
| v1.2 | Design change |
| v1.3 | Bug fix |
| v1.4 | Refactor |
| v1.5 | Changed behavior (F5 filters) |
| v1.6 | Cold-start F13 |

## 20. Bug Log

No bugs yet. Each entry records the symptom, the **root cause**, the fix and the version.

**Open:** none. **Fixed:** none.

Template:
```
Bug #<n> — <short title>
- Version: v<x.y>   Status: Open | Fixed
- Symptom: what the user saw
- Steps to reproduce: ...
- Root cause: the actual reason, not just where it surfaced
- Fix: what changed
- Prevention: what stops it recurring (test, rule)
```

## 21. AI Working Rules

**Before any work**
1. Read this whole file. Check the Reflex version in `requirements.txt` and follow that version's API.

**Rules**
- Implement ONLY features marked **Planned** (Section 17) or explicitly requested in the task.
- Never modify **Done** features unless the task names them.
- Reuse components in Section 16 before creating new ones.
- Use only tokens from Section 15 (`app/styles.py`). No hardcoded colors or spacing in pages.
- No unrequested refactors, renames or dependency changes.
- Folder rules in Section 14.2; Reflex rules in Section 14.4 (`rx.cond`, `rx.foreach`, state changes only in event handlers).
- No React/JS unless logged in Section 18.
- Keep the app runnable with `pip install -r requirements.txt && reflex run`.
- Do NOT create other `.md` files. Edit only the sections of this file that your change affects; do not rewrite or reformat the whole file.

**After any work (mandatory)**
- Update Section 17 (status and version), Section 16 (components), Section 19 (version history).
- Add a Section 18 entry for any non-obvious choice. Log fixed bugs in Section 20 with root cause.
- If requirements changed, update Sections 4 and 14 first.
- End with a summary of files changed.

## 22. Screenshot Index

Images are stored in the `screenshots/` folder (images are not `.md` files). Record each one here.
| Screen | Version | File | Notes |
|---|---|---|---|
| _none yet_ | | | |

---

## Appendices
**Glossary**
- **PRD:** Project Requirements Document.
- **Reflex:** A Python framework for building web apps without writing JavaScript.
- **State:** Reflex class holding app data and the functions that change it.
- **Token:** A named design value (for example `color_primary`, `space_4`) reused everywhere.

**References**
- Reflex documentation: reflex.dev
- Project PRD template provided by the mentor
