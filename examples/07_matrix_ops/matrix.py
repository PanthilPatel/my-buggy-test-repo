"""Basic 2D matrix operations using nested lists.

Contains two bugs:
1. `multiply` swaps the row/column indices when computing the dot
   product, producing a transposed-looking but numerically wrong
   result.
2. `transpose` iterates rows/columns wrong, throwing away data when
   the matrix is not square.
"""


def shape(matrix: list[list[float]]) -> tuple[int, int]:
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    return rows, cols


def multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    a_rows, a_cols = shape(a)
    b_rows, b_cols = shape(b)
    if a_cols != b_rows:
        raise ValueError("Incompatible matrix dimensions for multiplication")

    result = [[0 for _ in range(b_cols)] for _ in range(a_rows)]
    for i in range(a_rows):
        for j in range(b_cols):
            total = 0
            for k in range(a_cols):
                # BUG: indices are swapped on `b` -- should be
                # b[k][j], not b[j][k]. This only produces correct
                # results by coincidence for square symmetric inputs.
                total += a[i][k] * b[j][k]
            result[i][j] = total
    return result


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    rows, cols = shape(matrix)
    # BUG: builds a `rows x rows` result instead of `cols x rows`,
    # so non-square matrices lose or gain the wrong dimensions.
    result = [[0 for _ in range(rows)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result
