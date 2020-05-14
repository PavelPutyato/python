from functools import reduce
list_gen = [el for el in range(100, 1001, 2)]
print('Сгеренируемый список: ', list_gen)
result = reduce(lambda arg1, arg2: arg1 * arg2, list_gen)
print('Результат после умножения всех чисел в списке = ', result)
