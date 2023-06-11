# contains mutable data
first_list = [1, 3.1, "hello", True]
print("Length of first list: ", len(first_list))
print("1st element of first list: ", first_list[0])
print("Last element of first list: ", first_list[-1])

# change the elements in the list
first_list[0] = 2
first_list[2:4] = ["Bob", False]
# insert at index without deleting
first_list[2:2] = ["Bob", 9]

second_list = first_list + ["Egg", 4]
second_list.remove("Bob")
second_list.pop(0)
print("Second list: ", second_list)

second_list = ["egg", 4] + first_list
third_list = [[1, 2], [3, 4]]
print("[1, 1]", third_list[1][1])

print("1 Exists ", (1 in first_list))
print("Min ", min([1, 2, 3]))
print("Max ", max([1, 2, 3]))

print("1dt 2", first_list[0:2])
print("Every Other ", first_list[0:-1:2])
print("Reverse", first_list[::-1])
