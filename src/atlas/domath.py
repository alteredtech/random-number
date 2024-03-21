"""Get input from user to perform math"""

#!/usr/bin/env python3 # noqa: E265

# pylint: disable=import-error
import random
import classes.math as maths
from InquirerPy import inquirer

# pylint: enable=import-error


def main():
    """Get input from user"""

    user_answer = inquirer.text(message="Enter a number:").execute()
    operator = maths.Math(user_answer, user_answer)

    print(operator.multiply())

    multiply(user_answer)


def multiply(input_number):
    """Get input to generate random number"""

    print(random.randint(1, int(input_number)) * random.randint(1, 100))
