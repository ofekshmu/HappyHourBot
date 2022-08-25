from datetime import datetime
from time import sleep 
from config import MessageType, Hour, day, _1PM, _8AM, _9PM
from functions import isToday, alert
from queue import Queue
from readJSON import Myjson
from random import shuffle
from mail import Mail

class HappyApp:
    def __init__(self,):
        # For taking into account a sadir solider who was chosen to solo
        self.sadir_left_over = None
        self.db = Myjson()
        self.__roll()
        self.mail = Mail(local = True)

    def __roll(self):

        # Read names
        keva_names  = list(self.db.keva().keys())
        sadir_names = list(self.db.sadir().keys())

        # Remove from current round a sadir solider who soloed last round
        if self.sadir_left_over in sadir_names:
            sadir_names.remove(self.sadir_left_over)
            self.sadir_left_over = None

        shuffle(sadir_names)

        sadir_pairs = []
        for i in range(0, len(sadir_names) - 1, 2):
            sadir_pairs.append((sadir_names[i], sadir_names[i + 1]))
        
        if len(sadir_names) % 2 != 0:
            self.sadir_left_over = sadir_names[-1]
            sadir_pairs += sadir_names[-1]

        all_names = sadir_pairs + keva_names

        shuffle(all_names)
        self.queue = Queue(all_names)

    def __popQueue(self):
        self.queue.dequeue()
        if self.queue.isEmpty():
            self.__roll()
            alert(self.mail,
                  data=self.queue.getQueue(),
                  msg_type=MessageType.new_period)
        else:
            alert(self.mail,
                  data=self.queue.head(), 
                  msg_type=MessageType.reminder)

    def run(self, debug):
        while True:

            if isToday(day.saturday, _9PM):
                alert(self.queue.head(), MessageType.reminder)

            if isToday(day.tuesday, _8AM):
                alert(self.queue.head(), MessageType.reminder)

            print("TEST - before")
            self.mail.sendMail("ofek.shmuel1@gmail.com", "This will work now")
            print("TEST - after")
            sleep(Hour)

            if isToday(day.wednesday, _1PM):
                self.__popQueue()

