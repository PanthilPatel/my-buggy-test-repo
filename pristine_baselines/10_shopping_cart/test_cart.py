import pytest

from cart import Cart
from pricing import subtotal, total_with_tax


def test_adding_same_sku_twice_merges_quantity():
    cart = Cart()
    cart.add_item("SKU1", unit_price=9.99, quantity=2)
    cart.add_item("SKU1", unit_price=9.99, quantity=3)
    assert cart.unique_sku_count() == 1
    assert cart.total_quantity() == 5
    assert len(cart.line_items) == 1


def test_adding_different_skus_creates_separate_lines():
    cart = Cart()
    cart.add_item("SKU1", unit_price=5.0, quantity=1)
    cart.add_item("SKU2", unit_price=7.5, quantity=2)
    assert cart.unique_sku_count() == 2
    assert len(cart.line_items) == 2


def test_remove_item_removes_all_of_that_sku():
    cart = Cart()
    cart.add_item("SKU1", unit_price=9.99, quantity=2)
    cart.add_item("SKU1", unit_price=9.99, quantity=3)
    cart.remove_item("SKU1")
    assert cart.total_quantity() == 0


def test_subtotal_calculation():
    cart = Cart()
    cart.add_item("SKU1", unit_price=10.0, quantity=2)  # 20.00
    cart.add_item("SKU2", unit_price=5.0, quantity=3)   # 15.00
    assert subtotal(cart) == 35.00


def test_total_with_tax_8_percent():
    cart = Cart()
    cart.add_item("SKU1", unit_price=100.0, quantity=1)
    # 8% tax on $100 subtotal -> $108.00
    assert total_with_tax(cart, tax_rate=8) == 108.00
