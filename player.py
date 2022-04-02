from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Player:
    # install webdriver service manager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    words = []
    keys = {}
    
    def __init__(self):
        # open wordle
        self.driver.get("https://www.wordleunlimited.com/")
        self.driver.implicitly_wait(5)
        # close modal
        try: 
            self.driver.find_element(By.CLASS_NAME, 'btn-close').click()
        except:
            pass
        # access words
        self.words = self.driver.find_elements(By.CLASS_NAME, 'RowL')
        # create dictionary of keys
        for key in self.driver.find_elements(By.CLASS_NAME, 'wp-key'):
            self.keys[
                self.driver.execute_script("return arguments[0].innerHTML", key)
                ] = key
    
    def PressKey(self, key_press):
        self.keys[key_press].click()

    def GetLastWord(self):
        w = self.driver.find_elements(By.CLASS_NAME, "RowL-locked-in")[-1]
        w = w.find_elements(By.CLASS_NAME, 'RowL-letter')
        keys = [self.driver.execute_script('return arguments[0].innerHTML', cell) for cell in w]
        values = [self.driver.execute_script('return arguments[0].classList', cell).pop() for cell in w]
        d = []
        for i in range(len(keys)):
            d.append(
                (keys[i], values[i])
            )
        return d or "NoWordsEntered"

person = Player()
string = 'APPLE'
for letter in string:
    person.PressKey(letter)
person.PressKey('ENTER')
person.GetLastWord()