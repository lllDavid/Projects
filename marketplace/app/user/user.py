from dataclasses import dataclass

from marketplace.helpers.roles import Role
from marketplace.app.user.user_bank import UserBank
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.user.user_fingerprint import UserFingerprint

@dataclass
class User:
    id: int | None
    username: str
    email: str
    role: Role
    user_bank: UserBank
    user_status: UserStatus
    user_history: UserHistory
    user_security: UserSecurity
    user_fingerprint: UserFingerprint

    def update_user_bank(self, new_user_bank: UserBank):
        self.user_bank = new_user_bank
        print("Bank information updated.")

    def update_user_status(self, new_user_status: UserStatus):
        self.user_status = new_user_status
        print("Status updated.")

    def update_user_history(self, new_user_history: UserHistory):
        self.user_history = new_user_history
        print("User history updated.")
    
    def update_user_security(self, new_user_security: UserSecurity):
        self.user_security = new_user_security
        print("Security info updated.")

    def update_user_fingerprint(self, new_user_fingerprint: UserFingerprint):
        self.user_fingerprint = new_user_fingerprint
        print("User fingerprint updated.")

    def __str__(self):
        return (f"User ID: {self.id}, Bank: {self.user_bank}, "
                f"Status: {self.user_status}, History: {self.user_history}, "
                f"Security: {self.user_security}, Fingerprint: {self.user_fingerprint}")
