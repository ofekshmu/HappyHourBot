from email.policy import default
from xml.dom import NotFoundErr
import certifi
from pymongo import MongoClient
import json
from datetime import datetime

from readJSON import Myjson

class Mongo:
    def __init__(self):
        f = open('credentials.json')
        dict = json.load(f)["Mongo Credentials"]
        password = dict["DBpassword"]
        user_name = dict["user_name"]
        ca = certifi.where()
        cluster = MongoClient(f"mongodb+srv://{user_name}:{password}@cluster0.liy1wfj.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
        self.db = cluster["happy_hour"]


    def load_initial_db(self):
        dict = json.load(open('config.json'))
        self.db['section'].insert_many([{k:v} for k, v in dict.items()])
        print("Completed 'load_initial_db'...")

    def insert_user(self, id, name, mail):
        """Get user info and inserts to database

        Parameters
        ----------
        id : int
            a unique id to represent the user
        name : str
            the user's name
        mail : str
            the user's mail
        """
        # check if id is unique
        if self.db['section'].count_documents({"_id": id}, limit=1):
            return False
        self.db['section'].insert_one({"_id": id, "name": name, "mail": mail})
        return True

    def get_users(self, type):
        """Returns entire user data according to type parameter
        for 'all' -> returns 2 dictionaries; keva and sadir
        for 'sadir'/'keva' -> returns a dictionay 
         Parameters
        ----------
        type : str
            indicate what type of users to return - 'sadir' or 'keva'
            values allowed are 'sadir'/'keva'/'all'
        """
        match type:
            case 'all':
                return self.db['section']
            case 'sadir':
                return self.db['section']['Sadir']
            case 'keva':
                return self.db['section']['Keva']
            case other:
                raise ValueError(f"O-Error: Wrong input argument ({type}) in get_users\n\
                                  Should be 'sadir'/'keva'/'all'")

    def insert_round(self, name_lst):
        """Insert a new, random, name list to the database

        Parameters
        ----------
        name_lst : List
            A randomly sorted list of names.
        """
        self.db['rounds'].insert_one({"_id": datetime.now(), "queue": name_lst })
        return True

    def get_round(self, date):
        """ get a specific round upon a given date
        
        Parameters
        ----------
        date : datetime
            a date of format ??????
            the date should fit the start date of the relevant round
        """
        
        if self.db['rounds'].count_documents(date, limit=1):
            return self.db['rounds'].find_one(date)
        else:
            raise KeyError(f"O-Error: the date {date} is not found in data 'section'.")

    def get_recent_round(self):
        """
        """
        if self.db['rounds'].count_documents({}, limit=1):
            answer = self.db['rounds'].find().sort("_id",-1).limit(1)
            for x in answer:
                return x
        else:
            raise NotFoundErr(f"O-Error: No rounds in data base.")
