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

    def getMail(self, name):
        """
        Given a name, return its Mail. returns error if doesnt exist.
        """
        if name in self.keva().keys():
            return self.keva()[name][0]
        if name in self.sadir().keys():
            return self.sadir()[name][0]

        raise KeyError("Name received in 'getMail' does not match data.")