import json
from cryptography.fernet import Fernet
from encKey import key
key = key()

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
            with open('userNames.json') as data:
                self.userName = json.load(data)
            with open('userPasswords.json') as data:
                self.userPassword = json.load(data)
        except FileNotFoundError:
            self.userName = {}
            self.userPassword = {}
            pass
        except json.JSONDecodeError:
            self.userName = {}
            self.userPassword = {}
            pass
        # End loading json files into the program
    def CheckUser(self, userName, userPassword):
        if userName + " username" in self.userName and userName + " password" in self.userPassword:
            # Decrypting the data in the json files
            self.userNameCrypt = self.userName[userName + " username"]
            self.userNameKey = key.encNameKey[userName + " username key"]
            self.userName = key.encNameKey.decrypt(self.userNameCrypt).decode()
            self.userPasswordCrypt = self.userPassword[userName + " password"]
            self.userPasswordKey = key.encPasswordKey[userName + " password key"]
            self.userPassword = key.encPasswordKey.decrypt(self.userPasswordCrypt).decode()
            # End decryption of data in the json files
            return self.userName, self.userPassword
        else:
            # Encryption
            self.key = Fernet.generate_key()
            self.key2 = Fernet.generate_key()
            self.keyUser = Fernet(self.key)
            self.keyPwd = Fernet(self.key2)
            self.encName = self.keyUser.encrypt(userName.encode())
            self.encPassword = self.keyPwd.encrypt(userPassword.encode())
            # End encryption
            # Store in a dictionary
            self.userName = {f"{userName} username": str(self.encName)}
            self.userPassword = {f'{userName} password': str(self.encPassword)}
            self.encNameKey = {f'{userName} username key': str(self.keyUser)}
            self.encPasswordKey = {f'{userName} password key': str(self.keyPwd)}
            # End dictionary storage
            # Save to json files
            with open('userNames.json', 'w') as data:
                json.dump(self.userName, data, indent=4, ensure_ascii = False)
            with open('userPasswords.json', 'w') as data:
                json.dump(self.userPassword, data, indent=4, ensure_ascii = False)
            # End saving to json files
            # Saving to the key.py file
            key.AppendUserKey(self.encNameKey)
            key.AppendPasswordKey(self.encPasswordKey)
            # End saving to the key.py file
            return self.userName, self.userPassword