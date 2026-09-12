"""Run explicitly; these checks intentionally fail on the unfinished starter."""

import unittest

from starter.order_service import Order, apply_tier_discount


class DiscountAcceptanceTests(unittest.TestCase):
    def assert_total(self, subtotal, tier, expected):
        result = apply_tier_discount(Order(subtotal, tier))
        self.assertIs(type(result), int, "Return a whole number of cents")
        self.assertEqual(result, expected)

    def assert_unknown_tier(self, subtotal, tier):
        with self.assertRaises(ValueError) as error:
            apply_tier_discount(Order(subtotal, tier))
        message = str(error.exception).lower()
        self.assertIn("tier", message)
        self.assertTrue("unknown" in message or "unsupported" in message)

    def test_standard_pays_full_price(self):
        self.assert_total(10_000, "standard", 10_000)

    def test_default_tier_is_standard(self):
        result = apply_tier_discount(Order(123))
        self.assertIs(type(result), int)
        self.assertEqual(result, 123)

    def test_gold_pays_ninety_percent(self):
        self.assert_total(10_000, "gold", 9_000)

    def test_gold_rounds_half_cent_up(self):
        for subtotal, expected in [(5, 5), (15, 14)]:
            with self.subTest(subtotal=subtotal):
                self.assert_total(subtotal, "gold", expected)

    def test_gold_rounds_down_below_half(self):
        self.assert_total(6, "gold", 5)

    def test_gold_rounds_up_above_half(self):
        self.assert_total(1, "gold", 1)

    def test_zero_is_valid_for_both_tiers(self):
        for tier in ("standard", "gold"):
            with self.subTest(tier=tier):
                self.assert_total(0, tier, 0)

    def test_negative_is_rejected_for_both_tiers(self):
        for tier in ("standard", "gold"):
            with self.subTest(tier=tier):
                with self.assertRaisesRegex(ValueError, r"(?i)non[- ]negative"):
                    apply_tier_discount(Order(-1, tier))

    def test_unknown_tier_is_rejected(self):
        self.assert_unknown_tier(100, "silver")

    def test_tiers_are_case_sensitive(self):
        self.assert_unknown_tier(100, "Gold")

    def test_empty_tier_is_rejected_even_for_zero(self):
        self.assert_unknown_tier(0, "")

    def test_large_subtotal_retains_exact_cents(self):
        self.assert_total(10_000_000_000_000_015, "gold", 9_000_000_000_000_014)
