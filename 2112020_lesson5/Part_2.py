my_f = open("text_part_2.txt", "r")
for ind, line in enumerate(my_f, 1):
    print(ind, line, len(line.split()))
my_f.close()



