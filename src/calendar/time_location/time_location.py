import pytz
from datetime import datetime

def get_time_location(location):
    if '/' in location:
        continents, location = [location.split('/')[0]], location.split('/')[1]
    else:
        continents = [
            "Africa",
            "America",
            "Antarctica",
            "Asia",
            "Atlantic",
            "Australia",
            "Europe",
            "Indian",
            "Pacific"
        ]
    for continent in continents:
        try:
            # Get the timezone of the location
            timezone = pytz.timezone(f"{continent}/{location}")
            
            # Get the current time in the specified timezone
            current_time = datetime.now(timezone)
            
            # Format and return the current time
            print(f"The current time in {location} is {current_time.strftime('%H:%M:%S')} ({continent})")
        
        except pytz.UnknownTimeZoneError:
            pass

