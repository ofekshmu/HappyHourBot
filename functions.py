import random
from datetime import datetime
from config import day

def random_lst_gen(n : int):
    """
    input: @n - a positive integer number
    output: a random sequence of numbers from 1 to n.
    """
    lst = list(range(n))
    rnd_lst = []
    for _ in range(n):
        i = random.randint(0,len(lst) - 1)
        rnd_lst.append(lst.pop(i))
    return rnd_lst

def isToday(d : day):
    if day.f