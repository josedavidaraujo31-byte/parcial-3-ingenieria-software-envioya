import pytest

from envios import calc


@pytest.mark.parametrize(
    ("zone", "day"),
    [
        ("desconocida", 1),
        ("urbana", 0),
        ("urbana", 8),
    ],
)
def test_def01_rejects_invalid_zone_and_day(zone, day):
    with pytest.raises(ValueError):
        calc(4, zone, "normal", day)
