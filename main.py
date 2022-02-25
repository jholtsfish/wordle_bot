from login import Log_in
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