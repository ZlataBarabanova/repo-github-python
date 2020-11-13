# Создать список + поменять местами элементы
my_list = list(input('Введите предложение ').split(" "))
length = len(my_list)
if length % 2 != 0:
    for el in range(0, length - 1, 2):
        temp = my_list[el]
        my_list[el] = my_list[el + 1]
        my_list[el + 1] = temp
    print(my_list)
else:
    for el in range(0, length, 2):
        temp = my_list[el]
        my_list[el] = my_list[el + 1]
        my_list[el + 1] = temp
    print(my_list)
