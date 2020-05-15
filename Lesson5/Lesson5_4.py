numbers_rus = ['Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
number_ru = open('number_ru.txt', 'w', encoding='utf-8')
try:
    with open('number_en.txt', 'r', encoding='utf-8') as f_line_en:
        for line in f_line_en:
            list_en = line.split()
            number_ru.writelines(numbers_rus[int(list_en[2])]+' - '+list_en[2]+'\n')
    number_ru.close()
except FileNotFoundError:
    print('Файл не существует!')
