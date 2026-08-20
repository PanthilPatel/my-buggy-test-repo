import pytest

from calculator import evaluate, evaluate_sequence


def test_evaluate_add():
    assert evaluate(2, "+", 3) == 5


def test_evaluate_power():
    assert evaluate(2, "^", 5) == 32


def test_evaluate_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        evaluate(10, "/", 0)


def test_evaluate_sequence_sum_includes_first_number():
    assert evaluate_sequence([1, 2, 3, 4], "+") == 10


def test_evaluate_sequence_single_number():
    assert evaluate_sequence([7], "+") == 7


def test_evaluate_sequence_product():
    assert evaluate_sequence([1, 2, 3, 4], "*") == 24
