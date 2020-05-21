class TrafficLight:
    from itertools import cycle
    __colors = cycle(['Красный', 'Желтый', 'Зеленый'])
    def __running(self):
        from time import sleep
        for color in TrafficLight.__colors:
            print(color)
            sleep(7) if color == 'Красный' else sleep(2) if color == 'Желтый' else sleep(8)

mt = TrafficLight()
mt._TrafficLight__running()
