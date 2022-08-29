import pymongo
import certifi
from pymongo import MongoClient
import json

class Mongo:
    def __init__(self, Empty = False):
        f = open('credentials.json')
        dict = json.load(f)["Mongo Credentials"]
        password = dict["DBpassword"]
        user_name = dict["user_name"]
        ca = certifi.where()
        #cluster = MongoClient(f"mongodb://{user_name}:{password}@127.0.0.1:27017/dbname?keepAlive=true&poolSize=30&autoReconnect=true&socketTimeoutMS=360000&connectTimeoutMS=360000")
        cluster = MongoClient(f"mongodb+srv://{user_name}:{password}@cluster0.liy1wfj.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
        self.db = cluster["happy_hour"]
        self.collection = self.db["section"]


    def insert_user(self, name, mail):
        pass

    def delete_user(self, name):
        pass

    def update_user(self, name, mail = None, phone = None):
        pass

    def insert_round(self, name_lst):
        pass

    def get_round(self, date):
        pass

    def get_recent_round(self):
        pass
