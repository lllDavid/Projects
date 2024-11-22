from argon2 import PasswordHasher
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import base64

# Function to derive a key using Argon2
def derive_key_argon2(password: str, salt: bytes, time_cost: int = 2, memory_cost: int = 102400, parallelism: int = 8, key_length: int = 32):
    """Derives an AES key using Argon2"""
    ph = PasswordHasher(time_cost=time_cost, memory_cost=memory_cost, parallelism=parallelism)
    derived_key = ph.hash(password.encode())
    return derived_key.encode()[:key_length]  # Truncate to desired length (AES 256 = 32 bytes)

# Function to encrypt data using AES
def encrypt_data(key: bytes, data: str):
    """Encrypt data with AES CBC mode"""
    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted_data

# Function to decrypt data using AES
def decrypt_data(key: bytes, encrypted_data: bytes):
    """Decrypt data with AES CBC mode"""
    iv = encrypted_data[:16]
    cipher_text = encrypted_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(cipher_text) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    original_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return original_data.decode()

# Example usage:
if __name__ == "__main__":
    password = "my_secure_password"
    
    salt = os.urandom(16)  # Random salt
    key = derive_key_argon2(password, salt)  # Derive key using Argon2

    backup_codes = "backup_code_1: 123456\nbackup_code_2: 789012"
    
    encrypted_backup_codes = encrypt_data(key, backup_codes)
    print("Encrypted Backup Codes:", base64.b64encode(encrypted_backup_codes).decode())

    decrypted_backup_codes = decrypt_data(key, encrypted_backup_codes)
    print("Decrypted Backup Codes:", decrypted_backup_codes)
