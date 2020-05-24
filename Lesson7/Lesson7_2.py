from abc import ABC, abstractmethod


class Decor(ABC):

    @abstractmethod
    def __init__(self, type_clothes, size_height):
        self._type_clothes = type_clothes

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def type_clothes(self):
        pass


class Clothes(Decor):
    def __init__(self, type_clothes, size_height):
        self._type_clothes = type_clothes
        self._size_height = size_height

    def __str__(self):
        if self._type_clothes == 'пальто':
            self._full = self._size_height / 6.5 + 0.5
        elif self._type_clothes == 'костюм':
            self._full = 2 * self._size_height + 0.3
        return f'Расход ткани для изготовления {self._type_clothes} = {round(self._full, 2)} м.' \
            if self._type_clothes == 'пальто' or self._type_clothes == 'костюм' \
            else 'Вы ввели не верный тип одежды!'

    @property
    def type_clothes(self):
        return self._type_clothes


a = Clothes('пальто', 34)
print(a)
a = Clothes('костюм', 4)
print(a)
a = Clothes('рубашка', 42)
print(a)
# Проверка работы декоратора @property
print(a.type_clothes)

