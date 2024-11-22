import random
import string
from datetime import datetime, timedelta
from ..models.user import UserSecurity 

def initialize_user_security() -> UserSecurity:
    return UserSecurity(
        password_hash="",
        backup_codes=[],
        seed_phrase_hash="",
        passphrase_viewed=False,
        passphrase_hash = "",
        two_factor_enabled=False,
        two_factor_code="",
        two_factor_code_expiry=datetime.now()
        
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



