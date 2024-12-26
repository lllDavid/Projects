from mariadb import connect

from marketplace.config import Config
from marketplace.app.coin.coin import Coin
from marketplace.app.coin.coin_specs import CoinSpecs
from marketplace.app.coin.coin_market_data import CoinMarketData

conn = connect(
    user=Config.COIN_DB_CONFIG["user"],
    password=Config.COIN_DB_CONFIG["password"],
    host=Config.COIN_DB_CONFIG["host"],
    port=Config.COIN_DB_CONFIG["port"],
    database=Config.COIN_DB_CONFIG["database"]
)

# --------------------------------------------------------------
# Section 1: Insert, Delete, and Update Coin Data
# --------------------------------------------------------------

def insert_coin(coin: Coin) -> Coin | None:
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Coin (name, symbol, category, description, price) "
            "VALUES (%s, %s, %s, %s, %s)",
            (coin.name, coin.symbol, coin.category, coin.description, coin.price)
        )

        coin_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO CoinSpecs (algorithm, consensus_mechanism, blockchain_network, average_block_time, "
            "security_features, privacy_features, max_supply, genesis_block_date, token_type, governance_model, "
            "development_activity, hard_cap, forking_coin, tokenomics) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (coin_id,
                coin.coin_specs.algorithm, coin.coin_specs.consensus_mechanism, coin.coin_specs.blockchain_network, coin.coin_specs.average_block_time,
                coin.coin_specs.security_features, coin.coin_specs.privacy_features, coin.coin_specs.max_supply, coin.coin_specs.genesis_block_date,
                coin.coin_specs.token_type, coin.coin_specs.governance_model, coin.coin_specs.development_activity, coin.coin_specs.hard_cap,
                coin.coin_specs.forking_coin, coin.coin_specs.tokenomics
            )
        )

        cursor.execute(
            "INSERT INTO CoinMarketData (rank, price_usd, market_cap_usd, volume_24h_usd, high_24h_usd, low_24h_usd, "
            "change_24h_percent, all_time_high, all_time_low, circulating_supply, market_dominance, "
            "last_updated) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (coin_id,
                coin.coin_market_data.rank, coin.coin_market_data.price_usd, coin.coin_market_data.market_cap_usd, coin.coin_market_data.volume_24h_usd,
                coin.coin_market_data.high_24h_usd, coin.coin_market_data.low_24h_usd, coin.coin_market_data.change_24h_percent,
                coin.coin_market_data.all_time_high, coin.coin_market_data.all_time_low, coin.coin_market_data.circulating_supply,
                coin.coin_market_data.market_dominance, coin.coin_market_data.last_updated
            )
        )

        conn.commit()
        print("Coin inserted into the database.")
        coin.id = coin_id
        return coin
    
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()

# --------------------------------------------------------------
# Section 2: Retrieval by Specific Criteria
# --------------------------------------------------------------

def get_coin_by_id(coin_id: int) -> Coin | None:
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, symbol, category, description, price, coin_specs_id, coin_market_data_id FROM Coin WHERE id = %s", (coin_id,))
    coin_data = cursor.fetchone()
    cursor.close()
    if coin_data:
        return get_complete_coin(coin_data[0])
    return None


def get_coin_specs_by_id(specs_id: int) -> CoinSpecs | None:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, algorithm, consensus_mechanism, blockchain_network, average_block_time, security_features, "
        "privacy_features, max_supply, genesis_block_date, token_type, governance_model, development_activity, "
        "hard_cap, forking_coin, tokenomics FROM CoinSpecs WHERE id = %s", (specs_id,)
    )
    specs_data = cursor.fetchone()
    cursor.close()
    if specs_data:
        return CoinSpecs(*specs_data[1:])
    return None


def get_coin_market_data_by_id(market_data_id: int) -> CoinMarketData | None:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, rank, price_usd, market_cap_usd, volume_24h_usd, high_24h_usd, low_24h_usd, change_24h_percent, "
        "all_time_high, all_time_low, circulating_supply, max_supply, market_dominance, last_updated "
        "FROM CoinMarketData WHERE id = %s", (market_data_id,)
    )
    coin.coin_market_data = cursor.fetchone()
    cursor.close()
    if coin.coin_market_data:
        return CoinMarketData(*coin.coin_market_data[1:])
    return None

# --------------------------------------------------------------
# Section 3: Complete Coin Retrieval
# --------------------------------------------------------------

def get_complete_coin(coin_id: int) -> Coin | None:
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, symbol, category, description, price, coin_specs_id, coin_market_data_id FROM Coin WHERE id = %s", (coin_id,))
    coin_data = cursor.fetchone()
    cursor.close()

    if not coin_data:
        return None

    coin_specs = get_coin_specs_by_id(coin_data[6])
    coin_market_data = get_coin_market_data_by_id(coin_data[7])

    if not coin_specs or not coin_market_data:
        return None

    return Coin(
        id=coin_data[0],
        name=coin_data[1],
        symbol=coin_data[2],
        category=coin_data[3],
        description=coin_data[4],
        price=coin_data[5],
        coin_specs=coin_specs,
        coin_market_data=coin_market_data
    )
