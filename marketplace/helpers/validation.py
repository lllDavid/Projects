from re import match
from flask import flash
from mariadb import connect
from marketplace.config import Config

conn = connect(
    user=Config.DB_CONFIG["user"],
    password=Config.DB_CONFIG["password"],
    host=Config.DB_CONFIG["host"],
    port=Config.DB_CONFIG["port"],
    database=Config.DB_CONFIG["database"]
)

def is_unique_user_and_email(username: str, email: str):
    cursor = conn.cursor()
    cursor.execute(""" 
        SELECT username, email FROM user_profile WHERE username = %s OR email = %s """, (username, email))
    user = cursor.fetchone()
    cursor.close()

    if user:
        if user[0] == username:
            return "username"
        elif user[1] == email:
            return "email"
    return None

def is_valid_username(username):
    # 1. Check if username length is between 3 and 20 characters
    if len(username) < 3 or len(username) > 20:
        return "Username must be between 3 and 20 characters long."

    if not match(r'^[A-Za-z0-9_-]+$', username):
        return "Username can only contain letters, numbers, underscores, and hyphens."
    
    # 3. Check if username has no leading or trailing whitespace
    if username != username.strip():
        return "Username cannot have leading or trailing spaces."
    
    # 4. Check for reserved words
    reserved_words = ['admin', 'root', 'superuser', 'shutdown', 'localhost']
    if username.lower() in reserved_words:
        return "Username contains reserved or sensitive words."
    # 5. Check for common database manipulation or SQL injection-related keywords
    sql_keywords = ['select', 'insert', 'delete', 'drop', 'update', 'truncate', 'union', 'where', 'from', 'alter', 'join', 'drop']
    if any(keyword in username.lower() for keyword in sql_keywords):
        return "Username contains database manipulation or SQL injection-related words."

    # 6. Check for common Linux commands or system-related terms
    linux_commands = ['ls', 'rm', 'cat', 'chmod', 'chown', 'touch', 'mkdir', 'rmdir', 'sudo', 'passwd', 'shutdown', 'reboot', 'halt', 'ping', 'ps', 'kill', 'ifconfig', 'df', 'mount']
    if any(command in username.lower() for command in linux_commands):
        return "Username contains Linux commands or system-related terms."
    
    # 7. Check for periods not in the first or last position
    if username.startswith('.') or username.endswith('.'):
        return "Username cannot start or end with a period."
    
    return True



def is_valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(match(email_regex, email))

def is_valid_password(password: str) -> bool:
    password = password.strip()

    if len(password) > 40:
        return False

    regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_])[\s\S]{30,}$'

    if not match(regex, password):
        return False

    return True

def validate_user_input(username, email, password):
    if not all([username, email, password]):
        flash("All fields are required!", "error")
        return False
    
    user_status = is_unique_user_and_email(username, email)
    
    if user_status == "username":
        flash("Username is already taken.", "error")
        return False
    elif user_status == "email":
        flash("Email is already taken.", "error")
        return False
    
    username_validation = is_valid_username(username)
    if username_validation != True:
        flash(username_validation, "error")
        return False

    if not is_valid_email(email):
        flash("Invalid email format.", "error")
        return False

    if not is_valid_password(password):
        flash("Password must be between 30 and 40 characters, contain an uppercase letter, a number, and a special character.", "error")
        return False
    
    return True