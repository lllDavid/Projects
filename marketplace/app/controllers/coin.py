from app.models.coin import Coin, add_new_coin
import app.databases.coin_db as coin_db
from datetime import datetime

def create_new_coin(coin:Coin):
    coin = Coin(id = coin.id, 
                name = coin.name, 
                symbol = coin.symbol, 
                category = coin.category, 
                description = coin.description, 
                price = coin.price, 
                last_updated = coin.last_updated)
    return coin

coin1 = Coin(id=1, 
             name="Bitcoin", 
             symbol="BTC", 
             category="Cryptocurrency",
             description="A decentralized digital currency.", 
             price=45000.75, 
             last_updated=datetime.now())

def add_coin_to_db(coin:Coin):
    coin_db.save_coin(coin)

if __name__ == "__main__":
    create_new_coin(coin1)
    add_coin_to_db(coin1)