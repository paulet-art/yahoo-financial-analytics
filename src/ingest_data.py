import pandas as pd
from api_client import AlphaVantageClient
from logger import log_error, log_info
from validator import ResponseValidator
from db import engine

client = AlphaVantageClient()

def run(symbols):

    for symbol in symbols:

        log_info(f"starting data ingestion for symbol: {symbol}")

        data = client.fetch_daily(symbol)

        is_valid, message = ResponseValidator.validate(data)

        if not is_valid:
            log_error(f"{symbol} failed: {message}")
            continue

        log_info(f"{symbol} processed successfully")

        time_series = data.get("Time Series (Daily)", {})

        df = pd.DataFrame.from_dict(time_series, orient="index")

        df.index = pd.to_datetime(df.index)
        df = df.reset_index().rename(columns={"index": "date"})

        df.columns = ["open", "high", "low", "close", "volume"]

        df["symbol"] = symbol

        df = df[["date", "symbol", "open", "high", "low", "close", "volume"]]

        df["date"] = pd.to_datetime(df["date"])

        df[["open", "high", "low", "close", "volume"]] = df[
            ["open", "high", "low", "close", "volume"]
        ].astype(float)

        log_info(f"Inserting {symbol} into Postgres")

        df.to_sql(
            "stock_prices",
            engine,
            if_exists="append",
            index=False
        )

        log_info(f"{symbol} inserted successfully")