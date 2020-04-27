
revenue = int(input("Введите полученную выручку компании: "))
costs = int(input("Введите издержки компании: "))
if (revenue - costs) > 0:
    print('Компания в прибыли!')
    print('Рентабильность компании: ', round((revenue - costs) / revenue, 4))
    dig = int(input("Введите колличество сотрудников в компании: "))
    print('Прибыль компании в расчете на сотрудника :', round((revenue - costs) / dig, 4))
elif (revenue - costs) == 0:
    print('Компания работает в "0".')
else:
    print('Компания в убытке!')





