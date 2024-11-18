import requests

def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',  # You can change this to other currencies
        'order': 'market_cap_desc',  # Sort by market cap
        'per_page': 10,  # Get top 10 coins
        'page': 1
    }
    response = requests.get(url, params=params)
    data = response.json()  # Parse the response as JSON
    return data

crypto_data = get_crypto_data()
print(crypto_data)
