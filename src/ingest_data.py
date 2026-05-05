import pandas as pd
from api_client import AlphaVantageClient
from validator import ResponseValidator
from logger import log_info, log_error

client = AlphaVantageClient()

def run(symbol: str):
    log_info(f"starting data ingestion for symbol: {symbol}")

    data = client.fetch_daily(symbol)

    is_valid, message = ResponseValidator.validate(data)

    if not is_valid:
        log_error(f"Data validation failed: {message}")
        return

    time_series = data.get("Time Series (Daily)", {})
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.index = pd.to_datetime(df.index)
    df.to_csv(f"{symbol}_daily.csv")
    log_info(f"Data ingestion completed for symbol: {symbol}")

if __name__ == "__main__":
    symbols = ["NVDA"]
    for symbol in symbols:
        run(symbol)