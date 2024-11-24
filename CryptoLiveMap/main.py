import requests
import matplotlib.pyplot as plt
import numpy as np

# Function to plot cryptocurrency price history (line plot)
def plot_price_history(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {'vs_currency': 'usd', 'days': '7'}
    response = requests.get(url, params=params)
    data = response.json()
    
    prices = [item[1] for item in data['prices']]
    timestamps = [item[0] for item in data['prices']]

    return timestamps, prices

# Function to plot a bar chart (custom data)
def plot_bar_chart():
    x = 0.5 + np.arange(8)
    y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))
    return fig, ax  # Return the figure and axis to reuse later if necessary

# Combine both plots
def combine_plots(coin_id):
    # Create the first plot: Cryptocurrency price history (line plot)
    timestamps, prices = plot_price_history(coin_id)
    fig, ax1 = plt.subplots(figsize=(12, 8))

    ax1.plot(timestamps, prices, label=f"{coin_id} Price History (Last 7 Days)")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Price (USD)")
    ax1.set_title(f"{coin_id} Price History & Custom Bar Chart")
    
    # Second plot: Bar chart (custom data)
    ax2 = ax1.twinx()  # Create a second y-axis
    plot_bar_chart()[1].bar(0.5 + np.arange(8), [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0], width=1, edgecolor="white", linewidth=0.7)
    ax2.set_ylabel("Custom Data")

    # Final layout and showing both plots
    plt.tight_layout()  # Adjust layout to avoid overlap
    plt.show()

# Example usage: Combine plots for "bitcoin"
combine_plots("bitcoin")
