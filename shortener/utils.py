import secrets
import string


def generate_short_code(length=6) -> str:
    """Генератор "рандомной" строки для слага URL."""
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return "".join(secrets.choice(characters) for _ in range(length))
