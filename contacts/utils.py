class WeakPasswordError(Exception):
    """Raised when a password does not meet strength requirements."""


def strong_password(password: str) -> bool:
    """
    Validate password strength.

    Time complexity: O(n)
    because we scan the password characters to check conditions.
    """
    if not isinstance(password, str):
        raise WeakPasswordError("Password must be a string")

    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters long")

    if password.strip() != password:
        raise WeakPasswordError("Password must not start or end with spaces")

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if not has_upper:
        raise WeakPasswordError("Password must contain at least one uppercase letter")

    if not has_lower:
        raise WeakPasswordError("Password must contain at least one lowercase letter")

    if not has_digit:
        raise WeakPasswordError("Password must contain at least one digit")

    if not has_special:
        raise WeakPasswordError("Password must contain at least one special character")

    return True
