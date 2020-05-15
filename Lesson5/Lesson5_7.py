import json
dic = {}
i = 0
profit_n = 0
try:
    with open('company.txt', 'r', encoding='utf-8') as f_line:
        for line in f_line:
            list_line = line.split()
            profit = int(list_line[len(list_line)-2]) - int(list_line[len(list_line)-1])
            firm = ' '.join(list_line[:-3])
            print(f'Прибыль компании {firm} состовляет: {profit}')
            dic.update({firm: profit})
            if profit > 0:
                profit_n += profit
                i += 1
        if i == 0:
            print(f'Все {i} компаний убыточные!')
        print(f'Средня прибыль от прибыльных {i} компаний составляет: {round(profit_n / i, 2)}')
        list_dic = [dic, {'average_profit': round(profit_n / i, 2)}]
        print(list_dic)
    with open('company.jon', 'w', encoding='utf-8') as f_json:
        json.dump(list_dic, f_json)
except FileNotFoundError:
    print('Файл не существует!')

