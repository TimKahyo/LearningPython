# file_status_example.py
#!/usr/bin/env python3
import os
import sys


def check_file_status(filename):
    if os.path.exists(filename):
        print(f"The file '{filename}' exists.")
        sys.exit(0)
    else:
        print(f"Error: The file '{filename}' does not exist.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: file_status_example.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    check_file_status(filename)

# Usage:
# ./file_status_example.py example.txt
# If example.txt exists:
# Output: The file 'example.txt' exists.
# Exit code: 0
# If example.txt does not exist:
# Output: Error: The file 'example.txt' does not exist.
# Exit code: 1
