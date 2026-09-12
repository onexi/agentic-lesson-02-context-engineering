"""These checks intentionally fail on the unfinished starter."""

from starter.order_service import apply_tier_discount
from test_support import expect_value_error, run_tests


def check_total(subtotal, tier, expected):
    result = apply_tier_discount(subtotal, tier)
    assert type(result) is int, "Return a whole number of cents"
    assert result == expected, f"Expected {expected} cents, got {result}"


def check_unknown_tier(subtotal, tier):
    message = expect_value_error(apply_tier_discount, subtotal, tier).lower()
    assert "tier" in message, "The error must identify the customer tier"
    assert "unknown" in message or "unsupported" in message


def test_standard_pays_full_price():
    check_total(10_000, "standard", 10_000)


def test_default_tier_is_standard():
    result = apply_tier_discount(123)
    assert type(result) is int
    assert result == 123


def test_gold_pays_ninety_percent():
    check_total(10_000, "gold", 9_000)


def test_gold_rounds_half_cent_up():
    check_total(5, "gold", 5)
    check_total(15, "gold", 14)


def test_gold_rounds_down_below_half():
    check_total(6, "gold", 5)


def test_gold_rounds_up_above_half():
    check_total(1, "gold", 1)


def test_zero_is_valid_for_both_tiers():
    check_total(0, "standard", 0)
    check_total(0, "gold", 0)


def test_negative_is_rejected_for_both_tiers():
    for tier in ("standard", "gold"):
        message = expect_value_error(apply_tier_discount, -1, tier).lower()
        assert "non negative" in message.replace("-", " ")


def test_unknown_tier_is_rejected():
    check_unknown_tier(100, "silver")


def test_tiers_are_case_sensitive():
    check_unknown_tier(100, "Gold")


def test_empty_tier_is_rejected_even_for_zero():
    check_unknown_tier(0, "")


def test_large_subtotal_retains_exact_cents():
    check_total(10_000_000_000_000_015, "gold", 9_000_000_000_000_014)


if __name__ == "__main__":
    run_tests([
        test_standard_pays_full_price,
        test_default_tier_is_standard,
        test_gold_pays_ninety_percent,
        test_gold_rounds_half_cent_up,
        test_gold_rounds_down_below_half,
        test_gold_rounds_up_above_half,
        test_zero_is_valid_for_both_tiers,
        test_negative_is_rejected_for_both_tiers,
        test_unknown_tier_is_rejected,
        test_tiers_are_case_sensitive,
        test_empty_tier_is_rejected_even_for_zero,
        test_large_subtotal_retains_exact_cents,
    ])
