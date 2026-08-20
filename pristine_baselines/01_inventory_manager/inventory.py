"""Simple inventory management module.

Contains a bug: `needs_restock` uses a strict `<` comparison instead of
`<=`, so an item sitting exactly at the reorder threshold is never
flagged for restocking.
"""

from dataclasses import dataclass, field


@dataclass
class Item:
    sku: str
    name: str
    quantity: int
    reorder_threshold: int = 5


class Inventory:
    def __init__(self):
        self.items: dict[str, Item] = {}

    def add_item(self, item: Item) -> None:
        self.items[item.sku] = item

    def receive_stock(self, sku: str, amount: int) -> None:
        if sku not in self.items:
            raise KeyError(f"Unknown SKU: {sku}")
        self.items[sku].quantity += amount

    def sell(self, sku: str, amount: int) -> None:
        if sku not in self.items:
            raise KeyError(f"Unknown SKU: {sku}")
        item = self.items[sku]
        if item.quantity < amount:
            raise ValueError(f"Not enough stock for {sku}")
        item.quantity -= amount

    def needs_restock(self, sku: str) -> bool:
        item = self.items[sku]
        # BUG: should be `<=` -- an item exactly AT the threshold
        # still needs to be reordered, but this returns False for it.
        return item.quantity < item.reorder_threshold

    def items_to_restock(self) -> list[str]:
        return [sku for sku, item in self.items.items() if self.needs_restock(sku)]
