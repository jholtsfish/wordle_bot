
from userInfo import user

from programInfo import WordleGet

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

WordleGet = WordleGet()
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
from wordLogic import Login

thing = Login()

with open("valid_words.txt") as file:
    # words = file.readlines()
    # words = [word.strip() for word in words]
    words = [word for word in (word.strip() for word in file.readlines()) if len(word) == 5]

    file.close()

print(words)
print(thing)

WordleGet.EnterWord('crane', driver=driver)