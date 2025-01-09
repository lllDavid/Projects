from os import getenv

class Config:
    USER_DB_CONFIG = {
        "user": "root",
        "password": "root",
        "host": "localhost",
        "port": 3306,
        "database": "marketplace_users"
    }

    COIN_DB_CONFIG = {
        "user": "root",
        "password": "root",
        "host": "localhost",
        "port": 3306,
        "database": "marketplace_coins"
    }

    WALLET_DB_CONFIG = {
        "user": "root",
        "password": "root",
        "host": "localhost",
        "port": 3306,
        "database": "marketplace_wallets"
    }