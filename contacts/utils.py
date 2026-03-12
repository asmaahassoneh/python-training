class WeakPasswordError(Exception):
    """Raised when a password does not meet strength requirements."""


def strong_password(password: str) -> bool:
    if not isinstance(password, str):
        raise WeakPasswordError("Password must be a string")

    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters long")

    if password.strip() != password:
        raise WeakPasswordError("Password must not start or end with spaces")

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if not has_upper:
        raise WeakPasswordError("Password must contain at least one uppercase letter")

    if not has_lower:
        raise WeakPasswordError("Password must contain at least one lowercase letter")

    if not has_digit:
        raise WeakPasswordError("Password must contain at least one digit")

    return True
