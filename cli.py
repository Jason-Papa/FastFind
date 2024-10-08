import argparse
from src.calendar.bank_holiday import next_holiday
from src.calendar.days_until import parse_date_until_string
from src.calendar.time_location import get_time_location
from src.finance.stocks.stock import fetch_stock_value
from src.weather import get_weather
from src.finance.exchange_rate import get_exchange_rate
from src.finance.crypto import get_crypto_price
from src.networking.ip import get_public_ip
from src.networking.speedtest import perform_speedtest

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Fetch stock value and check bank holidays.")
    parser.add_argument('--stock', '-s',  help="The stock symbol to fetch (e.g., AAPL, ^GSPC for S&P 500).")
    parser.add_argument('--bank-holiday', '-bh', action='store_true', help="Check when is the next bank holiday.")
    parser.add_argument('--days-until', '-du', type=str, help="Calculates how many days are left until the specified date (dd-mm-yyyy).")
    parser.add_argument('--time-in', '-ti', type=str, help="Returns the time in selected location (eg. Europe/London, Athens etc)")
    parser.add_argument('--weather', '-w', type=str, help="Returns the weather for a specific location.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--days', '-d', type=int, default=1, help="Get weather for the next n days.")
    parser.add_argument(
        '--exchange-rate', '-er', nargs=2, metavar=('BASE', 'TARGET'),
        help="Get the exchange rate between two currencies (e.g., USD EUR)."
    )
    parser.add_argument('--crypto-price', '-cp',  help="Fetch the value of the crypto (eg. bitcoin)")
    parser.add_argument('--my-ip', '-ip', action='store_true', help="Prints out the public ip address of the computer")
    parser.add_argument('--speedtest', '-st', action='store_true', help="Performs a speedtest of the internet connection")

    # add verbose options
    # Parse the arguments
    args = parser.parse_args()
    
    # Handle stock fetching
    if args.stock:
        fetch_stock_value(args.stock)
    
    # Handle bank holiday checking
    elif args.bank_holiday:
        next_holiday()
    
    elif args.time_in:
        get_time_location(args.time_in)

    elif args.days_until:
        parse_date_until_string(args.days_until)

    elif args.weather:
        get_weather(args.weather, days=args.days)

    elif args.exchange_rate:
        base_currency, target_currency = args.exchange_rate
        get_exchange_rate(base_currency, target_currency)

    elif args.crypto_price:
        get_crypto_price(args.crypto_price)

    elif args.my_ip:
        get_public_ip()
    
    elif args.speedtest:
        perform_speedtest()

if __name__ == "__main__":
    main()