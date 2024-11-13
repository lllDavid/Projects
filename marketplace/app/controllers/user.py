from models.user import User
from models.user_db import User_DB

def register() -> None:
    # Get input from the user
    username = str(input("Choose a username: "))
    password = str(input("Choose a password: "))
    email = str(input("Enter an e-mail address: "))
    reset_email = str(input("Enter a backup e-mail: "))

    # Hash the password
    hashed_password = User.hash_password(password)

    # Create the user object (this also returns the user)
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
    
    # Once the user is created, add them to the database
    add_user_to_db(user)

def add_user_to_db(user: User):
    # Add the user to the database
    User_DB.add_user(user)
    print(f"User {user.username} added to the database!")

if __name__ == "main":
    register()