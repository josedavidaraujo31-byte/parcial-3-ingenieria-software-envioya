from decimal import Decimal

import pytest

from envios import calc


@pytest.mark.parametrize(
    ("case_id", "weight", "zone", "customer", "day", "coupon", "expected"),
    [
        ("CP02", 0.001, "urbana", "normal", 1, None, 6000),
        ("CP03", 2.999, "urbana", "normal", 1, None, 6000),
        ("CP04", 3, "urbana", "normal", 1, None, 6000),
        ("CP05", 3.001, "urbana", "normal", 1, None, 9000),
        ("CP06", 9.999, "urbana", "normal", 1, None, 9000),
        ("CP07", 10, "urbana", "normal", 1, None, 9000),
        ("CP08", 10.001, "urbana", "normal", 1, None, 9000),
        ("CP09", 10.0625, "urbana", "normal", 1, None, 9100),
        ("CP10", 50, "urbana", "normal", 1, None, 41000),
        ("CP13", 4, "rural", "normal", 1, None, 10800),
        ("CP14", 4, "nacional", "normal", 1, None, 12600),
        ("CP15", 4, "urbana", "normal", 6, None, 11000),
        ("CP16", 4, "urbana", "normal", 7, None, 11000),
        ("CP17", 4, "urbana", "normal", 5, None, 9000),
        ("CP21", 4, "urbana", "frecuente", 1, None, 8600),
        ("CP22", 4, "urbana", "vip", 1, None, 7700),
        ("CP23", 4, "urbana", "normal", 1, "ENVIO10", 8100),
        ("CP24", 4, "urbana", "frecuente", 1, "ENVIO10", 7700),
        ("CP25", 4, "urbana", "vip", 1, "ENVIO10", 6900),
        ("CP26", 4, "urbana", "normal", 1, "OTRO", 9000),
        ("CP27", 4, "urbana", "frecuente", 6, "ENVIO10", 9400),
        ("CP28", 1, "urbana", "vip", 1, "ENVIO10", 5000),
        ("CP29", 10.5, "urbana", "normal", 1, None, 9400),
        ("CP30", 4, "urbana", "normal", 6, "ENVIO10", 9900),
        ("CP31", 4, "urbana", "normal", 6, "OTRO", 11000),
        ("CP32", 4, "urbana", "frecuente", 6, None, 10500),
        ("CP33", 4, "urbana", "frecuente", 5, "OTRO", 8600),
        ("CP34", 4, "urbana", "frecuente", 6, "OTRO", 10500),
        ("CP35", 4, "urbana", "vip", 6, None, 9400),
        ("CP36", 4, "urbana", "vip", 6, "ENVIO10", 8400),
        ("CP37", 4, "urbana", "vip", 5, "OTRO", 7700),
        ("CP38", 4, "urbana", "vip", 6, "OTRO", 9400),
    ],
)
def test_cost_matches_specification(
    case_id, weight, zone, customer, day, coupon, expected
):
    assert calc(weight, zone, customer, day, coupon) == expected, case_id


@pytest.mark.parametrize(
    ("case_id", "weight"),
    [("CP01", 0), ("CP11", 50.001), ("CP12", -0.001)],
)
def test_invalid_weight_raises_specified_error(case_id, weight):
    with pytest.raises(ValueError, match="peso inválido"):
        calc(weight, "urbana", "normal", 1)


@pytest.mark.parametrize(
    ("case_id", "zone", "day"),
    [
        ("CP18", "desconocida", 1),
        ("CP19", "urbana", 0),
        ("CP20", "urbana", 8),
    ],
)
def test_invalid_zone_or_day_is_rejected(case_id, zone, day):
    with pytest.raises(ValueError):
        calc(4, zone, "normal", day)


@pytest.mark.parametrize("weight", [Decimal("NaN"), Decimal("Infinity")])
def test_non_finite_weight_is_rejected(weight):
    with pytest.raises(ValueError, match="peso inválido"):
        calc(weight, "urbana", "normal", 1)


@pytest.mark.parametrize("day", [True, 1.5, "1"])
def test_day_must_be_an_integer(day):
    with pytest.raises(ValueError, match="día inválido"):
        calc(4, "urbana", "normal", day)
