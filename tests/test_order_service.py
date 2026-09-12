import unittest
from starter.order_service import Order, total_cents


class OrderServiceTests(unittest.TestCase):
    def test_total_rejects_negative_values(self):
        with self.assertRaises(ValueError):
            total_cents(Order(-1))

    def test_total_preserves_subtotal(self):
        self.assertEqual(total_cents(Order(10_000)), 10_000)

    def test_total_accepts_zero(self):
        self.assertEqual(total_cents(Order(0)), 0)
