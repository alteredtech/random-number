"""Checks to see if number is prime"""

#!/usr/bin/env python3

import time
from rich.console import Console
from primePy import primes


def main():
    # Example usage

    # console = Console()
    # number = 10**100
    # with console.status("[bold green]Calculating...") as status:
    #     for i in range(number, 67, -1):
    #         status.update(f"Calculating... {i}")
    #         if primes.check(i):
    #             print(f"{i} is prime")
    #             print(f"perfect: {perfect_number(i)}")
    #         if i % 1000 == 0:
    #             time.sleep(1)
    print(perfect_number(6))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(int(n**0.5) + 1, 2, -1):
        print(i)
        if n % i == 0:
            return False
    return True


def perfect_number(n):
    sum = (2**n - 1) * (2**(n-1))
    return sum


if __name__ == "__main__":
    main()
