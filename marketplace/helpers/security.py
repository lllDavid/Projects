from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_data(key, data):
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    return iv + ciphertext

def decrypt_data(key, encrypted_data):
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_data, AES.block_size).decode()

key = get_random_bytes(32)
data = "This is a secret message."

encrypted_data = encrypt_data(key, data)
print("Encrypted data:", encrypted_data)

decrypted_data = decrypt_data(key, encrypted_data)
print("Decrypted data:", decrypted_data)
