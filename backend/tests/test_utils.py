from app.utils import is_palindrome


def test_is_palindrome_true():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True


def test_is_palindrome_false():
    assert is_palindrome("hello") is False
