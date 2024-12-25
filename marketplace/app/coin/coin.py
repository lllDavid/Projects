from dataclasses import dataclass

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

    def update_coin_specs(self, new_coin_specs: CoinSpecs):
        self.coin_specs = new_coin_specs
    
    def update_coin_market_data(self, new_coin_market_data: CoinMarketData):
        self.coin_market_data = new_coin_market_data

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Symbol: {self.symbol}\n"
                f"Category: {self.category}\n"
                f"Description: {self.description}\n"
                f"Price: ${self.price:,.2f}\n"
                f"Coin Specs: {self.coin_specs}\n"
                f"Coin Market Data: {self.coin_market_data}")


