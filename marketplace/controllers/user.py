import models
import models.user
from datetime import datetime


models.user.User.add_user(
    id=1,  # Corrected parameter name to 'id'
    ip_address="192.168.0.1",
    role="admin",
    username="john_doe",
    email="john_doe@example.com",
    reset_email="reset_john_doe@example.com",
    password_hash="hashed_password_12345",
    two_factor_enabled=True,
    is_verified=True,
    is_banned=False,
    ban_reason="",
    is_active=True,
    login_count=5,
    failed_login_attempts=0,
    last_login=datetime(2024, 11, 11, 14, 30),  # Correct datetime format
    created_at=datetime(2024, 11, 10, 10, 0),  # Correct datetime format
    updated_at=datetime(2024, 11, 11, 15, 0)  # Correct datetime format
)