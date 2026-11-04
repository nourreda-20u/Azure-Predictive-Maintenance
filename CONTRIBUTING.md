# Collaboration Guide

1. Choose an issue and create a feature branch from `main`.
2. Work on small, reviewable commits. Do not push directly to `main`.
3. Open a pull request with clear tests, assumptions, and handover evidence.
4. Ask the downstream role to approve the handover before merging.
5. Keep raw datasets, model binaries, credentials, and SQL backups out of Git.

Suggested branches: `feature/sql-data-pipeline`, `feature/eda-preprocessing`, `feature/decision-tree-rf`, `feature/svm-evaluation`.

Branch protection and repository collaborators must be configured in GitHub settings by an administrator; this file documents the policy but does not enforce it.
