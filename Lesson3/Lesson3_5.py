def func(arg1):
    number_sum = 0
    i = True
    for el in arg1:
        if el.isdigit():
            number_sum += int(el)
        elif el == 'q':
            i = False
    return number_sum, i

i = True
number_sum_fin = 0
list_l = []
while i:
    number = input('Введите числа разделенные пробелом (симвот [q] - выход):')
    list_l = number.split()
    number_sum, i = func(list_l)
    list_l.clear()
    number_sum_fin += number_sum
    print('Сумма введенных чисел = ', number_sum_fin)
print('Вы ввели символ [q] для выхода из цыкла.')
