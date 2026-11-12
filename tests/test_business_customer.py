import pytest

from envios import calc


@pytest.mark.parametrize(
    ("case_id", "weight", "zone", "day", "coupon", "expected"),
    [
        ("CP39", 4, "urbana", 1, None, 7900),
        ("CP40", 10, "rural", 1, None, 9500),
        ("CP41", 10.5, "rural", 1, None, 8300),
        ("CP42", 10.5, "nacional", 1, None, 8300),
        ("CP43", 4, "urbana", 1, "ENVIO10", 7100),
        ("CP44", 4, "urbana", 6, None, 9700),
    ],
)
def test_business_change_cases(case_id, weight, zone, day, coupon, expected):
    assert calc(weight, zone, "empresarial", day, coupon) == expected, case_id
