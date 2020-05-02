def division(arg_1, arg_2):
    try:
        result_division = arg_1 / arg_2
    except ZeroDivisionError:
        return '"нельзя делить на 0 !!!"'
    return round(result_division, 2)

numerator = int(input('Введите числитель: '))
denominator = int(input('Введите знаменатель: '))
print(f'{numerator} / {denominator} = {division(numerator, denominator)}')
