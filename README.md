# Cryptocurrency Price Crawler

This project is a USDT price (in iranian Tomans) crawler that fetches live exchange data from a MihanExchange website sends the results as a message via Telegram.

## Features
- Scrapes cryptocurrency exchange data from a specified URL.
- Cleans and processes the data to display relevant information such as "Buy" and "Sell" prices.
- Removes unwanted exchanges based on user-defined criteria.
- Sends a summary of the processed data to a Telegram channel at a set interval.

## Requirements
- Python 3.x
- `requests` library
- `cloudscraper` library
- `python-dotenv` library
- `logging` library
- Telegram bot token and channel ID

## Installation

1. Clone the repository:

   
   git clone https://github.com/alikehtari/udst-price-bot
Navigate to the project folder:


cd cryptocurrency-price-crawler
Create and activate a virtual environment (optional but recommended):




pip install -r requirements.txt
Create a .env file in the project root directory with the following contents:


BOT_TOKEN=your-telegram-bot-token
CHANNEL_ID=your-telegram-channel-id
MIHANBLOCKCHAIN_URL=https://mihanblockchain.com/exchange-prices/#usdt
SCRAPE_INTERVAL=300  # Set interval in seconds (e.g., 300 seconds = 5 minutes)
Replace your-telegram-bot-token and your-telegram-channel-id with your actual Telegram bot token and channel ID.

Usage
Run the crawler:


python main.py
This will:

Scrape the exchange data every 5 minutes (or whatever interval you set in .env).
Clean and process the data.
Send the message to your Telegram channel.
To change the frequency of data scraping, update the SCRAPE_INTERVAL variable in the .env file. The value is in seconds (e.g., 300 for 5 minutes, 600 for 10 minutes).

Logs:

Logs will be stored in the crawler.log file.
The logs contain information about scraping status, errors, and any issues encountered during the process.

Example Message Format
The messages sent to your Telegram channel will look something like this:

Exchange: excoino
Sell: 7400
Buy: 74500

Exchange: mellichange
Sell: 7420
Buy: 74200

Ensure that the .env file is correctly configured with the Telegram bot token, channel ID, and the URL.
Check the crawler.log file for any errors or issues that occur during scraping or message sending.