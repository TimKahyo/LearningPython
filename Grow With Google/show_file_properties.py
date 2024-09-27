import os
import datetime

file_name = "dummy_text.txt"

file_size = os.path.getsize(file_name)
print(f"File size: {file_size} bytes")

file_timestamp = os.path.getmtime(file_name)
print("Last Modified: ", datetime.datetime.fromtimestamp(file_timestamp))

file_path = os.path.abspath(file_name)
print("File's absolute path: ", file_path)