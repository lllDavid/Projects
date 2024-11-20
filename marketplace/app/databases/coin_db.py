from datetime import datetime
from ..models.coin import Coin

coins = []
amount_of_coins_in_db = 1000

def add_coin(coin: Coin):
    coins.append(coin)
    print(f"Coin: {coin.name} added to Coin DB")

def delete_coin(coin: Coin):
    if coin in coins:
        coins.remove(coin)
        print(f"Coin {coin.name} deleted from Coin DB")
    else:
        print(f"Coin {coin.name} not found in Coin DB")

def retrieve_coin(amount: float):
    global amount_of_coins_in_db
    if amount < amount_of_coins_in_db:
        amount_of_coins_in_db -= amount
        print(f"Retrieved {amount} from Coin DB")
    else:
        print("Not enough coins available")
