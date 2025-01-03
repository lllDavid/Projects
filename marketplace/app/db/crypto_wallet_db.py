from json import dumps

from mariadb import ConnectionPool

from marketplace.config import Config
from marketplace.app.wallets.crypto.crypto_wallet import CryptoWallet

pool = ConnectionPool(
    pool_name="crypto_wallet_db_pool",
    pool_size=20,
    user=Config.WALLET_DB_CONFIG["user"],
    password=Config.WALLET_DB_CONFIG["password"],
    host=Config.WALLET_DB_CONFIG["host"],
    port=Config.WALLET_DB_CONFIG["port"],
    database=Config.WALLET_DB_CONFIG["database"]
)

def insert_crypto_wallet(wallet: CryptoWallet) -> CryptoWallet | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                print(f"Executing INSERT query for CryptoWallet with user_id: {wallet.user_id}.")
                cursor.execute(
                    "INSERT INTO crypto_wallet (user_id, wallet_address, balance, total_coin_value, last_accessed, encryption_key, deposit_history, withdrawal_history) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s); ",
                    (wallet.user_id, wallet.wallet_address, 
                     dumps(wallet.balance), wallet.total_coin_value, 
                     wallet.last_accessed, wallet.encryption_key, 
                     dumps(wallet.deposit_history), dumps(wallet.withdrawal_history))
                )

                conn.commit()
                print("Wallet inserted into the database.")

                wallet.wallet_id = cursor.lastrowid
                print(f"Wallet ID assigned: {wallet.wallet_id}")
                return wallet

    except conn.Error as e:
        print(f"Error inserting the wallet: {e}")
        return None
