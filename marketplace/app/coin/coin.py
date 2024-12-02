from dataclasses import dataclass
from datetime import datetime

@dataclass
class Coin:
    name: str
    symbol: str
    category: str
    description: str
    price: float
    last_updated: datetime

    def update_price(self, new_price: float):
        self.price = new_price
        self.last_updated = datetime.now()

    def update_description(self, new_description: str):
        self.description = new_description
        self.last_updated = datetime.now()

    def update_category(self, new_category: str):
        self.category = new_category
        self.last_updated = datetime.now()

    def display_details(self):
        return (f"Coin Name: {self.name} ({self.symbol})\n"
                f"Category: {self.category}\n"
                f"Description: {self.description}\n"
                f"Price: ${self.price}\n"
                f"Last Updated: {self.last_updated}")

def add_new_coin(coin: Coin, coins_list: list):
    coins_list.append(coin)
    print(f"Coin {coin.name} added.")

def get_coin_by_id(coin_id: int, coins_list: list):
    for coin in coins_list:
        if coin.id == coin_id:
            return coin
    return None

def remove_coin_by_id(coin_id: int, coins_list: list):
    coin_to_remove = get_coin_by_id(coin_id, coins_list)
    if coin_to_remove:
        coins_list.remove(coin_to_remove)
        print(f"Coin {coin_to_remove.name} removed.")
    else:
        print("Coin not found.")

def update_coin_price_by_id(coin_id: int, new_price: float, coins_list: list):
    coin_to_update = get_coin_by_id(coin_id, coins_list)
    if coin_to_update:
        coin_to_update.update_price(new_price)
        print(f"Price of {coin_to_update.name} updated to ${new_price}.")
    else:
        print("Coin not found.")


