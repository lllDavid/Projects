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
    last_updated: datetime  # to keep track of the last update time
    
    def update_price_usd(self, new_price: float):
        """Update the price in USD and update the last_updated timestamp."""
        self.price_usd = new_price
        self.last_updated = datetime.now()

    def update_market_cap_usd(self, new_market_cap: float):
        """Update the market capitalization in USD and update the last_updated timestamp."""
        self.market_cap_usd = new_market_cap
        self.last_updated = datetime.now()

    def update_volume_24h_usd(self, new_volume: float):
        """Update the 24h trading volume in USD and update the last_updated timestamp."""
        self.volume_24h_usd = new_volume
        self.last_updated = datetime.now()

    def update_high_24h_usd(self, new_high: float):
        """Update the 24h high in USD and update the last_updated timestamp."""
        self.high_24h_usd = new_high
        self.last_updated = datetime.now()

    def update_low_24h_usd(self, new_low: float):
        """Update the 24h low in USD and update the last_updated timestamp."""
        self.low_24h_usd = new_low
        self.last_updated = datetime.now()

    def update_change_24h_percent(self, new_change_percent: float):
        """Update the 24h price change percentage and update the last_updated timestamp."""
        self.change_24h_percent = new_change_percent
        self.last_updated = datetime.now()

    def update_all_time_high(self, new_all_time_high: float):
        """Update the all-time high price and update the last_updated timestamp."""
        self.all_time_high = new_all_time_high
        self.last_updated = datetime.now()

    def update_all_time_low(self, new_all_time_low: float):
        """Update the all-time low price and update the last_updated timestamp."""
        self.all_time_low = new_all_time_low
        self.last_updated = datetime.now()

    def update_circulating_supply(self, new_supply: float):
        """Update the circulating supply and update the last_updated timestamp."""
        self.circulating_supply = new_supply
        self.last_updated = datetime.now()

    def update_max_supply(self, new_max_supply: float):
        """Update the max supply and update the last_updated timestamp."""
        self.max_supply = new_max_supply
        self.last_updated = datetime.now()

    def update_market_dominance(self, new_dominance: float):
        """Update the market dominance and update the last_updated timestamp."""
        self.market_dominance = new_dominance
        self.last_updated = datetime.now()


    def __str__(self):
        return (f"Price: ${self.price_usd}, "
                f"Market Cap: ${self.market_cap_usd}, "
                f"24h Volume: ${self.volume_24h_usd}, "
                f"24h High: ${self.high_24h_usd}, "
                f"24h Low: ${self.low_24h_usd}, "
                f"Price Change (24h): {self.price_change_24h}%, "
                f"Circulating Supply: {self.circulating_supply}, "
                f"Max Supply: {self.max_supply}")
