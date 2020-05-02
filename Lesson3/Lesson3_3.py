def my_func(arg_1, arg_2, arg_3):
    if arg_1 <= arg_2 and arg_1 <= arg_3:
        result_sum = arg_2 + arg_3
    elif arg_2 <= arg_1 and arg_2 <= arg_3:
        result_sum = arg_1 + arg_3
    else:
        result_sum = arg_1 + arg_2
    return result_sum

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))

print(f'Сумма двух наибольших чисел = {my_func(number_1, number_2, number_3)}')
