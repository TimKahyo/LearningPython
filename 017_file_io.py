# save and read data directly from a file

with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("This is a test file")
    
with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.read())
    
print(my_file.closed)
