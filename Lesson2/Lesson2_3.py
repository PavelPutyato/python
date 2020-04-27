mount_n = int(input('Введите номер месяца от 1 до 12: '))
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
if mount_n == 12 or mount_n == 1 or mount_n == 2:
    print(f'Время года: {seasons_list[0]}')
elif mount_n == 3 or mount_n == 4 or mount_n == 5:
    print(f'Время года: {seasons_list[1]}')
elif mount_n == 6 or mount_n == 7 or mount_n == 8:
    print(f'Время года: {seasons_list[2]}')
elif mount_n == 9 or mount_n == 10 or mount_n == 11:
    print(f'Время года: {seasons_list[3]}')
else:
    print('Вы ввели несуществующий номер месяца!')
print('---------------------------')
seasons_dict = {12: 'Зима', 1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна',
                6: 'Лето', 7: 'Лето', 8: 'Лето',  9: 'Осень', 10: 'Осень', 11: 'Осень'}
try:
    print(f'Время года: {seasons_dict[mount_n]}')
except KeyError:
    print('Вы ввели несуществующий номер месяца!')



