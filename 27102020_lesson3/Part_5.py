def sum_number(str):
    e = ''
    sum = 0
    symbol = '~'
    while e != '~':
        str = input('Введите строку чисел, разделенных пробелом. Для выхода использовать ~ ').split()
        for el in str:
            if el != symbol:
               sum += int(el)
            else:
                e = el
    return sum
print(sum_number(str))
