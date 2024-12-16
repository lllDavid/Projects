from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserBank:
    account_holder: str
    account_number: str
    routing_number: str
    iban: str
    swift_bic: str
    date_linked: datetime | None
