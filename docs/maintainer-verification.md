# Verification of the function-based starter

The starter intentionally leaves `apply_tier_discount` unimplemented. Verification must distinguish a working teaching scaffold from a completed student solution.

## Checks performed

Environment: Python 3.12.

| Check | Observed result |
| --- | --- |
| `python3.12 -m tests.test_order_service` | 3/3 passed; exit 0 |
| `python3.12 -m tests.test_test_support` | 8/8 passed; exit 0 |
| `python3.12 -m acceptance_tests.test_discount_acceptance` on the starter | 0/12 passed; exit 1 with the expected NotImplementedError |
| Both pricing suites with a temporary correct integer implementation | 3/3 and 12/12 passed |
| Temporary implementation using floor rounding | Acceptance suite rejected it |
| Temporary implementation using floating-point rounding | Acceptance suite rejected it |
| Temporary implementation accepting unknown tiers | Acceptance suite rejected it |
| Temporary implementation accepting negative subtotals | Acceptance suite rejected it |

The temporary implementations were evaluated outside the repository; no student solution was committed. The class-free source and test registrations were also inspected. There is no configured linter or third-party dependency to install.

## Regression found and fixed

Before the fix, the runner reported success for an empty test list and when Python optimization disabled assertions. The new regression checks reproduced both failures (6/8 checks passed before the fix, 8/8 after). The runner now rejects both situations before running tests.

The regression suite also verifies normal success, nonzero failure status, continuing after a failed check, unexpected exceptions, expected ValueError messages, missing errors, and wrong exception types. GitHub runs the 3 existing-behavior tests and 8 runner checks; students must additionally pass the 12 feature acceptance tests to finish the assignment.
