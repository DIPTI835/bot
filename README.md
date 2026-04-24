This project is a command-line interface CLI trading bot built in Python.
It connects to the Binance Futures Testnet using the official pythonbinance library
The bot allows users to place test trades programmatically by passing arguments such as symbol, side, type, quantity and price
# Bot
A Python command‑line trading bot for Binance Futures Testnet.
## Overview
This bot connects to Binance Futures Testnet and allows users to place BUY/SELL orders from the command line. It is designed for practicing algorithmic trading safely without risking real funds.
## Installation
Python 3.10+
Install dependencies:
pip install python-binance

## Usage
Run from terminal:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
## Why This Project Matters
Demonstrates secure API key handling with environment variables.
Provides hands‑on experience with Binance Futures Testnet.
Helped me learn CLI design, logging, and API integration.
