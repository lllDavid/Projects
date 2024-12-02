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
    database=Config.DB_CONFIG["database"]
)

def insert_coin(coin: Coin, coin_details: CoinDetails, coin_market_data: CoinMarketData):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO coins (name, symbol, category, description, price, last_updated) VALUES (%s, %s, %s, %s, %s, %s)", 
                   (coin.name, coin.symbol, coin.category, coin.description, coin.price, coin.last_updated))
    coin_id = cursor.lastrowid 
    cursor.execute("INSERT INTO coin_details (coin_id, algorithm, consensus_mechanism, block_time, max_supply, circulating_supply, transaction_speed, security_features, privacy_features) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                   (coin_id, coin_details.algorithm, coin_details.consensus_mechanism, coin_details.block_time, 
                    coin_details.max_supply, coin_details.circulating_supply, coin_details.transaction_speed, 
                    coin_details.security_features, coin_details.privacy_features))
    cursor.execute("INSERT INTO coin_market_data (coin_id, price_usd, market_cap_usd, volume_24h_usd, high_24h_usd, low_24h_usd, price_change_24h, circulating_supply, max_supply) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                   (coin_id, coin_market_data.price_usd, coin_market_data.market_cap_usd, coin_market_data.volume_24h_usd, 
                    coin_market_data.high_24h_usd, coin_market_data.low_24h_usd, coin_market_data.price_change_24h, 
                    coin_market_data.circulating_supply, coin_market_data.max_supply))
    conn.commit() 
    cursor.close()  
    print("Coin and associated details inserted into the database.")

def update_coin(coin_id: int, coin: Coin, coin_details: CoinDetails, coin_market_data: CoinMarketData):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE coins 
        SET name = %s, symbol = %s, category = %s, description = %s, price = %s, last_updated = %s 
        WHERE coin_id = %s
    """, (coin.name, coin.symbol, coin.category, coin.description, coin.price, coin.last_updated, coin_id))
    cursor.execute("""
        UPDATE coin_details 
        SET algorithm = %s, consensus_mechanism = %s, block_time = %s, max_supply = %s, 
            circulating_supply = %s, transaction_speed = %s, security_features = %s, privacy_features = %s
        WHERE coin_id = %s
    """, (coin_details.algorithm, coin_details.consensus_mechanism, coin_details.block_time, 
          coin_details.max_supply, coin_details.circulating_supply, coin_details.transaction_speed, 
          coin_details.security_features, coin_details.privacy_features, coin_id))
    cursor.execute("""
        UPDATE coin_market_data 
        SET price_usd = %s, market_cap_usd = %s, volume_24h_usd = %s, high_24h_usd = %s, 
            low_24h_usd = %s, price_change_24h = %s, circulating_supply = %s, max_supply = %s
        WHERE coin_id = %s
    """, (coin_market_data.price_usd, coin_market_data.market_cap_usd, coin_market_data.volume_24h_usd, 
          coin_market_data.high_24h_usd, coin_market_data.low_24h_usd, coin_market_data.price_change_24h, 
          coin_market_data.circulating_supply, coin_market_data.max_supply, coin_id))
    conn.commit()
    cursor.close()
    print("Coin details updated successfully.")

def delete_coin(coin_id: int):
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM coin_market_data WHERE coin_id = %s", (coin_id,))
        cursor.execute("DELETE FROM coin_details WHERE coin_id = %s", (coin_id,))
        cursor.execute("DELETE FROM coins WHERE coin_id = %s", (coin_id,))
        conn.commit()
        print("Coin and associated data deleted successfully.")
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()
