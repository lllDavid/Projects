from json import dumps
from mariadb import connect

from marketplace.config import Config
from marketplace.app.user.user import User
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_details import UserDetails
from marketplace.app.user.user_security import UserSecurity

conn = connect(
    user=Config.DB_CONFIG["user"],       
    password=Config.DB_CONFIG["password"],   
    host=Config.DB_CONFIG["host"],           
    port=Config.DB_CONFIG["port"],                  
    database=Config.DB_CONFIG["database"]  
)

def insert_user(user_details: UserDetails):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, email, role) VALUES (%s, %s, %s)", 
            (user_details.user.username, user_details.user.email, user_details.user.role.value)
        )  
        user_id = cursor.lastrowid  

        # Convert set of hashed backup codes to a list before inserting into the database
        two_factor_backup_codes_hash_json = dumps(list(user_details.user_security.two_factor_backup_codes_hash)) if user_details.user_security.two_factor_backup_codes_hash else None

        cursor.execute(
            "INSERT INTO user_security (user_id, password_hash, two_factor_enabled, two_factor_secret_key, two_factor_backup_codes_hash) VALUES (%s, %s, %s, %s, %s)",
            (user_id, 
             user_details.user_security.password_hash,  
             user_details.user_security.two_factor_enabled,
             user_details.user_security.two_factor_secret_key,
             two_factor_backup_codes_hash_json)
        )

        cursor.execute(
            "INSERT INTO user_status (user_id, is_banned, ban_reason, ban_duration) VALUES (%s, %s, %s, %s)", 
            (user_id, user_details.user_status.is_banned, user_details.user_status.ban_reason, user_details.user_status.ban_duration)
        )

        cursor.execute(
            "INSERT INTO user_history (user_id, login_count, last_login, failed_login_count, last_failed_login, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
            (user_id, 
             user_details.user_history.login_count,
             user_details.user_history.last_login,
             user_details.user_history.failed_login_count,  
             user_details.user_history.last_failed_login, 
             user_details.user_history.created_at, 
             user_details.user_history.updated_at)
        )

        conn.commit()  
        print("User and associated details inserted into the database.")
        user_details.user.id = user_id  
        return user_details  
    
    except conn.Error as e:
        conn.rollback()  
        print(f"Error occurred: {e}")
    finally:
        cursor.close()  

def update_user(user_id: int, username: str):
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET username = %s WHERE user_id = %s", 
                       (username, user_id))  
        conn.commit() 
        print("User updated successfully.")
        
    except conn.Error as e:
        conn.rollback() 
        print(f"Error occurred: {e}")
    finally:
        cursor.close()  

def delete_user(user_id: int):
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM user_history WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM user_status WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM user_security WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))

        conn.commit()  
        print("User and associated data deleted successfully.")
        
    except conn.Error as e:
        conn.rollback()  
        print(f"Error occurred: {e}")
    finally:
        cursor.close()  

def get_user_by_id(user_id: int) -> User | None:
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, username, email, role FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    if user:
        return User(id=user[0], username=user[1], email=user[2], role=user[3])
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
    user_security = get_user_security(user_id)
    if not user_security:
        return None
    user_status = get_user_status(user_id)
    if not user_status:
        return None
    user_history = get_user_history(user_id)
    if not user_history:
        return None
    
    user_details = UserDetails(
        user=user, 
        user_security=user_security, 
        user_status=user_status, 
        user_history=user_history
    )
    
    return user_details

def get_user_security(user_id: int) -> UserSecurity | None:
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

def get_user_status(user_id: int) -> UserStatus | None:
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, is_banned, ban_reason, ban_duration FROM user_status WHERE user_id = %s", (user_id,))
    status = cursor.fetchone()
    cursor.close()
    if status:
        return UserStatus(
            is_online=False,
            is_banned=status[0],
            ban_reason=status[1],
            ban_duration=status[2],
        )
    return None

def get_user_history(user_id: int) -> UserHistory | None:
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, login_count, failed_login_count, last_login, last_failed_login, created_at, updated_at FROM user_history WHERE user_id = %s", (user_id,))
    history = cursor.fetchone()
    cursor.close()
    if history:
        return UserHistory(
            login_count=history[0],
            failed_login_count=history[1],
            last_login=history[2],
            last_failed_login=history[3],
            created_at=history[4],
            updated_at=history[5],
        )
    return None

