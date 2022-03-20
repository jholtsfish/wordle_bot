<<<<<<< HEAD
<<<<<<< HEAD
from userInfo import user
=======
from programInfo import WordleGet
>>>>>>> 62cce161fd65a211f066860a1bab7dc1f0b91662
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
<<<<<<< HEAD
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
=======
WordleGet.EnterWord('crane', driver=driver)
>>>>>>> 62cce161fd65a211f066860a1bab7dc1f0b91662
