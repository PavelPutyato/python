my_file = open('text1.txt', 'w')
while True:
    my_str = input('Введите строку: ')
    if my_str == '':
        print('Файл заполнен.')
        my_file.close()
        break
    my_file.write(my_str + '\n')


