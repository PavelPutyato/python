try:
    my_file = open('text.txt', 'r')
    i = 1
    while True:
        content = my_file.readline().split()
        if not content:
            my_file.close()
            break
        print(f'Колличество слов в {i}-ой строке = {len(content)}')
        i += 1
except FileNotFoundError:
    print('Файл не существует!')
