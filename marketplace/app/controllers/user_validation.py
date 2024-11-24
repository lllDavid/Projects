from re import match

def is_valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(match(email_regex, email))

def is_valid_password(password: str) -> bool:
    password = password.strip()  
    return bool(match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_])[\s\S]{30,}$', password))

def is_unique_user(username: str) -> bool:
    return not ("taken" in username)

def validate_user_data(username: str, email: str, password: str):
    if not is_valid_email(email):
        raise ValueError("Invalid email format.")

    if not is_valid_password(password):
        raise ValueError("Password must be at least 30 characters long, contain an uppercase letter, a number, and a special character.")

    if not is_unique_user(username):
        raise ValueError("Username already taken.")
