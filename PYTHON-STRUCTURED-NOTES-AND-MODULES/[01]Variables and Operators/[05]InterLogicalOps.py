"""
INTERMEDIATE | Topic: Comparison & Logical Operators
Notes: Evaluates boolean expressions with ==, !=, >=, and, or, not.
"""

attendance = 90.0
project_done = True
has_penalty = False

can_graduate = (attendance >= 80.0) and project_done and (not has_penalty)
print("Eligible:", can_graduate)