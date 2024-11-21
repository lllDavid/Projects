from app.models.user import UserSecurity

class UserSecurityService:
    def create_security(self, email: str, password: str) -> UserSecurity:
        return UserSecurity(
            two_factor_enabled=False,
            password_hash=password,  
            reset_email=email,
            is_verified=False
        )
