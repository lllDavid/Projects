from models.user import User

def register():
    username = str(input("Choose a username: "))
    password = str(input("Choose a password: "))
    email = str(input("Enter a e-mail address: "))
    reset_email = str(input("Enter a backup e-mail:"))

    hashed_password = User.hash_password(password)

    User.add_user(
        id=1,  
        ip_address="127.0.0.1",
        role="User",
        username=username,
        email=email,
        reset_email=reset_email,
        password_hash=hashed_password,
        two_factor_enabled=True,
        is_verified=True,
        is_banned=False,
        ban_reason="",
        is_active=True,
        login_count=5,
        failed_login_attempts=0, 
    )

register()
