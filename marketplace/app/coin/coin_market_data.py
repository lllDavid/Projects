from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

@dataclass
class CoinMarketData:
    rank: int
    price_usd: Decimal
    market_cap_usd: Decimal
    volume_24h_usd: Decimal
    high_24h_usd: Decimal
    low_24h_usd: Decimal
    change_24h_percent: Decimal
    all_time_high: Decimal | None
    all_time_low: Decimal | None
    circulating_supply: Decimal
    market_dominance: Decimal | None
    last_updated: datetime | None

    def update_rank(self, new_rank: int):
        self.rank = new_rank
        self.update_last_updated()

    def update_price_usd(self, new_price: Decimal):
        self.price_usd = new_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.update_last_updated()

    def update_market_cap_usd(self, new_market_cap: Decimal):
        self.market_cap_usd = new_market_cap.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.update_last_updated()

    def update_volume_24h_usd(self, new_volume: Decimal):
        self.volume_24h_usd = new_volume.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.update_last_updated()

    def update_high_24h_usd(self, new_high: Decimal):
        self.high_24h_usd = new_high.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.update_last_updated()

    def update_low_24h_usd(self, new_low: Decimal):
        self.low_24h_usd = new_low.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.update_last_updated()

    def update_change_24h_percent(self, new_change_percent: Decimal):
        self.change_24h_percent = new_change_percent.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.update_last_updated()

    def update_all_time_high(self, new_all_time_high: Decimal):
        self.all_time_high = new_all_time_high.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.update_last_updated()

    def update_all_time_low(self, new_all_time_low: Decimal):
        self.all_time_low = new_all_time_low.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.update_last_updated()

    def update_circulating_supply(self, new_supply: Decimal):
        self.circulating_supply = new_supply.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.update_last_updated()

    def update_market_dominance(self, new_dominance: Decimal):
        self.market_dominance = new_dominance.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.update_last_updated()

    def update_last_updated(self):
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
            f"Market Dominance: {self.market_dominance:.2f}%, "
            f"Last Updated: {self.last_updated}"
        )
