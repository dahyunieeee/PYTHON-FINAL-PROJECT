"""
HARD | Topic: Optimized Prime Number Algorithm (Functions + Loops)
Notes: Checks divisibility only up to sqrt(n) using for-else loop construct.
"""

def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True

for number in range(10, 25):
    if is_prime(number):
        print(f"{number} is prime")