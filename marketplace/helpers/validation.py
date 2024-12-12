from re import match
from flask import flash
from mariadb import connect
from marketplace.config import Config

conn = connect(
    user=Config.DB_CONFIG["user"],
    password=Config.DB_CONFIG["password"],
    host=Config.DB_CONFIG["host"],
    port=Config.DB_CONFIG["port"],
    database=Config.DB_CONFIG["database"],
)


def is_valid_email(email: str) -> bool:
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(match(email_regex, email))


def is_valid_password(password: str) -> bool:
    password = password.strip()

    if len(password) > 40:
        return False

    regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_])[\s\S]{30,}$"

    if not match(regex, password):
        return False

    return True


def is_unique_user(username: str) -> bool:
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return False

    return True


def is_unique_email(email: str) -> bool:
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return False

    return True


def validate_user_input(username, email, password):
    if not all([username, email, password]):
        flash("All fields are required!", "error")
        return False

    if not is_valid_email(email):
        flash("Invalid email format.", "error")
        return False

    if not is_valid_password(password):
        flash(
            "Password must be between 30 and 40 characters, contain an uppercase letter, a number, and a special character.",
            "error",
        )
        return False

    if not is_unique_user(username):
        flash("Username already taken.", "error")
        return False

    if not is_unique_email(email):
        flash("Email already registered.", "error")
        return False

    return True
