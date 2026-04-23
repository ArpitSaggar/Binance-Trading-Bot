Binance Futures Testnet Trading Bot

This is a Python-based CLI trading bot built to interact with the Binance Futures Testnet (USDT-M).  
It allows users to place MARKET, LIMIT, and STOP orders with proper validation, logging, and error handling.

Features- 

- It can place MARKET, LIMIT, and STOP orders
- It supports both BUY and SELL
- Inputs validation to prevent incorrect orders
- Proper logging of API requests, responses, and errors
- Has a clean modular architecture


Project Structure-
trading_bot/
│
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md

How It Works

The application is structured into different modules for clarity and maintainability:

- cli.py → Handles user interaction via command-line prompts  
- client.py → Manages Binance API communication  
- orders.py → Contains order placement logic  
- validators.py → Validates user inputs  
- logging_config.py → Handles logging configuration  

Execution Flow

1. Run the bot using `python cli.py`
2. Enter order details (symbol, side, type, quantity)
3. Inputs are validated
4. Order is sent to Binance API
5. Response is displayed and logged
6. Logs are stored in `bot.log`


## VERY IMPORTANT -  Testnet vs Live Trading

This project uses the Binance Futures Testnet environment.

Why Testnet?

Live trading on Binance requires:
- Identity verification (KYC)
- Real funds

To avoid these requirements and ensure safe testing, this project uses testnet API keys.



Behavior

On testnet:

- Orders may **not execute**
- Market orders may stay in `NEW` status
- `executedQty` can be `0`

Working with TestNet (Real screenshots taken from my PC) 
<img width="1916" height="1130" alt="Screenshot 2026-04-23 110856" src="https://github.com/user-attachments/assets/51c41fc5-a31d-4db9-a895-b45c7c8669df" />
<img width="1915" height="1129" alt="Screenshot 2026-04-23 110835" src="https://github.com/user-attachments/assets/d6884515-b0dc-4710-b990-d0fab8d18a6b" />


Why this happens?

Testnet does not have real market liquidity, so orders are not always matched.

What This Proves

Even if orders are not filled, the bot is working correctly because it:

- Sends API requests successfully  
- Receives valid responses  
- Logs all actions  
- Handles errors properly  


How to Run-
1. Install dependencies
2. Add API keys in `.env`
3. Run the bot

Assumptions -

- User has a Binance Futures Testnet account
- API keys are valid
- Symbol exists on Binance (e.g., BTCUSDT)
- Testnet limitations are (Important)

Security Note
- `.env` file is ignored using `.gitignore`
- API keys are not exposed in the repository

Thus, this project demonstrates a complete trading workflow including:

- API integration
- CLI interaction
- Input validation
- Logging
- Error handling

It is designed to simulate real-world trading system behavior in a safe testnet environment.

Thank you for reading till here,
Arpit





