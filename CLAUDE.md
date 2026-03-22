# Claude Operating Instructions

## Branch Policy

All work must happen on the `claude-staging` branch. Before making any changes, ensure you are on this branch. If it does not exist, create it from the current HEAD.

```bash
git checkout claude-staging 2>/dev/null || git checkout -b claude-staging
```

## What Claude is allowed to do

- Read, create, edit, and delete any file in this repository
- Stage files and create commits with appropriate commit messages
- Create new branches off `claude-staging`
- Run scripts, tests, and other local commands

## Hard limits — never do these

- **Do not merge** `claude-staging` into `main` (or any other branch)
- **Do not push** to any remote under any circumstances
- **Do not force-push** anything, ever
- **Do not modify** `CLAUDE.md` itself unless the user explicitly asks

## Workflow summary

1. Switch to `claude-staging` before touching anything.
2. Make changes freely — no need to ask for permission on individual file edits, commits, or test runs.
3. Commit regularly with clear messages so the user can review the history.
4. Stop at the boundary: local commits on `claude-staging` are the final step. Merging and pushing are the user's responsibility.
