from enum import Enum

class day(Enum):
    sunday = 6
    monday = 0
    tuesday = 1
    wednesday = 2
    tursday = 3
    friday = 4
    saturday = 5

class MessageType(Enum):
    reminder = 0
    NewPeriod = 1


_Hour = 60*60
_8AM = 8
_8PM = 20
_1PM = 13