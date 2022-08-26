from datetime import datetime
from time import sleep 
from config import MessageType, Hour, day, _1PM, _8AM, _9PM
from functions import Msg
from myQueue import MyQueue
from readJSON import Myjson
from random import shuffle
from mail import Mail
#import keyboard

class HappyApp:
    def __init__(self, debug):

        # debug tools
        self.debug = debug
        self.curr_day = 3
        self.curr_hour = 0

        # For taking into account a sadir solider who was chosen to solo
        self.sadir_left_over = None
        self.db = Myjson()
        self.queue = MyQueue()
        self.mail = Mail(local = debug)

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
            sadir_pairs.append(sadir_names[-1])

        all_names = sadir_pairs + keva_names

        shuffle(all_names)
        self.queue = MyQueue(all_names)

    def __popQueue(self):
        if self.queue.isEmpty():
            self.__roll()
            Msg.alert(self.mail,
                  data=self.queue.getQueue(),
                  msg_type=MessageType.new_period)
        else:
            self.queue.dequeue()
            Msg.alert(self.mail,
                  data=self.queue.head(), 
                  msg_type=MessageType.reminder)

    def __debugTime(self, time_period = 1):
        self.curr_hour = (self.curr_hour + 1) % 24  
        if self.curr_hour == 0:
            self.curr_day = (self.curr_day + 1) % 7 
        sleep(time_period)
        return f"Today is: {self.curr_day}, Hour: {self.curr_hour}."

    def run(self):
        while True:

            if Msg.isToday(day.wednesday, _1PM,
                           debug_time = (self.curr_day, self.curr_hour),
                           debug = self.debug ):
                if self.debug: 
                    print(f"Its now: Wednesday 1Pm")
                self.__popQueue()

            if Msg.isToday(day.saturday, _9PM, 
                           debug_time = (self.curr_day, self.curr_hour),
                           debug = self.debug ):
                if self.debug: 
                    print(f"Its now: Saturday 9PM")
                Msg.alert(self.mail, self.queue.head(), MessageType.reminder)

            if Msg.isToday(day.tuesday, _8AM,
                           debug_time = (self.curr_day, self.curr_hour),
                           debug = self.debug ):
                if self.debug: 
                    print(f"Its now: Tuesday 8PM")
                Msg.alert(self.mail, self.queue.head(), MessageType.reminder)


            if not self.debug:
                sleep(Hour)
            else:
                print(self.__debugTime(0.001))




