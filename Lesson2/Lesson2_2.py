e_int = int(input('Введите длинну списка: '))
a_list = []
i = 0
while i < e_int:
    print('Введите ', i+1, '-й элемент списка: ', end='')
    a_list.append(input())
    i += 1
print('Начальный заданный список :', a_list)
if (e_int % 2) == 1:
    e_int -= 1
i = 0
while i < e_int:
    var_1 = a_list[i]
    var_2 = a_list[i+1]
    a_list[i], a_list[i+1] = var_2, var_1
    i += 2
print('Список после обмена значениями :', a_list)
