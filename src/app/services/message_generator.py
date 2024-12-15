class MessageGenerator:
    @staticmethod
    def generate_message(exchange_data):
        """
        Generates a formatted message from the list of dictionaries.

        :param exchange_data: List of dictionaries containing exchange data
                              Each dictionary must have keys: 'id', 'sell', 'buy'
        :return: A formatted string
        """
        if not exchange_data:
            return "No data available."

        # Create the message lines
        lines = []
        for exchange in exchange_data:
            id = exchange.get('id', 'N/A')
            sell = exchange.get('sell', 'N/A')
            buy = exchange.get('buy', 'N/A')

            lines.append(f"Exchange: {id}\nSell: {sell}\nBuy: {buy}\n")

        # Combine all lines into a single message
        return "\n".join(lines)
