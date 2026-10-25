# Pocket Expense Tracker

A small Python expense tracker for Assignment 2. It records income and expenses in memory, checks monthly category budgets, and summarizes spending. Data resets when the program exits; there is no database, server, or external API.

Project status: Core features and tests are ready; team collaboration and GitHub setup are in progress.

## Team and feature plan

Group size: 3. Chosen theme: Expense Tracker.

| Member | GitHub username | Assigned feature |
| --- | --- | --- |
| Member A - add full name | add username | A: transaction creation and validation (`records.py`) |
| Member B - add full name | add username | B: category budget status (`budgets.py`) |
| Member C - add full name | add username | C: monthly summaries (`summaries.py`) |

Replace every team placeholder before publishing. Each person should work from their own clone and account, use a feature branch, make at least two meaningful commits, add at least two meaningful tests, and open a PR.

## Run locally

Use Python 3.12 or later:

```sh
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -r requirements.txt
python -m expense_tracker
```

Run tests:

```sh
python -m pytest -q
```

## Team pull request rotation

After adding the real names, rotate reviews so every member authors a feature PR and reviews another member's PR. Each reviewer should leave a useful line comment. On one PR, use **Request changes**, let its author correct the same branch, and review it again before approval. The report must name the actual PRs and review comments.

## Required README conflict exercise

The README already has a shared `Project status:` line. Two members should branch from the same main revision and change that exact line to different wording. Merge the first PR. On the second branch, fetch and merge `origin/main`, resolve the conflict into one accurate status sentence, commit the resolution, push, and merge after review. Capture the actual conflict and resolution for the report.

## CI, branch rules, and Pages

The workflow in `.github/workflows/tests.yml` runs pytest on pushes and PRs. Once it appears as a status check, require that check and one PR approval in a ruleset for `main`; also block force pushes and branch deletion, and do not use a bypass for normal assignment work. A group member must capture a genuine failed run, diagnose and fix it, and then capture a passing run. The first Pages deployment should use `docs/`; make a visible change through a PR after setup and verify the live URL before writing it below.

GitHub Pages URL: add after publishing: `https://<owner>.github.io/<repository>/`

## Project structure

```text
expense_tracker/          Python app logic and interactive demo
 tests/                    pytest unit tests
 .github/workflows/        GitHub Actions CI
 docs/                     GitHub Pages project page
 report/                   report completion checklist
```

## Report

Complete `report/REPORT_CHECKLIST.md` only after the real GitHub workflow has happened. The assignment asks for one evidence-based group PDF in the repository; do not describe planned actions as completed.
