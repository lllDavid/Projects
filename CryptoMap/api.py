import requests

def get_trending_coins():
    url = "https://api.coingecko.com/api/v3/search/trending"
    response = requests.get(url)
    data = response.json()
    
    # Debugging the structure of the response
    print(data)  # Print the response data to understand its structure
    
    # Assuming the correct structure is as follows (adjust based on actual data)
    trending_coins = [coin['item']['id'] for coin in data['coins']][:10]  # Access the 'item' dictionary for 'id'
    
    return trending_coins

# Test the function
trending_coins = get_trending_coins()
print(trending_coins)
