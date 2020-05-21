class Car:
    speed = 70
    color = 'Red'
    name = 'Mazda'
    is_police = True

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print('Машино повернула на', direction)

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч.')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости на {60 - self.speed} км/ч. Машина едет > 60 км/ч!')
        print(f'Текущая скорость автомобиля: {self.speed} км/ч.')


class SportCar(Car):
    def show_speed(self):
        if self.speed > 100:
            print(f'Превышение скорости на {100 - self.speed} км/ч. Машина едет > 100 км/ч!')
        print(f'Текущая скорость автомобиля: {self.speed} км/ч.')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости на {40 - self.speed} км/ч. Машина едет > 40 км/ч!')
        print(f'Текущая скорость автомобиля: {self.speed} км/ч.')


class PoliceCar(Car):
    def __init__(self):
        if Car.is_police:
            print('Вы нарушили и вас просит остановиться полиция!')
        else:
            print('Вы не нарушаете ПДД!')


a = Car()
a.go()
a.stop()
a.turn('право')
a.show_speed()
a = TownCar()
a.show_speed()
a = PoliceCar()
