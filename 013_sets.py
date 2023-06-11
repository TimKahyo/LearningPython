# a set is a list that is unordered
# only has unique values
# while values can change
# those values themselves
# must be immutable

first_set = set(["John", 1])
second_set = {"Paul", 1}

print("Length: ", len(second_set))

# union
third_set = first_set | second_set  # join sets
print(third_set)

third_set.add("Doug")
third_set.discard("John")

# remove random value
print("Random", third_set.pop())

#
third_set |= second_set

print(first_set.intersection(second_set))
print(first_set.symmetric_difference(second_set))
print(first_set.difference(second_set))

third_set.clear()

# frozen set # cant be change in any way
fourth_set = frozenset(["Paul", 7])
