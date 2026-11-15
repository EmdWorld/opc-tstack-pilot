"""math utils — pilot repo for tstack full-stop pipeline."""

import math


def add(a, b):
    return a + b


def fibonacci(n):
    """Return the n-th Fibonacci number (n >= 0)."""
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_prime(n):
    """Return True if n is a prime number, else False.

    n < 2 is not prime; trial division up to sqrt(n).
    """
    if n < 2:
        return False
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            return False
    return True
