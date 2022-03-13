<<<<<<< HEAD
# Why is this necessary? Wordle doesn't have a login. What is this for????

'''from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class Log_in:

# No vars needed for this one

# Init vars
    def __init__(self):
        self.EMAILFIELD = (By.ID, "i0116")
        self.PASSWORDFIELD = (By.ID, "i0118")
        self.NEXTBUTTON = (By.ID, "idSIButton9")
        self.SIGNINBUTTON = (By.ID, "id_a")
# End init vars


# Define a function that logs into wordle
    def WordleLogin(self, driver, name, pwd):
        # Go to wordle website
        driver.get('https://login.live.com')


        # Wait for email field and enter email
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.EMAILFIELD)).send_keys(name)


        # Click Next
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.NEXTBUTTON)).click()


        # Wait for password field and enter password
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.PASSWORDFIELD)).send_keys(pwd)


        # Click Login
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.NEXTBUTTON)).click()


        # Click Yes
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.NEXTBUTTON)).click()


        # Wait a bit
        time.sleep(1)
# End defining'''
=======
from attr import attr
import selenium as sl

class Login:
    attribute = None

>>>>>>> cc171c18b70c1f0af11b6c72e8438b4aa1e05093
