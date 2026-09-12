# Context Engineering: Give AI the Information It Needs

MIT Agentic Computing Apprenticeship • Lesson 02 • 90-minute workshop, after setup

**Your goal:** help an AI make one small, correct change, then use evidence to compare what happened with minimal instructions and with a carefully written project briefing. No previous coding experience is assumed. Ask for explanations whenever you encounter unfamiliar code or terminology.

This project is a small Python calculation, not a website. It calculates an order total in cents. You will complete `apply_tier_discount` so that standard customers pay full price and gold customers receive a 10% discount. For example, a gold customer's $100 order should cost $90. You will not build an entire application.

## Two simple functions

`total_cents(10000)` checks the price and returns `10000` unchanged. The function you complete is called like this:

```python
apply_tier_discount(10000, "gold")  # Should return 9000 when implemented.
apply_tier_discount(10000)          # Default tier is standard; should return 10000.
```

The arguments are a whole number of cents and a tier name. There are no classes, objects to construct, or factory functions to learn.

## Start here

1. Follow [Setup and the two-attempt walkthrough](docs/student-guide.md). It explains GitHub terms, copying the project, running checks, saving each attempt, and submitting your work.
2. Read [Your assignment and definition of success](docs/assignment.md). This is the complete task, including requirements formerly available only in [issue #1](https://github.com/onexi/agentic-lesson-02-context-engineering/issues/1). GitHub does not copy issues when you create a repository from a template.
3. Use [the comparison worksheet](docs/comparison-template.md) to record evidence.

## What counts as success?

- **The feature works:** both commands below finish with `OK`, with no failures, errors, or skipped tests. The acceptance examples in [the assignment](docs/assignment.md) all hold.
- **You explain the project:** create `docs/codex-context.md` using [the briefing outline](docs/context-template.md), with verified file references and observed commands/results.
- **You compare two attempts fairly:** start each from the same saved version; record both exact prompts, plans, changes, and test results. Discuss at least three observations. An honest tie or a worse second result is acceptable; do not invent improvements.
- **You understand the result:** both partners can explain each changed file and trace an example through the calculation.
- **You submit reviewable evidence:** a draft pull request in your own repository links both attempts and includes the completed checklist and comparison. Submit its URL and final commit ID.

The minimally prompted attempt may fail. That is useful evidence and does not by itself make the lesson unsuccessful. The final submitted implementation must satisfy the requirements.

## The two checks

Run these in the project's terminal (see setup for choosing your Python command):

```bash
python3 -m tests.test_order_service
python3 -m acceptance_tests.test_discount_acceptance
```

The first command checks existing behavior: **3 tests pass in the starter**. The second checks the assigned feature: **12 tests initially fail because the feature is unfinished**. A completed feature reports `3/3 tests passed` and `12/12 tests passed`, each followed by `OK`. Do not delete, skip, or weaken checks to obtain a pass.

The automatic GitHub workflow checks existing behavior and the test runner so the unfinished template stays usable. **A green GitHub check alone does not mean the assignment is complete.** Include output from both commands in your submission.

## Files you will encounter

| File or folder | Purpose |
| --- | --- |
| `starter/order_service.py` | The small calculation you will improve |
| `docs/domain-rules.md` | Exact pricing policy |
| `tests/` | Checks that existing behavior still works |
| `acceptance_tests/` | Checks defining completion of the feature |
| `test_support.py` | Small helpers that run the ordinary test functions |
| `AGENTS.md` | Standing instructions for the AI assistant |
| `docs/codex-context.md` | The project briefing you create for attempt B |
| `docs/comparison.md` | The completed comparison you submit |

There are no third-party dependencies, installation commands, web server, or configured lint tool. Python 3.10 or later and Git are sufficient for local work. Tests are the way to run and verify this project. Each test is an ordinary function. An `assert` checks that a statement is true; the test runner prints `PASS` or `FAIL` and exits with an error if a test fails. Use the exact commands above; do not add Python’s `-O` option, which disables assertions. The runner rejects optimized Python and empty test lists.

## Instructor note

This repository uses one 90-minute sequence, two implemented attempts, and one briefing filename: `docs/codex-context.md`. Use these repository instructions if the [original lesson brief](https://docs.google.com/document/d/1U0RULD0rD95nlXe9mARu8VRwdfSD7N0EaEUJSo_duO4/edit) differs. The original brief's `CONTEXT.md` refers to this same deliverable; students should not create two briefings. Setup should be completed before the timed workshop. Lesson 02 is the course identifier even when this is a student's first coding exercise.

[Fall 2026 course schedule](https://docs.google.com/spreadsheets/d/1JMbgBQlmLbLhXaRGhf5DeWaE31Wu0ROAByPyzyIxn9E/edit?usp=sharing)

Maintainer check: `python3 -m tests.test_test_support` verifies the test runner itself (8 checks). GitHub also runs these checks. They are separate from the 15 student feature/compatibility tests.
