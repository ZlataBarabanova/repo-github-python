from itertools import count, cycle
el = 0
for i in count(int(input('Enter start number: '))):
   # if el >= 10:
   #      break
    print(i)
    # el += 1

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
iter = cycle(my_list)
stop = ''
while stop !='q':
    print(next(iter), end = '')
    stop = input()