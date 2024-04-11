"""Get input from user to generate random number"""

#!/usr/bin/env python3 # noqa: E265

# pylint: disable=import-error
import random
from InquirerPy import inquirer

# pylint: enable=import-error


def main():
    """Get input from user to generate random number"""

    user_answer = inquirer.text(message="Enter a number:").execute()

    print(random.randint(1, int(user_answer)))

    result = multiply(user_answer)
    print(result)


def multiply(input_number: int) -> int:
    """
    Get input to generate random number

    Args:
        input_number (int): User input
    
    Returns:
        int: Random number
    """

    return random.randint(1, int(input_number)) * random.randint(1, 100)
