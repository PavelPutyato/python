class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self):
        self.voltage = 220
        self.phase = 1


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.quality = 5


class Scanner(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.resolution = 1400


class Copier(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.speed = 40


