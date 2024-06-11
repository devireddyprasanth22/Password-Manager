from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secretkey", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secretkey", "rb").read()

generate_key()


def encrypt(str):
    key = load_key()
    f_key = Fernet(key)
    encrypted = f_key.encrypt(str.encode())
    return encrypted.decode()


def decrypt(str):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(str.encode())
    return decrypted.decode()

