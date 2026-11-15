from src.math_utils import add, fibonacci


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55


def test_fibonacci_negative():
    import pytest
    with pytest.raises(ValueError):
        fibonacci(-1)
