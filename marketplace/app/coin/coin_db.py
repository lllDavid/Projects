from mariadb import connect
from app.models.coin import Coin, CoinSpecifications, CoinMarketData

conn = connect(
    user="root",       
    password="root",   
    host="localhost",           
    port=3306,                   
    database="marketplace"  
)

def insert_coin(coin: Coin, coin_specifications: CoinSpecifications, coin_market_data: CoinMarketData):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO coins (name, symbol, category, description, price, last_updated) VALUES (%s, %s, %s, %s, %s, %s)", 
                   (coin.name, coin.symbol, coin.category, coin.description, coin.price, coin.last_updated))
    coin_id = cursor.lastrowid 
    cursor.execute("INSERT INTO coin_specifications (coin_id, algorithm, consensus_mechanism, block_time, max_supply, circulating_supply, transaction_speed, security_features, privacy_features) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                   (coin_id, coin_specifications.algorithm, coin_specifications.consensus_mechanism, coin_specifications.block_time, 
                    coin_specifications.max_supply, coin_specifications.circulating_supply, coin_specifications.transaction_speed, 
                    coin_specifications.security_features, coin_specifications.privacy_features))
    cursor.execute("INSERT INTO coin_market_data (coin_id, price_usd, market_cap_usd, volume_24h_usd, high_24h_usd, low_24h_usd, price_change_24h, circulating_supply, max_supply) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                   (coin_id, coin_market_data.price_usd, coin_market_data.market_cap_usd, coin_market_data.volume_24h_usd, 
                    coin_market_data.high_24h_usd, coin_market_data.low_24h_usd, coin_market_data.price_change_24h, 
                    coin_market_data.circulating_supply, coin_market_data.max_supply))
    conn.commit() 
    cursor.close()  
    print("Coin and associated details inserted into the database.")

def update_coin(coin_id: int, coin: Coin, coin_specifications: CoinSpecifications, coin_market_data: CoinMarketData):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE coins 
        SET name = %s, symbol = %s, category = %s, description = %s, price = %s, last_updated = %s 
        WHERE coin_id = %s
    """, (coin.name, coin.symbol, coin.category, coin.description, coin.price, coin.last_updated, coin_id))
    cursor.execute("""
        UPDATE coin_specifications 
        SET algorithm = %s, consensus_mechanism = %s, block_time = %s, max_supply = %s, 
            circulating_supply = %s, transaction_speed = %s, security_features = %s, privacy_features = %s
        WHERE coin_id = %s
    """, (coin_specifications.algorithm, coin_specifications.consensus_mechanism, coin_specifications.block_time, 
          coin_specifications.max_supply, coin_specifications.circulating_supply, coin_specifications.transaction_speed, 
          coin_specifications.security_features, coin_specifications.privacy_features, coin_id))
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
        cursor.execute("DELETE FROM coin_specifications WHERE coin_id = %s", (coin_id,))
        cursor.execute("DELETE FROM coins WHERE coin_id = %s", (coin_id,))
        conn.commit()
        print("Coin and associated data deleted successfully.")
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()
