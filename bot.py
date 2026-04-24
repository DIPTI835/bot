# bot/client.py
from binance.client import Client

class BinanceClient:
    def __init__(self, api_key: str, api_secret: str, base_url: str):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.API_URL = base_url

    def place_order(self, symbol, side, order_type, quantity, price=None):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            price=price
        )
