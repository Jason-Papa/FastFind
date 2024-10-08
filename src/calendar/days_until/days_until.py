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
    try:
        date = date_str.split('-')
        if len(date) != 3:
            raise ValueError
        day, month, year = date
        days_until(int(day), int(month), int(year))
    except ValueError:
        typer.echo(
            "Date must be in the format dd-mm-yy."
            "Empty mm and yy is assumed to be current month and year"
        )

