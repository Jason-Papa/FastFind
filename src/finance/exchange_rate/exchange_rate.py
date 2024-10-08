import requests
import typer

# Function to fetch exchange rate between two currencies
def get_exchange_rate(base_currency: str, target_currency: str):
    base_currency = base_currency.upper()
    target_currency = target_currency.upper()
    # API endpoint for exchange rates (you can use your preferred exchange rate API)
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    try:
        # Send a request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request failed
        
        # Parse the JSON response
        data = response.json()
        
        # Extract the exchange rate for the target currency
        rate = data['rates'].get(target_currency)
        if rate:
            typer.echo(f"Exchange rate from {base_currency} to {target_currency}: {rate}")
        else:
            print(f"Error: Unable to find exchange rate for {target_currency}.")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
