from os import path, getenv

def get_db_host():
    return getenv("DB_HOST", "localhost") 

class Config:
    USER_DB_CONFIG = {
        "user": "root",
        "password": "root",
        "host": get_db_host(),  
        "port": 3306,  
        "database": "marketplace_users"
    }

    COIN_DB_CONFIG = {
        "user": "root",
        "password": "root",
        "host": get_db_host(),  
        "port": 3306,
        "database": "marketplace_coins"
    }

    WALLET_DB_CONFIG = {
        "user": "root",
        "password": "root",
        "host": get_db_host(), 
        "port": 3306,
        "database": "marketplace_wallets"
    }
