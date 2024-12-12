from mariadb import connect

from marketplace.config import Config
from marketplace.app.coin.coin import Coin
from marketplace.app.coin.coin_details import CoinDetails
from marketplace.app.coin.coin_market_data import CoinMarketData

conn = connect(
    user=Config.DB_CONFIG["user"],
    password=Config.DB_CONFIG["password"],
    host=Config.DB_CONFIG["host"],
    port=Config.DB_CONFIG["port"],
    database=Config.DB_CONFIG["database"],
)
