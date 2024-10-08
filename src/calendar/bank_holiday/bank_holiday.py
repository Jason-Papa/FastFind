import requests
import typer
from datetime import datetime

app = typer.Typer()

BANK_HOLIDAYS_API = "https://www.gov.uk/bank-holidays.json"

def get_next_bank_holiday(region: str="england-and-wales"):
    try:
        response = requests.get(BANK_HOLIDAYS_API)
        response.raise_for_status()
        data = response.json()
        holidays = data[region]["events"]
        
        today = datetime.now().date()
        for holiday in holidays:
            holiday_date = datetime.strptime(holiday["date"], "%Y-%m-%d").date()
            if holiday_date > today:
                return  holiday
        return None
    except Exception as e:
        typer.echo(f"error: {e}")

def next_holiday(region:str = "england-and-wales"):
    holiday = get_next_bank_holiday(region)
    if holiday:
        days_to_holiday = (datetime.strptime(holiday["date"], "%Y-%m-%d").date() - datetime.now().date()).days
        typer.echo(f"Next one in {region} is {holiday['title']} on {holiday['date']} which is in {days_to_holiday} days")
    else:
        typer.echo("Could not find one")