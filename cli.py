import argparse
import logging
import os
from bot.client import BinanceClient

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True)
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")
    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(filename="logs/trading.log", level=logging.INFO)

    # Load API keys from environment variables
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    client = BinanceClient(api_key, api_secret, "https://testnet.binancefuture.com")

    logging.info(f"Placing {args.type} {args.side} order for {args.symbol}")
    response = client.place_order(args.symbol, args.side, args.type, args.quantity, args.price)

    print("Order Summary:")
    print(response)

if __name__ == "__main__":
    main()
