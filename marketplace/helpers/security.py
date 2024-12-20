from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def encrypt_data(key, data):
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")
    
    # Generate a random IV (16 bytes for AES)
    iv = get_random_bytes(16)
    
    # Create a cipher object using AES CBC mode and the random IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the data to be a multiple of the block size (AES.block_size = 16 bytes)
    padded_data = pad(data.encode(), AES.block_size)
    
    # Encrypt the padded data
    ciphertext = cipher.encrypt(padded_data)
    
    # Combine the IV and ciphertext
    encrypted_data = iv + ciphertext
    
    # Encode the result in base64 to make it a safe text string for storage/transmission
    return b64encode(encrypted_data).decode('utf-8')

def decrypt_data(key, encrypted_data):
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")
    
    # Decode the base64-encoded string to bytes
    encrypted_data_bytes = b64decode(encrypted_data)
    
    # Extract the IV (first 16 bytes)
    iv = encrypted_data_bytes[:16]
    
    # Extract the ciphertext (remaining bytes after the IV)
    ciphertext = encrypted_data_bytes[16:]
    
    # Create a cipher object using AES CBC mode and the extracted IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    decrypted_padded_data = cipher.decrypt(ciphertext)
    
    # Remove padding
    decrypted_data = unpad(decrypted_padded_data, AES.block_size)
    
    # Return the decrypted data as a string
    return decrypted_data.decode('utf-8')

# Example usage:
key = get_random_bytes(32)  # AES-256 key (32 bytes)
data = "Sensitive data to encrypt"

# Encrypt the data
encrypted_str = encrypt_data(key, data)
print(f"Encrypted Data: {encrypted_str}")

# Decrypt the data
decrypted_data = decrypt_data(key, encrypted_str)
print(f"Decrypted Data: {decrypted_data}")
