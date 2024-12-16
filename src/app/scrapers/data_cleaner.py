from services.math_operations import MathOperations


class DataCleaner:
    """
    A utility class for cleaning and processing raw exchange data.
    """

    @staticmethod
    def clean_data(raw_data):
        """
        Extracts relevant data from raw exchange data and returns a list of dictionaries.

        Args:
            raw_data (dict): The raw data containing exchange information.

        Returns:
            list[dict]: A list of dictionaries with 'id', 'buy', and 'sell' keys.
        """
        cleaned_data = []
        for exchange in raw_data.get("Exchanges", []):
            try:
                cleaned_data.append({
                    "id": exchange["id"],
                    "buy": MathOperations.convert_to_integer(exchange["best_bids_price"]),
                    "sell": MathOperations.convert_to_integer(exchange["best_asks_price"]),
                })
            except KeyError as e:
                print(f"Missing key in exchange data: {e}")
            except ValueError as e:
                print(f"Invalid value in exchange data: {e}")
        return cleaned_data

    @staticmethod
    def remove_exchanges(data, ids_to_remove):
        """
        Removes exchanges from the cleaned data based on a list of IDs.

        Args:
            data (list[dict]): A list of dictionaries with exchange data.
            ids_to_remove (list[str]): A list of exchange IDs to remove.

        Returns:
            list[dict]: A filtered list of dictionaries with specified exchanges removed.
        """
        return [exchange for exchange in data if exchange["id"] not in ids_to_remove]

    @staticmethod
    def calculate_average_price(cleaned_data):
        """
        Calculates the mean (average) of the buy and sell prices from cleaned data.

        Args:
            cleaned_data (list[dict]): A list of dictionaries with 'buy' and 'sell' prices.

        Returns:
            float: The average price of all buy and sell prices combined.
        """
        total_price = 0
        count = 0

        for exchange in cleaned_data:
            try:
                total_price += exchange["buy"] + exchange["sell"]
                count += 2  # Adding two values (buy and sell)
            except KeyError as e:
                print(f"Missing key in exchange data: {e}")

        if count == 0:
            return 0  # Avoid division by zero

        return MathOperations.divide(total_price, count)
