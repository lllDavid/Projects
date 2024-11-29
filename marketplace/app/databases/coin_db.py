import mariadb
from app.models.coin import Coin, CoinSpecifications, CoinMarketData

conn = mariadb.connect(
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
