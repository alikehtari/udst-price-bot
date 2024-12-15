import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Console
        logging.FileHandler("crawler.log", mode="a", encoding="utf-8")  # File with UTF-8 encoding
    ]
)

logging.info("This should write to both the console and the log file.")
