import requests
from geopy.geocoders import Nominatim
from datetime import datetime

def get_sunrise_sunset(location_name):
    location_name = location_name.lower()
    try:
        # Step 1: Get latitude and longitude from location name
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(location_name)
        
        if not location:
            print(f"Error: Could not find location '{location_name}'.")
            return
        
        latitude = location.latitude
        longitude = location.longitude
        
        # Step 2: Call the sunrise-sunset API to get sunrise and sunset times
        api_url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0"
        response = requests.get(api_url)
        data = response.json()

        if data['status'] == 'OK':
            sunrise_utc = datetime.fromisoformat(data['results']['sunrise'].replace("Z", "+00:00"))
            sunset_utc = datetime.fromisoformat(data['results']['sunset'].replace("Z", "+00:00"))

            # Format and display the date and time separately
            print(f"Location: {location_name.capitalize()}")
            print(f"Sunrise Date: {sunrise_utc.strftime('%Y-%m-%d')}")
            print(f"Sunrise Time (UTC): {sunrise_utc.strftime('%H:%M:%S')}")
            print(f"Sunset Date: {sunset_utc.strftime('%Y-%m-%d')}")
            print(f"Sunset Time (UTC): {sunset_utc.strftime('%H:%M:%S')}")
        else:
            print(f"Error fetching sunrise/sunset data for '{location_name}'.")

    except Exception as e:
        print(f"An error occurred: {e}")
