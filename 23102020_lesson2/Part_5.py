# "Рейтинг"
el = int(input('Введите значение рейтинга '))
my_list = [7, 5, 3, 3, 2]
my_list.append(el)
my_list.sort(reverse=True)
print(my_list)