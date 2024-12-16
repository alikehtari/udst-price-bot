import logging
import os
import time
from dotenv import load_dotenv
from numpy import average
from services.telegram_service import TelegramService
from services.message_generator import MessageGenerator
from scrapers.data_cleaner import DataCleaner
from scrapers.cloudscraper_service import CloudscraperService

# Load environment variables
load_dotenv()

# Configure logging
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "crawler.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE_PATH, mode="a", encoding="utf-8")
    ]
)

# Get interval from environment variables (default to 5 minutes)
try:
    INTERVAL_SECONDS = int(os.getenv("RUN_INTERVAL_SECONDS", 300))
except ValueError:
    logging.warning("Invalid CRAWLER_INTERVAL_SECONDS in .env, defaulting to 300 seconds")
    INTERVAL_SECONDS = 300

def main():
    """
    Main logic for fetching, processing, and sending messages.
    """
    crawler = CloudscraperService()
    telegram = TelegramService()

    try:
        # Step 1: Fetch and clean data
        raw_data = crawler.get_raw_data()

        cleaned_data = DataCleaner.clean_data(raw_data)
        cleaned_data = DataCleaner.remove_exchanges(cleaned_data, ['jibitex'])

        # Step 2: Generate message
        message = MessageGenerator.generate_message(cleaned_data)
        average_price = DataCleaner.calculate_average_price(cleaned_data)

        # Step 3: Send message to Telegram
        telegram.send_message(message)
        telegram.send_message(f"قیمت لحظه ای تتر : {average_price}")

    except Exception as e:
        logging.error("An error occurred during execution", exc_info=True)

if __name__ == "__main__":
    logging.info("Script initialized")
    while True:
        main()
        time.sleep(INTERVAL_SECONDS)
