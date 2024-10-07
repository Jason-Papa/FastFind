import argparse
from src.bank_holiday import next_holiday
from src.stocks.stock import fetch_stock_value
from src.days_until import parse_date_until_string
from src.weather import get_weather

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Fetch stock value and check bank holidays.")
    parser.add_argument('--stock', '-s',  help="The stock symbol to fetch (e.g., AAPL, ^GSPC for S&P 500).")
    parser.add_argument('--bank-holiday', '-bh', action='store_true', help="Check when is the next bank holiday.")
    parser.add_argument('--days-until', '-du', type=str, help="Calculates how many days are left until the specified date (dd-mm-yyyy).")
    parser.add_argument('--weather', '-w', type=str, help="Returns the weather for a specific location.")

    # Weather-specific arguments for today (-t) or week (-f) only when --weather is used
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--days', '-d', type=int, default=1, help="Get weather for the next n days.")
    
    # add verbose options
    # Parse the arguments
    args = parser.parse_args()
    
    # Handle stock fetching
    if args.stock:
        fetch_stock_value(args.stock)
    
    # Handle bank holiday checking
    elif args.bank_holiday:
        next_holiday()
    

    elif args.days_until:
        parse_date_until_string(args.days_until)


    elif args.weather:
        get_weather(args.weather, days=args.days)


if __name__ == "__main__":
    main()