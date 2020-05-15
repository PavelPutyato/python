from random import randint
numbers_rnd = open('numbers_rnd.txt', 'w', encoding='utf-8')
numbers = int(input('Введите колличество цифр: '))
number_max = int(input('Введите максимальное число: '))
i = 0
while i < numbers:
    numbers_rnd.writelines(str(randint(0, number_max + 1))+' ')
    i += 1
numbers_rnd.close()
# ---------------------------------------------------------------
numbers_rnd = open('numbers_rnd.txt', 'r', encoding='utf-8')
numbers_line = numbers_rnd.readline()
sum_n = 0
for i in numbers_line.split():
    sum_n += int(i)
print(f'Сумма всех чисел в файле = {sum_n}')
numbers_rnd.close()
