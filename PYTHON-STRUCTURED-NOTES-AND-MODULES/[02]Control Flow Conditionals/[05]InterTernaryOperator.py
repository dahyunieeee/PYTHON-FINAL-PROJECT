"""
INTERMEDIATE | Topic: Conditional Expression (Ternary Operator)
Notes: Compact single-line syntax -> value_if_true if condition else value_if_false.
"""

stock_count = 0
status = "In Stock" if stock_count > 0 else "Out of Stock"
print("Inventory Status:", status)