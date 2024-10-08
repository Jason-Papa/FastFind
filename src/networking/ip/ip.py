import requests
import typer

def get_public_ip():
    try:
        # Use the ipify API to get the public IP address
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Check if the request was successful

        # Parse the JSON response
        data = response.json()
        public_ip = data['ip']

        typer.echo(f"Your public IP address is: {public_ip}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")