from datetime import datetime
from time import sleep 
from config import MessageType, Hour, day, _1PM, _8AM, _9PM
from functions import isToday, scramble, alert
from queue import Queue
import readJSON
from random import shuffle
from mail import Mail

class HappyApp:
    def __init__(self,):
        # For taking into account a sadir solider who was chosen to solo
        self.sadirLeftOver = None
        self.__roll()
        self.mail = Mail()

    def __roll(self):

        # Read names
        keva_names  = list(readJSON().keva().keys())
        sadir_names = list(readJSON().sadir().keys())

        # Remove from current round a sadir solider who soloed last round
        if self.sadirLeftOver in sadir_names:
            sadir_names.remove(self.sadirLeftOver)
            self.sadirLeftOver = None

        shuffle(sadir_names)

        sadir_pairs = [(sadir_names[i],
                       sadir_names[i+1])
                       for i in range(0, len(sadir_names) - 1, 2)]

        if len(sadir_names) % 2 != 0:
            self.sadirLeftOver = sadir_names[-1]
            sadir_pairs += sadir_names[-1]

        tot_names = sadir_pairs + keva_names

        shuffle(tot_names)
        self.queue = Queue(tot_names)

    def __popQueue(self):
        self.queue.dequeue()
        if self.queue.isEmpty():
            self.__roll()
            alert(self.mail,
                  data=self.queue.getQueue(),
                  msg_type=MessageType.NewPeriod)
        else:
            alert(self.mail,
                  data=self.queue.head(), 
                  msg_type=MessageType.reminder)

    def run(self):

        while True:

            if isToday(day.saturday, _9PM):
                alert(self.queue.head(), MessageType.reminder)

            if isToday(day.tuesday, _8AM):
                alert(self.queue.head(), MessageType.reminder)

            sleep(Hour)

            if isToday(day.wednesday, _1PM):
                self.__popQueue()

