"""
HARD | Topic: Recursion (Base Case + Recursive Step)
Notes: A function calling itself to solve smaller subproblems until hitting a base case.
"""

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))