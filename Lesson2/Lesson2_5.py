my_list = [7, 5, 3, 3, 2]
while True:
    b_numb = int(input('Введите натуральное число: '))
    i = 0
    while i < len(my_list):
        if b_numb > my_list[i]:
            my_list.insert(i, b_numb)
            break
        else:
            i += 1
            if i == len(my_list):
                my_list.append(b_numb)
                break
    k_str = ', '.join(map(str, my_list))
    print(f'Пользователь ввел число {b_numb}. Результат: {k_str}.')



