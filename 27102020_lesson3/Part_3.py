var_1 = int(input('Введите первый аргумент '))
var_2 = int(input('Введите второй аргумент '))
var_3 = int(input('Введите третий аргумент '))
def my_func(var_1, var_2, var_3):
    my_dict = [var_1, var_2, var_3]
    my_dict.sort(reverse=True)
    return my_dict[0] + my_dict[1]
print(my_func(var_1, var_2, var_3))