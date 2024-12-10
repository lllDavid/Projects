from os import getenv

class Config:
    DB_CONFIG = {
        "user": "root",
        "password": "root",
        "host": "localhost",
        "port": 3306,
        "database": "marketplace"
    }

    LOGGING_CONFIG = {
        "level": "DEBUG",
        "file": "app.log"
    }

    COIN_API_CONFIG = {
        "api_key": getenv("COIN_API_KEY"),  
        "base_url": "https://pro-api.coinmarketcap.com/v1",
        "endpoints": {
            "cryptocurrency": {
                "listings": "/cryptocurrency/listings/latest",
                "quotes": "/cryptocurrency/quotes/latest",
                "metadata": "/cryptocurrency/info"
            },
            "market": {
                "global": "/global-metrics/quotes/latest",
                "historical": "/cryptocurrency/ohlcv/historical"
            },
            "fiat": {
                "currencies": "/fiat/map"
            }
        },
        "request_limits": {
            "free_plan": {
                "max_requests_per_month": 10000,
                "requests_per_minute": 10
            }
        },
        "headers": {
            "Accept": "application/json",
            "X-CMC_PRO_API_KEY": getenv("COIN_API_KEY"), 
            "Content-Type": "application/json"
        },
        "retry_policy": {
            "max_retries": 3,
            "retry_delay_seconds": 5
        },
        "logging": {
            "enabled": True,
            "log_level": "info",
            "log_file": "/path/to/log/file.log"
        },
        "timeout": {
            "connection": 10,
            "read": 30
        }
    }
