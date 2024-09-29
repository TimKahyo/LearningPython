# environment_example.py
#!/usr/bin/env python3
import os


def check_environment_variables():
    home_dir = os.environ.get("HOME", "Not Set")
    user_shell = os.environ.get("SHELL", "Not Set")
    favorite_fruit = os.environ.get("FRUIT", "Not Set")

    print(f"HOME Directory: {home_dir}")
    print(f"SHELL: {user_shell}")
    print(f"Favorite Fruit: {favorite_fruit}")


if __name__ == "__main__":
    check_environment_variables()

# Usage:
# export FRUIT=Apple
# ./environment_example.py
# Output:
# HOME Directory: /home/username
# SHELL: /bin/bash
# Favorite Fruit: Apple
