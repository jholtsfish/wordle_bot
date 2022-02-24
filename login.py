from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class Log_in:
    driver = None
    service = None

    def __init__(self):
        self.service = FirefoxService
        self.driver = webdriver.Firefox
    
    def DriverStart(self):
        self.service(executable_path=GeckoDriverManager().install())
        self.driver(service=self.service)
# Old example code
'''    bob = str()

    age = int()


    def __init__(
            self, 
            newBob = "Bob the Builder", 
            newAge = 10000
        ):
        
        self.bob = newBob
        self.age = newAge
    
    def GetAge(self):
        return self.age'''