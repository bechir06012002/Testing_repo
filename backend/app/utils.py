import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(value: str) -> bool:
    return bool(_EMAIL_RE.match(value))


def clamp(value: int, low: int, high: int) -> int:
    if value < low:
        return low
    if value > high:
        return high
    return value


def slugify(value: str) -> str:
    return value.strip().lower().replace(" ", "-")


def new_helper_function(value: int) -> int:
    return value * 2


def is_palindrome(value: str) -> bool:
    normalized = value.lower().replace(" ", "")
    return normalized == normalized[::-1]
