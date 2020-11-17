var_1 = float(input('Укажите первое число '))
var_2 = float(input('Укажите второе число '))
def first_funch(var_1, var_2):
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        return("Деление на ноль")

print(first_funch(var_1, var_2))