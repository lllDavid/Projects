from dataclasses import dataclass
from datetime import datetime

@dataclass
class Coin:
    name: str
    symbol: str
    category: str
    description: str
    price: float
    last_updated: datetime

    def update_price(self, new_price: float):
        self.price = new_price
        self.last_updated = datetime.now()

    def update_description(self, new_description: str):
        self.description = new_description
        self.last_updated = datetime.now()

    def update_category(self, new_category: str):
        self.category = new_category
        self.last_updated = datetime.now()

    def display_details(self):
        return (f"Coin Name: {self.name} ({self.symbol})\n"
                f"Category: {self.category}\n"
                f"Description: {self.description}\n"
                f"Price: ${self.price}\n"
                f"Last Updated: {self.last_updated}")

def add_new_coin(coin: Coin, coins_list: list):
    coins_list.append(coin)
    print(f"Coin {coin.name} added.")

def get_coin_by_id(coin_id: int, coins_list: list):
    for coin in coins_list:
        if coin.id == coin_id:
            return coin
    return None

def remove_coin_by_id(coin_id: int, coins_list: list):
    coin_to_remove = get_coin_by_id(coin_id, coins_list)
    if coin_to_remove:
        coins_list.remove(coin_to_remove)
        print(f"Coin {coin_to_remove.name} removed.")
    else:
        print("Coin not found.")

def update_coin_price_by_id(coin_id: int, new_price: float, coins_list: list):
    coin_to_update = get_coin_by_id(coin_id, coins_list)
    if coin_to_update:
        coin_to_update.update_price(new_price)
        print(f"Price of {coin_to_update.name} updated to ${new_price}.")
    else:
        print("Coin not found.")

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

    def update_security_features(self, new_security_features: str):
        self.security_features = new_security_features

    def update_privacy_features(self, new_privacy_features: str):
        self.privacy_features = new_privacy_features

    def display_specifications(self):
        return (f"Algorithm: {self.algorithm}\n"
                f"Consensus Mechanism: {self.consensus_mechanism}\n"
                f"Block Time: {self.block_time} seconds\n"
                f"Max Supply: {self.max_supply}\n"
                f"Circulating Supply: {self.circulating_supply}\n"
                f"Transaction Speed: {self.transaction_speed} transactions per second\n"
                f"Security Features: {self.security_features}\n"
                f"Privacy Features: {self.privacy_features}")

@dataclass
class CoinMarketData:
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

    def update_24h_volume(self, new_volume_24h: float):
        self.volume_24h_usd = new_volume_24h

    def update_market_cap(self):
        self.market_cap_usd = self.price_usd * self.circulating_supply

    def calculate_price_change_percentage(self):
        return ((self.price_usd - self.low_24h_usd) / self.low_24h_usd) * 100

    def display_market_data(self):
        return (f"Price: ${self.price_usd}\n"
                f"Market Cap: ${self.market_cap_usd}\n"
                f"24h Volume: ${self.volume_24h_usd}\n"
                f"24h High: ${self.high_24h_usd}\n"
                f"24h Low: ${self.low_24h_usd}\n"
                f"Price Change (24h): {self.price_change_24h}%\n"
                f"Circulating Supply: {self.circulating_supply}\n"
                f"Max Supply: {self.max_supply}")


