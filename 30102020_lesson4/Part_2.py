my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i - 1] and i != 0]
print(new_list)