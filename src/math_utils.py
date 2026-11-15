"""math utils — pilot repo for tstack full-stop pipeline."""


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
