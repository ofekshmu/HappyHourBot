from enum import Enum

class status(Enum):
    sadir = 0
    keva = 1

class day(Enum):
    sunday = 0
    monday = 1
    tuesday = 2
    wednesday = 3
    tursday = 4
    friday = 5
    saturday = 6

_Team = {'ofek_shmuel' : ("0543238582", status.keva),
        'harel_finaly': ("temp", status.keva),
        'ofek_ofir': ("temp", status.keva),
        'raz_gino': ("temp", status.keva)}

# class team(Enum):
#     ofek_shmuel = ("0543238582", status.sadir)
#     harel_finaly = ("temp", status.keva)
#     # TODO: add all 


_Hour = 60*60