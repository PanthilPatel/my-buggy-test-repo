"""Pricing calculations for a Cart.

Contains a bug: `total_with_tax` applies the tax rate to a value that
has already been rounded to 2 decimal places on EACH line item before
summing, and then rounds again, but more importantly it multiplies by
`1 + tax_rate` where `tax_rate` is expected as a whole percent (e.g.
8 for 8%) instead of a fraction -- so an 8% tax rate becomes an 800%
markup.
"""

from cart import Cart


def subtotal(cart: Cart) -> float:
    return round(sum(item.unit_price * item.quantity for item in cart.line_items), 2)


def total_with_tax(cart: Cart, tax_rate: float) -> float:
    """`tax_rate` is a percentage like 8 for 8% -- NOT a fraction."""
    base = subtotal(cart)
    # BUG: tax_rate is treated as already a fraction (e.g. 0.08)
    # instead of being divided by 100 first.
    return round(base * (1 + tax_rate), 2)
