import pytest

from matrix import multiply, transpose, shape


def test_multiply_2x2():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    # [[1*5+2*7, 1*6+2*8], [3*5+4*7, 3*6+4*8]] = [[19,22],[43,50]]
    assert multiply(a, b) == [[19, 22], [43, 50]]


def test_multiply_non_square():
    a = [[1, 2, 3], [4, 5, 6]]  # 2x3
    b = [[7, 8], [9, 10], [11, 12]]  # 3x2
    # Expected result is 2x2:
    # [[1*7+2*9+3*11, 1*8+2*10+3*12], [4*7+5*9+6*11, 4*8+5*10+6*12]]
    # = [[58, 64], [139, 154]]
    assert multiply(a, b) == [[58, 64], [139, 154]]


def test_transpose_square():
    m = [[1, 2], [3, 4]]
    assert transpose(m) == [[1, 3], [2, 4]]


def test_transpose_non_square_shape():
    m = [[1, 2, 3], [4, 5, 6]]  # 2x3
    result = transpose(m)
    assert shape(result) == (3, 2)
    assert result == [[1, 4], [2, 5], [3, 6]]
