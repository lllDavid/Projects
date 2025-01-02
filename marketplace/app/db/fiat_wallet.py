from json import dumps
from mariadb import connect
from marketplace.config import Config
from marketplace.app.wallets.fiat.fiat_wallet import FiatWallet

conn = connect(
    user=Config.WALLET_DB_CONFIG["user"],
    password=Config.WALLET_DB_CONFIG["password"],
    host=Config.WALLET_DB_CONFIG["host"],
    port=Config.WALLET_DB_CONFIG["port"],
    database=Config.WALLET_DB_CONFIG["database"]
)

def insert_fiat_wallet(wallet: FiatWallet) -> FiatWallet| None:
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                " INSERT INTO fiat_wallets (user_id, balance, iban, swift_code, routing_number, encryption_key, deposit_history, withdrawal_history) VALUES (%s, %s, %s, %s, %s, %s, %s, %s); ",
                (wallet.user_id, wallet.balance, wallet.iban, wallet.swift_code, wallet.routing_number, wallet.encryption_key, dumps(wallet.deposit_history), dumps(wallet.withdrawal_history))
            )

            conn.commit()

            print(f"Wallet inserted into the database.")
            wallet.wallet_id = cursor.lastrowid
            return wallet
        
    except conn.Error as e:
        conn.rollback()
        print(f"Error inserting the wallet: {e}")

