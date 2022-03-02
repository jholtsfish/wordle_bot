from base64 import b64encode
import json
from cryptography.fernet import Fernet
import pickle

class user:
    userName = None
    userPassword = None
    encName = None
    encPassword = None
    encNameKey = None
    encPasswordKey = None
    def __init__(self):
        try:
            # Loading json files into the program
            with open('userNames.json', 'rb') as data:
                self.userName = json.load(data)
            with open('userPasswords.json', 'rb') as data:
                self.userPassword = json.load(data)
            with open('userNamesKey.json', 'rb') as data:
                self.encNameKey = json.load(data)  
            with open('userPasswordsKey.json', 'rb') as data:
                self.encPasswordKey = json.load(data)
            self.ogUserName = self.userName
            self.ogUserPassword = self.userPassword
            self.ogEncNameKey = self.encNameKey
            self.ogEncPasswordKey = self.encPasswordKey   
        except FileNotFoundError:
            self.userName = {}
            self.userPassword = {}
            self.encNameKey = {}
            self.userPasswordKey = {}
            self.ogUserName = {}
            self.ogUserPassword = {}
            self.ogEncNameKey = {}
            self.ogEncPasswordKey = {}
            pass
        # End loading json files into the program
    def CheckUser(self, name, pwd):

        if name + " username" in self.userName and name + " password" in self.userPassword:
            # Decrypting the data in the json files
            self.userNameCrypt = self.userName[name + " username"]
            self.encNameKey = Fernet(bytes(self.encNameKey[name + " username key"], 'utf-8'))
            self.userName = self.encNameKey.decrypt(self.userNameCrypt).decode()
            self.userPasswordCrypt = self.userPassword[name + " password"]
            self.encPasswordKey = self.userPasswordKey[name + " password key"]
            self.userPassword = self.encPasswordKey.decrypt(self.userPasswordCrypt).decode()
            # End decryption of data in the json files        
            return name, pwd
        else:
            # Encryption
            self.key = Fernet.generate_key()
            self.key2 = Fernet.generate_key()
            self.keyUser = Fernet(self.key)
            self.keyPwd = Fernet(self.key2)
            self.encName = self.keyUser.encrypt(name.encode())
            self.encPassword = self.keyPwd.encrypt(pwd.encode())
            # End encryption
            # Store in a dictionary
            self.userName = {f"{name} username": str(self.encName)}
            self.userPassword = {f'{name} password': str(self.encPassword)}
            self.encNameKey = {f'{name} username key': str(self.keyUser)}
            self.encPasswordKey = {f'{name} password key': str(self.keyPwd)}
            # End dictionary storage
            self.userName.update(self.ogUserName)
            self.userPassword.update(self.ogUserPassword)
            self.encNameKey.update(self.ogEncNameKey)
            self.encPasswordKey.update(self.ogEncPasswordKey)
            print(self.userName, self.userPassword, self.encNameKey, self.encPasswordKey)
            # Save to json files
            with open('userNames.json', 'w') as data:
                json.dump(self.userName, data)
            with open('userPasswords.json', 'w') as data:
                json.dump(self.userPassword, data)
            with open('userNamesKey.json', 'w') as data:
                json.dump(self.encNameKey, data)
            with open('userPasswordsKey.json', 'w') as data:
                json.dump(self.encPasswordKey, data)
            # End saving to json files
            return name, pwd