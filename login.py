from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class Log_in:
    EMAILFIELD = None
    # Password web content on the Wordle account page
    PASSWORDFIELD = None
    # Next button content on the Microsoft account page
    NEXTBUTTON = None
    # Sign in button on the bing search page
    SIGNINBUTTON = None

    def __init__(self):
        self.EMAILFIELD = (By.ID, "i0116")
        self.PASSWORDFIELD = (By.ID, "i0118")
        self.NEXTBUTTON = (By.ID, "idSIButton9")
        self.SIGNINBUTTON = (By.ID, "id_a")

    def WordleLogin(self, driver):
        # Login for the first webdriver instance
        driver.get('https://login.live.com')
        # Wait for email field and enter email
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.EMAILFIELD)).send_keys(email)
        # Click Next
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.NEXTBUTTON)).click()
        # Wait for password field and enter password
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.PASSWORDFIELD)).send_keys(pwd)
        # Click Login
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.NEXTBUTTON)).click()
        # Click Yes
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.NEXTBUTTON)).click()
        time.sleep(1)


# def DriverStart():
#     driver(service=service)
# # Old example code
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