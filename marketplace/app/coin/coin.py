from dataclasses import dataclass
from datetime import datetime

from marketplace.app.coin.coin_specs import CoinSpecs
from marketplace.app.coin.coin_market_data import CoinMarketData

@dataclass
class Coin:
    id: int
    name: str
    symbol: str
    category: str
    description: str
    price: float
    last_updated: datetime | None
    coin_specs: CoinSpecs | None
    coin_market_data: CoinMarketData | None

    def update_name(self, new_name: str):
        self.name = new_name

    def update_symbol(self, new_symbol: str):
        self.symbol = new_symbol

    def update_category(self, new_category: str):
        self.category = new_category

    def update_description(self, new_description: str):
        self.description = new_description

    def update_price(self, new_price: float):
        self.price = new_price

    def update_last_updated(self):
        self.last_updated = datetime.now()
    
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Symbol: {self.symbol}\n"
                f"Category: {self.category}\n"
                f"Description: {self.description}\n"
                f"Price: ${self.price:,.2f}\n"
                f"Last Updated: {self.last_updated}")

c1 = Coin(1,"bitcoin","btc", "coin", "coin",1.23,None,None,None)
print(c1)

c1.update_name("Litecoin")

print(c1)
