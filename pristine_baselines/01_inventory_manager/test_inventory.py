import pytest

from inventory import Inventory, Item
from discounts import bulk_discount_price, apply_flat_discount


def make_inventory():
    inv = Inventory()
    inv.add_item(Item(sku="A1", name="Widget", quantity=5, reorder_threshold=5))
    inv.add_item(Item(sku="A2", name="Gadget", quantity=10, reorder_threshold=5))
    return inv


def test_item_exactly_at_threshold_needs_restock():
    inv = make_inventory()
    # Quantity (5) equals the threshold (5) -> should still need restock.
    assert inv.needs_restock("A1") is True


def test_item_above_threshold_does_not_need_restock():
    inv = make_inventory()
    assert inv.needs_restock("A2") is False


def test_items_to_restock_includes_boundary_item():
    inv = make_inventory()
    assert "A1" in inv.items_to_restock()


def test_sell_reduces_quantity():
    inv = make_inventory()
    inv.sell("A2", 3)
    assert inv.items["A2"].quantity == 7


def test_bulk_discount_10_percent():
    # 10 units at $20 each = $200 subtotal, 10% off -> $180
    total = bulk_discount_price(unit_price=20.0, quantity=10, discount_percent=10)
    assert total == 180.0


def test_bulk_discount_25_percent():
    # 4 units at $50 each = $200 subtotal, 25% off -> $150
    total = bulk_discount_price(unit_price=50.0, quantity=4, discount_percent=25)
    assert total == 150.0


def test_flat_discount_never_negative():
    assert apply_flat_discount(price=10.0, flat_amount=25.0) == 0.0
