from binance import Client
import logging
import time

# ---------- SETUP LOGGING ----------
logging.basicConfig(filename="trading_bot.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# ---------- BASIC BOT CLASS ----------
class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        # Use Binance Futures Testnet URL
        self.client.API_URL = "https://testnet.binancefuture.com"
        logging.info("Bot initialized (testnet=%s)", testnet)

        # Synchronize client time offset automatically
        try:
            server_time = self.client.get_server_time()['serverTime']
            self.client.time_offset = server_time - int(time.time() * 1000)
            logging.info("Time offset synced with server: %d ms", self.client.time_offset)
        except Exception as e:
            logging.warning("Failed to sync time offset: %s", e)

    def place_market_order(self, symbol, side, quantity):
        """Place a simple market order with auto timestamp"""
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='MARKET',
                quantity=quantity
            )
            print("✅ Market order placed successfully!")
            print(order)
            logging.info("Market order success: %s", order)
        except Exception as e:
            print("❌ Error placing market order:", e)
            logging.error("Market order failed: %s", e)

    def place_limit_order(self, symbol, side, quantity, price):
        """Place a simple limit order with auto timestamp"""
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            print("✅ Limit order placed successfully!")
            print(order)
            logging.info("Limit order success: %s", order)
        except Exception as e:
            print("❌ Error placing limit order:", e)
            logging.error("Limit order failed: %s", e)

    def place_stop_limit_order(self, symbol, side, quantity, stopPrice, price):
        """Place a stop-limit order with auto timestamp"""
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='STOP',
                stopPrice=stopPrice,
                price=price,
                timeInForce='GTC',
                quantity=quantity
            )
            print("✅ Stop-limit order placed successfully!")
            print(order)
            logging.info("Stop-limit order success: %s", order)
        except Exception as e:
            print("❌ Error placing stop-limit order:", e)
            logging.error("Stop-limit order failed: %s", e)

# ---------- MAIN SCRIPT ----------
if __name__ == "__main__":
    # 1. ENTER your Testnet API keys here 👇
    api_key = "OJqawsZwL5CAlBfrP787uv8dccCe57ZGSbVSqcZbo7pIWRltjD35RTIQDW530t0b"
    api_secret = "hGEv1WJXrDKoWOaO4zphO2oFOWxUl93yXtoQIm1luWFLAyPI8GP7bsKvxaNmkX4w"

    # 2. Create bot
    bot = BasicBot(api_key, api_secret)

    # 3. Example orders (use one at a time)
    print("Placing MARKET BUY...")
    bot.place_market_order("BTCUSDT", "BUY", 0.001)

    print("\nPlacing LIMIT SELL...")
    current_price = 105000  # example, check testnet price
    bot.place_limit_order("BTCUSDT", "SELL", 0.001, current_price + 100)


    # Uncomment below for a Stop-Limit order example
    # print("\nPlacing STOP-LIMIT SELL...")
    # bot.place_stop_limit_order("BTCUSDT", "SELL", 0.001, stopPrice=81000, price=80000)
