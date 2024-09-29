# streams_use_case.py
#!/usr/bin/env python3


def get_user_input():
    data = input("Enter a number to add 10 to it: ")
    try:
        result = int(data) + 10
        print(f"Result after adding 10: {result}")
    except ValueError:
        print("Invalid input, please enter a valid number.", file=sys.stderr)


if __name__ == "__main__":
    get_user_input()

# Usage:
# Run the script and provide user input.
# Example:
# ./streams_use_case.py
# Enter a number to add 10 to it: 5
# Output: Result after adding 10: 15
