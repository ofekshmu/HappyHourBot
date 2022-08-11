from datetime import datetime
from time import sleep 
from config import status,_Hour, day
from functions import random_lst_gen, isToday, alert
class HappyApp:
    def __init__(self, team : dict):
        self.team = team

        keva = {k:v[0] for k, v in team.items() \
                                if v[1] == status.keva}
        sadir = {k:v[0] for k, v in team.items() \
                                if v[1] == status.sadir}

        rnd_dict = dict(zip(list(keva.keys()),
                            random_lst_gen(len(keva)))
                        )
        keva_sorted = {k: v for k, v in sorted(rnd_dict.items(), key=lambda item: item[1])}

        rnd_dict = dict(zip(list(sadir.keys()),
                            random_lst_gen(len(sadir)))
                        )
        sadir_sorted = {k: v for k, v in sorted(rnd_dict.items(), key=lambda item: item[1])}

    def run(self):

        while True:
            
            if isToday(day.saturday):
                alert() # add enum for alert code
            if isToday(day.tuesday):
                alert() # add enum for alert code
                
            sleep(_Hour)
        

