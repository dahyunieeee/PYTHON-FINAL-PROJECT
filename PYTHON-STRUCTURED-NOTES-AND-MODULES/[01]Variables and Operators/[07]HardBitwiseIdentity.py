"""
HARD | Topic: Identity (is) vs Equality (==) and Bitwise Flags
Notes: '==' compares values; 'is' checks if two variables point to the same object.
"""

x = 1000
y = int("1000")
print("x == y:", x == y)   # True
print("x is y:", x is y)   # False (distinct integer objects in memory)

# Bitwise permission flags: Read=4 (100), Write=2 (010), Exec=1 (001)
READ, WRITE, EXEC = 0b100, 0b010, 0b001
perms = READ | WRITE
print("Can Write:", bool(perms & WRITE))
print("Can Exec:", bool(perms & EXEC))