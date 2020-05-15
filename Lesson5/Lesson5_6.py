dic = {}
try:
    with open('study.txt', 'r', encoding='utf-8') as f_line:
        for line in f_line:
            list_line = line.split()
            sum_time = 0
            for line2 in list_line:
                number_time = line2.split('(')
                if number_time[0].isdigit():
                    sum_time += int(number_time[0])
            dic.update({list_line[0][:-1]: sum_time})
        print(dic)
except FileNotFoundError:
    print('Файл не существует!')

