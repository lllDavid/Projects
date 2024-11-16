from app.models.user import User
import app.models.user_db as user_db
import app.models.roles as roles

def register_user(username:str, email:str, reset_email:str, hashed_password:str) -> User:
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
    return user

def get_user_input() -> dict[str, str]:
    username = str(input("Choose a username: "))
    password = str(input("Choose a password: "))
    email = str(input("Enter an e-mail address: "))
    reset_email = str(input("Enter a backup e-mail: "))

    return {
        "username": username,
        "password": password,
        "email": email,
        "reset_email": reset_email
    }

def hash_user_password(password:str):
    hashed_password = User.hash_password(password)
    return hashed_password

def reset_user_password(user:User):
    ...

def ban_user(user:User):
    ...

def verify_user(user:User):
    ...

def add_user_to_db(user: User):
    user_db.add_user(user)

def delete_user_from_db(user: User):
    user_db.delete_user(user)

def get_all_users_from_db():
    user_db.get_all_users()

def get_user_role(user:User):
    roles.get_role(user)
    
def main():
    user_input = get_user_input()

    hashed_password = hash_user_password(user_input["password"])

    user = register_user(
        username=user_input["username"],
        email=user_input["email"],
        reset_email=user_input["reset_email"],
        hashed_password=hashed_password
    )

    add_user_to_db(user)

    get_user_role(user)

if __name__ == "__main__":
    main()