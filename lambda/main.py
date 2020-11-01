from functools import reduce


def double(x):
    return x * 2


def add(x, y):
    return x + y


def product(x, y, z):
    return x * y * z


print(double(2))
print(add(2, 4))
print(product(2, 4, 6))

# ---------lambda function---------
my_list1 = [2, 3, 9, 7, 6, 4, 5, 2, 8, 3]
my_list2 = [5, 7, 5, 3, 1, 9, 5, 4, 7, 1]

double_map = map(lambda x: x * 2, my_list1)
print(list(double_map))

add_map = map(lambda x, y: x + y, my_list1, my_list2)
print(list(add_map))

even_filter = filter(lambda x: x % 2 == 0, my_list1)
print(list(even_filter))

greater_filter = filter(lambda x: True if x >= 5 else False, my_list1)
print(list(greater_filter))

add_reduce = reduce(lambda x, y: x + y, my_list1)
print(add_reduce)
# ---------lambda function---------
