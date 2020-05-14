from itertools import count
from sys import argv
script_name, number_begin, number_end = argv
def my_count(number_begin, number_end):
    for el in count(int(number_begin)):
        if el == int(number_end) + 1:
            break
        else:
            print(el)
    return
my_count(number_begin, number_end)
