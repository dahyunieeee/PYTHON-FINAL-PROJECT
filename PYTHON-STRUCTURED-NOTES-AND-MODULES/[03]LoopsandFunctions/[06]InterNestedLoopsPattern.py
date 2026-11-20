"""
INTERMEDIATE | Topic: Nested Loops
Notes: An inner loop finishes all its iterations for every single outer loop step.
"""

rows = 5
for r in range(1, rows + 1):
    for c in range(1, r + 1):
        print("*", end=" ")
    print()  # Newline after each row