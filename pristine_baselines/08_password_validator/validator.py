"""Top-level password validation.

Contains a bug: `is_valid_password` uses `any(...)` to combine the
individual rule checks, so a password only needs to satisfy ONE rule
(e.g. just being long enough) to be considered valid, instead of
satisfying ALL of them.
"""

from rules import has_min_length, has_uppercase, has_digit, has_special_char


def is_valid_password(password: str) -> bool:
    checks = [
        has_min_length(password),
        has_uppercase(password),
        has_digit(password),
        has_special_char(password),
    ]
    # BUG: should require ALL checks to pass (all(checks)), not just
    # one of them.
    return any(checks)


def validation_errors(password: str) -> list[str]:
    errors = []
    if not has_min_length(password):
        errors.append("Password must be at least 8 characters long")
    if not has_uppercase(password):
        errors.append("Password must contain an uppercase letter")
    if not has_digit(password):
        errors.append("Password must contain a digit")
    if not has_special_char(password):
        errors.append("Password must contain a special character")
    return errors
