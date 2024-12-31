from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def encrypt_data(key, data):
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")
    
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    encrypted_data = iv + ciphertext
    
    return b64encode(encrypted_data).decode('utf-8')

def decrypt_data(key, encrypted_data):
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")
    
    encrypted_data_bytes = b64decode(encrypted_data)
    iv = encrypted_data_bytes[:16]
    ciphertext = encrypted_data_bytes[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_data = cipher.decrypt(ciphertext)
    decrypted_data = unpad(decrypted_padded_data, AES.block_size)
    
    return decrypted_data.decode('utf-8')

key = get_random_bytes(32)
data = "Sensitive data to encrypt"

encrypted_str = encrypt_data(key, data)
print(f"Encrypted Data: {encrypted_str}")

decrypted_data = decrypt_data(key, encrypted_str)
print(f"Decrypted Data: {decrypted_data}")
