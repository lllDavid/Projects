from dataclasses import dataclass
from datetime import datetime

@dataclass
class CoinProfile:
    id: int
    name: str
    symbol: str
    category: str
    description: str
    price: float
    last_updated: datetime

    def update_name(self, new_name: str):
        self.name = new_name
        self.last_updated = datetime.now()

    def update_symbol(self, new_symbol: str):
        self.symbol = new_symbol
        self.last_updated = datetime.now()

    def update_category(self, new_category: str):
        self.category = new_category
        self.last_updated = datetime.now()

    def update_description(self, new_description: str):
        self.description = new_description
        self.last_updated = datetime.now()

    def update_price(self, new_price: float):
        self.price = new_price
        self.last_updated = datetime.now()

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Symbol: {self.symbol}\n"
                f"Category: {self.category}\n"
                f"Description: {self.description}\n"
                f"Price: ${self.price:,.2f}\n"
                f"Last Updated: {self.last_updated}")
