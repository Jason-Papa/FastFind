import argparse
from src.calendar.bank_holiday import next_holiday
from src.calendar.days_until import parse_date_until_string
from src.calendar.time_location import get_time_location
from src.calendar.sunrise_sunset import get_sunrise_sunset
from src.finance.stocks.stock import fetch_stock_value
from src.weather import get_weather
from src.finance.exchange_rate import get_exchange_rate
from src.finance.crypto import get_crypto_price
from src.networking.ip import get_public_ip
from src.networking.speedtest import perform_speedtest
from src.language.translate import translate_text
from src.language.synonyms import find_synonyms
from src.email.temp_email import create_email_wait_for_message
from src.calendar.calendar_events import calendar_events
from src.fun.random_facts import generate_random_fact 

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Fetch stock value and check bank holidays.")
    parser.add_argument('--stock', '-s',  help="The stock symbol to fetch (e.g., AAPL, ^GSPC for S&P 500).")
    parser.add_argument('--bank-holiday', '-bh', action='store_true', help="Check when is the next bank holiday.")
    parser.add_argument('--days-until', '-du', type=str, help="Calculates how many days are left until the specified date (dd-mm-yyyy).")
    parser.add_argument('--sunrise-sunset', '-ss', type=str, help="Returns the sunrise and sunset times in the selected location")
    parser.add_argument('--time-in', '-ti', type=str, help="Returns the time in selected location (eg. Europe/London, Athens etc)")
    parser.add_argument('--weather', '-w', type=str, help="Returns the weather for a specific location.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--days', '-ds', type=int, default=1, help="Get weather for the next n days.")
    parser.add_argument(
        '--exchange-rate', '-er', nargs=2, metavar=('BASE', 'TARGET'),
        help="Get the exchange rate between two currencies (e.g., USD EUR)."
    )
    parser.add_argument('--crypto-price', '-cp',  help="Fetch the value of the crypto (eg. bitcoin)")
    parser.add_argument('--my-ip', '-ip', action='store_true', help="Prints out the public ip address of the computer")
    parser.add_argument('--speedtest', '-st', action='store_true', help="Performs a speedtest of the internet connection")

    
    parser.add_argument('--translate', '-tr', type=str, help="Translate text to language determined by --target and --source")
    parser.add_argument('--source', '-src', type=str, help="Source language of the text to translate")
    parser.add_argument('--target', '-trg', type=str, help="Target language of the translated text")

    parser.add_argument('--synonym', '-sy', type=str, help="Gives synonyms for a word")
    parser.add_argument('--limit', '-l', default=10, type=int, help="Limit of the number of synonyms returned (default = 10)")

    parser.add_argument('--temporary-email', '-te', action='store_true', help="Create temporary email and wait for message")

    parser.add_argument('--calendar', '-ca', action='store_true', help="Fetches events for a day in the week from google calendar")
    parser.add_argument('--day', '-d', type=str, default='today', help="Determines which day to fetch calendar events from")

    parser.add_argument('--random-fact', '-rf', action='store_true', help="Generate random fact.")
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
    
    elif args.sunrise_sunset:
        get_sunrise_sunset(args.sunrise_sunset)

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
    
    elif args.translate:
        translate_text(args.translate,source_lang=args.source , target_lang=args.target)

    elif args.synonym:
        find_synonyms(args.synonym, limit= args.limit)

    elif args.temporary_email:
        create_email_wait_for_message()

    elif args.calendar:
        calendar_events(args.day)

    elif args.random_fact:
        generate_random_fact()

if __name__ == "__main__":
    main()