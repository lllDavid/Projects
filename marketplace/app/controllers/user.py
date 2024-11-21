from app.models.user import UserDetails, User, UserSecurity, UserStatus, UserLoginHistory
from app.models.roles import Role
from datetime import datetime

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

def create_and_save_user():
    user_data = get_user_input()

    user_details = create_user_details(user_data['username'], user_data['email'], user_data['password'])

    print(f"Created user: {user_data['username']}")
    return user_details


if __name__ == "__main__":
    user_input = get_user_input()
    user_details = create_user(user_input['username'], user_input['email'], user_input['password'])
