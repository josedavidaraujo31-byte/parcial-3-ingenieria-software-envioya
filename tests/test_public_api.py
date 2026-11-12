from inspect import signature

from envios import calc


def test_calc_api_no_longer_exposes_legacy_flag():
    assert list(signature(calc).parameters) == [
        "weight",
        "zone",
        "customer_type",
        "day",
        "coupon",
    ]
