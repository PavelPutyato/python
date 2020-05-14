from itertools import cycle
from sys import argv
script_name, my_list, number_repeat = argv
def my_cycle(my_list, number_repeat):
    c = 0
    for el in cycle(my_list):
        if c == int(number_repeat):
            break
        print(el)
        c += 1
    return

my_cycle(my_list, number_repeat)
