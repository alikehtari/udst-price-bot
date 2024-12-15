import os
import json
import cloudscraper
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class CloudscraperService:
    """
    A service for scraping data using Cloudscraper.
    """
    def __init__(self):
        self.base_url = os.getenv("MIHANBLOCKCHAIN_URL")
        self.scraper = cloudscraper.create_scraper()

    def get_nonce(self):
        """
        Fetches the 'nonce' value from the base URL's script data.

        Returns:
            str: The nonce value if found.
        Raises:
            ValueError: If nonce is not found in the response.
        """
        response = self.scraper.get(self.base_url)
        if response.status_code != 200:
            raise ConnectionError(f"Failed to fetch page: {response.status_code}")

        # Extract the JavaScript object containing the nonce
        text = response.text
        start = text.find("var mihanObj =")
        if start == -1:
            raise ValueError("mihanObj not found in the response.")

        start += len("var mihanObj =")
        end = text.find("};", start) + 1  # Find the end of the object
        json_data = text[start:end]

        # Parse the JSON data
        try:
            mihan_obj = json.loads(json_data)
            return mihan_obj.get("Nonce", None)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse mihanObj JSON: {e}")

    def get_raw_data(self, coin="usdt"):
        """
        Fetches the raw data using the coin type.

        Args:
            coin (str): The coin type (default is 'usdt').

        Returns:
            dict: Parsed JSON response from the second URL.
        Raises:
            ValueError: If response data is invalid.
        """
        # Automatically fetch nonce
        nonce = self.get_nonce()
        if not nonce:
            raise ValueError("Failed to fetch nonce. Cannot proceed.")

        url = f"https://mihanblockchain.com/wp-admin/admin-ajax.php?action=ajax_get_best_exchanges_orders&nonce={nonce}&coin={coin}"
        response = self.scraper.get(url)
        if response.status_code != 200:
            raise ConnectionError(f"Failed to fetch raw data: {response.status_code}")

        # Parse the JSON response
        try:
            return response.json()
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON response: {e}")
