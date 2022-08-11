from enum import Enum

class status(Enum):
    sadir = 0
    keva = 1

class day(Enum):
    sunday = 6
    monday = 0
    tuesday = 1
    wednesday = 2
    tursday = 3
    friday = 4
    saturday = 5

_Team = {'ofek_shmuel' : ("0543238582", status.keva),
        'harel_finaly': ("temp", status.keva),
        'ofek_ofir': ("temp", status.keva),
        'raz_gino': ("temp", status.keva)}

# class team(Enum):
#     ofek_shmuel = ("0543238582", status.sadir)
#     harel_finaly = ("temp", status.keva)
#     # TODO: add all 


_Hour = 60*60
_8AM = 8
_8PM = 20
_1PM = 13