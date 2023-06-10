import sys
import math
import random
import threading
import time
from functools import reduce

# this is line separator
# will output 12/21/1974
print(12, 21, 1974, sep="/")

# no new line
print("No new line: ", end="")

# string formatting
# %d is integer, %f is float, %s is string, %c is for char
print("\n%04d %s %.2f %c" % (1, "Derek", 1.234, "A"))
