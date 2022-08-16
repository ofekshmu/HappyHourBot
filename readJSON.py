import json

class Myjson:
    def __init__(self):
        self.readConfig()
    
    def readConfig(self):
       
        f = open('config.json')
        self.data = json.load(f)
        f.close()
    
    def madorInfo(self):
        return self.data["Mador"]

    def credentials(self):
        dict = self.data["Credentials"]
        return dict['port'], \
               dict['sender email'], \
               dict['password']
    
    def keva(self):
        return self.data['Mador']['Keva']

    def sadir(self):
        return self.data['Mador']['Sadir']