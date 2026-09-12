# Setup and the two-attempt walkthrough

## A few useful words

| Term | Meaning in this lesson |
| --- | --- |
| GitHub | The website holding your project and its review page |
| Git | The tool that records versions of project files |
| Repository (repo) | The project files plus their version history |
| Template | Starter files from which you create your own project |
| Clone | Download your repository and its history to your computer |
| Terminal | A window where you type commands; run these commands inside your project folder |
| Branch | A named line of work, allowing attempts to be kept separately |
| Commit / commit ID (SHA) | A saved version and its unique identifier |
| Push | Upload your saved commits to GitHub |
| Diff | A display of exactly which lines changed |
| Issue | A written task; this task is also in assignment.md |
| Pull request (PR) | A page for reviewing proposed changes before combining them with main |

## Before the timed workshop

1. Sign in to GitHub (a free account is sufficient). Open the [starter repository](https://github.com/onexi/agentic-lesson-02-context-engineering), choose **Use this template → Create a new repository**, select your account as owner, and name it `context-engineering-lab`. Use the visibility requested by your instructor; public repositories are visible to everyone. Leave **Include all branches** unchecked. Create the repository. Use the template option, not Fork.
2. On **your** new repository, select **Code → HTTPS** and copy its URL. In a terminal, type `git clone ` followed by that URL. Then run `cd context-engineering-lab` (or your chosen name). You can instead use your editor's clone command. Do not clone the instructor's repository for your student submission.
3. Open that local folder in the class's configured coding environment. Confirm that your AI assistant can inspect its files. If the assistant or Python/Git is not set up, ask the instructor or TA before starting the timer.
4. Run `git --version` and `python3 --version`. Python must be 3.10 or later. On Windows, try `py --version`; on systems where Python 3 is named `python`, use `python --version`. Substitute that working command everywhere this guide says `python3`. No package installation is needed.
5. Run both test commands from the README. Expect 3 existing-behavior tests to pass and 12 acceptance tests to report errors from the unimplemented feature. That confirms the starter, not a completed assignment. A missing interpreter or import error is a setup problem; a `NotImplementedError` from `apply_tier_discount` is the expected starting state.

You may ask the assistant to help with commands, but read what each command will do. Never paste a destructive reset/clean command to switch attempts. The branch procedure below keeps both attempts.

## 0–10 minutes: understand and save the starting point

Work in pairs: the **Driver** operates the tools; the **Navigator** questions assumptions and checks evidence. Read [the assignment](assignment.md) and restate its requirements in your own words.

Run:

```bash
git status
git rev-parse HEAD
```

`git status` should say the working tree is clean (no unsaved file changes). Record the full commit ID printed by the second command outside the repository, along with your notes. Call it **START_SHA**. In commands below, replace `START_SHA` with that actual ID; it is a placeholder, not a command or variable.

## 10–20 minutes: observe the instructor

Watch the instructor inspect a file, propose a small change, and verify it. Note one constraint, one piece of evidence, and one possible failure. Use a separate demonstration so your starter remains unchanged.

## 20–35 minutes: attempt A, minimal prompt

Create your first branch:

```bash
git switch -c attempt-a
```

In a fresh AI conversation using this project, give exactly this prompt:

> Implement the customer-tier discount feature in apply_tier_discount. Inspect the project, briefly state your plan, and make the change.

Do not supply a custom project briefing yet. The assistant still has the repository and its standing instructions; this is a minimal-prompt comparison, not an experiment with no context at all. Record the plan, any files read, questions, assumptions, and your answers. Let it implement one attempt. Record both test commands and their complete output, including failures. Avoid improving A repeatedly before recording its initial result.

Inspect `git diff`. Save only relevant changed files: `git add starter/order_service.py`, plus any other reviewed, relevant files explicitly by name. Then run:

```bash
git commit -m "Record attempt A"
git rev-parse HEAD
git diff START_SHA HEAD -- starter tests acceptance_tests
git push -u origin attempt-a
```

If no files changed, skip the commit and record that fact; the branch still points to the starting version. Preserve the prompt, plan, outputs, resulting commit ID, and diff outside the repository until you add them to the final comparison. If Git asks for identity or GitHub authentication, ask the TA to help configure your own account.

## 35–65 minutes: attempt B, with a project briefing

Confirm `git status` is clean. If changes remain, save and record them before switching. Create the second branch from the original version, substituting your saved ID:

```bash
git switch -c attempt-b START_SHA
```

This preserves A on its own branch and gives B the original code. Do not merge or copy A's solution into B. Start a fresh AI conversation so the prior conversation does not supply A's solution.

Inspect the files and create `docs/codex-context.md` from [context-template.md](context-template.md). You may ask the assistant to help explain files and draft it, but verify every claim. Switch Driver/Navigator at minute 45. Save your briefing:

```bash
git add docs/codex-context.md
git commit -m "Add verified project briefing"
```

Write a precise prompt that explicitly asks the assistant to read `docs/codex-context.md`, identifies the function to complete, states the constraints and expected behavior, and requests a plan followed by implementation and both test commands. Record your exact wording. The briefing should be used explicitly; its filename alone is not evidence that the assistant read it.

Record B's first result before asking for corrections. Then make any corrections needed for a working final feature, recording each follow-up separately. The Navigator must challenge at least one assumption using an actual repository file. Compare outcomes honestly, including if A already succeeded.

## 65–80 minutes: verify and package

1. Run both test commands. A complete implementation passes all 15 tests without skips. Review the diff for integer arithmetic, preserved interfaces, and unrelated edits.
2. Create `docs/comparison.md` from [comparison-template.md](comparison-template.md). Paste both prompts, plans, and observed outputs. Link A's saved commit on GitHub (or include its diff) so its evidence survives outside your local computer.
3. Inspect `git diff` and `git status`. Stage only the reviewed implementation, briefing, comparison, and any relevant additional tests by name. Commit them with `git commit -m "Complete context engineering comparison"`.
4. Run `git diff START_SHA HEAD -- starter tests acceptance_tests` and save/link B's feature diff. Run `git rev-parse HEAD` and record the final ID. Push with `git push -u origin attempt-b`.

## 80–90 minutes: submit and reflect

On **your repository** in GitHub, open **Pull requests → New pull request**. Choose `main` as the base (starting version) and `attempt-b` as the compare branch. Review the changed files. Fill in the provided PR template and choose **Create draft pull request** from the create button's dropdown. Leave it unmerged for instructor review.

Submit the PR URL and final commit ID using the course's submission channel. Put both partners' names in the PR. A shared submission is appropriate for the pair unless the instructor requests individual submissions; the second partner can link the same PR.

In the comparison, explain what you initially misunderstood, what evidence changed your mind, and which instruction you would reuse. Each partner should be ready to trace a gold order, a rounding case, and an invalid input through the final code.
