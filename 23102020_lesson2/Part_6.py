# "Товары"
count = 1
my_super_list = []
while count != 4:
    print(f"Введите информацию о {count} товаре")
    name = input("Введите название ")
    price = int(input("Введите цену "))
    quantity = int(input("Введите количество "))
    unit = input("Введите единицу ")
    my_tuple = (count, {"название": name, "цена": price, "количество": quantity, "ед.": unit})
    my_super_list.append(my_tuple)
    count += 1

products = {}
name = []
price = []
quantity = []
unit = []
for item in my_super_list:
    print(item)
    for key, value in item[1].items():
        if(key == "название"):
            name.append(item[1][key])
        if (key == "цена"):
            price.append(item[1][key])
        if (key == "количество"):
            quantity.append(item[1][key])
        if (key == "ед."):
            unit.append(item[1][key])

products["название"] = name
products["цена"] = price
products["количество"] = quantity
products["ед."] = unit

print(products, end="\n")



