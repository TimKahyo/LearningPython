import os
import dummy_file_generator as dfg

try:
    dfg.create_dummy_file("novel.txt")
except:
    print("Error when creating the file.")
else:
    print("The file was created successfully.")
    
    
print()

try:
    os.remove("novel.txt")
except:
    print("Error when removing the file")
else:
    print("The file was successfully removed.")

if os.path.exists("novel.txt"):
    print("novel.txt exist")
else:
    print("novel.txt might have already been removed")
  
print()

file_name: str = "test_file.txt"
try:
    dfg.create_dummy_file(file_name)
except:
    print("Error when creating the file.")
else:
    print(f"The {file_name} was created successfully.")
    
try:
    os.rename(file_name, "renamed_test_file.txt")
except:
    print("Error when renaming the file.")
else:
    print("The file was successfully renamed.")
    
    


