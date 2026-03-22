"""Tests for calculator.py"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from calculator import (
    add, subtract, multiply, divide, power,
    square_root, factorial, is_prime, fibonacci,
)


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 7) == 21
    assert multiply(-2, 4) == -8
    assert multiply(0, 999) == 0


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


def test_power():
    assert power(2, 10) == 1024
    assert power(3, 0) == 1


def test_square_root():
    assert square_root(9) == 3.0
    assert square_root(2) == pytest.approx(1.41421356, rel=1e-6)


def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-1)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


@pytest.mark.parametrize("n,expected", [
    (0, False), (1, False), (2, True),
    (3, True), (4, False), (17, True), (100, False),
])
def test_is_prime(n, expected):
    assert is_prime(n) == expected


def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
