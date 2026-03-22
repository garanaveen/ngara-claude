"""A simple calculator module with basic and advanced operations."""

import math
from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    return a + b


def subtract(a: Number, b: Number) -> Number:
    return a - b


def multiply(a: Number, b: Number) -> Number:
    return a * b


def divide(a: Number, b: Number) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: Number, exp: Number) -> Number:
    return base ** exp


def square_root(n: Number) -> float:
    if n < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(n)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if not isinstance(n, int):
        raise TypeError("Factorial requires an integer")
    return math.factorial(n)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    print("Basic operations:")
    print(f"  3 + 4 = {add(3, 4)}")
    print(f"  10 - 6 = {subtract(10, 6)}")
    print(f"  5 * 7 = {multiply(5, 7)}")
    print(f"  15 / 4 = {divide(15, 4)}")
    print(f"  2 ^ 10 = {power(2, 10)}")
    print(f"  sqrt(144) = {square_root(144)}")
    print(f"  10! = {factorial(10)}")
    print(f"\nFirst 10 Fibonacci numbers: {fibonacci(10)}")
    print(f"\nPrimes up to 30: {[n for n in range(2, 31) if is_prime(n)]}")
