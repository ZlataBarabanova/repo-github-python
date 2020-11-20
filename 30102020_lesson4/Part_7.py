from math import factorial
from itertools import count
def factor_val():
    for val in count(1):
        yield factorial(val)
n = 0
for i in factor_val():
    print("Factorial {} - {}".format(n + 1, i))
    if n == 14:
        break
    n += 1