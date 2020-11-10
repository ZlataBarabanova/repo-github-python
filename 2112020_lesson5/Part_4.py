my_f = open('text_part_4.txt', 'r')
new_f = open('text_part_4_2.txt', 'w+')
for line in my_f:
    if '1' in line:
        line = line.replace('One', 'Один')
    elif '2' in line:
        line = line.replace('Two', 'Два')
    elif '3' in line:
        line = line.replace('Three', 'Три')
    elif '4' in line:
        line = line.replace('Four', 'Четыре')
    print(line)
    new_f.write(line)
new_f.close()
my_f.close()