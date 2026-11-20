"""
INTERMEDIATE | Topic: Nested Conditionals
Notes: Placing an if-else statement inside another conditional block.
"""

has_ticket = True
age = 16

if has_ticket:
    if age >= 18:
        print("Access granted: Adult section.")
    else:
        print("Access granted: Student/Minor section.")
else:
    print("Access denied: Please purchase a ticket.")