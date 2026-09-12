# AGENTS.md

- Read README.md and docs/assignment.md before changing code. The assignment is the in-repository version of issue #1 and is available in template copies.
- Verify existing behavior with `python3 -m tests.test_order_service` and the feature with `python3 -m acceptance_tests.test_discount_acceptance`. Use `python` or `py` if that is the available Python 3.10+ interpreter.
- Make one bounded change at a time and inspect the diff after each change.
- Do not add dependencies, secrets, generated artifacts, or unrelated refactors.
- Do not remove, skip, or weaken tests to make the suite pass. Acceptance tests intentionally fail on the unfinished starter.
- Keep the student briefing in docs/codex-context.md and comparison evidence in docs/comparison.md; link the evidence in the pull-request description.
- Do not invent results or guarantee that the second attempt will improve on the first. Students must explain their own observations.
- Use simple functions with a subtotal and tier as inputs. Do not introduce classes or an order object. Tests are ordinary functions listed in each test module; add any new test to its run_tests list.
