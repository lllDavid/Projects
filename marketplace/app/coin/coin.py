from dataclasses import dataclass

from marketplace.app.coin.coin_profile import CoinProfile
from marketplace.app.coin.coin_specs import CoinSpecs
from marketplace.app.coin.coin_market_data import CoinMarketData

@dataclass
class Coin:
    coin_profile: CoinProfile
    coin_specs: CoinSpecs
    coin_market_data: CoinMarketData
