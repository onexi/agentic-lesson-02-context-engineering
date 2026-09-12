from starter.order_service import total_cents
from test_support import expect_value_error, run_tests


def test_total_rejects_negative_values():
    expect_value_error(total_cents, -1)


def test_total_preserves_subtotal():
    assert total_cents(10_000) == 10_000


def test_total_accepts_zero():
    assert total_cents(0) == 0


if __name__ == "__main__":
    run_tests([
        test_total_rejects_negative_values,
        test_total_preserves_subtotal,
        test_total_accepts_zero,
    ])
