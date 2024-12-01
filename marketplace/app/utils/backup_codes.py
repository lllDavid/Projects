from random import randint
from typing import List
from argon2 import PasswordHasher

ph = PasswordHasher()

def generate_backup_codes(num_codes: int = 6) -> List[str]:
    return [str(randint(100000, 999999)) for _ in range(num_codes)]

def hash_backup_codes(backup_codes: List[str]) -> List[str]:
    return [ph.hash(code) for code in backup_codes]



