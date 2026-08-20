"""Individual password rule checks."""

import re

SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;:,.<>?"


def has_min_length(password: str, min_len: int = 8) -> bool:
    return len(password) >= min_len


def has_uppercase(password: str) -> bool:
    return bool(re.search(r"[A-Z]", password))


def has_digit(password: str) -> bool:
    return bool(re.search(r"[0-9]", password))


def has_special_char(password: str) -> bool:
    return any(ch in SPECIAL_CHARS for ch in password)
