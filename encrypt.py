import os
from cryptography.fernet import Fernet

def generate_key():
    if not os.path.exists("secretkey"):
        key = Fernet.generate_key()
        with open("secretkey", "wb") as key_file:
            key_file.write(key)
    else:
        print("Key file already exists. Skipping key generation.")

def load_key():
    return open("secretkey", "rb").read()

generate_key()

def encrypt(string):
    key = load_key()
    f_key = Fernet(key)
    encrypted = f_key.encrypt(string.encode())
    return encrypted.decode()


def decrypt(string):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(string.encode())
    return decrypted.decode()

