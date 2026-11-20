"""
INTERMEDIATE | Topic: F-String Alignment & Precision
Notes: :<N left-aligns, :>N right-aligns, .2f locks two decimal places.
"""

print(f"{'ITEM':<18} | {'PRICE':>8}")
print("-" * 29)
print(f"{'Iced Americano':<18} | {110.0:>8.2f}")
print(f"{'Matcha Latte':<18} | {155.5:>8.2f}")