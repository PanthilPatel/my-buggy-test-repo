import pytest

from string_utils import tag_words, truncate, is_palindrome


def test_tag_words_basic():
    result = tag_words(["a", "b", "c"])
    assert result == [("a", 0), ("b", 1), ("c", 2)]


def test_tag_words_does_not_leak_between_calls():
    first = tag_words(["x", "y"])
    second = tag_words(["z"])
    # `second` should only contain tags from THIS call, not from the
    # previous call to tag_words.
    assert second == [("z", 0)]


def test_truncate_respects_max_len():
    result = truncate("Hello, World!", max_len=8, suffix="...")
    assert len(result) == 8
    assert result == "Hello..."


def test_truncate_short_text_unchanged():
    assert truncate("hi", max_len=10) == "hi"


def test_is_palindrome_true():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_is_palindrome_false():
    assert is_palindrome("Not a palindrome") is False
