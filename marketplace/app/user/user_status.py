from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserStatus:
    is_online: bool
    is_banned: bool
    ban_reason: str | None = None
    ban_duration: int | None = None

    def update_ban_status(self, is_banned: bool, reason: str, duration: int):
        self.is_banned = is_banned
        self.ban_reason = reason
        self.ban_duration = duration
        self.updated_at = datetime.now()
        print(f"User banned: {is_banned}, Reason: {reason}, Duration: {duration}")

    def update_online_status(self, is_online: bool):
        self.is_online = is_online
        print(f"User Online: {is_online}.")

    def __str__(self):
        return (
            f"Online: {self.is_online}, "
            f"Banned: {self.is_banned}, "
            f"Ban Reason: {self.ban_reason}, "
            f"Ban Duration: {self.ban_duration}, "
        )
