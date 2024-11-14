from app.models.user import User
from app.models.user_db import UserDB

user_db = UserDB()

def register_user():
    username = str(input("Choose a username: "))
    password = str(input("Choose a password: "))
    email = str(input("Enter an e-mail address: "))
    reset_email = str(input("Enter a backup e-mail: "))

    hashed_password = User.hash_password(password)

    user = User.add_user(
        id=1,  
        ip_address="127.0.0.1",
        role="User",
        username=username,
        email=email,
        reset_email=reset_email,
        password_hash=hashed_password,
        two_factor_enabled=False,
        is_verified=False,
        is_banned=False,
        ban_reason="",
        is_active=False,
        login_count=0,
        failed_login_attempts=0, 
    )
    add_user_to_db(user)

def add_user_to_db(user: User):
    user_db.add_user(user)

def delete_user_from_db(user: User):
    user_db.delete_user(user)

