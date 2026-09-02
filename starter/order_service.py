from dataclasses import dataclass

@dataclass(frozen=True)
class Order:
    subtotal_cents: int
    customer_tier: str = "standard"

def total_cents(order: Order) -> int:
    if order.subtotal_cents < 0:
        raise ValueError("subtotal_cents must be non-negative")
    return order.subtotal_cents

def apply_tier_discount(order: Order) -> int:
    # Challenge: implement the policy documented in docs/domain-rules.md.
    raise NotImplementedError("Implement from verified repository context")
