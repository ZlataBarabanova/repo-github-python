with open('text_part_3.txt') as my_f:
    line_list ={}
    average = 0
    new_f = my_f.readlines()
    for line in new_f:
        element = line.split(' ')
        line_list[element[0]] = int(element[1])
    for key, value in line_list.items():
        if value < 20000:
            print(key)
        average += value
    print(f"average = {average / len(line_list)}")




