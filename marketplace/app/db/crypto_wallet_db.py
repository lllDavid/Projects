from json import dumps, loads
from decimal import Decimal
from mariadb import ConnectionPool
from marketplace.config import Config
from marketplace.app.wallets.crypto.crypto_wallet import CryptoWallet

# Create a connection pool for database
pool = ConnectionPool(
    pool_name="crypto_wallet_db_pool",
    pool_size=20,
    user=Config.WALLET_DB_CONFIG["user"],
    password=Config.WALLET_DB_CONFIG["password"],
    host=Config.WALLET_DB_CONFIG["host"],
    port=Config.WALLET_DB_CONFIG["port"],
    database=Config.WALLET_DB_CONFIG["database"]
)

# Helper function for serializing Decimal objects
def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError(f"Type {type(obj)} not serializable")

# Helper function for deserializing JSON strings into dictionaries
def deserialize_data(data):
    return loads(data) if isinstance(data, str) else data

# Helper function to convert string values in dictionary to Decimal
def convert_to_decimal(data):
    return {key: Decimal(value) if isinstance(value, str) else value for key, value in data.items()}

# Insert new crypto wallet into the database
def insert_crypto_wallet(wallet: CryptoWallet) -> CryptoWallet | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                print(f"Executing INSERT query for CryptoWallet with user_id: {wallet.user_id}.")

                cursor.execute(
                    "INSERT INTO crypto_wallet (user_id, wallet_address, coins, total_coin_value, last_accessed, encryption_key, deposit_history, withdrawal_history) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s); ",
                    (
                        wallet.user_id, 
                        wallet.wallet_address, 
                        dumps(wallet.coins, default=decimal_serializer), 
                        wallet.total_coin_value, 
                        wallet.last_accessed, 
                        wallet.encryption_key, 
                        dumps(wallet.deposit_history, default=decimal_serializer), 
                        dumps(wallet.withdrawal_history, default=decimal_serializer)
                    )
                )

                conn.commit()
                wallet.wallet_id = cursor.lastrowid
                print(f"Wallet inserted with wallet_id: {wallet.wallet_id}")
                return wallet

    except Exception as e:
        print(f"Error inserting the wallet: {e}")
        return None

# Retrieve crypto wallet by user ID
def get_crypto_wallet_by_user_id(user_id: int) -> CryptoWallet | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                print(f"Executing SELECT query for CryptoWallet with user_id: {user_id}.")

                cursor.execute(
                    "SELECT wallet_id, user_id, wallet_address, coins, total_coin_value, last_accessed, encryption_key, deposit_history, withdrawal_history "
                    "FROM crypto_wallet WHERE user_id = %s LIMIT 1;",
                    (user_id,)
                )

                result = cursor.fetchone()

                if result:
                    wallet_id, user_id, wallet_address, coins, total_coin_value, last_accessed, encryption_key, deposit_history, withdrawal_history = result

                    # Deserializing and converting data
                    coins = convert_to_decimal(deserialize_data(coins))
                    deposit_history = deserialize_data(deposit_history)
                    withdrawal_history = deserialize_data(withdrawal_history)

                    wallet = CryptoWallet(
                        wallet_id=wallet_id,
                        user_id=user_id,
                        wallet_address=wallet_address,
                        coins=coins,
                        total_coin_value=total_coin_value,
                        last_accessed=last_accessed,
                        encryption_key=encryption_key,
                        deposit_history=deposit_history,
                        withdrawal_history=withdrawal_history
                    )

                    print(f"Wallet with user_id {user_id} found.")
                    return wallet
                else:
                    print(f"No wallet found for user_id: {user_id}.")
                    return None

    except Exception as e:
        print(f"Error retrieving the wallet for user_id {user_id}: {e}")
        return None

# Update an existing crypto wallet
def update_crypto_wallet(wallet: CryptoWallet) -> CryptoWallet | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                print(f"Executing UPDATE query for wallet with wallet_id: {wallet.wallet_id}.")

                cursor.execute(
                    """
                    UPDATE crypto_wallet
                    SET 
                        wallet_address = %s, 
                        coins = %s, 
                        total_coin_value = %s, 
                        last_accessed = %s, 
                        encryption_key = %s, 
                        deposit_history = %s, 
                        withdrawal_history = %s
                    WHERE wallet_id = %s;
                    """,
                    (
                        wallet.wallet_address, 
                        dumps(wallet.coins, default=decimal_serializer), 
                        wallet.total_coin_value, 
                        wallet.last_accessed, 
                        wallet.encryption_key, 
                        dumps(wallet.deposit_history, default=decimal_serializer), 
                        dumps(wallet.withdrawal_history, default=decimal_serializer), 
                        wallet.wallet_id
                    )
                )

                conn.commit()

                if cursor.rowcount > 0:
                    print(f"Wallet with wallet_id {wallet.wallet_id} updated successfully.")
                    return wallet
                else:
                    print(f"No updates made to wallet with wallet_id {wallet.wallet_id}.")
                    return None

    except Exception as e:
        print(f"Error updating CryptoWallet: {e}")
        return None
