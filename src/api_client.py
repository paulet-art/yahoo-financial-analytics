import requests
import time
from config import API_KEY, BASE_URL

class AlphaVantageClient:

    def fetch_daily(self, symbol:str):
        params ={
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": API_KEY
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 429:
            print("--> Rate limit exceeded. Waiting for 60 seconds before retrying...")
            time.sleep(60)
            return self.fetch_daily(symbol)
        
        return response.json()