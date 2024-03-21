"""Large number random script."""

#!/usr/bin/env python3 # noqa: E265

import random


def main():
    """Prints a random number between a small number and large number."""

    end_value = 545

    random_number = random.randint(1, int(end_value))

    print("Random number:", random_number)


if __name__ == "__main__":
    main()

    print("This is to see if command runs here2")
