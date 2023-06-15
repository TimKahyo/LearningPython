from functools import reduce

one_to_four = range(1, 5)
times_two = lambda x: x * 2
print(list(map(times_two, one_to_four)))

print(list(filter(lambda x: x %  2 == 0, range(1, 11))))

print(reduce((lambda x, y: x + y), range(1, 6)))

