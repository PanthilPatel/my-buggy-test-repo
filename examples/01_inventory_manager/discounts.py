"""Discount calculation helpers used by the inventory system.

Contains a bug: `bulk_discount_price` applies the discount percentage
directly as a fraction of 1 instead of dividing by 100, so passing
`discount_percent=10` (meaning 10%) wipes out 10x the intended amount
of the price.
"""


def bulk_discount_price(unit_price: float, quantity: int, discount_percent: float) -> float:
    """Return total price for `quantity` units with a percent discount applied.

    `discount_percent` is expressed like 10 for 10%, 25 for 25%, etc.
    """
    subtotal = unit_price * quantity
    # BUG: discount_percent should be divided by 100 before use.
    discount_amount = subtotal * discount_percent
    total = subtotal - discount_amount
    return round(total, 2)


def apply_flat_discount(price: float, flat_amount: float) -> float:
    result = price - flat_amount
    return round(max(result, 0.0), 2)
