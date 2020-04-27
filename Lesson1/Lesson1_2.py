second = int(input('Введите общее колличество секунд: '))
clock = second // 3600
minut_sum = second - (clock * 3600)
minut = minut_sum // 60
sec = minut_sum - (minut * 60)
if len(str(clock)) < 2:
      clock = '0' + str(clock)
if len(str(minut)) != 2:
      minut = '0' + str(minut)
if len(str(second)) != 2:
      second = '0' + str(second)
print('Общее количество секунд:', second)
print(f'Время: {clock}:{minut}:{sec}')

