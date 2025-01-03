from json import dumps, loads

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
    
def get_crypto_wallet_by_user_id(user_id: int) -> CryptoWallet | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                print(f"Executing SELECT query for CryptoWallet with user_id: {user_id}.")
                
                cursor.execute(
                    "SELECT wallet_id, user_id, wallet_address, balance, total_coin_value, last_accessed, encryption_key, deposit_history, withdrawal_history "
                    "FROM crypto_wallet WHERE user_id = %s LIMIT 1;",
                    (user_id,)
                )

                result = cursor.fetchone()
                
                if result:
                    wallet_id, user_id, wallet_address, balance, total_coin_value, last_accessed, encryption_key, deposit_history, withdrawal_history = result

                    balance = loads(balance)
                    deposit_history = loads(deposit_history)
                    withdrawal_history = loads(withdrawal_history)
                    
                    wallet = CryptoWallet(
                        wallet_id=wallet_id,
                        user_id=user_id,
                        wallet_address=wallet_address,
                        balance=balance,
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
