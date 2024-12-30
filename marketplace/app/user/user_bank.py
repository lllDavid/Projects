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

    def update_bank_name(self, new_bank_name: str) -> None:
        self.bank_name = new_bank_name

    def update_account_holder(self, new_holder: str) -> None:
        self.account_holder = new_holder

    def update_account_number(self, new_account_number: str) -> None:
        self.account_number = new_account_number

    def update_routing_number(self, new_routing_number: str) -> None:
        self.routing_number = new_routing_number

    def update_iban(self, new_iban: str) -> None:
        self.iban = new_iban

    def update_swift_bic(self, new_swift_bic: str) -> None:
        self.swift_bic = new_swift_bic

    def update_date_linked(self, new_date_linked: datetime) -> None:
        self.date_linked = new_date_linked

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(bank_name={self.bank_name!r}, "
                f"account_holder={self.account_holder!r}, "
                f"account_number={self.account_number!r}, "
                f"routing_number={self.routing_number!r}, "
                f"iban={self.iban!r}, "
                f"swift_bic={self.swift_bic!r}, "
                f"date_linked={self.date_linked!r})")


