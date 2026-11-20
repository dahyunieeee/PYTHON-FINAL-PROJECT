"""
EASY | Topic: Multi-Branch elif Ladder
Notes: Evaluates conditions top-to-bottom and runs the first True branch.
"""

grade = 88
if grade >= 90:
    remark = "Excellent"
elif grade >= 80:
    remark = "Very Good"
elif grade >= 75:
    remark = "Passed"
else:
    remark = "Failed"

print(f"Grade {grade}: {remark}")