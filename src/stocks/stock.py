import yfinance as yf
import argparse

def fetch_stock_value(stock_symbol, period='1d'):
    # Fetch the data for the specified stock
    ticker = yf.Ticker(f"{stock_symbol}")
    
    # Get the current stock price info (this contains today's high, low, open, close, etc.)
    data = ticker.history(period=period)
    
    # Get the last 'Close' value of the day
    if not data.empty:
        current_value = data['Close'].iloc[-1]
        open_value = data['Open'].iloc[-1]
        color = '\033[32m ↑' if open_value < current_value else '\033[31m ↓'
        percentage_change = (current_value - open_value)/open_value * 100
        print(f"Current value of {stock_symbol}:{color}{current_value:.2f} ({percentage_change:.2f}%)\033[0m")
    else:
        print(f"Failed to retrieve data for {stock_symbol}")

