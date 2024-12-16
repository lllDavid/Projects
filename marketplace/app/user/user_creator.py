from datetime import datetime

from marketplace.app.user import user_db
from marketplace.helpers.roles import Role
from marketplace.app.user.user import User
from marketplace.app.user.user_profile import UserProfile
from marketplace.app.user.user_bank import UserBank
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.user.user_fingerprint import UserFingerprint

class UserCreator:
    def create_user_profile(self, username: str, email: str, role: Role) -> UserProfile:
        return UserProfile(id=None, username=username, email=email, role=role)
    
    def create_user_bank(self) -> UserBank:
        return UserBank(
            account_holder=None,
            account_number=None,
            routing_number=None,
            iban=None,
            swift_bic=None,
            date_linked=None
        )

    def create_user_status(self) -> UserStatus:
        return UserStatus(
            is_online=False,
            is_banned=False,
            is_inactive=True,
            ban_reason=None,
            ban_duration=None,
            ban_type=None,
            ban_start_time=None,
            ban_end_time=None
        )

    def create_user_history(self) -> UserHistory:
        return UserHistory(
            login_count=0,
            failed_login_count=0,
            last_login=None,
            last_failed_login=None,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    
    def create_user_security(self, password: str) -> UserSecurity:
        return UserSecurity(
            password_hash=UserSecurity.hash_password(password),
            two_factor_enabled=False,
            two_factor_secret_key=None,
            two_factor_backup_codes=None,
            two_factor_backup_codes_hash=None
        )
    
    def create_user_fingerprint(self) -> UserFingerprint:
        return UserFingerprint(
            username_history=set(),
            email_address_history=set(),
            mac_address=None,
            associated_ips=None,
            avg_login_frequency=None,
            avg_session_duration=None,
            geolocation_country=None,
            geolocation_city=None,
            geolocation_latitude=None,
            geolocation_longitude=None,
            browser_info=None,
            os_name=None,
            os_version=None,
            device_type=None,
            device_manufacturer=None,
            device_model=None,
            user_preferences=None,
            user_agent=None,
            device_id=None,
            screen_resolution=None,
            two_factor_enabled=None,
            transaction_history=None,
            vpn_usage=None,
            behavioral_biometrics=None
        )

    def create_user(self, username: str, email: str, password: str) -> User:
        user_profile = self.create_user_profile(username, email, role=Role.USER)
        user_bank = self.create_user_bank()
        user_status = self.create_user_status()
        user_history = self.create_user_history()
        user_security = self.create_user_security(password)
        user_fingerprint = self.create_user_fingerprint()

        return User(
            user_profile=user_profile,
            user_bank = user_bank,
            user_status=user_status,
            user_history=user_history,
            user_security=user_security,
            user_fingerprint=user_fingerprint
        )

    def create_and_save_user(self, username: str, email: str, password: str) -> User | None:
        try:
            user = self.create_user(username, email, password)
            user_db.insert_user(user)
            return user
        except ValueError as e:
            print(f"Error: {e}")
            return None 
        except Exception as e:
            print(f"Error: {e}")
            return None

        
