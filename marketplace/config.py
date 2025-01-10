from os import getenv

class Config:
    USER_DB_CONFIG = {
        "user": getenv("DB_USER", "user"),
        "password": getenv("DB_PASSWORD", "user_password"),
        "host": getenv("DB_HOST", "db"),  # Use the MariaDB container name as the host
        "port": 3306,  # Ensure the correct port is used (3306 for MariaDB)
        "database": getenv("DB_NAME", "crypto_app_db")
    }

    COIN_DB_CONFIG = {
        "user": getenv("DB_USER", "user"),
        "password": getenv("DB_PASSWORD", "user_password"),
        "host": getenv("DB_HOST", "db"),
        "port": 3306,
        "database": getenv("DB_NAME", "crypto_app_db")
    }

    WALLET_DB_CONFIG = {
        "user": getenv("DB_USER", "user"),
        "password": getenv("DB_PASSWORD", "user_password"),
        "host": getenv("DB_HOST", "db"),
        "port": 3306,
        "database": getenv("DB_NAME", "crypto_app_db")
    }
