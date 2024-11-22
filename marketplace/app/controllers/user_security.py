import random
import string
from typing import List
from datetime import datetime, timedelta
from ..models.user import UserSecurity 

# Updated function to accept values for user security
def initialize_user_security(
    password_hash: str,
    backup_codes: List[str],
    seed_phrase_hash: str,
    passphrase_viewed: bool,
    passphrase_hash: str,
    two_factor_enabled: bool,
    two_factor_code: str,
    two_factor_code_expiry: datetime | None
) -> UserSecurity:
    return UserSecurity(
        password_hash=password_hash,
        backup_codes=backup_codes,
        seed_phrase_hash=seed_phrase_hash,
        passphrase_viewed=passphrase_viewed,
        passphrase_hash=passphrase_hash,
        two_factor_enabled=two_factor_enabled,
        two_factor_code=two_factor_code,
        two_factor_code_expiry=two_factor_code_expiry
    )

def enable_two_factor(user: UserSecurity) -> bool:
    if user.two_factor_enabled:
        return False  

    user.two_factor_enabled = True
    user.two_factor_code = generate_2fa_code()
    user.two_factor_code_expiry = datetime.now() + timedelta(minutes=1)  
    return True

def disable_two_factor(user: UserSecurity) -> bool:
    if not user.two_factor_enabled:
        return False  

    user.two_factor_enabled = False
    user.two_factor_code = ""
    user.two_factor_code_expiry = datetime.now()
    return True

def verify_two_factor_code(user: UserSecurity, code: str) -> bool:
    if user.two_factor_code_expiry and datetime.now() > user.two_factor_code_expiry:
        return False  

    return user.two_factor_code == code

def generate_2fa_code():
    return ''.join(random.choices(string.digits, k=6))

