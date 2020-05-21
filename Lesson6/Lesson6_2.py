class Road:
    def __init__(self, length, width, thickness=1):
        self._length = length
        self._width = width
        self._thickness = thickness
    def weight(self):
        return self._length * self._width * 25 * self._thickness / 1000

mt = Road(5000, 20, 5)
print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {mt.weight()} тон.')
