from datetime import datetime
from time import sleep 
from config import status,_Hour, day, _1PM, _8AM, _8PM
from functions import random_lst_gen, isToday, alert, scramble
from queue import Queue
class HappyApp:
    def __init__(self, team : dict):
        self.team = team
        self.roll()

    def roll(self):

        keva_names =  [k for k, v in self.team.items() if v[1] == status.keva]
        sadir_names = [k for k, v in self.team.items() if v[1] == status.sadir]

        sadir_names_rnd = scramble(sadir_names)

        sadir_pairs = [(sadir_names_rnd[i],
                       sadir_names_rnd[i+1])
                       for i in range(0, len(sadir_names_rnd) - 1, 2)]

        if len(sadir_names_rnd) % 2 != 0:
            sadir_pairs += sadir_names_rnd[-1]

        tot_names = sadir_pairs + keva_names

        self.queue = Queue(scramble(tot_names))


    def run(self):

        while True:

            if self.queue.isEmpty():
                self.roll()
                alert()

            if isToday(day.saturday, _8PM):
                alert() # add enum for alert code
            if isToday(day.tuesday, _8AM):
                alert() # add enum for alert code
            if isToday(day.wednesday, _1PM):
                alert() # add enum for alert code
                
            sleep(_Hour)
        

