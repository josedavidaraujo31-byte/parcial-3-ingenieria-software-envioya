import pytest

from envios import calc


@pytest.mark.parametrize(
    ("weight", "expected"),
    [
        (10.06125, 9000),
        (10.0625, 9100),
        (10.06375, 9100),
    ],
)
def test_def03_rounds_to_nearest_hundred_half_up(weight, expected):
    assert calc(weight, "urbana", "normal", 1) == expected
