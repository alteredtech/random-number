"""Script to show random number between 1-5."""

#!/usr/bin/env python3

import random


def main():
    """Shows a random number"""

    print("Showing random number between 1-5")

    print(random.randrange(1, 5))


if __name__ == "__main__":
    main()

    print("This is to see if command runs here")
