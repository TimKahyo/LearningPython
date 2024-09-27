import os

# Print the current working directory
print(os.getcwd())

# Create a "website" directory and change into it
os.mkdir("website")
os.chdir("./website")

# Create a subdirectory called "new_dir"
new_dir = "new_dir"
os.mkdir(new_dir)

# Print the current working directory again
print(os.getcwd())

# Create and remove another subdirectory called "newer_dir"
newer_dir = "newer_dir"
os.mkdir(newer_dir)
os.rmdir(newer_dir)

# List all items in the current directory
print(os.listdir(os.getcwd()))

# Now iterate over the items in the current directory (./website) and check if they are directories
for name in os.listdir("."):  # Use the current directory (".") instead of "website"
    fullname = os.path.join(os.getcwd(), name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))