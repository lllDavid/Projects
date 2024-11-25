import os
import random
from argon2 import PasswordHasher

# Initialize Argon2id PasswordHasher
ph = PasswordHasher()

# Function to generate a 6-digit backup code
def generate_backup_code() -> str:
    # Generate a 6-digit random number as a string (e.g., '123456')
    return str(random.randint(100000, 999999))

# Function to hash a single backup code using Argon2id
def hash_backup_code(backup_code: str) -> str:
    # Hash the backup code using Argon2id
    return ph.hash(backup_code)

# Example of generating and hashing backup codes
def generate_and_hash_backup_codes(num_codes: int = 6):
    hashed_codes = []
    
    for _ in range(num_codes):
        backup_code = generate_backup_code()  # Generate a random 6-digit code
        hashed_code = hash_backup_code(backup_code)  # Hash the code using Argon2id
        hashed_codes.append((backup_code, hashed_code))  # Store original and hashed codes
    
    return hashed_codes

# Example usage
hashed_codes = generate_and_hash_backup_codes()

# Output the original and hashed backup codes
for original_code, hashed_code in hashed_codes:
    print(f"Original Code: {original_code}, Hashed Code: {hashed_code}")
