from src.math_utils import add, fibonacci, is_prime


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


def test_is_prime():
    assert is_prime(2) is True


def test_is_prime_one():
    assert is_prime(1) is False


def test_is_prime_negative():
    assert is_prime(-7) is False


def test_is_prime_composite():
    assert is_prime(9) is False


def test_is_prime_large_prime():
    assert is_prime(97) is True


def test_is_prime_large_composite():
    assert is_prime(100) is False
