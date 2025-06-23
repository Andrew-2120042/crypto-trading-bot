import streamlit as st
from main import BasicBot

st.set_page_config(page_title="Binance Futures Trading Bot", layout="centered")

bot = BasicBot()

st.title("📈 Binance Futures Trading Bot (Testnet)")

symbol = st.text_input("Symbol (e.g., BTCUSDT)", "BTCUSDT")
side = st.selectbox("Order Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP_MARKET"])
quantity = st.number_input("Quantity", min_value=0.001, step=0.001, format="%.6f")
price = None
stop_price = None

if order_type == "LIMIT":
    price = st.text_input("Limit Price (e.g., 30000)")
elif order_type == "STOP_MARKET":
    stop_price = st.text_input("Stop Price (e.g., 28000)")

if st.button("🚀 Place Order"):
    order = bot.place_order(symbol, side, order_type, quantity, price, stop_price)
    if order:
        st.success("✅ Order placed successfully!")
        st.json(order)
    else:
        st.error("❌ Order failed. Check logs or try again.")
