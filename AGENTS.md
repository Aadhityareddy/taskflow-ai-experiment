# TaskFlow (Reflex) - AI Instructions

prd.md is the PRD and the single source of truth. Stack: Python + Reflex (pure Python UI), SQLite.
Do NOT write React/JavaScript unless there is no Reflex-native way (log it in docs/DECISIONS.md).

## Before any work
1. Read prd.md, then docs/FEATURES.md, ARCHITECTURE.md, DESIGN_SYSTEM.md, COMPONENTS.md.
2. Skim the last 3 entries of docs/CHANGELOG.md and docs/DECISIONS.md.
3. Check the Reflex version in requirements.txt and follow that version's API.

## Rules
- Implement ONLY features marked "Planned" or explicitly requested in the task.
- Never modify features marked "Done" unless the task names them.
- Reuse components listed in docs/COMPONENTS.md before creating new ones.
- Use only design tokens from docs/DESIGN_SYSTEM.md (app/styles.py). No hardcoded colors/spacing in pages.
- No unrequested refactors, renames, or dependency changes.
- State classes in app/state/, pages in app/pages/, reusable components in app/components/.
- Reflex rules: use rx.cond (not Python `if`) and rx.foreach (not Python loops) on State Vars; change state only inside event handlers.
- Keep the app runnable with: pip install -r requirements.txt && reflex run

## After any work (mandatory)
- Update prd.md if requirements changed.
- Update docs/FEATURES.md status, docs/COMPONENTS.md, docs/CHANGELOG.md.
- Add a docs/DECISIONS.md entry for any non-obvious choice (what, why, what must not change).
- Log fixed bugs in docs/BUGS.md with root cause.
- End with a summary of files changed.
