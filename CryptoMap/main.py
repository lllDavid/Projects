import requests
import matplotlib.pyplot as plt

def plot_price_history(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {'vs_currency': 'usd', 'days': '7'}
    response = requests.get(url, params=params)
    data = response.json()
    
    prices = [item[1] for item in data['prices']]
    timestamps = [item[0] for item in data['prices']]

    plt.plot(timestamps, prices)
    plt.title(f"{coin_id} Price History (Last 7 Days)")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.show()

plot_price_history("bitcoin")  