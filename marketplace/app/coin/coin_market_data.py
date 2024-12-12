from dataclasses import dataclass

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

    def __str__(self):
        return (f"Price: ${self.price_usd}, "
                f"Market Cap: ${self.market_cap_usd}, "
                f"24h Volume: ${self.volume_24h_usd}, "
                f"24h High: ${self.high_24h_usd}, "
                f"24h Low: ${self.low_24h_usd}, "
                f"Price Change (24h): {self.price_change_24h}%, "
                f"Circulating Supply: {self.circulating_supply}, "
                f"Max Supply: {self.max_supply}")
