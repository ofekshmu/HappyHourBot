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
        #cluster = MongoClient(f"mongodb://{user_name}:{password}@127.0.0.1:27017/dbname?keepAlive=true&poolSize=30&autoReconnect=true&socketTimeoutMS=360000&connectTimeoutMS=360000")
        cluster = MongoClient(f"mongodb+srv://{user_name}:{password}@cluster0.liy1wfj.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
        self.db = cluster["happy_hour"]
        self.section = self.db["section"]
        self.rounds = self.db["rounds"]

    def load_initial_db(self):
        dict = json.load(open('config.json'))
        self.section.insert_many([{k:v} for k, v in dict.items()])
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
        if self.section.count_documents({"_id": id}, limit=1):
            return False
        self.section.insert_one({"_id": id, "name": name, "mail": mail})
        return True

    def delete_user(self, name):
        pass

    def update_user(self, name, mail = None, phone = None):
        pass

    def insert_round(self, name_lst):
        """Insert a new, random, name list to the database

        Parameters
        ----------
        name_lst : List
            A randomly sorted list of names.
        """
        self.rounds({"date": datetime.now(), "queue": name_lst })

    def get_round(self, date):
        pass
        #self.rounds.find

    def get_recent_round(self):
        pass

mymongo = Mongo()
mymongo.load_initial_db()
