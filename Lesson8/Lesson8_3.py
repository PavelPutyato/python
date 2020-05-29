class ListNumbers(Exception):
    def __str__(self):
        return f'Вы ввели не число!'


my_list = []
while True:
    try:
        my_list.append(input('Введите числитель: '))
        if my_list[-1] == 'stop':
            my_list.pop(-1)
            print(my_list)
            break
        elif not(my_list[-1].isdigit()):
            my_list.pop(-1)
            raise ListNumbers()
    except ListNumbers as err:
        print(err)
    print(my_list)
