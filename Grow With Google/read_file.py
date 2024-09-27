def read_file(filename):
    # Reading the whole file
    with open(filename, 'r') as file:
        content = file.read()
        print("Read entire file:")
        print(content)

    # Reading the file line by line
    with open(filename, 'r') as file:
        print("\nReading file line by line:")
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())

    # Reading all lines into a list
    with open(filename, 'r') as file:
        lines = file.readlines()
        print("\nReading all lines into a list:")
        for i, line in enumerate(lines):
            print(f"Line {i + 1}: {line.strip()}")

if __name__ == "__main__":
    read_file("dummy_text.txt")