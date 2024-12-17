from datetime import datetime
from mariadb import connect

from marketplace.config import Config
from marketplace.app.coin.coin_profile import CoinProfile
from marketplace.app.coin.coin_details import CoinDetails
from marketplace.app.coin.coin_market_data import CoinMarketData
from marketplace.app.coin.coin_specs import CoinSpecs

conn = connect(
    user=Config.COIN_DB_CONFIG["user"],
    password=Config.COIN_DB_CONFIG["password"],
    host=Config.COIN_DB_CONFIG["host"],
    port=Config.COIN_DB_CONFIG["port"],
    database=Config.COIN_DB_CONFIG["database"]
)

# --------------------------------------------------------------
# Section 1: Insert, Delete and Update Coin attributes
# --------------------------------------------------------------

def insert_coin(coin: Coin) -> Coin | None:
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO coins (name, symbol, category, description, price, last_updated) VALUES (%s, %s, %s, %s, %s, %s)",
            (coin.name, coin.symbol, coin.category, coin.description, coin.price, coin.last_updated)
        )
        coin_id = cursor.lastrowid
        conn.commit()
        print("Coin inserted into the database.")
        coin.id = coin_id  
        return coin
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()

def update_coin_price(coin_id: int, new_price: float) -> None:
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE coins SET price = %s, last_updated = %s WHERE id = %s", 
            (new_price, datetime.now(), coin_id)
        )
        conn.commit()
        print("Coin price updated successfully.")
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()

def delete_coin(coin_id: int) -> None:
    cursor = conn.cursor()
    try:
        # Delete related coin_specs and coin_market_data first
        cursor.execute("DELETE FROM coin_specs WHERE coin_id = %s", (coin_id,))
        cursor.execute("DELETE FROM coin_market_data WHERE coin_id = %s", (coin_id,))
        
        # Then delete the coin itself
        cursor.execute("DELETE FROM coins WHERE id = %s", (coin_id,))
        conn.commit()
        print("Coin deleted from the database.")
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()

# --------------------------------------------------------------
# Section 2: Retrieve Coin by Specific Criteria
# --------------------------------------------------------------

def get_coin_by_name(name: str) -> Coin | None:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM coins WHERE name = %s", (name,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return Coin(*result)
    return None

def get_coin_by_symbol(symbol: str) -> Coin | None:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM coins WHERE symbol = %s", (symbol,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return Coin(*result)
    return None

def get_coin_by_category(category: str) -> list[Coin]:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM coins WHERE category = %s", (category,))
    result = cursor.fetchall()
    cursor.close()
    return [Coin(*row) for row in result] if result else []

# --------------------------------------------------------------
# Section 3: Coin Details Retrieval
# --------------------------------------------------------------

def get_coin_specs(coin_id: int) -> CoinSpecs | None:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM coin_specs WHERE coin_id = %s", (coin_id,)
    )
    specs = cursor.fetchone()
    cursor.close()
    if specs:
        return CoinSpecs(*specs)
    return None

def get_coin_market_data(coin_id: int) -> CoinMarketData | None:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM coin_market_data WHERE coin_id = %s", (coin_id,)
    )
    market_data = cursor.fetchone()
    cursor.close()
    if market_data:
        return CoinMarketData(*market_data)
    return None

# --------------------------------------------------------------
# Section 4: Complete Coin Retrieval
# --------------------------------------------------------------

def get_full_coin(coin_id: int) -> CoinDetails | None:
    cursor = conn.cursor()
    
    # Fetch Coin
    cursor.execute("SELECT * FROM coins WHERE id = %s", (coin_id,))
    coin_row = cursor.fetchone()
    if not coin_row:
        return None
    coin = Coin(*coin_row)
    
    # Fetch CoinSpecs
    coin_specs = get_coin_specs(coin_id)
    
    # Fetch CoinMarketData
    coin_market_data = get_coin_market_data(coin_id)
    
    # Combine all into CoinDetails
    coin_details = CoinDetails(coin=coin, coin_specs=coin_specs, coin_market_data=coin_market_data)

    cursor.close()
    return coin_details
