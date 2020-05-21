class Worker:
    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        print(f'Полное имя сотрудника: {full_name}')

    def get_total_income(self):
        full_income = self._income.get("wage") + self._income.get("bonus")
        print(f'Полный доход сотрудника составляет: {full_income} рублей.')


pos = Position('Вася', 'Пупкин', 'Менеджер', 60000, 10000)
pos.get_full_name()
pos.get_total_income()
