import requests
import typer

def get_crypto_price(crypto_id):
    # URL for CoinGecko API (public, no API key needed)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    
    try:
        # Send a GET request to fetch the crypto price
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request was unsuccessful
        
        # Parse the JSON response
        data = response.json()
        
        # Extract the price for the specified crypto
        price = data[crypto_id]['usd']
        typer.echo(f"The current price of {crypto_id.capitalize()} is ${price}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
