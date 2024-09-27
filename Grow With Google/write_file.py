def write_file(filename):
    # Writing to the file with 'w' mode (overwrite)
    with open(filename, 'w') as file:
        file.write("This will overwrite the entire file.\n")
        file.write("Only these two lines will be in the file.\n")

    # Appending to the file with 'a' mode
    with open(filename, 'a') as file:
        file.write("This line is added to the existing content.\n")
        file.write("Another appended line.\n")

    # Writing multiple lines
    with open(filename, 'a') as file:
        lines_to_add = [
            "Adding one more line.\n",
            "And yet another line.\n"
        ]
        file.writelines(lines_to_add)

    print(f"Data written to {filename} successfully.")

if __name__ == "__main__":
    write_file("dummy_text.txt")