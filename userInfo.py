# Import Fernet for encryption
from cryptography.fernet import Fernet
# End import

# Import needed libraries
import pickle, sys, time, json
# End import

from coninfo import user

newdict = {'username': 'conner'}
user.writeuser(newdict)
"""class user:


    # Declare any vars needed
    '''userName = None
    userPassword = None
    encName = None
    encPassword = None
    encNameKey = None
    encPasswordKey = None'''
    # Done declaring


    def __init__(self):


    # Loading pickle files into the program. We load them first so we have any data needed.  
        try:

            """with open('userNames.pkl', 'rb') as data:
                self.userName = pickle.load(data)
            with open('userPasswords.pkl', 'rb') as data:
                self.userPassword = pickle.load(data)
            with open('userNamesKey.pkl', 'rb') as data:
                self.encNameKey = pickle.load(data)  
            with open('userPasswordsKey.pkl', 'rb') as data:
                self.encPasswordKey = pickle.load(data)"""
            unneededData = open('info.json', 'r')
            self.userInfo = json.load(unneededData)


            # Declare vars that we add to the dictionary later to add multi-user support
            '''self.ogUserName = self.userName
            self.ogUserPassword = self.userPassword
            self.ogEncNameKey = self.encNameKey
            self.ogEncPasswordKey = self.encPasswordKey'''
            self.ogUserInfo = self.userInfo
            # End declaring


        # If the pickle files don't exist, we make sure the program doesn't crash  
        except FileNotFoundError:
            '''self.userName = {}
            self.userPassword = {}
            self.encNameKey = {}
            self.userPasswordKey = {}
            self.ogUserName = {}
            self.ogUserPassword = {}
            self.ogEncNameKey = {}
            self.ogEncPasswordKey = {}'''
            self.userInfo = {'nothing here': 'nope'}
            self.ogUserInfo = {}
            error = "File not found"
            pass

        except:
            '''self.userName = {}
            self.userPassword = {}
            self.encNameKey = {}
            self.userPasswordKey = {}
            self.ogUserName = {}
            self.ogUserPassword = {}
            self.ogEncNameKey = {}
            self.ogEncPasswordKey = {}'''
            self.userInfo = {'nothing here': 'nope'}
            self.ogUserInfo = {}
            error = "Unknown error"
            pass
        # End crash handling


    # End loading pickle files


    # Check user funtion 1: Checks if a user exists. 2: Loads the user if it does exist. 3: If the user doesn't exist, it calls CreateUser to create a user.
    def CheckUser(self, name, pwd):

        # Decrypting the data in the json files
        try:
            self.userNameCrypt = self.userInfo[name + " username"]
            self.encNameKey = Fernet(bytes(self.userInfo[name + " username key"], 'utf-8'))
            self.userName = self.encNameKey.decrypt(self.userNameCrypt).decode()
            self.userPasswordCrypt = self.userInfo[name + " password"]
            self.encPasswordKey = Fernet(bytes(self.userInfo[name + " password key"], 'utf-8'))
            self.userPassword = self.encPasswordKey.decrypt(self.userPasswordCrypt).decode()
        except:
            # This makes sure that if there isn't any keys, or if the user doesn't exist in the pickle file, the program will continue and not crash
            self.userName = ''
            self.userPassword = ''
            pass
        # End decryption of data in the json files 


        # Check if the username and password match up with the ones in the pickle file  
        for i in range(5):
            if i == 0:
                rightPassword = True
                create = True
            elif i != 0:
                rightPassword = False
                create = False
            if self.userName == name and self.userPassword == pwd:
                # These rightPassword variables enhance the process
                rightPassword = True
                create = False
                print("Correct!")
                break
            elif name not in self.userName and rightPassword and pwd not in self.userPassword and create:
                # Create a user if one doesn't exist. 
                createUser = str.lower(str(input("Sorry! That user doesn't exist! Create a new user?\ny/n --> ")))
                if createUser == 'y':
                    self.CreateUser(name, pwd)
                    rightPassword = True
                    create = False
                    break
                # If the user doesn't want to create an account
                else:
                    rightPassword = False
                    # Not create enhances the process of not making a user
                    create = True
                    print("Okay. We won't save your details.")
                    break
                    # End not wanting an account
                # End creating a new user
            elif self.userName == name and self.userPassword != pwd and i == 0:
                print("Sorry! You typed the wrong password. Try again.")
                rightPassword = False
                create = False
                continue            
            elif rightPassword == False and name in self.userName and create == False and i != 0:
                pwd = str(input("\nPlease reenter your password.\n--> "))
                if self.userPassword == pwd:
                    rightPassword = True
                    break
                else:
                    rightPassword = False
                    continue


        if rightPassword:
            # Return vars needed for the program
            return name, pwd
        elif create == False:
            # Return vars needed for the program
            return name, pwd
        else:
            print("Sorry! Your password didn't match our database, so we'll have to exit.\nTry running the program again.")
            time.sleep(3)
            sys.exit()
        # End checking if the user exists, and if they typed the right password


    # Funtion to encrypt, and store variables to create a user
    def CreateUser(self, name, pwd):

        # Encryption
        self.key = Fernet.generate_key()
        self.key2 = Fernet.generate_key()
        self.keyUser = Fernet(self.key)
        self.keyPwd = Fernet(self.key2)
        self.encName = self.keyUser.encrypt(name.encode())
        self.encPassword = self.keyPwd.encrypt(pwd.encode())
        self.keyUser = bytes(self.keyUser)
        self.keyPwd = bytes(self.keyPwd)
        # End encryption


        # Store in a dictionary
        '''self.userName = {f"{name} username": self.encName}
        self.userPassword = {f'{name} password': self.encPassword}
        self.encNameKey = {f'{name} username key': self.keyUser}
        self.encPasswordKey = {f'{name} password key': self.keyPwd}'''
        self.userInfo = {f'{name} username': str(self.encName, 'utf-8'), f'{name} password': str(self.encPassword, 'utf-8'), f'{name} username key': str(self.keyUser, 'utf-8'), f'{name} password key': str(self.keyPwd, 'utf-8')}
        # End dictionary storage


        # Update the dictionaries for multi-user support
        '''self.userName.update(self.ogUserName)
        self.userPassword.update(self.ogUserPassword)
        self.encNameKey.update(self.ogEncNameKey)
        self.encPasswordKey.update(self.ogEncPasswordKey)'''
        self.userInfo.update(self.ogUserInfo)
        self.userInfo = self.userInfo
        # End updating


        # Save to pickle files
        '''with open('userNames.pkl', 'wb') as data:
            pickle.dump(self.userName, data)
        with open('userPasswords.pkl', 'wb') as data:
            pickle.dump(self.userPassword, data)
        with open('userNamesKey.pkl', 'wb') as data:
            pickle.dump(self.encNameKey, data)
        with open('userPasswordsKey.pkl', 'wb') as data:
            pickle.dump(self.encPasswordKey, data)'''
        '''unneededData = open('userInfo.json', 'w')
        object = json.dump(unneededData)
        self.userInfo()'''
        with open('userInfo.json', 'w') as data:
            json.dumps(data, self.userInfo)
        # End saving to pickle files


        # Return the vars needed for the program
        return name, pwd"""
