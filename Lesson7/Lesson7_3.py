class Cell:
    def __init__(self, cell_numbers):
        self.cell_numbers = cell_numbers

    def __add__(self, other):
        return self.cell_numbers + other.cell_numbers

    def __sub__(self, other):
        return self.cell_numbers - other.cell_numbers

    def __mul__(self, other):
        return self.cell_numbers * other.cell_numbers

    def __truediv__(self, other):
        return self.cell_numbers // other.cell_numbers

    def make_order(self, numbers, row):
        my_str = str()
        for i in range(numbers // row):
            my_str += '*' * row + '\n'
        my_str += '*' * (numbers - (numbers // row) * row)
        return my_str


a = Cell(20)
b = Cell(10)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(12, 5))
print(a.make_order(15, 5))




"""
from random import randint


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])
        self.matrix_str = str()
        for y in range(self.rows):
            for x in range(self.columns):
                self.matrix_str += (str(self.matrix[y][x])+' ')
            self.matrix_str += '\n'
        return f'Матрица с параметрами ( строк: {self.rows} , столбцов: {self.columns} )\n{self.matrix_str}'

    def __add__(self, other):
        self.matrix_sum = str()
        for y in range(self.rows):
            for x in range(self.columns):
                self.matrix_sum += (str(self.matrix[y][x] + other.matrix[y][x])+' ')
            self.matrix_sum += '\n'
        return f'Сумма двух матриц:\n{self.matrix_sum}'


rows = int(input('Введите колличество строк в матрце: '))
columns = int(input('Введите колличество столбцов в матрце: '))
matrix_1 = Matrix([[randint(-100, 100) for _ in range(columns)] for _ in range(rows)])
print(matrix_1.matrix)
print(matrix_1)
matrix_2 = Matrix([[randint(-100, 100) for _ in range(columns)] for _ in range(rows)])
print(matrix_2)
print(matrix_1 + matrix_2)

"""