# Lesson 02: Context Engineering for Codex

Starter repository for the MIT Agentic Computing Apprenticeship.

## Challenge

Build a verified context packet and use it to make a convention-aligned change.

- [Open the lesson challenge brief](https://docs.google.com/document/d/1U0RULD0rD95nlXe9mARu8VRwdfSD7N0EaEUJSo_duO4/edit)
- [Open the Fall 2026 course schedule](https://docs.google.com/spreadsheets/d/1JMbgBQlmLbLhXaRGhf5DeWaE31Wu0ROAByPyzyIxn9E/edit?usp=sharing)
- Start with GitHub issue #1.

## Apprentice loop

1. **Observe** — inspect the repository and issue before editing.
2. **Imitate** — reproduce the instructor's smallest verified move.
3. **Extend** — implement one bounded component at a time with Codex.
4. **Reflect** — explain what evidence changed your plan.

## Run the baseline

```bash
python -m unittest discover -s tests -v
```

The baseline tests pass. A skipped challenge test documents part of issue #1. Enable it only when you are ready to observe the expected failure.

## Definition of done

- Issue acceptance criteria are satisfied.
- Challenge test is enabled and the full suite passes.
- The diff contains no unrelated changes.
- The pull request records the commands and observed results.
- Every team member can explain the final control flow.
