"""Checks to see if number is prime"""

#!/usr/bin/env python3 # noqa: E265


def main():
    """Main entry point"""

    print(perfect_number(6))


def is_prime(n):
    """Check if number is prime"""

    if n <= 1:
        return False
    for i in range(int(n**0.5) + 1, 2, -1):
        print(i)
        if n % i == 0:
            return False
    return True


def perfect_number(n):
    """Check if number is perfect"""

    total = (2**n - 1) * (2 ** (n - 1))
    return total


if __name__ == "__main__":
    main()
