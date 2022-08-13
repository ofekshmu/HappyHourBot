from datetime import datetime
from time import sleep 
from config import MessageType, status,_Hour, day, _1PM, _8AM, _8PM
from functions import isToday, scramble, alert
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

    def popQueue(self):
        self.queue.dequeue()
        if self.queue.isEmpty():
            self.roll()
            alert(data=self.queue.getQueue(),
                  msg_type=MessageType.NewPeriod)
        else:
            alert(data=self.queue.head(), 
                  msg_type=MessageType.reminder)

    def run(self):

        while True:

            if isToday(day.saturday, _8PM):
                alert(self.queue.head(), MessageType.reminder)

            if isToday(day.tuesday, _8AM):
                alert(self.queue.head(), MessageType.reminder)

            if isToday(day.wednesday, _1PM):
                self.popQueue()

