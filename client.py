from binance.client import Client
import logging
import os

class BinanceClient:
    def __init__(self, api_key, api_secret, base_url):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.API_URL = base_url

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == "MARKET":
                return self.client.futures_create_order(
                    symbol=symbol, side=side, type=order_type, quantity=quantity
                )
            elif order_type == "LIMIT":
                return self.client.futures_create_order(
                    symbol=symbol, side=side, type=order_type,
                    timeInForce="GTC", quantity=quantity, price=price
                )
        except Exception as e:
            logging.error(f"Order failed: {e}")
            raise

# Load API keys from environment variables
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")
client = BinanceClient(api_key, api_secret, "https://testnet.binancefuture.com")
