

import random
import string

def generate_unique_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(random.choice(characters) for _ in range(length))

        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in string.punctuation for char in password)
        if has_upper and has_lower and has_digit and has_special:
            return password