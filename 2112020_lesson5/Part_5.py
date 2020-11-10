with open('text_part_5.txt', 'w') as new_f:
    line = input('Enter number ')
    new_f.write(line + '\n')
    line = map(int, line.split())
    print(f"Amount numbers =  {sum(line)}")

