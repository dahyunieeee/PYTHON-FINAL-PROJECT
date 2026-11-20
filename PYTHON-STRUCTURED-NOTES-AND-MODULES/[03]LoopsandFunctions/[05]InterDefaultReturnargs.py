"""
INTERMEDIATE | Topic: Default Parameters and Return Values
Notes: Functions return computed values via 'return' and support fallback defaults.
"""

def compute_final_price(price, discount_rate=0.10):
    final = price * (1 - discount_rate)
    return round(final, 2)

print("Default 10% off:", compute_final_price(500))
print("Custom 25% off :", compute_final_price(500, 0.25))