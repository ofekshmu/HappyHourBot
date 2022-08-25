import json
from shutil import ReadError

class Myjson:
    def __init__(self):
        self.readConfig()
        self.readCreds()
    
    def readConfig(self):
        try:
            f = open('config.json')
            self.data = json.load(f)
            f.close()
        except:
            raise ReadError("Error while trying to load config.json")    
    def readCreds(self):
        try:
            f = open('credentials.json')
            self.cred = json.load(f)["Credentials"]
            f.close()
        except:
            raise ReadError("Error while trying to load credentials.json")    


    def madorInfo(self):
        return self.data["Mador"]

    def credentials(self):
        return self.cred['port'], \
               self.cred['sender email'], \
               self.cred['password']
    
    def keva(self):
        return self.data['Mador']['Keva']

    def sadir(self):
        return self.data['Mador']['Sadir']

    def getMail(self, name):
        """
        Given a name, return its Mail. returns error if doesnt exist.
        """
        if name in self.keva().keys():
            return self.keva()[name][0]
        if name in self.sadir().keys():
            return self.sadir()[name][0]

        raise KeyError("Name received in 'getMail' does not match data.")