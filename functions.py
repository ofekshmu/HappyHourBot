from math import remainder
import random
from datetime import datetime
from typing import List

from .readJSON import Myjson
from .HappyApp import HappyApp
from config import day, _Team, MessageType
from mail import Mail

def random_lst_gen(n : int):
    """
    input: n - a positive integer number
    output: a random sequence of numbers from 1 to n
            sequence has all unique numbers
    """
    lst = list(range(n))
    rnd_lst = []
    for _ in range(n):
        i = random.randint(0,len(lst) - 1)
        rnd_lst.append(lst.pop(i))
    return rnd_lst

def isToday(d : day, time = None):
    """
    Input: @time - integer constant indicating an hour 0 - 23
           @d - day enum 
    Output: True if current time matches day and hour, else False.
    """
    if time == None:
        return datetime.today().weekday() == day.value
    else:
        return datetime.today().weekday() == day.value and \
            time == datetime.today().hour

def scramble(lst : List):
    """
    Input: lst of strings
    Output: scrambled list according to indexes given by 'random_lst_gen'
    """
    rnd_lst = random_lst_gen(len(lst))
    return [x for _, x in sorted(zip(lst, rnd_lst), key=lambda pair: pair[1])]

def alert(data , msg_type : MessageType):
    """
    Input: @data - relevant data for send a message.
           @msg_type - message type enum
    Calls 'createalert' according to data
    """
    # Case where data is combined out of 2 different names (sadir soliders)
    if type(data) == tuple:
        createAlert(data[0], msg_type)
        createAlert(data[1], msg_type)
    else:
        createAlert(data, msg_type)    

def createAlert(mail : Mail, data, msg_Type : MessageType):
    """
    Create and send message according to the @msg_Type
    @mail - mail object for sending mail
    @data - a list of receivers, size 1 or max receivers in db
    """
    match msg_Type:
        case MessageType.reminder:
            mail.sendMail(receiver_email= Myjson.getMail(data),
                          message = "") # TODO add message
        case MessageType.NewPeriod:
            for name in data:
                mail.sendMail(receiver_email= Myjson.getMail(name),
                              message = "") # TODO add message
