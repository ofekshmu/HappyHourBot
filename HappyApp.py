from datetime import datetime 
from config import status
from functions import random_lst_gen
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
        print(keva_sorted)

    def run(self):
        
        
