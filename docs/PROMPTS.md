# Ready-to-paste task prompts (tool-neutral)
Open a NEW chat/session for each task. Start each with: "Read AGENTS.md and prd.md first and follow them."

## Task 1 - Docs only
Create docs/ARCHITECTURE.md, DESIGN_SYSTEM.md, COMPONENTS.md, FEATURES.md, DECISIONS.md, CHANGELOG.md and BUGS.md from prd.md, for a Reflex (Python) app. Define design tokens (colors, spacing, radius, typography) in DESIGN_SYSTEM.md. Do not write application code.

## Task 2 - Skeleton
Read all files in docs/. Initialize a Reflex project with the blank template using the structure in ARCHITECTURE.md. Create requirements.txt (pin the reflex version) and .gitignore (.web, .states, __pycache__, *.db, venv). Confirm `reflex run` starts. No features yet.

## Task 3 - F1 to F3
Implement F1, F2 and F3 only. Update docs per AGENTS.md.

## Task 4 - F4 to F6
Implement F4, F5 and F6 only. Update docs per AGENTS.md.

## Task 5 - F7 to F10
Implement F7, F8, F9 and F10. Update docs per AGENTS.md.

## F11/F12 round (add them to prd.md and FEATURES.md as Planned first)
FEATURES.md lists F11 and F12 as Planned. Implement only those. Do not modify other features. Update docs.

## Design change (edit DESIGN_SYSTEM.md first)
DESIGN_SYSTEM.md was updated. Apply the new tokens everywhere through styles.py. No behavior changes.

## Bug fix (add the bug to BUGS.md first)
Fix bug #<n> in BUGS.md. Find the root cause, fix it, record it in BUGS.md. Change nothing else.

## Refactor
Extract the duplicated task card markup into a shared component in app/components/. No behavior or visual change. Update COMPONENTS.md.

## Changed behavior (edit prd.md and FEATURES.md first)
F5 changed: filters are stored in State, not the URL. Update code, remove obsolete code, update all docs.

## Cold start
Implement F13 (task tags) as described in FEATURES.md.
