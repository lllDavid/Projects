from dataclasses import dataclass
from datetime import datetime

@dataclass
class Coin:
    id: int
    name: str
    symbol: str
    category: str
    description: str
    price: float
    last_updated: datetime

    def update_price(self, new_price: float):
            self.price = new_price
            self.last_updated = datetime.now()
    
def add_new_coin(coin:Coin):
        print(f"Coin {coin.name} added.")

@dataclass
class CoinDetails:
    specifications: 'CoinSpecifications'
    market_data: 'MarketData'

    def update_market_data(self, new_market_data: 'MarketData'):
        self.market_data = new_market_data

    def get_market_cap(self) -> float:
        return self.market_data.market_cap_usd

@dataclass
class CoinSpecifications:
    algorithm: str
    consensus_mechanism: str
    block_time: float
    max_supply: float
    circulating_supply: float
    transaction_speed: float
    security_features: str
    privacy_features: str

    def update_supply(self, new_circulating_supply: float, new_max_supply: float):
        self.circulating_supply = new_circulating_supply
        self.max_supply = new_max_supply

    def calculate_remaining_supply(self) -> float:
        return self.max_supply - self.circulating_supply


@dataclass
class MarketData:
    price_usd: float
    market_cap_usd: float
    volume_24h_usd: float
    high_24h_usd: float
    low_24h_usd: float
    price_change_24h: float
    circulating_supply: float
    max_supply: float

    def update_price(self, new_price_usd: float):
        self.price_usd = new_price_usd
        self.price_change_24h = ((self.price_usd - self.low_24h_usd) / self.low_24h_usd) * 100

    def get_24h_price_range(self) -> tuple:
        return (self.low_24h_usd, self.high_24h_usd)

    def __str__(self):
        return f"Price: ${self.price_usd:.2f}, Market Cap: ${self.market_cap_usd:.2f}, 24h Volume: ${self.volume_24h_usd:.2f}"


