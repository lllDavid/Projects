from json import dumps, loads
from decimal import Decimal

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

def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError(f"Type {type(obj)} not serializable")

def deserialize_data(data):
    return loads(data) if isinstance(data, str) else data

def insert_fiat_wallet(wallet: FiatWallet) -> FiatWallet | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO fiat_wallet (user_id, balance, iban, swift_code, routing_number, encryption_key, deposit_history, withdrawal_history) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s); ",
                    (wallet.user_id, 
                     wallet.balance, 
                     wallet.iban, 
                     wallet.swift_code, 
                     wallet.routing_number, 
                     wallet.encryption_key, 
                     dumps(wallet.deposit_history, default=decimal_serializer), 
                     dumps(wallet.withdrawal_history, default=decimal_serializer))
                )

                conn.commit()

                wallet.wallet_id = cursor.lastrowid
                return wallet

    except Exception as e:
        return None

def get_fiat_wallet_by_user_id(user_id: int) -> FiatWallet | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT wallet_id, user_id, balance, iban, swift_code, routing_number, last_accessed, encryption_key, deposit_history, withdrawal_history "
                    "FROM fiat_wallet WHERE user_id = %s LIMIT 1;", 
                    (user_id,)
                )

                result = cursor.fetchone()
                
                if result:
                    wallet_id, user_id, balance, iban, swift_code, routing_number, last_accessed, encryption_key, deposit_history, withdrawal_history = result

                    deposit_history = deserialize_data(deposit_history)
                    withdrawal_history = deserialize_data(withdrawal_history)

                    wallet = FiatWallet(
                        wallet_id=wallet_id,
                        user_id=user_id,
                        balance=balance,
                        iban=iban,
                        swift_code=swift_code,
                        routing_number=routing_number,
                        last_accessed=last_accessed,
                        encryption_key=encryption_key,
                        deposit_history=deposit_history,
                        withdrawal_history=withdrawal_history
                    )

                    return wallet
                else:
                    return None

    except Exception as e:
        return None

def update_fiat_wallet(wallet: FiatWallet) -> FiatWallet | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE fiat_wallet
                    SET 
                        balance = %s, 
                        iban = %s, 
                        swift_code = %s, 
                        routing_number = %s, 
                        last_accessed = %s, 
                        encryption_key = %s, 
                        deposit_history = %s, 
                        withdrawal_history = %s
                    WHERE wallet_id = %s;
                    """,
                    (
                        wallet.balance, 
                        wallet.iban, 
                        wallet.swift_code, 
                        wallet.routing_number, 
                        wallet.last_accessed, 
                        wallet.encryption_key, 
                        dumps(wallet.deposit_history, default=decimal_serializer), 
                        dumps(wallet.withdrawal_history, default=decimal_serializer), 
                        wallet.wallet_id
                    )
                )

                conn.commit()

                if cursor.rowcount > 0:
                    return wallet
                else:
                    return None

    except Exception as e:
        return None

