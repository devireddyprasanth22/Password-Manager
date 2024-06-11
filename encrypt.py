from cryptography.fernet import Fernet

# Function to generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key
def load_key():
    return open("secret.key", "rb").read()

# Call this function once to generate and save the key
generate_key()

# Function to encrypt a message
def encrypt(message: str) -> str:
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message.decode()

# Function to decrypt a message
def decrypt(encrypted_message: str) -> str:
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

# Example usage
if __name__ == "__main__":
    original_message = "Secret message"
    encrypted = encrypt(original_message)
    print(f"Encrypted: {encrypted}")

    decrypted = decrypt(encrypted)
    print(f"Decrypted: {decrypted}")