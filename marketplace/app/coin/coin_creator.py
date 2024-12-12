from datetime import datetime
from flask import Blueprint

from marketplace.app.coin import coin_db
from marketplace.app.coin.coin import Coin
from marketplace.app.coin.coin_specs import CoinSpecs
from marketplace.app.coin.coin_details import CoinDetails
from marketplace.app.coin.coin_market_data import CoinMarketData

coin_creator = Blueprint('coin_creator', __name__)

class CoinCreator:
    def create_coin(self, name:str, symbol:str, category:str, description:str, price:float, last_updated:datetime) -> Coin:
        return Coin(
            name=name, 
            symbol=symbol, 
            category=category,
            description=description, 
            price=price, 
            last_updated=last_updated
        )
    
    def create_coin_specs(self, algorithm:str, consensus_mechanism:str, block_time:float, max_supply:float, circulating_supply:float, transaction_speed: float, security_features:str, privacy_features:str)  -> CoinSpecs:
        return CoinSpecs(
            algorithm=algorithm, 
            consensus_mechanism=consensus_mechanism, 
            block_time=block_time, 
            max_supply=max_supply, 
            circulating_supply=circulating_supply, 
            transaction_speed=transaction_speed, 
            security_features=security_features, 
            privacy_features=privacy_features
        )
    
    def create_coin_market_data(self, price_usd:float, market_cap_usd:float, volume_24h_usd:float, high_24h_usd:float, low_24h_usd:float, price_change_24h:float, circulating_supply:float, max_supply:float) -> CoinMarketData:
        return CoinMarketData(
            price_usd=price_usd,
            market_cap_usd=market_cap_usd,  
            volume_24h_usd=volume_24h_usd,
            high_24h_usd=high_24h_usd,
            low_24h_usd=low_24h_usd,
            price_change_24h=price_change_24h,
            circulating_supply=circulating_supply,
            max_supply=max_supply
        )

    def create_coin_details(self):
        coin = self.create_coin()
        coin_specs = self.create_coin_specs()
        coin_market_data = self.create_coin_market_data()

        return CoinDetails(coin=coin, coin_specs=coin_specs, coin_market_data=coin_market_data)
    
    def create_and_save_coin(self):
        ...

