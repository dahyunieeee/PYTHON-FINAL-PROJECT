"""
HARD | Topic: Truthiness & Short-Circuit Guard Clauses
Notes: Empty strings "", 0, and None evaluate to False in boolean contexts.
"""

username_input = "   "
cleaned_user = username_input.strip()

# Guard clause prevents invalid processing early
if not cleaned_user:
    print("Validation Error: Username cannot be blank.")
elif len(cleaned_user) < 4:
    print("Validation Error: Username must be at least 4 characters.")
else:
    print(f"Valid username registered: {cleaned_user}")