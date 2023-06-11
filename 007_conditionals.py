import sys
import math
import random
import threading
import time
from functools import reduce

age = 21

# conditionals
if age > 21:
    print("You can drink")
elif age < 21:
    print("You can't drink")
else:
    print("You can't drink")

# and or not
if age < 5:
    print("You should stay home")
elif age >= 5 and age <= 6:
    print("You should go to the kindergarten")
elif age > 6 and age <= 17:
    print("Grade %d", age - 5)
else:
    print("College")

# ternary operator
# condition_true if condition else condition_false
canVote = True if age >= 18 else False
print(canVote)
