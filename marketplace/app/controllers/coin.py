from datetime import datetime
from app.databases import coin_db
from app.models.coin import Coin, CoinSpecifications, CoinMarketData

class CoinCreator:
    def create_new_coin(self, name:str, symbol:str, category:str, description:str, price:float,last_updated:datetime) -> Coin:
        return Coin(
            name=name, 
            symbol=symbol, 
            category=category,
            description=description, 
            price=price, 
            last_updated=last_updated
        )
    
    def initialize_coin_specifications(self) -> CoinSpecifications:
        return CoinSpecifications(
            algorithm="SHA-256", 
            consensus_mechanism="Proof of Work", 
            block_time=10, 
            max_supply=21000000, 
            circulating_supply=19000000, 
            transaction_speed=7, 
            security_features="High cryptographic security", 
            privacy_features="Pseudonymous"
        )
    
    def initialize_coin_market_data(self) -> CoinMarketData:
        return CoinMarketData(
            price_usd=45000.75,
            market_cap_usd=855000000000,  
            volume_24h_usd=3500000000,
            high_24h_usd=46000.00,
            low_24h_usd=44000.00,
            price_change_24h=2.27,
            circulating_supply=19000000,
            max_supply=21000000
        )

def main():
    coin_creator = CoinCreator()

    coin = coin_creator.create_new_coin(
        name="Bitcoin", 
        symbol="BTC", 
        category="Cryptocurrency", 
        description="A decentralized digital currency.", 
        price=45000.75, 
        last_updated=datetime.now()
        )
    
    coin_specifications = coin_creator.initialize_coin_specifications()
    coin_market_data = coin_creator.initialize_coin_market_data()
    coin_db.insert_coin(coin, coin_specifications, coin_market_data )

if __name__ == "__main__":
    main()