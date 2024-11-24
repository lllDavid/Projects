from argon2 import PasswordHasher

def hash_password(password: str, time_cost: int = 2, memory_cost: int = 102400, parallelism: int = 8):
    ph = PasswordHasher(time_cost=time_cost, memory_cost=memory_cost, parallelism=parallelism)
    
    hashed_password = ph.hash(password)
    return hashed_password

def verify_password(stored_hash: str, password: str):
    ph = PasswordHasher()
    try:
        ph.verify(stored_hash, password)  
        return True
    except:
        return False

