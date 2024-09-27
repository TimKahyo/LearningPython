def create_dummy_file(filename):
    with open(filename, 'w') as file:
        file.write("This is the first line of the dummy text.\n")
        file.write("Here is the second line.\n")
        file.write("The third line is here.\n")
        file.write("This is the fourth line.\n")
        file.write("Finally, this is the fifth line.\n")

if __name__ == "__main__":
    create_dummy_file("dummy_text.txt")
    print("Dummy file created successfully.")