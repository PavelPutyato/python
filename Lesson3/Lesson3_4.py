def my_func_1(x, y):
    return x**y

def my_func_2(x, y):
    resul = 1
    for _ in range(abs(y)):
        resul *= x
    if y < 0:
        resul_fin = 1 / resul
    else:
        resul_fin = resul
    return resul_fin

number_1 = int(input('Введите действительное положительное число X: '))
number_2 = int(input('Введите целое отрицательное число Y: '))

print(f'Решение первым способом : {number_1} в степрент {number_2} = {my_func_1(number_1, number_2)}')
print(f'Решение вторым способом : {number_1} в степрент {number_2} = {(lambda x, y : x ** y)(number_1, number_2)}')
print(f'Решение третьем способом : {number_1} в степрент {number_2} = {my_func_2(number_1, number_2)}')