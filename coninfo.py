import json

class user:
    def __init__(self):
        self.userName = ''
        self.userPassword = ''
        self.encName = ''
        self.encPassword = ''
        self.encNameKey = ''
        self.encPasswordKey = ''
    def loaduser(self):
        loadfile = open('info.json', 'r')
        loadfile2 = json.load(loadfile)
        self.userName = loadfile2[username]
    def writeuser(self):
        writefile = open('info.json', 'w')
        jsonobject = json.dumps(self)
        writefile.write(jsonobject)




