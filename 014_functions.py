# functions!
def get_sum(a, b):
    return a + b


print(get_sum(1, 2))


# if you dont know how many values you're gonna get
# just use *args
# remember to put it last
# ex: get_sum(a, b, *args)
def get_sum_2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(get_sum_2(1, 2, 3, 4, 5))


# get both values
def next_2(nums):
    return num + 1, num + 2


ret_1, ret_2 = next_2(5)
print(ret_1, ret_2)


# create a function that returns a function
def mult_by(num):
    return lambda x: x * num


print(" 3 * 5 =", (mult_by(3)(5)))


# pass a function to a function
def mult_list(list, func):
    for x in list:
        print(func(x))


mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)

# you can create a list of function
power_list = [lambda x: x**2, lambda x: x**3]
