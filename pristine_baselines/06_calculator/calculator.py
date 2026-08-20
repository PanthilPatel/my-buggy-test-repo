"""A small calculator that evaluates simple two-operand expressions.

Also contains a logic bug: `evaluate_sequence` folds the operations
left-to-right but starts the accumulator at the SECOND number instead
of the first, silently dropping the first number from the result.
"""

from operations import add, subtract, multiply, divide, power

OPS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
}


def evaluate(a, op, b):
    if op not in OPS:
        raise ValueError(f"Unknown operator: {op}")
    return OPS[op](a, b)


def evaluate_sequence(numbers: list[float], op: str) -> float:
    """Fold `op` across `numbers` left to right.

    e.g. evaluate_sequence([1, 2, 3, 4], "+") should be 10.
    """
    if not numbers:
        raise ValueError("numbers must not be empty")
    # BUG: should start with numbers[0], but starts at numbers[1],
    # so the first number never participates in the fold.
    acc = numbers[1] if len(numbers) > 1 else numbers[0]
    for n in numbers[2:]:
        acc = evaluate(acc, op, n)
    return acc
