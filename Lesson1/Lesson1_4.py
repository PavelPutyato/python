n1 = int(input("Введите целое число: "))
n2 = 0
while n1 > 0:
    digit = n1 % 10
    if digit > n2:
        n2 = digit
    n1 = n1 // 10
print('Самое большое число:', n2)
