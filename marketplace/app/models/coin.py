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

    def __str__(self):
        return f"{self.name} ({self.symbol}) - {self.category} - {self.description}, ${self.price:.2f}"

@dataclass
class CoinDetails:
    specifications: 'CoinSpecifications'
    market_data: 'MarketData'

    def update_market_data(self, new_market_data: 'MarketData'):
        self.market_data = new_market_data

    def get_market_cap(self) -> float:
        return self.market_data.market_cap_usd

    def __str__(self):
        return f"Specifications: {self.specifications}, Market Data: {self.market_data}"

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

    def __str__(self):
        return f"Algorithm: {self.algorithm}, Consensus: {self.consensus_mechanism}, Block Time: {self.block_time}s"

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


coin_specs = CoinSpecifications(
    algorithm="SHA-256",
    consensus_mechanism="Proof of Work",
    block_time=10.0,
    max_supply=21000000,
    circulating_supply=19000000,
    transaction_speed=7.0,
    security_features="AES-256 encryption",
    privacy_features="Optional privacy features"
)

market_data = MarketData(
    price_usd=35000.00,
    market_cap_usd=665000000000,
    volume_24h_usd=50000000000,
    high_24h_usd=36000.00,
    low_24h_usd=34000.00,
    price_change_24h=5.0,
    circulating_supply=19000000,
    max_supply=21000000
)

coin = Coin(
    id=1,
    name="Bitcoin",
    symbol="BTC",
    category="Cryptocurrency",
    description="The first and most well-known cryptocurrency",
    price=35000.00,
    last_updated=datetime.now()
)

coin_details = CoinDetails(
    specifications=coin_specs,
    market_data=market_data
)

print(coin)
print(coin_details)

coin.update_price(35500.00)
print(coin)

coin_specs.update_supply(19100000, 21000000)
print(coin_specs)

market_data.update_price(35500.00)
print(market_data)

remaining_supply = coin_specs.calculate_remaining_supply()
print(f"Remaining Supply: {remaining_supply}")
