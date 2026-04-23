from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

class BinanceClient:
    def __init__(self, api_key, api_secret):
        if not api_key or not api_secret:
            raise ValueError("API credentials are missing. Check your .env file.")

        self.client = Client(api_key, api_secret, testnet=True)

    def create_order(self, **params):
        try:
            return self.client.futures_create_order(**params)

        except BinanceAPIException as e:
            raise Exception(f"Binance API Error: {e.message}")

        except BinanceRequestException as e:
            raise Exception(f"Network Error: {str(e)}")

        except Exception as e:
            raise Exception(f"Unexpected Error: {str(e)}")