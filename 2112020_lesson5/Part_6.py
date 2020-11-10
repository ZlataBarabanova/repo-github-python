my_dict = {}
with open("text_part_6.txt") as new_f:
    my_f = new_f.readlines()
    for line in my_f:
        element_line = line.split()
        lesson = element_line[0]
        sum_lessons = sum([int(x[:x.find('(')]) for x in element_line[1:] if '(' in x])
        my_dict[lesson[:-1]] = sum_lessons
print(my_dict)
        