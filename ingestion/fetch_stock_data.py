import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_stock_data(ticker, start = "2025-01-01"):
    df = yf.download(ticker,start=start)
    df.reset_index(inplace=True)
    df['ticker'] = ticker
    return df

def save_to_csv(df, ticker):
    date_str = datetime.now().strftime("%Y%m%d")
    file_path = f"data/{ticker}_{date_str}.csv"
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL"]
    for ticker in tickers:
        data = fetch_stock_data(ticker)
        save_to_csv(data, ticker)
