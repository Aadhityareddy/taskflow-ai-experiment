# TaskFlow – Project Requirements Document (PRD)

> **This README is the single source of truth for the project.** AI tools must read it before any work and keep it in sync with the code.

## 1. Project Overview
| Field | Value |
|---|---|
| Project Name | TaskFlow |
| Project ID | TF-001 |
| Date | 06-Oct-2026 |
| Version | 1.0 (planned) |
| Prepared By | [Aadhitya Reddy Seelam] |
| Approved By | [Siddhid Gopujkar] |

### 1.1 Purpose of the Project
Build a task and project manager web app, using AI for the whole frontend lifecycle. The real goal is an experiment: can `.md` files act as persistent memory so an AI can build and evolve a UI app across many versions without losing context?

### 1.2 Project Background
AI coding tools forget earlier decisions between sessions and may drift or break existing features. This project tests whether well-structured documentation (PRD, architecture, design system, changelog, decisions) prevents that, and records what works.

### 1.3 Scope of the Project
**In-Scope**
- A Reflex (Python) web app with features F1–F10 (v1.0), then F11+ added through documentation
- Supporting docs in `docs/`, multiple tagged versions, enhancements, bug fixes, refactors
- Final recommendations on keeping AI context during UI development

**Out-of-Scope**
Real authentication, multi-user support, a separate backend API, notifications, deployment/hosting.

## 2. Stakeholders
**Primary:** Developer ([Your Name]) – builds and runs the experiment. Senior/Mentor – reviews the approach and results.
**Secondary:** The AI coding tool (acts as the implementer); future readers of the recommendations.
**Communication Plan:** Update `docs/EXPERIMENT_LOG.md` after every iteration; share a short status with the mentor weekly.

## 3. Objectives and Goals
**Key Objectives**
1. Deliver a working app with ~10 features from this PRD.
2. Add features in later versions by editing docs first, and check the AI changes only what was asked.
3. Test design changes, bug fixes, refactors, and changed behavior.
4. Produce recommendations for long-term AI context.

**Success Criteria**
- App runs with `reflex run` and every v1.0 feature meets its acceptance criteria.
- New features do not break old ones (no regressions).
- Docs match the code after each version.
- A fresh AI session can add a feature correctly using only the docs.

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

Later features (F11, F12, F13...) are added here and in `docs/FEATURES.md` as **Planned** before any code is written.

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

### 4.3 Validations
- Title: required, 3–80 characters. Due date: today or later.
- Project name: required, unique, max 30 characters.
- Errors show inline under the field using the `danger` design token.

### 4.4 User Flows
1. Login → Dashboard → "Add task" → fill dialog → save → toast → task appears in list.
2. Tasks → filter "High" → open task → change status → back (filter preserved).

## 5. Non-Functional Requirements
- **Performance:** Pages respond in under 1 second for up to 500 tasks (local use).
- **Security:** Mock auth only; no real credentials or personal data stored.
- **Usability:** Responsive (mobile and desktop); readable contrast in both themes; consistent components and tokens.
- **Availability:** Local development only.
- **Compliance:** None required.

## 6. Assumptions
- Python 3.10+ and Git are installed on the developer's machine.
- Reflex may download extra tooling (such as Node.js) on first run, so internet access is needed.
- One user, one browser.

## 7. Constraints
- Zero budget: only free AI tools and free tiers.
- Stack fixed: Python + Reflex, SQLite for storage.
- Free-tier AI limits may slow progress.

## 8. Dependencies
- GitHub (repo and version history).
- Reflex framework (version pinned in `requirements.txt`).
- A free AI coding tool (chosen by the developer; recorded in the experiment log).

## 9. Risks
| Risk | Mitigation |
|---|---|
| AI is less familiar with Reflex's API | Pin the version, keep tasks small, paste real errors back to the AI |
| AI changes unrelated features | State "implement only X" in every task; review the diff before committing |
| AI ignores the docs | Start every task with "Read AGENTS.md and README.md first"; log failures |
| Free-tier limits reached | Split work into small tasks; continue next day or switch tools |
| Docs become too long to follow | Keep each doc focused; one purpose per file |

## 10. Deliverables
1. This PRD (README.md) and supporting docs in `docs/`
2. v1.0 working app (F1–F10)
3. v1.1+ with new features, design change, bug fix, refactor, changed behavior
4. `docs/EXPERIMENT_LOG.md` with observations
5. Final recommendations for long-term AI context

## 11. Timeline
| Milestone | Target |
|---|---|
| Setup (Git, Python, repo, docs) | Week 1 |
| Supporting docs generated and reviewed | Week 1 |
| v1.0 (F1–F10) | Week 2 |
| v1.1 (F11, F12) | Week 3 |
| v1.2–v1.6 (design, bug fix, refactor, changed behavior, cold-start F13) | Week 3–4 |
| Final recommendations | Week 4 |

## 12. Budget
**Estimated Budget:** ₹0. **Breakdown:** free AI tool tier, free GitHub, free tools. **Constraint:** free-tier usage limits.

## 13. Approval & Sign-off
| Name | Role | Signature | Date |
|---|---|---|---|
| [Aadhitya Reddy Seelam] | Developer | | |
| [Siddhid Gopujkar] | Approver | | |

---

## 14. Frontend Architecture & Design (additions for this UI experiment)
```
rxconfig.py
requirements.txt
app/
  app.py          # rx.App and routes
  models.py       # Task, Project (SQLite)
  styles.py       # design tokens
  state/          # AuthState, TaskState, ProjectState, SettingsState
  pages/          # one file per screen
  components/     # reusable UI pieces
```
- One state class per domain; all changes happen in event handlers.
- Login session is stored in a cookie/local storage, because Reflex state resets on refresh.
- Design values come only from tokens in `styles.py` (documented in `docs/DESIGN_SYSTEM.md`).

## 15. Document Map (how the AI should use the docs)
| File | Purpose |
|---|---|
| `AGENTS.md` | Rules the AI must follow |
| `README.md` | Requirements (this file) |
| `docs/ARCHITECTURE.md` | Stack, structure, patterns |
| `docs/DESIGN_SYSTEM.md` | Colors, spacing, typography tokens |
| `docs/COMPONENTS.md` | Component catalog |
| `docs/FEATURES.md` | Feature status (Planned/Done) |
| `docs/CHANGELOG.md` | Version history: what changed, why, what must not change |
| `docs/DECISIONS.md` | Architecture decisions and reasons |
| `docs/BUGS.md` | Bugs and root causes |
| `docs/EXPERIMENT_LOG.md` | Observations for the final report |
| `docs/PROMPTS.md` | Ready-to-paste task prompts |
| `docs/screenshots/` | UI reference images per screen/version |

## Appendices
**Glossary**
- **PRD:** Project Requirements Document.
- **Reflex:** A Python framework for building web apps without writing JavaScript.
- **State:** Reflex class holding app data and the functions that change it.
- **Token:** A named design value (e.g., `primary`, `space-4`) reused everywhere.
- **ADR:** Architecture Decision Record.

**References**
- Reflex documentation: reflex.dev
- Project PRD template provided by the mentor
