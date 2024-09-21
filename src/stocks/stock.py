import yfinance as yf
import argparse

def fetch_stock_value(stock_symbol):
    # Fetch the data for the specified stock
    ticker = yf.Ticker(f"{stock_symbol}")
    
    # Get the current stock price info (this contains today's high, low, open, close, etc.)
    data = ticker.history(period="1d")
    
    # Get the last 'Close' value of the day
    if not data.empty:
        current_value = data['Close'].iloc[-1]
        print(f"Current value of {stock_symbol}: {current_value}")
    else:
        print(f"Failed to retrieve data for {stock_symbol}")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Fetch current stock value using Yahoo Finance")
    parser.add_argument('--stock', required=True, help='The stock symbol to fetch (e.g., "^GSPC" for S&P 500 and AAPL for Apple)')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Fetch and print the stock value
    fetch_stock_value(args.stock)

if __name__ == "__main__":
    main()

