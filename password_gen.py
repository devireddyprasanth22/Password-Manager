# parameters involved -> length (8-16), alphanumeric, special characters
import string
import random
import secrets

def password_generator():
    length = random.randint(8,16)
    set_of_chars = string.ascii_letters + string.punctuation + string.digits
    password = ''.join(secrets.choice(set_of_chars) for _ in range(length))
    return password