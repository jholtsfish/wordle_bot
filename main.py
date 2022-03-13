<<<<<<< HEAD
from userInfo import user
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

userInfo = user()
userName = input("Please input your login credentials for wordle.\nUser name -->")
userPassword = input("Password -->")
userVar = userInfo.CheckUser(userName, userPassword)
print(userVar)
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
=======
from login import Login

thing = Login()

with open("valid_words.txt") as file:
    # words = file.readlines()
    # words = [word.strip() for word in words]
    words = [word for word in (word.strip() for word in file.readlines()) if len(word) == 5]

    file.close()

print(words)
print(thing)
>>>>>>> cc171c18b70c1f0af11b6c72e8438b4aa1e05093
