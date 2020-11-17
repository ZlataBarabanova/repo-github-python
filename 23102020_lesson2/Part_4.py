# Вывод слов в столбец + нумерация
# element = input('Введите одно предложение ')

my_str = (input('Введите одно предложение '))
my_list = (my_str.split())
for ind, el in enumerate(my_list, 1):
   print(ind, el[0:10])