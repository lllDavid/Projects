from mariadb import connect

from marketplace.config import Config
from marketplace.app.coin.coin import Coin
from marketplace.app.coin.coin_details import CoinDetails
from marketplace.app.coin.coin_market_data import CoinMarketData

conn = connect(
    user=Config.COIN_DB_CONFIG["user"],
    password=Config.COIN_DB_CONFIG["password"],
    host=Config.COIN_DB_CONFIG["host"],
    port=Config.COIN_DB_CONFIG["port"],
    database=Config.COIN_DB_CONFIG["database"]
)

