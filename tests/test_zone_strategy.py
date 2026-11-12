from decimal import Decimal

import pytest

from envios import ZONE_STRATEGIES


@pytest.mark.parametrize(
    ("zone", "expected"),
    [
        ("urbana", Decimal("9000")),
        ("rural", Decimal("10800")),
        ("nacional", Decimal("12600")),
    ],
)
def test_zone_strategy_applies_its_own_policy(zone, expected):
    assert ZONE_STRATEGIES[zone].apply(Decimal("9000")) == expected
