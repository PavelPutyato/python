def fact(number_n):
    for el in range(1, number_n + 1):
        yield el
number_n = int(input('Введите число n: '))
factorial = 1
print(f'Факториал числа {number_n}! = ', end='')
for el in fact(number_n):
    print(el, '* ', end='')
    factorial *= el
print('\b' * 2, '= ', factorial)



