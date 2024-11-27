import secrets
import string


# Генератор "рандомной" строки
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return "".join(secrets.choice(characters) for _ in range(length))
