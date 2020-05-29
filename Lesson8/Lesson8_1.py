class Data:
    def __init__(self, dey_month_year):
        self.dey_month_year = dey_month_year

    @classmethod
    def dey_month_year_number(cls, txt):
        dey_str, month_str, year_str = txt.split('-')
        dey, month, year = int(dey_str), int(month_str), int(year_str)
        return print(cls, dey, month, year)

    @staticmethod
    def month_validation(txt):
        _, month_str, _ = txt.split('-')
        if 0 < int(month_str) < 13:
            return print('Заданный месяц валидный.')
        else:
            return print('Заданный месяц НЕ валидный.')


Data.dey_month_year_number('10-12-1973')
Data.month_validation('10-12-1973')
Data.month_validation('10-14-1973')