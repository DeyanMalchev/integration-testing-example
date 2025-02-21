# discount_module.py

def apply_discount(total_price):
    """
    Applies discounts based on total_price.
    """
    if total_price > 1000:
        return total_price * 0.9  # 10% discount
    elif total_price > 500:
        return total_price * 0.95  # 5% discount
    else:
        return total_price  # No discount
