#any_text =[]
with open("text_part_1.txt", "w") as new_text:
    while True:
        line = input("Enter anything words... ")
        if line == '':
            break
        new_text.write(line + '\n')




