from app.utils import is_palindrome, truncate


def test_is_palindrome_true():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True


def test_is_palindrome_false():
    assert is_palindrome("hello") is False


def test_truncate_returns_value_unchanged_when_short_enough():
    assert truncate("hello", 10) == "hello"


def test_truncate_appends_ellipsis_when_too_long():
    assert truncate("hello world", 5) == "hello..."
