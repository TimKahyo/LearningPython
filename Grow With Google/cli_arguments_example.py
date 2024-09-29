# cli_arguments_example.py
#!/usr/bin/env python3
import sys


def process_arguments(args):
    if len(args) < 2:
        print("Usage: cli_arguments_example.py <arg1> <arg2> ...")
        sys.exit(1)
    for index, arg in enumerate(args):
        print(f"Argument {index}: {arg}")


if __name__ == "__main__":
    process_arguments(sys.argv)

# Usage:
# ./cli_arguments_example.py Hello World Python
# Output:
# Argument 0: ./cli_arguments_example.py
# Argument 1: Hello
# Argument 2: World
# Argument 3: Python
