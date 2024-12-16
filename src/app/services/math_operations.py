class MathOperations:
    """
    A collection of mathematical utility functions.
    """

    @staticmethod
    def calculate_average(numbers):
        """
        Calculates the average of a list of numbers.

        Args:
            numbers (list[float]): A list of numbers.

        Returns:
            float: The average of the numbers.
        Raises:
            ValueError: If the input list is empty.
        """
        if not numbers:
            raise ValueError("Cannot calculate average of an empty list.")
        return sum(numbers) / len(numbers)

    @staticmethod
    def convert_to_integer(number_str):
        """
        Converts a string representing a number with trailing zeros to an integer.

        Args:
            number_str (str): The input number as a string (e.g., "74213.0000000000").

        Returns:
            int: The number converted to an integer.
        Raises:
            ValueError: If the input is not a valid number string.
        """
        try:
            # Convert to float first to handle cases like "74213.0" correctly
            return int(float(number_str))
        except ValueError:
            raise ValueError(f"Invalid number string: {number_str}")
    

    def divide(numerator, denominator):
        """
        Safely divides two numbers and handles division by zero.

        Args:
            numerator (float): The numerator of the division.
            denominator (float): The denominator of the division.

        Returns:
            float: The result of the division. Returns 0 if the denominator is 0.
        """
        if denominator == 0:
            print("Warning: Division by zero. Returning 0.")
            return "0"
        result = numerator // denominator
        return f"{result:,}"
