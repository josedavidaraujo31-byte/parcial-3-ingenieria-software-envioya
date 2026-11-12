from abc import ABC, abstractmethod
from decimal import Decimal, ROUND_HALF_UP


MAX_WEIGHT = Decimal("50")
ONE = Decimal("1")
FIRST_WEIGHT_LIMIT = Decimal("3")
SECOND_WEIGHT_LIMIT = Decimal("10")
FIRST_TIER_PRICE = Decimal("6000")
SECOND_TIER_PRICE = Decimal("9000")
PRICE_PER_EXTRA_KILOGRAM = Decimal("800")
RURAL_SURCHARGE_RATE = Decimal("0.20")
NATIONAL_SURCHARGE_RATE = Decimal("0.40")
FREQUENT_CUSTOMER_DISCOUNT = Decimal("0.05")
VIP_CUSTOMER_DISCOUNT = Decimal("0.15")
COUPON_DISCOUNT = Decimal("0.10")
WEEKEND_SURCHARGE = Decimal("2000")
MINIMUM_PRICE = Decimal("5000")
ROUNDING_UNIT = Decimal("100")
ZERO = Decimal("0")
FIRST_DAY = 1
SATURDAY = 6
SUNDAY = 7
LAST_DAY = SUNDAY
VALID_DAYS = range(FIRST_DAY, LAST_DAY + 1)
WEEKEND_DAYS = frozenset((SATURDAY, SUNDAY))
VALID_COUPON = "ENVIO10"


class ZoneStrategy(ABC):
    @abstractmethod
    def apply(self, amount: Decimal) -> Decimal:
        raise NotImplementedError  # pragma: no cover


class UrbanZoneStrategy(ZoneStrategy):
    def apply(self, amount: Decimal) -> Decimal:
        return amount


class RuralZoneStrategy(ZoneStrategy):
    def apply(self, amount: Decimal) -> Decimal:
        return amount * (ONE + RURAL_SURCHARGE_RATE)


class NationalZoneStrategy(ZoneStrategy):
    def apply(self, amount: Decimal) -> Decimal:
        return amount * (ONE + NATIONAL_SURCHARGE_RATE)


ZONE_STRATEGIES = {
    "urbana": UrbanZoneStrategy(),
    "rural": RuralZoneStrategy(),
    "nacional": NationalZoneStrategy(),
}

CUSTOMER_DISCOUNTS = {
    "frecuente": FREQUENT_CUSTOMER_DISCOUNT,
    "vip": VIP_CUSTOMER_DISCOUNT,
}


def _calculate_base_price(weight: Decimal) -> Decimal:
    if weight <= FIRST_WEIGHT_LIMIT:
        return FIRST_TIER_PRICE
    if weight <= SECOND_WEIGHT_LIMIT:
        return SECOND_TIER_PRICE
    return (
        SECOND_TIER_PRICE
        + (weight - SECOND_WEIGHT_LIMIT) * PRICE_PER_EXTRA_KILOGRAM
    )


def _apply_customer_discount(amount: Decimal, customer_type: str) -> Decimal:
    discount = CUSTOMER_DISCOUNTS.get(customer_type, ZERO)
    return amount * (ONE - discount)


def _apply_coupon_discount(amount: Decimal, coupon: str | None) -> Decimal:
    if coupon == VALID_COUPON:
        return amount * (ONE - COUPON_DISCOUNT)
    return amount


def _round_to_nearest_unit(amount: Decimal) -> int:
    rounded_units = (amount / ROUNDING_UNIT).quantize(
        ONE, rounding=ROUND_HALF_UP
    )
    return int(rounded_units * ROUNDING_UNIT)


def calc(
    weight: int | float | Decimal,
    zone: str,
    customer_type: str,
    day: int,
    coupon: str | None = None,
) -> int:
    weight = Decimal(str(weight))
    if not weight.is_finite() or weight <= ZERO or weight > MAX_WEIGHT:
        raise ValueError("peso inválido")

    try:
        zone_strategy = ZONE_STRATEGIES[zone]
    except KeyError as error:
        raise ValueError("zona inválida") from error

    if (
        isinstance(day, bool)
        or not isinstance(day, int)
        or day not in VALID_DAYS
    ):
        raise ValueError("día inválido")

    amount = _calculate_base_price(weight)
    amount = zone_strategy.apply(amount)
    if day in WEEKEND_DAYS:
        amount += WEEKEND_SURCHARGE
    amount = _apply_customer_discount(amount, customer_type)
    amount = _apply_coupon_discount(amount, coupon)
    amount = max(amount, MINIMUM_PRICE)
    return _round_to_nearest_unit(amount)
