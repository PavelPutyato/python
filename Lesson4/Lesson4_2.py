from random import randint
gen_len = int(input('Введите длинну генерируемого списка: '))
number_max = int(input(('Введите максимальное число в генерируемом списке: ')))
list_gen = []
for el in range(gen_len):
    list_gen.append(randint(0, number_max + 1))
print('Сгеренируемый список: ', list_gen)
new_list = []
previous = number_max + 1
for el in list_gen:
    if el > previous:
        new_list.append(el)
        previous = el
    previous = el
print('Список после фильтрации: ', new_list)