from json import dumps, loads
from decimal import Decimal
from datetime import datetime

from mariadb import ConnectionPool

from marketplace.config import Config
from marketplace.app.wallets.fiat.fiat_wallet import FiatWallet

pool = ConnectionPool(
    pool_name="fiat_wallet_db_pool",
    pool_size=20,  
    user=Config.WALLET_DB_CONFIG["user"],
    password=Config.WALLET_DB_CONFIG["password"],
    host=Config.WALLET_DB_CONFIG["host"],
    port=Config.WALLET_DB_CONFIG["port"],
    database=Config.WALLET_DB_CONFIG["database"]
)

def insert_fiat_wallet(wallet: FiatWallet) -> FiatWallet | None:
    try:
        with pool.get_connection() as conn:  
            with conn.cursor() as cursor:
                print(f"Executing INSERT query for FiatWallet with user_id: {wallet.user_id}.")
                cursor.execute(
                    "INSERT INTO fiat_wallet (user_id, balance, iban, swift_code, routing_number, encryption_key, deposit_history, withdrawal_history) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s); ",
                    (wallet.user_id, wallet.balance, wallet.iban, wallet.swift_code, wallet.routing_number, wallet.encryption_key, 
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

def get_fiat_wallet_by_user_id(user_id: int) -> FiatWallet | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                print(f"Executing SELECT query for FiatWallet with user_id: {user_id}.")
                
                # Execute the SELECT query to retrieve the fiat wallet based on the user_id
                cursor.execute(
                    "SELECT wallet_id, user_id, balance, iban, swift_code, routing_number, last_accessed, encryption_key, deposit_history, withdrawal_history "
                    "FROM fiat_wallet WHERE user_id = %s LIMIT 1;", 
                    (user_id,)
                )

                result = cursor.fetchone()
                
                if result:
                    wallet_id, user_id, balance, iban, swift_code, routing_number, last_accessed, encryption_key, deposit_history, withdrawal_history = result

                    # Convert values to the appropriate types
                    balance = Decimal(balance)  # Assuming 'balance' is stored as a numeric string
                    last_accessed = datetime.fromisoformat(last_accessed) if last_accessed else None  # Convert to datetime
                    deposit_history = loads(deposit_history) if deposit_history else {}  # Deserialize JSON to dict
                    withdrawal_history = loads(withdrawal_history) if withdrawal_history else {}  # Deserialize JSON to dict
                    
                    # Create and return the FiatWallet object
                    wallet = FiatWallet(
                        user_id=user_id,
                        wallet_id=wallet_id,
                        balance=balance,
                        iban=iban,  # You may want to extract this if it's part of your database schema
                        swift_code=swift_code,  # Same here
                        routing_number=routing_number,  # And here
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