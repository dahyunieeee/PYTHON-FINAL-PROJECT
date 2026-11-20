"""
HARD | Topic: Progressive Tiered Bracket Calculation
Notes: Computes progressive tax across income thresholds using conditional ranges.
"""

annual_income = 450000.0

if annual_income <= 250000:
    tax = 0.0
elif annual_income <= 400000:
    tax = (annual_income - 250000) * 0.15
elif annual_income <= 800000:
    tax = 22500 + (annual_income - 400000) * 0.20
else:
    tax = 102500 + (annual_income - 800000) * 0.25

print(f"Income: PHP {annual_income:,.2f} | Computed Tax: PHP {tax:,.2f}")