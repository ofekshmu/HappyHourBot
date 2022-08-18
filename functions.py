from math import remainder
from datetime import datetime
from typing import List
from .readJSON import Myjson
from config import day, MessageType
from mail import Mail


def isToday(d : day, time = None):
    """
    Input: @time - integer constant indicating an hour 0 - 23
           @d - day enum 
    Output: True if current time matches day and hour, else False.
    """
    if time == None:
        return datetime.today().weekday() == day.value
    else:
        return datetime.today().weekday() == day.value and \
            time == datetime.today().hour

def alert(data , msg_type : MessageType):
    """
    Input: @data - relevant data for send a message.
           @msg_type - message type enum
    Calls 'createalert' according to data
    """
    # Case where data is combined out of 2 different names (sadir soliders)
    if type(data) == tuple:
        createAlert(data[0], msg_type)
        createAlert(data[1], msg_type)
    else:
        createAlert(data, msg_type)    

def createAlert(mail : Mail, data, msg_Type : MessageType):
    """
    Create and send message according to the @msg_Type
    @mail - mail object for sending mail
    @data - a list of receivers, size 1 or max receivers in db
    """
    match msg_Type:
        case MessageType.reminder:
            mail.sendMail(receiver_email= Myjson.getMail(data),
                          message = reminderMsg(data))
        case MessageType.NewPeriod:
            for name in data:
                mail.sendMail(receiver_email= Myjson.getMail(name),
                              message = newPeriodMsg(data)) 

def reminderMsg(name):
    return f""" \
    היי {name}, זה אפק בוט!
    רק מזכיר שהגיע תורך להאכיל את מדור 14 ברביעי הקרוב.
    אז אל תשכח להתכונן מראש ולהכין את מה שצריך.
    ה happy hour קורה בשעה עשר ולא מוקדם מזה.

    הסנטדרד המדורי הוא
    - לחם
    - ממרחים
    - חלב
    - כריות
    - מאפים
    - גבנ"צ

    בברכה,
    אפק בוט
    """

def newPeriodMsg(names):
    wednesday = datetime.date.today()
    msg = f"""
    היי, זה אפק בוט!
    התחלנו סבב חדש ואלו השיבוצים:

    """
    for name in names:
        wednesday = wednesday + datetime.timedelta(days=7)
        msg += f"name: {wednesday}."
    
    msg = """
    \nאפק בוט לא תומך בשינויים כרגע.
    בברכה,
    אפק בוט
    """
    return msg