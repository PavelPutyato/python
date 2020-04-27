my_dict = dict()
my_list = list()
dict_t = dict()
n = int(input('Веедите количество наименований товара (по заданию их 3): '))
i = 1
while i <= n:
    print('Введите название ', i, '-ого товара: ', end='')
    product_name = input()
    my_dict.update({"название": product_name})
    print('Введите цену ', i, '-ого товара: ', end='')
    product_cost = int(input())
    my_dict.update({"цена": product_cost})
    print('Введите колличество ', i, '-ого товара: ', end='')
    product_quantity = int(input())
    my_dict.update({"количество": product_quantity})
    print('Введите единицу измерения ', i, '-ого товара: ', end='')
    product_unit = input()
    my_dict.update({"ед": product_unit})
    my_list.append((i, my_dict.copy()))
    i += 1
    print('------------------------------------------------')
print('--- Не отфильтрованный список ---')
print(my_list)
list_1 = list()
list_2 = list()
list_3 = list()
list_4 = list()
i = 0
while i < n:
    dict_t = my_list[i][1]
    list_1.append(dict_t.get("название"))
    list_2.append((dict_t.get("цена")))
    list_3.append(dict_t.get("количество"))
    list_4.append(dict_t.get("ед"))
    i += 1
dict_filter = {"название": list_1, "цена": list_2, "количество": list_3, "ед": list(set(list_4))}
print('--- Отфильтрованный список ---')
print(dict_filter)
