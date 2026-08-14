"""Small collection of string helper functions.

Contains two bugs:
1. `tag_words` uses a mutable default argument (a list) as an
   accumulator, so results leak between separate calls.
2. `truncate` slices one character short of `max_len`, so the
   returned string is always shorter than requested.
"""


def tag_words(words, tags=[]):
    """Return a list of (word, index) tags, appending to `tags`.

    BUG: `tags=[]` is a mutable default argument. Because default
    arguments are evaluated once at function definition time, every
    call that doesn't pass its own `tags` list shares and mutates the
    SAME list, causing results to accumulate across calls.
    """
    for i, word in enumerate(words):
        tags.append((word, i))
    return tags


def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    """Truncate `text` to `max_len` characters (including suffix).

    BUG: uses `max_len - len(suffix) - 1` instead of
    `max_len - len(suffix)`, so the returned string ends up one
    character shorter than the caller asked for.
    """
    if len(text) <= max_len:
        return text
    cutoff = max_len - len(suffix) - 1
    return text[:cutoff] + suffix


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]
