from mariadb import connect
from marketplace.config import Config
from marketplace.app.user.user import User
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_details import UserDetails
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_security import UserSecurity

conn = connect(
    user=Config.DB_CONFIG["user"],       
    password=Config.DB_CONFIG["password"],   
    host=Config.DB_CONFIG["host"],           
    port=Config.DB_CONFIG["port"],                  
    database=Config.DB_CONFIG["database"]  
)

def get_user_by_id(user_id: int) -> User | None:
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, username, email, role FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    if user:
        return User(username=user[1], email=user[2], password="", role=user[3])
    return None

def get_user_by_username(username: str) -> UserDetails | None:
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, username, email, role FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        user_details = get_user_details(user[0])
        return user_details
    return None

def get_user_by_email(email: str) -> UserDetails | None:
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, username, email, role FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        user_details = get_user_details(user[0])
        return user_details
    return None

def get_user_details(user_id: int) -> UserDetails | None:
    user = get_user_by_id(user_id)
    if not user:
        return None
    security = get_user_security(user_id)
    if not security:
        return None
    status = get_user_status(user_id)
    if not status:
        return None
    history = get_user_history(user_id)
    if not history:
        return None
    
    user_details = UserDetails(
        user=user, 
        security=security, 
        status=status, 
        history=history
    )
    
    return user_details

def get_user_security(user_id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, password_hash, two_factor_enabled, two_factor_secret_key, two_factor_backup_codes_hash FROM user_security WHERE user_id = %s", (user_id,))
    security = cursor.fetchone()
    cursor.close()
    if security:
        return UserSecurity(
            password_hash=security[1],
            two_factor_enabled=security[2],
            two_factor_secret_key=security[3],
            two_factor_backup_codes=None,
            two_factor_backup_codes_hash=security[4],
        )
    return None

def get_user_status(user_id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, is_banned, ban_reason, ban_duration FROM user_status WHERE user_id = %s", (user_id,))
    status = cursor.fetchone()
    cursor.close()
    if status:
        return UserStatus(
            is_online=False,
            is_banned=status[1],
            ban_reason=status[2],
            ban_duration=status[3],
        )
    return None

def get_user_history(user_id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, login_count, failed_login_count last_login, last_failed_login, created_at, updated_at FROM user_history WHERE user_id = %s", (user_id,))
    history = cursor.fetchone()
    cursor.close()
    if history:
        return UserHistory(
            login_count=history[1],
            failed_login_count=history[2],
            last_login=history[3],
            last_failed_login=history[4],
            created_at=history[5],
            updated_at=history[6],
        )
    return None

def get_password_hash(username: str) -> str | None:
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM user_security WHERE user_id = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return result[0] 
    return None  
