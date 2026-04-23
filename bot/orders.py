from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

def place_order(client, logger, symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)

        order_data = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": float(quantity),
        }

        if order_type == "LIMIT":
            validate_price(price, order_type)
            order_data["price"] = float(price)
            order_data["timeInForce"] = "GTC"

        elif order_type == "STOP":
            if price is None or stop_price is None:
                raise ValueError("STOP order requires both price and stop_price")

            order_data["price"] = float(price)
            order_data["stopPrice"] = float(stop_price)
            order_data["timeInForce"] = "GTC"

        logger.info(f"Placing order: {order_data}")

        response = client.create_order(**order_data)

        logger.info(f"Order successful: {response}")

        return response

    except ValueError as ve:
        logger.error(f"Validation Error: {str(ve)}")
        raise

    except Exception as e:
        logger.error(f"Order Failed: {str(e)}")
        raise 