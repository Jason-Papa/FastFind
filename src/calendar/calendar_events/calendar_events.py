import os
import requests
from ics import Calendar
from datetime import datetime, timedelta
import sys

# Define the file name for storing the calendar link
CALENDAR_FILE = "calendar_link.txt"

# Function to get the calendar link from the local file or prompt user if it doesn't exist
def get_calendar_link():
    if not os.path.exists(CALENDAR_FILE) or os.stat(CALENDAR_FILE).st_size == 0:
        # Prompt the user to provide the Google Calendar ICS link
        calendar_link = input("Please provide your Google Calendar ICS link: ").strip()

        # Save the link to the local file
        with open(CALENDAR_FILE, "w") as f:
            f.write(calendar_link + '\n')
        return calendar_link
    else:
        # Read the ICS URL from the file
        with open(CALENDAR_FILE, "r") as f:
            calendar_link = f.readline().strip()
        return calendar_link

# Function to fetch and print events from the Google Calendar ICS link
def fetch_calendar_events(ics_url, target_day=None):
    try:
        # Download the ICS file
        response = requests.get(ics_url)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve calendar (status code {response.status_code}).")
            return

        # Parse the ICS file
        calendar = Calendar(response.text)

        print(f"Events for {target_day.strftime('%A, %B %d, %Y')}:")

        # Iterate through events and filter events for the target day
        for event in calendar.timeline:
            event_start = event.begin.datetime.date()
            event_finish = event.end.datetime
            if event_start == target_day:
                print(f"{event.name} at {event.begin.datetime.strftime('%H:%M')}-{event_finish.strftime('%H:%M')}")

    except Exception as e:
        print(f"An error occurred: {e}")

def calendar_events(target_day: str):
    today = datetime.now().date()

    # Map days of the week to numbers
    days_of_week = {
        "monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
        "friday": 4, "saturday": 5, "sunday": 6
    }

    # Parse arguments to get the target day
    if target_day != 'today':
        day_argument = target_day.lower()
        if day_argument in days_of_week:
            # Get the target day based on the provided day of the week
            today_weekday = today.weekday()
            target_weekday = days_of_week[day_argument]
            delta_days = (target_weekday - today_weekday) % 7
            target_day = today + timedelta(days=delta_days)
        else:
            print(f"Invalid day: {day_argument}. Defaulting to today's events.")
            target_day = today
    else:
        # Default to today if no argument is provided
        target_day = today

    # Get the calendar link (read from file or prompt if missing)
    ics_url = get_calendar_link()

    # Fetch and print events for the target day
    fetch_calendar_events(ics_url, target_day)