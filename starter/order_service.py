def total_cents(subtotal_cents):
    """Check that the price is valid and return it unchanged."""
    if subtotal_cents < 0:
        raise ValueError("subtotal_cents must be non-negative")
    return subtotal_cents


def apply_tier_discount(subtotal_cents, customer_tier="standard"):
    # Challenge: implement the policy documented in docs/domain-rules.md.
    raise NotImplementedError("Implement from verified repository context")
