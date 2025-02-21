# test_integration.py
import pytest
from product_module import add_product
from order_module import calculate_total_price

@pytest.fixture
def setup_products():
    add_product(1, "Laptop", 1200)
    add_product(2, "Mouse", 20)

def test_order_without_discount(setup_products):
    order_items = [(2, 3)]  # 3x Mouse (20 * 3 = 60)
    total_price = calculate_total_price(order_items)
    assert total_price == 60  # No discount

def test_order_with_multiple_products(setup_products):
    order_items = [(1, 1), (2, 2)]  # 1x Laptop (1200) + 2x Mouse (20 * 2 = 40) = 1240
    total_price = calculate_total_price(order_items)
    assert total_price == 1240 * 0.9  # 10% discount applied

def test_order_with_invalid_product(setup_products):
    order_items = [(99, 1)]  # Non-existent product
    total_price = calculate_total_price(order_items)
    assert total_price == 0  # No product, total price should be 0

def test_order_with_5_percent_discount(setup_products):
    order_items = [(2, 30)]  # 30x Mouse (20 * 30 = 600)
    total_price = calculate_total_price(order_items)
    assert total_price == 600 * 0.95  # 5% discount applied

def test_order_with_10_percent_discount(setup_products):
    order_items = [(1, 1), (2, 5)]  # 1x Laptop (1200) + 5x Mouse (20 * 5 = 100) = 1300
    total_price = calculate_total_price(order_items)
    assert total_price == 1300 * 0.9  # 10% discount applied
