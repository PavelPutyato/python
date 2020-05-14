from random import randint
gen_len = int(input('Введите длинну генерируемого спимка: '))
number_max = int(input(('Введите максимальное число в генерируемом списке: ')))
list_gen = [randint(0, number_max + 1) for el in range(gen_len)]
print('Сгеренируемый список: ', list_gen)
new_list = []
[new_list.append(list_gen[el]) for el in range(0, gen_len) if list_gen.count(list_gen[el]) == 1]
print('Список после фильтрации: ', new_list)
