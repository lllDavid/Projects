# In models/user.py

class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f"User(ID: {self.id}, Username: {self.username}, Email: {self.email})"


class UserSecurity:
    def __init__(self, password_hash, two_factor_enabled, two_factor_backup_codes, two_factor_code, two_factor_code_expiry):
        self.password_hash = password_hash
        self.two_factor_enabled = two_factor_enabled
        self.two_factor_backup_codes = two_factor_backup_codes
        self.two_factor_code = two_factor_code
        self.two_factor_code_expiry = two_factor_code_expiry

    def __str__(self):
        return (f"Security(Password Hash: {self.password_hash}, "
                f"2FA Enabled: {self.two_factor_enabled}, "
                f"2FA Backup Codes: {len(self.two_factor_backup_codes)}, "
                f"2FA Code: {self.two_factor_code}, "
                f"2FA Expiry: {self.two_factor_code_expiry})")


class UserStatus:
    def __init__(self, is_online, is_banned, ban_reason, ban_duration, created_at, updated_at):
        self.is_online = is_online
        self.is_banned = is_banned
        self.ban_reason = ban_reason
        self.ban_duration = ban_duration
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return (f"Status(Online: {self.is_online}, "
                f"Banned: {self.is_banned}, "
                f"Ban Reason: {self.ban_reason}, "
                f"Ban Duration: {self.ban_duration}, "
                f"Created At: {self.created_at}, "
                f"Updated At: {self.updated_at})")


class UserLoginHistory:
    def __init__(self, login_count, failed_login_attempts, last_failed_login, last_successful_login):
        self.login_count = login_count
        self.failed_login_attempts = failed_login_attempts
        self.last_failed_login = last_failed_login
        self.last_successful_login = last_successful_login

    def __str__(self):
        return (f"Login History(Login Count: {self.login_count}, "
                f"Failed Attempts: {self.failed_login_attempts}, "
                f"Last Failed: {self.last_failed_login}, "
                f"Last Successful: {self.last_successful_login})")


class UserDetails:
    def __init__(self, user, role, security, status, login_history, created_at, updated_at):
        self.user = user
        self.role = role
        self.security = security
        self.status = status
        self.login_history = login_history
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return (f"User Details:\n"
                f"{self.user}\n"
                f"Role: {self.role}\n"
                f"{self.security}\n"
                f"{self.status}\n"
                f"{self.login_history}\n"
                f"Created At: {self.created_at}\n"
                f"Updated At: {self.updated_at}")
