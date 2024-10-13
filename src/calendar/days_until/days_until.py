from datetime import datetime
import typer
import typing

def days_until(
        day: int,
        month: int | None,
        year=int | None,
    ) -> None:
    # Get today's date
    today = datetime.today()

    # Use current month and year if not provided
    if month is None:
        month = today.month
    if year is None:
        year = today.year

    # Target date
    target_date = datetime(year, month, day)

    # Calculate the difference in days
    difference = (target_date - today).days

    # If the target date is in the past for this year, calculate for the next year
    if difference < 0:
        target_date = datetime(year + 1, month, day)
        difference = (target_date - today).days

    typer.echo(difference)

def parse_date_until_string(date_str: str):
    if date_str.lower() in ["christmas", "xmas", "x-mas"]:
        date_str = "25-12"
    if date_str.lower() in ["new-years-eve", "nye", "ny"]:
        date_str = f"1-1-{datetime.now().year + 1}"

    months_map = {
        'january': 1,
        'february': 2,
        'march': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'july': 7,
        'august': 8,
        'september': 9,
        'october': 10,
        'november': 11,
        'december': 12
    }
    if date_str in months_map:
        now = datetime.now()
        date_month = months_map[date_str]
        year = now.year
        if now.month > months_map[date_str]:
            year += 1
        date_str = f"1-{months_map[date_str]}-{year}"
    try:
        date = date_str.split('-')
        if len(date) == 2:
            date.append(datetime.now().year)
        if len(date) != 3:
            raise ValueError
        day, month, year = date
        days_until(int(day), int(month), int(year))
    except ValueError:
        typer.echo(
            "Date must be in the format dd-mm-yy."
            "Empty mm and yy is assumed to be current month and year"
        )

