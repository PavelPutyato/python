a_int = 34
b_float = 76.45
c_str = 'Привет всем!'
d_bool = True
k_sum = a_int + b_float
e_int = int(input('Введите целое число: '))
f_float = float(input("Введите дробное число: "))
l_sum = e_int + f_float
dog_name = input('Введите кличку вашей собаки: ')
dog_age = int(input('Сколько лет вашей собаки: '))
print(c_str, 'и это: ', d_bool)
print('Числа занесенные в переменные: '
      'Целое число: ', a_int, ', дробное число:', b_float, 'и их сумма =', round(k_sum, 2))
print('Введенные числа: '
      'Целое число: ', e_int, ', дробное число:', f_float, 'и их сумма =', round(l_sum, 4))
print(f'Кличка вашей собаки: {dog_name} и ей {dog_age} лет.')
