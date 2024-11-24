from argon2 import PasswordHasher

def hash_password_argon2(password: str, time_cost: int = 2, memory_cost: int = 102400, parallelism: int = 8):
    ph = PasswordHasher(time_cost=time_cost, memory_cost=memory_cost, parallelism=parallelism)
    
    hashed_password = ph.hash(password)  
    return hashed_password

def verify_password_argon2(stored_hash: str, password: str):
    ph = PasswordHasher()
    try:
        # Argon2 handles salt extraction automatically from the stored hash
        ph.verify(stored_hash, password)  
        return True
    except:
        return False

if __name__ == "__main__":
    password = "my_secure_password"
    
    hashed_password = hash_password_argon2(password)
    print("Hashed Password:", hashed_password)

    is_valid = verify_password_argon2(hashed_password, password)
    print("Password verification result:", is_valid)
