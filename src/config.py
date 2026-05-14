import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

TECH_STOCKS = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "META"
]