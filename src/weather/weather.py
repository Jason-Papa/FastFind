import requests

def get_weather(location: str, days: int = 1):
    # Use wttr.in to get weather data in plain text format
    url = f"http://wttr.in/{location}?m&{days}"
    try:
        # Send a request to the wttr.in service
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        
        # Get the weather data as plain text
        weather_data = response.text
        
        # Print the weather information
        print(f"Weather in {location.capitalize()}:")
        print(weather_data)
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

