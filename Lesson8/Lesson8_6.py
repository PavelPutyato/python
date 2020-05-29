class Warehouse:
    def __init__(self, number, quantity_s):
        self.characteristics_printer = [Printer().voltage, Printer().logo, Printer().quality]
        self.characteristics_scanner = [Scanner().voltage, Scanner().logo, Scanner().resolution]
        self.characteristics_copier = [Copier().voltage, Copier().logo, Copier().speed]
        self.characteristics_list = [self.characteristics_printer, self.characteristics_scanner,
                                     self.characteristics_copier]
        self.storage = {}
        self.names = [Printer().name, Scanner().name, Copier().name]
        self.storage.update({self.names[number - 1]: quantity_s})

    def __str__(self):
        return f'Словарь для хранения данных: {self.storage}'


class Department:
    def __init__(self, *department_list):
        self.department_list = list(department_list)

    def departments(self):
        return f'Список департаментов: {self.department_list}'


class OfficeEquipment:
    def __init__(self):
        self.voltage = 220
        self.logo = 'HP'

    def __str__(self):
        return f'Напряжение в сети: {self.voltage}, лого фирмы: {self.logo}'


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.quality = 5
        self.name = 'Printer'


class Scanner(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.resolution = 1400
        self.name = 'Scanner'

    def __str__(self):
        return f'Напряжение в сети: {self.voltage}, колличество фаз: {self.logo}, ' \
               f'качество сканирование: {self.resolution}'


class Copier(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.speed = 40
        self.name = 'Copier'


d = Department('technical', 'salesman', 'accounting', 'development')
print(d.departments())
scan = Scanner()
print(scan)

try:
    numb = int(input('Введите номер товара из списка (1-Printer, 2-Scanner, 3-Copier):'))
    if numb == 1 or numb == 2 or numb == 3:
        quantity = int(input('Введите количество единиц данного товара: '))
        a = Warehouse(numb, quantity)
        print(f'Данные по характеристикам выбранного товара: {a.characteristics_list[numb - 1]}')
        print(a)

except ValueError:
    print('Вы ввели не число!')
