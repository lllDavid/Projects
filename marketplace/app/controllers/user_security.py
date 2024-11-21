import random
import string
from datetime import datetime, timedelta
from ..models.user import UserSecurity 

def initialize_user_security() -> UserSecurity:
    return UserSecurity(
        two_factor_enabled=False,
        password_hash="",
        reset_email="",
        two_factor_code="",
        two_factor_code_expiry=datetime.now(),
        is_verified=False
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

def initiate_password_reset(user: UserSecurity, reset_email: str) -> bool:
    user.reset_email = reset_email
    return True

def verify_reset_email(user: UserSecurity, reset_email: str) -> bool:
    return user.reset_email == reset_email

def generate_2fa_code():
    return ''.join(random.choices(string.digits, k=6))



