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

    GOOGLE_CLIENT_ID = getenv('GOOGLE_CLIENT_ID', 'your-google-client-id')
    GOOGLE_CLIENT_SECRET = getenv('GOOGLE_CLIENT_SECRET', 'your-google-client-secret')
    GOOGLE_DISCOVERY_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    