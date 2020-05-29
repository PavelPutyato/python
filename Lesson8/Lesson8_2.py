class DivisionByZero(Exception):
    def __str__(self):
        return f'Вы ввели знаменатель = 0'


try:
    numerator = int(input('Введите числитель: '))
    denominator = int(input('Введите знаменатель: '))
    if denominator == 0:
        raise DivisionByZero
    r = numerator / denominator
except ValueError:
    print("Вы ввели не число")
except DivisionByZero as error:
    print(error)

else:
    result = numerator / denominator
    print(f'Ваш результат: {numerator} / {denominator} = {round(result, 2)}')
