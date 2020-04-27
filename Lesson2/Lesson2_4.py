long_str = input('Введите слова разделенные пробелом: ')
line_str = long_str.split()
for ind, el in enumerate(line_str):
    a = len(el)
    if len(el) > 10:
        el = el[0:10]
    print(ind + 1, el)




