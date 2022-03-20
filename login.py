
# Why is this necessary? Wordle doesn't have a login. What is this for????

#lol using this file to test stuff now ~conner

from logic import wordlogic

wordlogic = wordlogic()

wordlogic.sortwords('5words.txt')



'''# Define a function that logs into wordle
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
# End defining
=======
from attr import attr
import selenium as sl

class Login:
    attribute = None'''


