"""Shopping cart line-item management.

Contains a bug: `add_item` always appends a new line item, even when
the SKU is already in the cart, instead of merging quantities into
the existing line. This causes duplicate line items and makes
`total_quantity` correct but `line_items` wrong/misleading, and it
also breaks `remove_item`, which only removes the first match.
"""

from dataclasses import dataclass


@dataclass
class LineItem:
    sku: str
    unit_price: float
    quantity: int


class Cart:
    def __init__(self):
        self.line_items: list[LineItem] = []

    def add_item(self, sku: str, unit_price: float, quantity: int = 1) -> None:
        # BUG: should look for an existing LineItem with this SKU and
        # increment its quantity; instead it always appends a new
        # line item, creating duplicates.
        self.line_items.append(LineItem(sku=sku, unit_price=unit_price, quantity=quantity))

    def remove_item(self, sku: str) -> None:
        for item in self.line_items:
            if item.sku == sku:
                self.line_items.remove(item)
                return
        raise KeyError(f"SKU not in cart: {sku}")

    def total_quantity(self) -> int:
        return sum(item.quantity for item in self.line_items)

    def unique_sku_count(self) -> int:
        return len({item.sku for item in self.line_items})
