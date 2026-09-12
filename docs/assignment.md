# Your assignment: make the customer discount correct

## The task in plain language

Complete `apply_tier_discount(order)` in `starter/order_service.py`. It receives an order containing a price in cents and a customer tier, then returns the amount that customer should pay as an integer number of cents. An invalid order must produce an explanatory error.

Use [domain-rules.md](domain-rules.md) as the pricing authority. Keep `Order`, `total_cents`, and the existing function signatures unchanged. Do not add dependencies or build extra features.

## Acceptance examples

These examples define observable success. A `ValueError` means the function rejects an invalid input instead of returning a price.

| Subtotal (cents) | Tier | Required result |
| --- | --- | --- |
| 10000 | standard | 10000 |
| 123 | omitted (default) | 123 |
| 10000 | gold | 9000 |
| 5 | gold | 5 (4.5 rounds up) |
| 15 | gold | 14 (13.5 rounds up) |
| 6 | gold | 5 (5.4 rounds down) |
| 1 | gold | 1 (0.9 rounds up) |
| 0 | standard or gold | 0 |
| -1 | standard or gold | `ValueError`; message explains non-negative subtotal requirement |
| 100 | silver or Gold | `ValueError`; message identifies unknown/unsupported tier |
| 0 | empty string | `ValueError`; message identifies unknown/unsupported tier |
| 10000000000000015 | gold | 9000000000000014, with no loss of precision |

Check these with `python3 -m unittest discover -s acceptance_tests -v`. Existing behavior must also pass `python3 -m unittest discover -s tests -v`. Each command must finish with `OK` and no skips. Review the code as well: passing examples alone cannot prove that integer arithmetic is used throughout or that the implementation is sensible for other valid inputs.

## Learning deliverables

1. **Project briefing:** `docs/codex-context.md`, written after inspecting the repository. Include purpose/users, file map, actual run/test commands, conventions, protected files, exact task, acceptance criteria, and resolved/unresolved questions. Cite the file supporting each claim. Use [context-template.md](context-template.md) as an outline, not as an already completed answer.
2. **Two recorded attempts:** the exact prompt, plan, starting commit ID, resulting commit ID/diff, test output, and corrections for each attempt. Preserve attempt A even if it fails. Attempt B starts from the same original code and uses your briefing.
3. **Working final feature:** attempt B may be corrected after its initial result is recorded. Label those corrections separately so the comparison remains honest.
4. **Evidence-based comparison:** complete `docs/comparison.md` using [comparison-template.md](comparison-template.md). Discuss at least three observations, which may be differences or similarities. Report whether better context helped; do not assume it did. This is a small classroom comparison, not proof of a general causal effect.
5. **Draft pull request:** in your own repository, from your final branch into `main`, with links to the above. Submit its URL and final commit ID. Both partners must be able to explain every changed file, the standard/gold paths, one rounding example, and an invalid-input example.

## Completion checklist

- [ ] All 3 existing-behavior tests and all 12 acceptance tests pass; no tests removed, weakened, or skipped.
- [ ] Code review confirms integer arithmetic, unchanged public interfaces, and no unrelated feature changes.
- [ ] Briefing contains verified file references, commands, and explicit constraints; uncertainties were answered or clearly flagged.
- [ ] Both attempts have saved prompts, plans, diffs, outputs, and correction counts.
- [ ] Comparison contains at least three specific observations supported by that evidence.
- [ ] Both partners can explain the final implementation in their own words.
- [ ] Draft PR contains the checklist, comparison link, verification output, and remaining limitations.
- [ ] Submitted PR URL and final commit ID identify the work to assess.

If you run out of time, submit the same evidence with unchecked items and the exact blocker. That documents progress; it is not a claim of full completion. Optional extensions are not required.
