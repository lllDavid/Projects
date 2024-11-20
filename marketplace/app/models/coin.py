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

@dataclass
class CoinDetails:
    specifications: CoinSpecifications
    market_data: MarketData

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

@dataclass
class TransactionDetails:
    transaction_id: str
    sender_address: str
    receiver_address: str
    amount: float
    timestamp: datetime
    transaction_fee: float
    status: str
