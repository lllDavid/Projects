from json import dumps
from mariadb import connect

from marketplace.helpers.roles import Role
from marketplace.config import Config
from marketplace.app.user.user import User
from marketplace.app.user.user_bank import UserBank
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.user.user_fingerprint import UserFingerprint

conn = connect(
    user=Config.USER_DB_CONFIG["user"],
    password=Config.USER_DB_CONFIG["password"],
    host=Config.USER_DB_CONFIG["host"],
    port=Config.USER_DB_CONFIG["port"],
    database=Config.USER_DB_CONFIG["database"]
)

# --------------------------------------------------------------
# Section 1: Insert, Delete and Update User attributes
# --------------------------------------------------------------

def insert_user(user: User):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO user (username, email, role) VALUES (%s, %s, %s)",
            (user.username, user.email, user.role.value)
        )
          
        user_id = cursor.lastrowid  

        two_factor_backup_codes_hash_json = dumps(list(user.user_security.two_factor_backup_codes_hash)) if user.user_security.two_factor_backup_codes_hash else None

        cursor.execute(
            "INSERT INTO user_bank (user_id, bank_name, account_holder, account_number, routing_number, iban, swift_bic, date_linked) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (user_id, user.user_bank.bank_name, user.user_bank.account_holder, user.user_bank.account_number,
             user.user_bank.routing_number, user.user_bank.iban, user.user_bank.swift_bic, user.user_bank.date_linked)
        )

        cursor.execute(
            "INSERT INTO user_status (user_id, is_banned, is_inactive, ban_type, ban_reason, ban_duration, "
            "ban_start_time, ban_end_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (user_id, user.user_status.is_banned, user.user_status.is_inactive, user.user_status.ban_type,
             user.user_status.ban_reason, user.user_status.ban_duration, user.user_status.ban_start_time,
             user.user_status.ban_end_time)
        )

        cursor.execute(
            "INSERT INTO user_history (user_id, login_count, last_login, failed_login_count, last_failed_login, "
            "created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (user_id, user.user_history.login_count, user.user_history.last_login,
             user.user_history.failed_login_count, user.user_history.last_failed_login,
             user.user_history.created_at, user.user_history.updated_at)
        )

        cursor.execute(
            "INSERT INTO user_security (user_id, password_hash, two_factor_enabled, two_factor_secret_key, "
            "two_factor_backup_codes_hash) VALUES (%s, %s, %s, %s, %s)",
            (user_id, user.user_security.password_hash, user.user_security.two_factor_enabled,
             user.user_security.two_factor_secret_key, two_factor_backup_codes_hash_json)
        )

        cursor.execute(
            "INSERT INTO user_fingerprint (user_id, username_history, email_address_history, mac_address, "
            "associated_ips, avg_login_frequency, avg_session_duration, geolocation_country, geolocation_city, "
            "geolocation_latitude, geolocation_longitude, browser_info, os_name, os_version, device_type, "
            "device_manufacturer, device_model, user_preferences, user_agent, device_id, screen_resolution, "
            "two_factor_enabled, vpn_usage, behavioral_biometrics) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                user_id,
                dumps(list(user.user_fingerprint.username_history)),
                dumps(list(user.user_fingerprint.email_address_history)),
                user.user_fingerprint.mac_address,
                dumps(user.user_fingerprint.associated_ips) if user.user_fingerprint.associated_ips else None,
                dumps(user.user_fingerprint.avg_login_frequency) if user.user_fingerprint.avg_login_frequency else None,
                dumps(user.user_fingerprint.avg_session_duration) if user.user_fingerprint.avg_session_duration else None,
                user.user_fingerprint.geolocation_country,
                user.user_fingerprint.geolocation_city,
                user.user_fingerprint.geolocation_latitude,
                user.user_fingerprint.geolocation_longitude,
                user.user_fingerprint.browser_info,
                user.user_fingerprint.os_name,
                user.user_fingerprint.os_version,
                user.user_fingerprint.device_type,
                user.user_fingerprint.device_manufacturer,
                user.user_fingerprint.device_model,
                dumps(user.user_fingerprint.user_preferences) if user.user_fingerprint.user_preferences else None,
                user.user_fingerprint.user_agent,
                user.user_fingerprint.device_id,
                user.user_fingerprint.screen_resolution,
                user.user_fingerprint.two_factor_enabled,
                user.user_fingerprint.vpn_usage,
                dumps(user.user_fingerprint.behavioral_biometrics) if user.user_fingerprint.behavioral_biometrics else None
            )
        )

        conn.commit()  
        print("User inserted into the database.")
        user.id = user_id  
        return user

    except conn.Error as e:
        conn.rollback()  
        print(f"Error occurred: {e}")
    finally:
        cursor.close()


def update_username(id: int, username: str):
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE user SET username = %s WHERE id = %s", (username, id))
        conn.commit()
        print("Username updated successfully.")
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()


def update_email(id: int, email: str):
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE user SET email = %s WHERE id = %s", (email, id))
        conn.commit()
        print("Email updated successfully.")
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()


def update_password(user_id: int, password: str):
    cursor = conn.cursor()
    try:
        password_hash = UserSecurity.hash_password(password)

        cursor.execute("UPDATE user_security SET password_hash = %s WHERE user_id = %s", (password_hash, user_id))
        conn.commit()
        print("Password updated successfully.")
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()


# --------------------------------------------------------------
# Section 2: User Retrieval by Specific Criteria
# --------------------------------------------------------------

def get_user_by_id(id: int) -> User | None:
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, role FROM user WHERE id = %s", (id,))
    user = cursor.fetchone()
    cursor.close()
    if user:
        return get_user_from_db(user[0])
    return None


def get_user_by_username(username: str) -> User | None:
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, role FROM user WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return get_user_from_db(user[0])
    return None


def get_user_by_email(email: str) -> User | None:
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, role FROM user WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return get_user_from_db(user[0])
    return None


# --------------------------------------------------------------
# Section 3: User Object Components by User ID
# --------------------------------------------------------------

def get_user(user_id: int) -> tuple[str, str, Role] | None:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, email, role FROM user WHERE id = %s",
        (user_id,)
    )
    user_data = cursor.fetchone()
    cursor.close()
    
    if user_data:
        username, email, role_str = user_data
        role = Role(role_str)
        return username, email, role 
    return None



def get_user_bank(user_id: int) -> UserBank | None:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_id, bank_name, account_holder, account_number, routing_number, iban, swift_bic, date_linked FROM user_bank WHERE user_id = %s", 
        (user_id,)
    )
    bank = cursor.fetchone()
    cursor.close()
    if bank:
        return UserBank(
            bank_name=bank[1],
            account_holder=bank[3],
            account_number=bank[4],
            routing_number=bank[5],
            iban=bank[5],
            swift_bic=bank[6],
            date_linked=bank[7]
        )
    return None


def get_user_status(user_id: int) -> UserStatus | None:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_id, is_banned, is_inactive, ban_type, ban_reason, ban_duration, "
        "ban_start_time, ban_end_time FROM user_status WHERE user_id = %s", (user_id,)
    )
    status = cursor.fetchone()
    cursor.close()
    if status:
        return UserStatus(
            is_online=False,
            is_banned=status[1],
            is_inactive=status[2],
            ban_type=status[3],
            ban_reason=status[4],
            ban_duration=status[5],
            ban_start_time=status[6],
            ban_end_time=status[7]
        )
    return None


def get_user_history(user_id: int) -> UserHistory | None:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_id, login_count, failed_login_count, last_login, last_failed_login, "
        "created_at, updated_at, transaction_history FROM user_history WHERE user_id = %s", (user_id,)
    )
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
            transaction_history=history[7]
        )
    return None


def get_user_security(user_id: int) -> UserSecurity | None:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_id, password_hash, two_factor_enabled, two_factor_secret_key, "
        "two_factor_backup_codes_hash FROM user_security WHERE user_id = %s", (user_id,)
    )
    security = cursor.fetchone()
    cursor.close()
    if security:
        return UserSecurity(
            password_hash=security[1],
            two_factor_enabled=security[2],
            two_factor_secret_key=security[3],
            two_factor_backup_codes=None,
            two_factor_backup_codes_hash=security[4]
        )
    return None


def get_user_fingerprint(user_id: int) -> UserFingerprint | None:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_id, username_history, email_address_history, mac_address, associated_ips, "
        "avg_login_frequency, avg_session_duration, geolocation_country, geolocation_city, "
        "geolocation_latitude, geolocation_longitude, browser_info, os_name, os_version, "
        "device_type, device_manufacturer, device_model, user_preferences, user_agent, device_id, "
        "screen_resolution, two_factor_enabled, vpn_usage, behavioral_biometrics "
        "FROM user_fingerprint WHERE user_id = %s", (user_id,)
    )
    fingerprint = cursor.fetchone()
    cursor.close()

    if fingerprint:
        return UserFingerprint(
            username_history=fingerprint[1],
            email_address_history=fingerprint[2],
            mac_address=fingerprint[3],
            associated_ips=fingerprint[4],
            avg_login_frequency=fingerprint[5],
            avg_session_duration=fingerprint[6],
            geolocation_country=fingerprint[7],
            geolocation_city=fingerprint[8],
            geolocation_latitude=fingerprint[9],
            geolocation_longitude=fingerprint[10],
            browser_info=fingerprint[11],
            os_name=fingerprint[12],
            os_version=fingerprint[13],
            device_type=fingerprint[14],
            device_manufacturer=fingerprint[15],
            device_model=fingerprint[16],
            user_preferences=fingerprint[17],
            user_agent=fingerprint[18],
            device_id=fingerprint[19],
            screen_resolution=fingerprint[20],
            two_factor_enabled=fingerprint[21],
            vpn_usage=fingerprint[23],
            behavioral_biometrics=fingerprint[24]
        )
    return None

# --------------------------------------------------------------
# Section 4: Complete User Retrieval
# --------------------------------------------------------------

def get_user_from_db(user_id: int) -> User | None:

    user_data = get_user(user_id)
    if not user_data:
        return None

    user_bank = get_user_bank(user_id)
    if not user_bank:
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

    user_fingerprint = get_user_fingerprint(user_id)
    if not user_fingerprint:
        return None

    user = User(
        id=user_id,
        username=user_data[0],
        email=user_data[1],
        role=user_data[2],
        user_bank=user_bank,
        user_security=user_security,
        user_status=user_status,
        user_history=user_history,
        user_fingerprint=user_fingerprint
    )

    return user
