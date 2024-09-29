# combined_use_case.py
#!/usr/bin/env python3
import os
import sys


def combined_example():
    fruit = os.environ.get("FRUIT", "No fruit set")
    print(f"Environment FRUIT: {fruit}")

    if len(sys.argv) < 2:
        print("Usage: combined_use_case.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        print(f"You provided the number: {number}")
        print(f"Number multiplied by 2: {number * 2}")
    except ValueError:
        print("Error: Please provide a valid integer as an argument.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    combined_example()

# Usage:
# export FRUIT=Mango
# ./combined_use_case.py 5
# Output:
# Environment FRUIT: Mango
# You provided the number: 5
# Number multiplied by 2: 10
