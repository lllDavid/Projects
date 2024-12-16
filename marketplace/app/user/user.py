from dataclasses import dataclass

from marketplace.app.user.user_profile import UserProfile
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.user.user_fingerprint import UserFingerprint

@dataclass
class User:
    user_profile: UserProfile
    user_status: UserStatus
    user_history: UserHistory
    user_security: UserSecurity
    user_fingerprint: UserFingerprint

    def update_user_profile(self, new_user_profile: UserProfile):
        self.user_profile = new_user_profile
        print(f"User profile updated.")

    def update_user_security(self, new_user_security: UserSecurity):
        self.user_security = new_user_security
        print("Security info updated.")

    def update_user_status(self, new_user_status: UserStatus):
        self.user_status = new_user_status
        print("Status updated.")

    def update_user_history(self, new_user_history: UserHistory):
        self.user_history = new_user_history
        print("User history updated.")
    
    def update_user_fingerprint(self, new_user_fingerprint: UserFingerprint):
        self.user_fingerprint = new_user_fingerprint
        
    def __str__(self):
        return (f"User: {self.user_profile}, Security: {self.user_security}, "
                f"Status: {self.user_status}, History: {self.user_history}, Fingerprint: {self.user_fingerprint}")

