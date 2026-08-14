import pytest

from validator import is_valid_password, validation_errors


def test_valid_password_passes():
    assert is_valid_password("Str0ng!Pass") is True


def test_password_missing_uppercase_fails():
    assert is_valid_password("weak1!weak") is False


def test_password_missing_digit_fails():
    assert is_valid_password("NoDigitsHere!") is False


def test_password_missing_special_char_fails():
    assert is_valid_password("NoSpecial123") is False


def test_password_too_short_fails():
    assert is_valid_password("Sh0rt!") is False


def test_long_password_with_only_length_is_invalid():
    # This password is long but has no uppercase, digit, or special
    # char, so it must be rejected.
    assert is_valid_password("lowercaseonlylongpassword") is False


def test_validation_errors_lists_all_missing_rules():
    errors = validation_errors("weak")
    assert "Password must be at least 8 characters long" in errors
    assert "Password must contain an uppercase letter" in errors
    assert "Password must contain a digit" in errors
    assert "Password must contain a special character" in errors
