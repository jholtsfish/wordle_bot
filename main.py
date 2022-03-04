from userInfo import user
from validwords import valid_words
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

userInfo = user()
userName = input("Please input your login credentials for wordle.\nUser name -->")
userPassword = input("Password -->")
userName, userPassword = userInfo.CheckUser(userName, userPassword)
print(userName, userPassword)
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)