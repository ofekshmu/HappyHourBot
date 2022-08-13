from math import remainder
import random
from datetime import datetime
from .HappyApp import HappyApp
from config import day, _Team, MessageType

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

def isToday(d : day, time = None):
    if time == None:
        return datetime.today().weekday() == day.value
    else:
        return datetime.today().weekday() == day.value and \
            time == datetime.today().hour

def scramble(lst):
    rnd_lst = random_lst_gen(len(lst))
    return [x for _, x in sorted(zip(lst, rnd_lst), key=lambda pair: pair[1])]

def alert(data , msg_type : MessageType):
    
    if type(data) == tuple:
        createAlert(data[0], msg_type)
        createAlert(data[1], msg_type)
    else:
        createAlert(data, msg_type)    

def getNumber(name):
    """
    Receives a string and returns a phone number
    """
    return _Team[name]



def createAlert(data, msg_Type : MessageType):
    match msg_Type:
        case MessageType.reminder:
            sendAlert(message="",
                      number = getNumber(data))
        case MessageType.NewPeriod:
            for name in data:
                sendAlert(message="",
                          number = getNumber(name))

def sendAlert(message, number = None):
    pass