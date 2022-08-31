from datetime import datetime,date,timedelta
from typing import List
from readJSON import Myjson
from config import day, MessageType
from mail import Mail

class Msg:

    @staticmethod
    def isToday(d : day, time, debug_time, debug):
        """
        Input: @time - integer constant indicating an hour 0 - 23
            @d - day enum 
        Output: True if current time matches day and hour, else False.
        """
        if debug:
            offset = 1
            return d.value + offset == debug_time[0] and \
                time == debug_time[1]
        else:
            return datetime.today().weekday() == d.value and \
                time == datetime.today().hour

    @staticmethod
    def alert(mail : Mail, data , msg_type : MessageType):
        """
        Input: @data - relevant data for send a message.
            @msg_type - message type enum
        Calls 'create_alert' according to data
        """
        # Case where data is combined out of 2 different names (sadir soliders)
        if type(data) == tuple:
            create_alert(mail, data[0], msg_type)
            create_alert(mail, data[1], msg_type)
        else:
            create_alert(mail, data, msg_type)    

def create_alert(mail : Mail, data, msg_Type : MessageType):
    """
    Create and send message according to the @msg_Type
    @mail - mail object for sending mail
    @data - a list of receivers, size 1 or max receivers in db
    """
    match msg_Type:
        case MessageType.reminder:
            mail.sendMail(receiver_email= Myjson().getMail(data),
                        message = reminderMsg(data))
        case MessageType.new_period:
            recv = []
            for e in data:
                if type(e) == tuple:
                    recv.append(e[0])
                    recv.append(e[1])
                else:
                    recv.append(e)
            recv = [Myjson().getMail(name) for name in recv]
            mail.sendMail(receiver_email= recv,
                          message = newPeriodMsg(data)) 

def newPeriodMsg(names):
    wednesday = date.today()
    msg = f"""
    Hi! Its Afek Bot
    A new Round of HH has started, These are the results:\n\n"""
    for name in names:
        wednesday = wednesday + timedelta(days=7)
        msg += f"    {name} -> {wednesday}\n"
    
    msg += """
    Currently, I do not support Changes, So dont mess up.
    """
    return msg


def reminderMsg(name):
    return f"""\
    Hi {name} ! Its Afek bot
    Just reminding you that its your time to feed the 14 Section this week,
    So dont forget to prepare ahead of time and get all that is needed.
    Your Due daye is WednesDay ??/??/???? At 10 AM

    Our Section Standard is:
    - Bread
    - Yellow Cheese
    - Milk
    - Spreads such as Pesto/garlic/Tapenad
    - Baked Goods

    Every thing is welcomed.

    Yours,
    Afek Bot
    """