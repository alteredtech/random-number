"""This is a basic random number multiplyer."""

#!/usr/bin/env python3 # noqa: E265

import random


def main():
    """Main entry point and does the math."""

    print(
        "Showing random number between 1-5 \
        multiplied by a random number between 1-5"
    )

    print(random.randrange(1, 5) * random.randrange(1, 5))


if __name__ == "__main__":
    main()

    print("This is to see if command runs here3")
