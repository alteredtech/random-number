#!/usr/bin/env python3

import random
import inquirer

def main():
    end_value = inquirer.text(message="Input end value for random number")

    random_number = random.randint(1, int(end_value))

    print("Random number:", random_number)

if __name__ == "__main__":
    main()
    print("This is to see if command runs here2")