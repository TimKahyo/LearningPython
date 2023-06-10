import sys

# There are several data types in python
# integers, floats, complex numbers, strings and booleans


# this will tell you the data type
print(type(10))
# maximum size of your data
print(sys.maxsize)
print(sys.float_info.max)

# float is only accurate up to the 15th digits
float_data = 1.1111111111111111
float_second_data = 1.1111111111111111
sum_data = float_data + float_second_data

print(sum_data)

# complex numbers are made of
# real part + imaginary part
example = 5 + 7j

# other data types
boolean_examples = False
string_example = "Escape sequences ' \" \t \\"
second_string_example = """Triple quoted string ' " """

# these are all variable converters
print("Cast", type(int(5.4)))
print("Cast", type(chr(5.4)))
print("Cast", type(str(58)))
print("Cast", type(ord("a")))
