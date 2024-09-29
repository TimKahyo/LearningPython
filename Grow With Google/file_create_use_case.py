# file_create_use_case.py
#!/usr/bin/env python3
import os
import sys


def create_or_update_file(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("This is a new file created.\n")
            print(f"File '{filename}' successfully created.")
    else:
        with open(filename, "a") as f:
            f.write("Additional content added.\n")
            print(f"File '{filename}' already exists. Content added.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: file_create_use_case.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    create_or_update_file(filename)

# Usage:
# ./file_create_use_case.py example.txt
# Output:
# File 'example.txt' successfully created.
#
# Run again:
# ./file_create_use_case.py example.txt
# Output:
# File 'example.txt' already exists. Content added.
