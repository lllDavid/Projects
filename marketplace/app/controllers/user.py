from app.models.user import UserDetails, User, UserSecurity, UserStatus, UserLoginHistory
from app.models.roles import Role
from datetime import datetime

def create_user(username: str, email: str, password: str):
    user = User(id=1, username=username, email=email, password=password) 

    security = UserSecurity(
        two_factor_enabled=False,
        password_hash=password,  
        reset_email=email,
        is_verified=False
    )

    status = UserStatus(
        is_banned=False,
        ban_reason="",
        is_active=True,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    login_history = UserLoginHistory(
        login_count=0,
        failed_login_attempts=0,
        last_login=datetime.now()
    )

    user_details = UserDetails(
        ip_address="",
        role=Role.USER,
        reset_email=email,
        password_hash=password,  
        security=security,
        status=status,
        login_history=login_history,
        user=user
    )
    
    print(f"Created user {username}")
    return user_details

def get_user_input():
    username = str(input("Username: "))
    email =  str(input("Email: "))
    password = str(input("Password: "))

    return {
        "username": username,
        "email": email,
        "password": password
    }

if __name__ == "__main__":
    user_input = get_user_input()
    user_details = create_user(user_input['username'], user_input['email'], user_input['password'])
