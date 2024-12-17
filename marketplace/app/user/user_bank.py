from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserBank:
    bank_name: str | None
    account_holder: str | None
    account_number: str | None
    routing_number: str | None
    iban: str | None
    swift_bic: str | None
    date_linked: datetime | None

from datetime import datetime
from dataclasses import dataclass

@dataclass
class UserBank:
    bank_name: str | None
    account_holder: str | None
    account_number: str | None
    routing_number: str | None
    iban: str | None
    swift_bic: str | None
    date_linked: datetime | None

    def is_valid_account(self) -> bool:
        required_fields = [self.account_number, self.routing_number, self.iban, self.swift_bic]
        return all(field is not None for field in required_fields)

    def update_account_holder(self, new_holder: str) -> None:
        self.account_holder = new_holder

    def get_account_summary(self) -> str:
        return (f"Bank: {self.bank_name}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Account Number: {self.account_number}\n"
                f"IBAN: {self.iban}\n"
                f"SWIFT/BIC: {self.swift_bic}\n"
                f"Date Linked: {self.date_linked}")

    def is_linked_recently(self, days: int) -> bool:
        if self.date_linked is None:
            return False
        return (datetime.now() - self.date_linked).days <= days

    def __str__(self) -> str:
        return (f"UserBank(bank_name={self.bank_name}, account_holder={self.account_holder}, "
                f"account_number={self.account_number}, iban={self.iban}, swift_bic={self.swift_bic}, "
                f"date_linked={self.date_linked})")
