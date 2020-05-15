try:
    my_file = open('zarplata.txt', 'r', encoding='utf-8')
    i = 0
    content_full = []
    while True:
        content = my_file.readline()
        if not content:
            my_file.close()
            break
        elif float(content.split()[1]) < 20000:
            print(f'Сотрудник: {content.split()[0]} имеет зарплату {content.split()[1]} и она меньше 20000.')
        content_full.append(float(content.split()[1]))
        i += 1
    print(f'Средняя величина дохода {i} сотрудников = {round(sum(content_full) / i, 2)}')
except FileNotFoundError:
    print('Файл не существует!')
