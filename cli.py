import argparse
from src.bank_holiday import next_holiday
from src.stocks.stock import fetch_stock_value


def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Fetch stock value and check bank holidays.")
    parser.add_argument('--stock', help="The stock symbol to fetch (e.g., AAPL, ^GSPC for S&P 500).")
    parser.add_argument('--bank-holiday', action='store_true', help="Check when is the next bank holiday.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Handle stock fetching
    if args.stock:
        fetch_stock_value(args.stock)
    
    # Handle bank holiday checking
    if args.bank_holiday:
        next_holiday()

if __name__ == "__main__":
    main()