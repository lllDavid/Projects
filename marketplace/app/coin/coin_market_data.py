from dataclasses import dataclass
from datetime import datetime

@dataclass
class CoinMarketData:
    rank: int 
    price_usd: float
    market_cap_usd: float
    volume_24h_usd: float
    high_24h_usd: float
    low_24h_usd: float
    change_24h_percent: float
    all_time_high: float
    all_time_low: float
    circulating_supply: float
    max_supply: float
    market_dominance: float
    last_updated: datetime  
    
    def update_price_usd(self, new_price: float):
        self.price_usd = new_price
        self.last_updated = datetime.now()

    def update_market_cap_usd(self, new_market_cap: float):
        self.market_cap_usd = new_market_cap
        self.last_updated = datetime.now()

    def update_volume_24h_usd(self, new_volume: float):
        self.volume_24h_usd = new_volume
        self.last_updated = datetime.now()

    def update_high_24h_usd(self, new_high: float):
        self.high_24h_usd = new_high
        self.last_updated = datetime.now()

    def update_low_24h_usd(self, new_low: float):
        self.low_24h_usd = new_low
        self.last_updated = datetime.now()

    def update_change_24h_percent(self, new_change_percent: float):
        self.change_24h_percent = new_change_percent
        self.last_updated = datetime.now()

    def update_all_time_high(self, new_all_time_high: float):
        self.all_time_high = new_all_time_high
        self.last_updated = datetime.now()

    def update_all_time_low(self, new_all_time_low: float):
        self.all_time_low = new_all_time_low
        self.last_updated = datetime.now()

    def update_circulating_supply(self, new_supply: float):
        self.circulating_supply = new_supply
        self.last_updated = datetime.now()

    def update_max_supply(self, new_max_supply: float):
        self.max_supply = new_max_supply
        self.last_updated = datetime.now()

    def update_market_dominance(self, new_dominance: float):
        self.market_dominance = new_dominance
        self.last_updated = datetime.now()


    def __str__(self) -> str:
        return (
            f"Rank: {self.rank}, "
            f"Price (USD): ${self.price_usd:,.2f}, "
            f"Market Cap (USD): ${self.market_cap_usd:,.2f}, "
            f"24h Volume (USD): ${self.volume_24h_usd:,.2f}, "
            f"24h High (USD): ${self.high_24h_usd:,.2f}, "
            f"24h Low (USD): ${self.low_24h_usd:,.2f}, "
            f"24h Price Change: {self.change_24h_percent:+.2f}%, "
            f"All Time High (USD): ${self.all_time_high:,.2f}, "
            f"All Time Low (USD): ${self.all_time_low:,.2f}, "
            f"Circulating Supply: {self.circulating_supply:,.0f}, "
            f"Max Supply: {self.max_supply:,.0f}, "
            f"Market Dominance: {self.market_dominance:.2f}%, "
            f"Last Updated: {self.last_updated.strftime('%Y-%m-%d %H:%M:%S')}"
        )
