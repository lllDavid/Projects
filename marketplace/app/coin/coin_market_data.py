from dataclasses import dataclass

@dataclass
class CoinMarketData:
    price_usd: float
    market_cap_usd: float
    volume_24h_usd: float
    high_24h_usd: float
    low_24h_usd: float
    all_time_high: float
    price_change_24h: float
    circulating_supply: float
    max_supply: float

    def update_price(self, new_price_usd: float):
        self.price_usd = new_price_usd

    def update_market_cap(self, new_market_cap_usd: float):
        self.market_cap_usd = new_market_cap_usd

    def update_volume_24h(self, new_volume_24h_usd: float):
        self.volume_24h_usd = new_volume_24h_usd

    def update_high_24h(self, new_high_24h_usd: float):
        self.high_24h_usd = new_high_24h_usd

    def update_low_24h(self, new_low_24h_usd: float):
        self.low_24h_usd = new_low_24h_usd

    def update_all_time_high(self, new_all_time_high: float):
        self.all_time_high = new_all_time_high

    def update_price_change_24h(self, new_price_change_24h: float):
        self.price_change_24h = new_price_change_24h

    def update_circulating_supply(self, new_circulating_supply: float):
        self.circulating_supply = new_circulating_supply

    def update_max_supply(self, new_max_supply: float):
        self.max_supply = new_max_supply

    def __str__(self):
        return (f"Price: ${self.price_usd}, "
                f"Market Cap: ${self.market_cap_usd}, "
                f"24h Volume: ${self.volume_24h_usd}, "
                f"24h High: ${self.high_24h_usd}, "
                f"24h Low: ${self.low_24h_usd}, "
                f"Price Change (24h): {self.price_change_24h}%, "
                f"Circulating Supply: {self.circulating_supply}, "
                f"Max Supply: {self.max_supply}")
