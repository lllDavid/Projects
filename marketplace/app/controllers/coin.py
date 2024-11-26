from datetime import datetime
from ..models.coin import Coin, add_new_coin
from ..databases import coin_db 

def create_new_coin(coin: Coin):
    return coin  # Simply return the same coin object (or remove this function)

# Sample coin data
coin1 = Coin(
    id=1, 
    name="Bitcoin", 
    symbol="BTC", 
    category="Cryptocurrency",
    description="A decentralized digital currency.", 
    price=45000.75, 
    last_updated=datetime.now()
)

# Function to insert the coin into the database
def add_coin_to_db(coin: Coin):
    coin_db.insert_coin(coin )  # Ensure insert_coin is correctly imported and works

if __name__ == "__main__":
    coin1 = create_new_coin(coin1)  # This step is now redundant but keeps the pattern you might want
    add_coin_to_db(coin1)