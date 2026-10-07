# Components

Source of truth: `prd.md`. This is the catalog of reusable UI pieces.
Rule (AGENTS.md): reuse a component listed here before creating a new one. New components must be added to this file.

Status legend: **Planned** = designed, not built yet. **Done** = built (none yet — no code written).

## 1. Layout

### `AppShell` — `app/components/layout.py`
- **Status:** Planned
- **Purpose:** Frame every protected screen (F2).
- **Contains:** `Sidebar` (desktop), `Topbar` with hamburger + theme toggle, `Drawer` (mobile), content slot.
- **Props:** `content` (the page body).
- **Tokens:** `color_surface`, `color_border`, `space_*`, `bp_*`.
- **Notes:** Active nav link highlighted with `color_primary` / `color_primary_soft`. Sidebar collapses under `bp_desktop`. Logout lives in the sidebar/topbar.

### `Sidebar` — `app/components/layout.py`
- **Status:** Planned
- **Purpose:** Primary navigation between the six routes.
- **Contains:** nav items (Dashboard, Tasks, Projects, Settings), active-link highlight, logout.
- **Tokens:** `color_surface`, `color_primary`, `color_text_muted`, `space_4`.

### `Topbar` — `app/components/layout.py`
- **Status:** Planned
- **Purpose:** Mobile hamburger trigger, current page title, theme toggle shortcut.
- **Tokens:** `color_surface`, `color_border`, `space_4`, `shadow_sm`.

## 2. Task components

### `TaskCard` — `app/components/task_card.py`
- **Status:** Planned
- **Purpose:** Render one task in the list (F3, F4).
- **Shows:** title, priority badge, status badge, due date, project color dot.
- **Actions:** open detail, edit, delete.
- **Tokens:** `color_surface`, `color_border`, `radius_lg`, `shadow_sm`, priority/status mapping tokens, `text_lg`, `text_sm`.
- **Notes:** This is the component the "Refactor" task (PROMPTS.md) extracts duplicated markup into.

### `TaskForm` — `app/components/task_form.py`
- **Status:** Planned
- **Purpose:** Create/edit dialog form (F3, F4, §4.3 validations).
- **Fields:** title, description, priority, due date, status, project.
- **Validation:** title required 3–80 chars; due date today or later; errors inline with `color_danger`.
- **Tokens:** `radius_lg`, `shadow_lg`, `space_4`, `color_danger`.

### `ConfirmDialog` — `app/components/confirm_dialog.py`
- **Status:** Planned
- **Purpose:** Confirm destructive actions (delete task, delete project) (F3, F7).
- **Tokens:** `shadow_lg`, `radius_lg`, `color_danger`, `space_6`.

## 3. Project components

### `ProjectCard` — `app/components/project_card.py`
- **Status:** Planned
- **Purpose:** Show one project with its color swatch and task count (F7).
- **Tokens:** project color set, `radius_lg`, `shadow_sm`, `space_4`.

### `ProjectForm` — `app/components/project_form.py`
- **Status:** Planned
- **Purpose:** Create/edit project (name + color) (F7).
- **Validation:** name required, unique, max 30 chars; inline error with `color_danger`.
- **Tokens:** `color_*` project set, `space_4`, `radius_sm`.

## 4. Dashboard components

### `StatCard` — `app/components/stat_card.py`
- **Status:** Planned
- **Purpose:** One dashboard metric: total, completed, overdue (F8).
- **Tokens:** `color_surface`, `radius_lg`, `shadow_sm`, `text_3xl`, `text_sm`, `color_success`, `color_warning`.
- **Notes:** Reused three times on the dashboard with different labels/tokens.

### `UpcomingTasks` — `app/components/stat_card.py`
- **Status:** Planned
- **Purpose:** List of the next 5 tasks due (F8).
- **Contains:** up to five `TaskCard`s or a compact row variant, plus an empty state.
- **Tokens:** `space_4`, `text_lg`.

## 5. State components

### `EmptyState` — `app/components/state_views.py`
- **Status:** Planned
- **Purpose:** Message + optional action when a list has no items (F10).
- **Tokens:** `color_text_muted`, `space_8`, `text_lg`.

### `LoadingState` — `app/components/state_views.py`
- **Status:** Planned
- **Purpose:** Loading indicator shown while data loads (F10).
- **Tokens:** `color_primary`, `space_6`.

### `ErrorState` — `app/components/state_views.py`
- **Status:** Planned
- **Purpose:** Error message + retry action (F10).
- **Tokens:** `color_danger`, `space_6`, `text_lg`.

## 6. Form primitives

### `FormField` — `app/components/form_field.py`
- **Status:** Planned
- **Purpose:** Label + input + inline error wrapper used by all forms.
- **Tokens:** `color_text_muted`, `color_border`, `color_danger`, `space_2`, `radius_sm`, `text_sm`.

## 7. Component rules
- Every interactive component gets its label/aria text for accessibility.
- Components receive data via props/State Vars; they do not mutate state directly.
- Any component that renders over a collection uses `rx.foreach`; conditional rendering uses `rx.cond`.
- Style only with tokens from DESIGN_SYSTEM.md.
