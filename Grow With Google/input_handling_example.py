# input_handling_example.py
#!/usr/bin/env python3


def evaluate_user_input():
    user_input = input("Enter a mathematical expression (e.g., 5 + 5): ")
    try:
        result = eval(user_input)
        print(f"Result of the evaluated expression: {result}")
    except (SyntaxError, NameError):
        print("Invalid expression. Please enter a valid mathematical expression.")


if __name__ == "__main__":
    evaluate_user_input()

# Usage:
# ./input_handling_example.py
# Enter a mathematical expression (e.g., 5 + 5): 3 * (4 + 5)
# Output:
# Result of the evaluated expression: 27
