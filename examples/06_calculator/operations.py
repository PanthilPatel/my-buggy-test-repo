"""Arithmetic operations used by the calculator.

Contains a SYNTAX ERROR: the `power` function is missing a colon at
the end of its `def` line, which means this module fails to import
at all (every test in the suite will error out, not just fail).
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(base, exponent)  # BUG: missing colon here -> SyntaxError
    return base ** exponent
