import json

firm_dict = {}
average_profit = []
with open('text_part_7.txt') as f:
    lines = f.readlines()
    for line in lines:
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firm_dict[name] = profit
        if profit > 0:
            average_profit.append(profit)

average_profit = sum(average_profit) / len(average_profit)
out_info = [firm_dict, {'avarege_profit': average_profit}]

with open('text_part_7.json', 'w') as f_json:
    json.dump(out_info, f_json)
    
with open('text_part_7.json') as f_json:
    print(json.load(f_json))