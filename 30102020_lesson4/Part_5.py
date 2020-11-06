from functools import reduce
def my_func(el1, el2):
    return el1 * el2
my_list = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(my_func, my_list))
