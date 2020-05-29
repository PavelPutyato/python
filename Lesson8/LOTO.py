class LottoCard:
    def __init__(self, name):
        self.name = name
        self.matrix1 = []

    def matrix(self):
        from random import randint
        for y in range(3):
            self.matrix1.append([])
            tab = 1
            for x in range(9):
                t = randint(tab, tab + 9)
                if y == 0:
                    self.matrix1[y].append(t)
                    tab += 10
                    continue
                else:
                    # Если новое случайное число из второй и третьей строки совпадают с числом из
                    # первой или второй строки, то оно перегеннерируется.
                    while True:
                        if y == 1 and self.matrix1[0].count(t) == 0:
                            self.matrix1[y].append(t)
                            tab += 10
                            break
                        elif y == 1 and self.matrix1[0].count(t) != 0:
                            t = randint(tab, tab + 9)
                            continue
                        elif y == 2 and self.matrix1[0].count(t) == 0 and self.matrix1[1].count(t) == 0:
                            self.matrix1[y].append(t)
                            tab += 10
                            break
                        elif (y == 2 and self.matrix1[0].count(t) != 0) or (y == 2 and self.matrix1[1].count(t) != 0):
                            t = randint(tab, tab + 9)
                            continue
            # Случайным образом убираем лишние цифры из матрицы заменяя их ' '.
            num = 1
            while num < 5:
                tt = randint(0, 8)
                if self.matrix1[y][tt] == '  ':
                    continue
                self.matrix1[y][tt] = '  '
                num += 1
        return self.matrix1

    def __str__(self):
        self.matrix1 = LottoCard.matrix(self)
        # Переводим в строковую матрицу
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.matrix1])


class LottoGame:
    def __init__(self, human, computer):
        self.human = human
        self.human_1 = LottoCard('  Игрок  ').matrix()
        self.human_name = '------ Ваша карточка ------'
        self.computer = computer
        self.computer_1 = LottoCard('Компьютер').matrix()
        self.computer_name = '--- Карточка компьютера ---'
        self.numbers = []

    def gen_number(self):   # Метод генерит уникальное не повторяющееся число из диапазона 1-90
        from random import randint
        while True:
            number = randint(1, 90)
            if self.numbers.count(number) == 0:
                self.numbers.append(number)
                break
        return number, 90 - len(self.numbers)

    def check_matrix(self, human_computer, number):
        self.hum_com = human_computer
        self.number = number
        ll = 0
        self.sw1 = False
        for y in range(3):
            for x in range(9):
                if self.hum_com[y][x] == self.number:
                    self.sw1 = True
                    self.hum_com[y][x] = '--'
                if type(self.hum_com[y][x]) == int:
                    ll += 1
        if ll == 0:
            self.sw2 = True
        else:
            self.sw2 = False
        return self.hum_com, self.sw1, self.sw2

    def start(self):
        while True:
            self.number, self.balance = LottoGame.gen_number(self)
            print(f'Новый бочонок: {self.number} (осталось {self.balance})')
            self.human_str = '\n'.join([' '.join([str(elem) for elem in line]) for line in self.human_1])
            print(f'{self.human_name}\n{self.human_str}\n---------------------------')
            self.computer_str = '\n'.join([' '.join([str(elem) for elem in line]) for line in self.computer_1])
            print(f'{self.computer_name}\n{self.computer_str}\n---------------------------')
            self.computer_1, self.sw1, self.sw2 = LottoGame.check_matrix(self, self.computer_1, self.number)
            # self.sw1 - говорит что в карточке есть такая цифра и она зачеркнулась если True
            # self.sw2 - говорит что все цифры в карточке зачеркнуты если True
            if self.sw2 == True:
                print('КОМПЬЮТЕР ВЫИГРАЛ!!!')
                break

            while True:
                question = input('Зачеркнуть цифру? (y/n) :')
                if question != 'n' and question != 'N' and question != 'y' and question != 'Y':
                    print('Вы нажали на символ не соответствующий (y/n)!')
                    continue
                break

            self.human_1, self.sw1, self.sw2 = LottoGame.check_matrix(self, self.human_1, self.number)
            if (question == 'y' or question == 'Y') and self.sw1 == False:
                print('ВЫ ПРОИГРАЛИ!!!')
                break
            elif (question == 'y' or question == 'Y') and self.sw1 == True and self.sw2 == True:
                print('ВЫ ВЫИГРАЛИ!!!')
                break
            elif (question == 'n' or question == 'N') and self.sw1 == True:
                print('ВЫ ПРОИГРАЛИ!!!')
                break


human_player = LottoCard('  Игрок  ')
computer_player = LottoCard('Компьютер')
game = LottoGame(human_player, computer_player)
game.start()
