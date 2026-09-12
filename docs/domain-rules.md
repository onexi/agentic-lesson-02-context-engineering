# Domain rules

- Money is represented as whole cents: `10000` means $100.00. Inputs for this lesson are integer subtotals and string customer tiers.
- `standard` customers pay the subtotal unchanged. This is also the default tier when none is supplied.
- `gold` customers receive a 10% discount: they pay 90% of the subtotal.
- Round the **final discounted total** to the nearest whole cent. At exactly half a cent, round up. For example, 5 cents becomes 5 cents (4.5 rounds up), 6 cents becomes 5 cents (5.4 rounds down), and 15 cents becomes 14 cents (13.5 rounds up).
- Use integer arithmetic throughout the price calculation; do not convert prices to floating-point numbers.
- A zero subtotal is valid for both supported tiers.
- Negative subtotals must raise `ValueError` with a message explaining that the subtotal must be non-negative.
- Only the exact, case-sensitive strings `standard` and `gold` are supported. Any other tier, including `Gold`, the empty string, or `silver`, must raise `ValueError` with a message identifying the tier as unknown or unsupported. Do not silently charge full price for an unknown tier.
- For an input that is both negative and an unknown tier, either applicable validation error is acceptable.
- Keep `total_cents(subtotal_cents)` and `apply_tier_discount(subtotal_cents, customer_tier="standard")` unchanged as interfaces. Use ordinary functions, not classes. `total_cents` remains the existing undiscounted subtotal validator; the new policy belongs in `apply_tier_discount`.
- Handling non-integer subtotals, currencies, tax, shipping, new tiers, and a user interface is outside this lesson's scope.
