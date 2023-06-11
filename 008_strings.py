import sys
import math
import random
import threading
import time
from functools import reduce

# raw string
print(r"I'll be ignored \n")
print("Hello " + "You")  # concatenation

# some more
stringExample = "Hello You"
print("Length: ", len(stringExample))
print("1st character: ", stringExample[0])
print("Last character: ", stringExample[-1])

# 1st 3 characters
print("1st 3", stringExample[0:3])
# Other characters
print("Every Other", stringExample[0:-1:2])

# replace
stringExample = stringExample.replace("Hello", "Goodbye")
print(stringExample)

# add y into the string
stringExample = stringExample[:8] + "y" + stringExample[9:]
print(stringExample)

# check if "you" are in stringExample
print("you" not in stringExample)

# find "you" at index
print("You index", stringExample.find("you"))

# trim blank spaces
print("   Hello   ".strip())

# separate words with spaces
print(" ".join(["Some", "words"]))

# delimiters
# split words and put it into list or commonly called an array,
# tho i think that python's list behave more like vector because it's dynamic
print("A string".split(" "))

# btw you can do this # python is mind blowing
int1 = int2 = 5
print(f"{int1} + {int2} = {int1 + int2}")

# convert to lower case
print("A string".lower())
# convert to upper case
print("A string".upper())

# checks if the string is a character or a number
print("AString123".isalnum())
print("AString".isalpha())
print("123".isdigit())
# all true!
