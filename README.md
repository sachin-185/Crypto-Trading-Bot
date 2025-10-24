# Binance Futures Testnet Trading Bot (Python)

A Python-based automated trading bot for Binance USDT-M Futures Testnet.  
Place MARKET, LIMIT, and STOP-LIMIT orders programmatically with safe price validation and real-time market checks — all without risking actual funds.

## Features
- Execute **market orders** instantly.
- Place **limit orders** with auto-adjusted safe prices.
- Place **stop-limit orders** with auto-calculated stop and limit prices.
- Detailed logging of all trades in `trading_bot.log`.
- Fully compatible with **Binance Futures Testnet**.
- Handles timestamp and price-related API errors automatically.

## Technologies
- Python 3.13  
- [`python-binance`](https://github.com/sammchardy/python-binance)  
- Binance Futures Testnet API  

## Usage Example
```bash
python trading_bot.py
