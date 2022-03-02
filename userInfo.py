from base64 import b64encode
import json
from cryptography.fernet import Fernet
import pickle
import sys
import time
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
            with open('userNames.pkl', 'rb') as data:
                self.userName = pickle.load(data)
            with open('userPasswords.pkl', 'rb') as data:
                self.userPassword = pickle.load(data)
            with open('userNamesKey.pkl', 'rb') as data:
                self.encNameKey = pickle.load(data)  
            with open('userPasswordsKey.pkl', 'rb') as data:
                self.encPasswordKey = pickle.load(data)
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
    def CheckUser(self, name, pwd):
        # Decrypting the data in the json files
        try:
            self.userNameCrypt = self.userName[name + " username"]
            self.encNameKey = self.encNameKey[name + " username key"]
            self.userName = self.encNameKey.decrypt(self.userNameCrypt).decode()
            self.userPasswordCrypt = self.userPassword[name + " password"]
            self.encPasswordKey = self.encPasswordKey[name + " password key"]
            self.userPassword = self.encPasswordKey.decrypt(self.userPasswordCrypt).decode()
        except:
            pass
        # End decryption of data in the json files   
        for i in range(5):
            if self.userName == name and self.userPassword == pwd:
                rightPassword = True
                break
            elif self.userName == name and self.userPassword != pwd:
                print("Sorry! You typed the wrong password. Try again.")
                rightPassword = False
                continue
            else:
                createUser = str.lower(str(input("Sorry! That user doesn't exist! Create a new user?\ny/n -->")))
                if createUser == 'y':
                    self.CreateUser(name, pwd)
                    rightPassword = True
                    break
                else:
                    rightPassword = False
                    notCreate = True
                    print("Okay. We won't save your details.")
                    break
        if rightPassword:
            return name, pwd
        elif notCreate:
            return name, pwd
        else:
            print("Sorry! Your password didn't match our database, so we'll have to exit.\nTry running the program again.")
            time.sleep(3)
            sys.exit()
    def CreateUser(self, name, pwd):
        # Encryption
        self.key = Fernet.generate_key()
        self.key2 = Fernet.generate_key()
        self.keyUser = Fernet(self.key)
        self.keyPwd = Fernet(self.key2)
        self.encName = self.keyUser.encrypt(name.encode())
        self.encPassword = self.keyPwd.encrypt(pwd.encode())
        # End encryption
        # Store in a dictionary
        self.userName = {f"{name} username": self.encName}
        self.userPassword = {f'{name} password': self.encPassword}
        self.encNameKey = {f'{name} username key': self.keyUser}
        self.encPasswordKey = {f'{name} password key': self.keyPwd}
        # End dictionary storage
        self.userName.update(self.ogUserName)
        self.userPassword.update(self.ogUserPassword)
        self.encNameKey.update(self.ogEncNameKey)
        self.encPasswordKey.update(self.ogEncPasswordKey)
        print(self.userName, self.userPassword, self.encNameKey, self.encPasswordKey)
        # Save to json files
        with open('userNames.pkl', 'wb') as data:
            pickle.dump(self.userName, data)
        with open('userPasswords.pkl', 'wb') as data:
            pickle.dump(self.userPassword, data)
        with open('userNamesKey.pkl', 'wb') as data:
            pickle.dump(self.encNameKey, data)
        with open('userPasswordsKey.pkl', 'wb') as data:
            pickle.dump(self.encPasswordKey, data)
        # End saving to json files
        return name, pwd
        # End loading json files into the program