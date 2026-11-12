import pytest

from envios import calc


@pytest.mark.parametrize(
    ("day", "coupon", "expected"),
    [
        (6, None, 11000),
        (7, None, 11000),
        (6, "ENVIO10", 9900),
    ],
)
def test_def02_charges_weekend_before_coupon(day, coupon, expected):
    assert calc(4, "urbana", "normal", day, coupon) == expected
