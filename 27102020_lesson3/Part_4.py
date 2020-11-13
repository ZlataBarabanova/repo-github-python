x = float(input('Введите положительное число '))
y = int(input('Введите отрицательное число '))

# Первый способ решения задачи:
def my_func(x, y):
    return x ** y
print(my_func(x, y))

# Второй способ решения задачи:
def my_second_func(x, y):
    num = 1
    result = x
    while num != abs(y):
        num+=1
        result *= x
    return (1 / result)
print(my_second_func(x, y))