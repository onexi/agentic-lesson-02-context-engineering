import unittest
from starter.order_service import Order, total_cents, apply_tier_discount

class OrderServiceTests(unittest.TestCase):
    def test_total_rejects_negative_values(self):
        with self.assertRaises(ValueError):
            total_cents(Order(-1))

    @unittest.skip("Challenge test: enable after implementing issue #1")
    def test_gold_discount_uses_repository_policy(self):
        self.assertEqual(apply_tier_discount(Order(10_000, "gold")), 9_000)
