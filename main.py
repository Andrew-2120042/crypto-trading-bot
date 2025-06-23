from binance.client import Client
import os
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(filename='trading_bot.log', level=logging.INFO)

class BasicBot:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.API_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol, side=side, type="MARKET", quantity=quantity
                )
            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol, side=side, type="LIMIT", quantity=quantity, price=price, timeInForce='GTC'
                )
            elif order_type == "STOP_MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol, side=side, type="STOP_MARKET", quantity=quantity, stopPrice=stop_price, timeInForce="GTC"
                )
            logging.info(f"Order response: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing order: {e}")
            return None

def get_user_input():
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Buy or Sell? ").upper()
    order_type = input("Order type (MARKET, LIMIT, STOP_MARKET): ").upper()
    quantity = float(input("Enter quantity: "))
    price = None
    stop_price = None
    if order_type == "LIMIT":
        price = input("Enter limit price: ")
    elif order_type == "STOP_MARKET":
        stop_price = input("Enter stop price: ")
    return symbol, side, order_type, quantity, price, stop_price

if __name__ == "__main__":
    bot = BasicBot()
    symbol, side, order_type, quantity, price, stop_price = get_user_input()
    result = bot.place_order(symbol, side, order_type, quantity, price, stop_price)
    print("Order Result:", result)
