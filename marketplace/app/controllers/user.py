import re
from app.models.user import UserDetails, User, UserSecurity, UserStatus, UserLoginHistory
from app.models.roles import Role
from datetime import datetime

def is_valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

def is_strong_password(password: str) -> bool:
    return bool(re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{20,}$', password))

def is_unique_user(username: str, email: str) -> bool:
    return not ("taken" in username or "taken" in email)

def get_user_input():
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    return {
        "username": username,
        "email": email,
        "password": password
    }

def create_user(username: str, email: str, password: str) -> User:
    return User(id=None, username=username, email=email, password=password)

def create_user_security(email: str, password: str) -> UserSecurity:
    return UserSecurity(
        two_factor_enabled=False,
        password_hash=password,  
        reset_email=email,
        is_verified=False
    )

def create_user_status() -> UserStatus:
    return UserStatus(
        is_banned=False,
        ban_reason="",
        is_active=True,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

def create_user_login_history() -> UserLoginHistory:
    return UserLoginHistory(
        login_count=0,
        failed_login_attempts=0,
        last_login=datetime.now()
    )

def create_user_details(username: str, email: str, password: str) -> UserDetails:
    user = create_user(username, email, password)
    security = create_user_security(email, password)
    status = create_user_status()
    login_history = create_user_login_history()

    return UserDetails(
        ip_address="",
        role=Role.USER,
        reset_email=email,
        password_hash=password,  
        security=security,
        status=status,
        login_history=login_history,
        user=user
    )

def validate_user_data(username: str, email: str, password: str):
    if not is_valid_email(email):
        raise ValueError("Invalid email format.")

    if not is_strong_password(password):
        raise ValueError("Password must be at least 20 characters long, contain an uppercase letter, a number, and a special character.")

    if not is_unique_user(username, email):
        raise ValueError("Username or email is already taken.")

def create_and_save_user():
    while True:
        try:
            user_data = get_user_input()

            validate_user_data(user_data['username'], user_data['email'], user_data['password'])

            user_details = create_user_details(user_data['username'], user_data['email'], user_data['password'])

            print(f"Created user: {user_data['username']}")
            return user_details

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    user_details = create_and_save_user()
    if user_details:
        print("User created successfully!")
    else:
        print("User creation failed due to validation errors.")
