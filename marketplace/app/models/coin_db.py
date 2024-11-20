from datetime import datetime
from dataclasses import dataclass
from .coin import Coin

@dataclass
class CoinDB:
    coins = []
    amount_of_coins_in_db:float

    def add_coin(self, coin:Coin):
        self.coins.append(coin)
        print(f"Coin: {coin.name} added to Coin DB")

    def delete_coin(self, coin:Coin):
        self.coins.remove(coin)
        print(f"Coin {coin.name} deleted from Coin DB")
        
    def retrieve_coin(self, amount:float):
        self.amount_of_coins_in_db = 1000
        if amount < self.amount_of_coins_in_db:
            self.amount_of_coins_in_db -= amount
            print(f"Retrieved {amount} from Coin DB")



 

