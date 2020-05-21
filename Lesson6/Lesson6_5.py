class Stationery:
    title = 'Ручка'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки пишущей ручки.')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандаша.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки рукоятки')


a_class = Stationery()
a_class.draw()
a_class = Pen()
a_class.draw()
a_class = Pencil()
a_class.draw()
a_class = Handle()
a_class.draw()
print('Атрибут внутри класса:', a_class.title)
