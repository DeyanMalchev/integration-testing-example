# test_discount_module.py
import pytest
from discount_module import apply_discount

def test_apply_discount_no_discount():
    assert apply_discount(300) == 300  # No discount

def test_apply_discount_5_percent():
    assert apply_discount(750) == 712.5  # 5% discount

def test_apply_discount_10_percent():
    assert apply_discount(1500) == 1350  # 10% discount
