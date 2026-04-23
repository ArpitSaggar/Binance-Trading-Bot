import os
import inquirer
from dotenv import load_dotenv

from bot.client import BinanceClient
from bot.orders import place_order
from bot.logging_config import setup_logger

load_dotenv()

def get_user_input():
    questions = [
        inquirer.Text("symbol", message="Enter symbol (e.g. BTCUSDT)"),
        inquirer.List("side", message="Select side", choices=["BUY", "SELL"]),
        inquirer.List("type", message="Order type", choices=["MARKET", "LIMIT", "STOP"]),
        inquirer.Text("quantity", message="Quantity"),
    ]

    answers = inquirer.prompt(questions)

    if answers["type"] in ["LIMIT", "STOP"]:
        price = input("Enter price: ")
        answers["price"] = float(price)

    if answers["type"] == "STOP":
        stop_price = input("Enter stop price: ")
        answers["stop_price"] = float(stop_price)

    return answers


def main():
    logger = setup_logger()

    try:
        user_input = get_user_input()

        symbol = user_input["symbol"]
        side = user_input["side"]
        order_type = user_input["type"]

        try:
            quantity = float(user_input["quantity"])
        except ValueError:
            raise ValueError("Quantity must be a number")

        price = user_input.get("price")
        stop_price = user_input.get("stop_price")

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        client = BinanceClient(api_key, api_secret)

        print("\n--- Order Summary ---")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        response = place_order(
            client,
            logger,
            symbol,
            side,
            order_type,
            quantity,
            price,
            stop_price
        )

        print("\n--- Order Response ---")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

        print("\n✅ Order placed successfully")

    except ValueError as ve:
        print(f"\n⚠️ Input Error: {str(ve)}")

    except Exception as e:
        print(f"\n❌ Something went wrong: {str(e)}")


if __name__ == "__main__":
    main() 