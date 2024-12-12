from dataclasses import dataclass

from marketplace.app.coin.coin import Coin
from marketplace.app.coin.coin_specs import CoinSpecs
from marketplace.app.coin.coin_market_data import CoinMarketData


@dataclass
class CoinDetails:
    coin: Coin
    coin_specs: CoinSpecs
    coin_market_data: CoinMarketData
