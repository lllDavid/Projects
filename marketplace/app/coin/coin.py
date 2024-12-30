from dataclasses import dataclass

from marketplace.app.coin.coin_specs import CoinSpecs
from marketplace.app.coin.coin_market_data import CoinMarketData

@dataclass
class Coin:
    id: int | None 
    name: str
    symbol: str
    category: str
    description: str
    price: float
    coin_specs: CoinSpecs 
    coin_market_data: CoinMarketData 

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

    def __repr__(self):
        return (f"{self.__class__.__name__}(id={self.id!r}, "
                f"name={self.name!r}, "
                f"symbol={self.symbol!r}, "
                f"category={self.category!r}, "
                f"description={self.description!r}, "
                f"price={self.price!r}, "
                f"coin_specs={self.coin_specs!r}, "
                f"coin_market_data={self.coin_market_data!r})")


