from models.user import User

def register():
    username = str(input("Choose a username: "))
    password = input("Choose a password: ")
    email = str("Enter a e-mail address: ")
    reset_email = str("Enter a backup e-mail:")

    User.add_user(
        id=1,  
        ip_address="192.168.0.1",
        role="admin",
        username=username,
        email=email,
        reset_email=reset_email,
        password_hash="hashed_password_12345",
        two_factor_enabled=True,
        is_verified=True,
        is_banned=False,
        ban_reason="",
        is_active=True,
        login_count=5,
        failed_login_attempts=0, 
    )

register()
