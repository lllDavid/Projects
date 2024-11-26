from datetime import datetime
from ..models.coin import Coin, CoinSpecifications, CoinMarketData, add_new_coin
from ..databases import coin_db 

class CoinCreator:
    def create_new_coin(self, coin: Coin):
        coin = Coin(
            id=1, 
            name="Bitcoin", 
            symbol="BTC", 
            category="Cryptocurrency",
            description="A decentralized digital currency.", 
            price=45000.75, 
            last_updated=datetime.now()
        )
        return coin

    coin_specs = CoinSpecifications(
        algorithm="SHA-256", 
        consensus_mechanism="Proof of Work", 
        block_time=10, 
        max_supply=21000000, 
        circulating_supply=19000000, 
        transaction_speed=7, 
        security_features="High cryptographic security", 
        privacy_features="Pseudonymous"
    )

    coin_market_data = CoinMarketData(
        price_usd=45000.75,
        market_cap_usd=855000000000,  # Example: 45k per coin * 19M circulating supply
        volume_24h_usd=3500000000,
        high_24h_usd=46000.00,
        low_24h_usd=44000.00,
        price_change_24h=2.27,
        circulating_supply=19000000,
        max_supply=21000000
    )
# Function to insert the coin into the database
def add_coin_to_db(coin: Coin):
    coin_db.insert_coin(coin )  # Ensure insert_coin is correctly imported and works
