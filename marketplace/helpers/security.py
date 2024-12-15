from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt data using AES-256
def encrypt_data(key, data):
    # Ensure the key is 32 bytes for AES-256
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")

    # Generate a random 16-byte initialization vector (IV)
    iv = get_random_bytes(16)

    # Create a cipher object using AES.MODE_CBC (Cipher Block Chaining)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the data to be a multiple of the block size (16 bytes)
    padded_data = pad(data.encode(), AES.block_size)

    # Encrypt the padded data
    ciphertext = cipher.encrypt(padded_data)

    # Return the IV + ciphertext, so it can be used for decryption
    return iv + ciphertext

# Function to decrypt data using AES-256
def decrypt_data(key, encrypted_data):
    # Ensure the key is 32 bytes for AES-256
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")

    # Extract the IV and the actual ciphertext
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    # Create a cipher object using AES.MODE_CBC
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    decrypted_data = cipher.decrypt(ciphertext)

    # Unpad the decrypted data to remove the padding
    return unpad(decrypted_data, AES.block_size).decode()

# Example usage:
key = get_random_bytes(32)  # AES-256 requires a 32-byte key
data = "This is a secret message."

# Encrypt the data
encrypted_data = encrypt_data(key, data)
print("Encrypted data:", encrypted_data)

# Decrypt the data
decrypted_data = decrypt_data(key, encrypted_data)
print("Decrypted data:", decrypted_data)
