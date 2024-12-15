import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TelegramService:

    def __init__(self):
        self.bot_token = os.getenv("BOT_TOKEN")
        self.channel_id = os.getenv("CHANNEL_ID")
        
        # Validate environment variables
        if not self.bot_token or not self.channel_id:
            raise ValueError("BOT_TOKEN or CHANNEL_ID is not set in the environment variables")

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.channel_id}&text={message}"
        try:
            # Send GET request
            r = requests.get(url)
            r.raise_for_status()  # Raise an exception for HTTP errors
            
        except requests.exceptions.RequestException as e:
            print(f"Failed to send message: {e}")
