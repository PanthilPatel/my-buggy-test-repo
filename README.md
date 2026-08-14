# my-buggy-test-repo

A collection of small, self-contained Python examples for exercising
autonomous coding agents. Each example under `examples/` ships with
one or more source files containing an intentionally injected bug,
plus a pytest suite that currently fails because of it.

## Structure

Each `examples/NN_name/` directory is independent and contains:

- One or more `*.py` source modules (the code to fix)
- A `test_*.py` pytest suite (do not need to be modified — tests
  describe the intended behavior)
- A local `pytest.ini` so the example can be run in isolation

| Example | Bug type |
|---|---|
| `01_inventory_manager` | Off-by-one boundary check + percentage-as-fraction math bug (multi-file) |
| `02_string_utils` | Mutable default argument bug + off-by-one string slicing |
| `03_bank_account` | Boundary comparison bug (`>=` vs `>`) + double-fee logic bug across two files |
| `04_linked_list` | Loop termination condition drops the last node during reversal |
| `05_todo_manager` | Inverted boolean filter + wrong sort direction |
| `06_calculator` | **Syntax error** (missing colon) that breaks import, plus a separate fold/accumulator logic bug |
| `07_matrix_ops` | Swapped indices in matrix multiplication + wrong result dimensions in transpose |
| `08_password_validator` | `any()` used where `all()` was intended |
| `09_event_scheduler` | Off-by-one interval overlap check (`<=`/`>=` vs `<`/`>`) |
| `10_shopping_cart` | Missing "merge existing line item" logic + tax rate treated as a fraction instead of a percent |

## Running a single example

```bash
cd examples/01_inventory_manager
pip install pytest
pytest -v
```

## Running everything

```bash
for d in examples/*/; do
  echo "=== $d ==="
  (cd "$d" && pytest -q)
done
```

Each example currently has a mix of passing and failing tests — the
goal is to get every test in every example to pass by fixing the bug
in the source file(s), without editing the test files.
