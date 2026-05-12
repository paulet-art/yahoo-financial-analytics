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

        print(data)

        is_valid, message = ResponseValidator.validate(data)

        print(is_valid)
        print(message)

        if not is_valid:
            log_error(f"{symbol} failed: {message}")
            continue

        log_info(f"{symbol} processed successfully")

        time_series = data.get("Time Series (Daily)", {})

        print(time_series)

        df = pd.DataFrame.from_dict(time_series, orient="index")

        print(df.head())

        df.index = pd.to_datetime(df.index)

        df.columns = ["open", "high", "low", "close", "volume"]

        df["symbol"] = symbol

        print("SAVING CSV NOW")

        df.to_csv(f"/opt/airflow/data/{symbol}_daily.csv")

        print("CSV SAVED")

        log_info(f"{symbol} data saved successfully")

        df.to_sql(
            "stock_prices",
            engine,
            if_exists="append",
            index=False
        )

        print("DATA SAVED TO POSTGRES")