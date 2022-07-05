
import secrets

from string import (
    ascii_letters as letters,
    digits,
    punctuation
)

chars = letters + digits + punctuation

secret_key = ''.join([secrets.choice(chars) for i in range(50)])

print(secret_key)