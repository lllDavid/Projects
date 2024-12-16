from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserBank:
    account_holder: str | None
    account_number: str | None
    routing_number: str | None
    iban: str | None
    swift_bic: str | None
    date_linked: datetime | None
