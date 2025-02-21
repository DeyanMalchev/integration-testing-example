# order_module.py
from discount_module import apply_discount
from product_module import get_product

def calculate_total_price(order_items):
    """
    Calculates the total price of an order.
    """
    total = 0
    for product_id, quantity in order_items:
        product = get_product(product_id)
        if product:
            total += product["price"] * quantity

    # Apply discount
    total = apply_discount(total)

    return total
