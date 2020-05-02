def int_func(text_arg):
    text_title = text_arg.title()
    return text_title

text_full = str()
text_lower = input('Введите слова через пробел строчными буквами: ')
list_lower = text_lower.split()
for i in range(len(list_lower)):
    text_full = text_full + int_func(list_lower[i]) + ' '
print('Введенные слова с заглавными буквами: ', text_full)

