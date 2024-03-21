"""Get input from user to perform math"""

#!/usr/bin/env python3 # noqa: E265

# pylint: disable=import-error
import random
import sys
from InquirerPy import inquirer

sys.path.insert(0, '../../../random-number/src/')
import classes.math as math  # noqa: E402
# pylint: enable=import-error


def main():
    """Get input from user"""

    user_answer = int(inquirer.text(message="Enter a number:").execute())
    operator = math.Math(user_answer, user_answer)

    print(operator.multiply())

    multiply(user_answer)


def multiply(input_number):
    """Get input to generate random number"""

    print(random.randint(1, int(input_number)) * random.randint(1, 100))
