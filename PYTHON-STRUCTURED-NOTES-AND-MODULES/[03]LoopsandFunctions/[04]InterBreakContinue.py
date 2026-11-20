"""
INTERMEDIATE | Topic: Loop Control (break and continue)
Notes: 'continue' skips the current iteration; 'break' exits the loop immediately.
"""

for i in range(1, 10):
    if i % 2 == 0:
        continue  # Skip even numbers
    if i == 7:
        break     # Stop loop completely at 7
    print("Odd number before 7:", i)