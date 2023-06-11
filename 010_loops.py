# while loop!
# you must define your index outside of the while loop

i = 1  # this value will change after you loop it
while i <= 5:
    print(i)
    i += 1

# add some space!
print("\n")

# more while loops!
# re-initialize the value of i
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        break
    else:
        i += 1
        continue
    i += 1

list = [1, 2, "John"]
while len(list):
    print(list.pop(0))

# for loop!
for x in range(0, 10):  # keep in mind that the range does not include 10!
    print(x, " ", end="")

another_list = [1, 2, "John"]
for x in another_list:
    print(x)

for x in [2, 4, 6]:
    print(x)

# iterators!
# this is kinda weird
new_list = [1, 2, 12, 13]

itr = iter(new_list)
print(next(itr))
print(next(itr))

# range!
print("range: \n")

# this one is error idk why
# print(list(range(0, 10, 2)))

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])
