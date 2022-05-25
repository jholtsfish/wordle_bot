from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class webinterface:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://wordlegame.org")
        self.youwin = False
        time.sleep(3)

        self.xpathdict = {'a': '//*[@id="game-wrapper"]/div[6]/div[2]/div[1]',
                        'b': '//*[@id="game-wrapper"]/div[6]/div[3]/div[6]',
                        'c': '//*[@id="game-wrapper"]/div[6]/div[3]/div[4]',
                        'd': '//*[@id="game-wrapper"]/div[6]/div[2]/div[3]',
                        'e': '//*[@id="game-wrapper"]/div[6]/div[1]/div[3]',
                        'f': '//*[@id="game-wrapper"]/div[6]/div[2]/div[4]',
                        'g': '//*[@id="game-wrapper"]/div[6]/div[2]/div[5]',
                        'h': '//*[@id="game-wrapper"]/div[6]/div[2]/div[6]',
                        'i': '//*[@id="game-wrapper"]/div[6]/div[1]/div[8]',
                        'j': '//*[@id="game-wrapper"]/div[6]/div[2]/div[8]',
                        'k': '//*[@id="game-wrapper"]/div[6]/div[2]/div[8]',
                        'l': '//*[@id="game-wrapper"]/div[6]/div[2]/div[9]',
                        'm': '//*[@id="game-wrapper"]/div[6]/div[3]/div[8]',
                        'n': '//*[@id="game-wrapper"]/div[6]/div[3]/div[7]',
                        'o': '//*[@id="game-wrapper"]/div[6]/div[1]/div[9]',
                        'p': '//*[@id="game-wrapper"]/div[6]/div[1]/div[10]',
                        'q': '//*[@id="game-wrapper"]/div[6]/div[1]/div[1]',
                        'r': '//*[@id="game-wrapper"]/div[6]/div[1]/div[4]',
                        's': '//*[@id="game-wrapper"]/div[6]/div[2]/div[2]',
                        't': '//*[@id="game-wrapper"]/div[6]/div[1]/div[5]',
                        'u': '//*[@id="game-wrapper"]/div[6]/div[1]/div[7]',
                        'v': '//*[@id="game-wrapper"]/div[6]/div[3]/div[5]',
                        'w': '//*[@id="game-wrapper"]/div[6]/div[1]/div[2]',
                        'x': '//*[@id="game-wrapper"]/div[6]/div[3]/div[3]',
                        'y': '//*[@id="game-wrapper"]/div[6]/div[1]/div[6]',
                        'z': '//*[@id="game-wrapper"]/div[6]/div[3]/div[2]',
                        'enter': '//*[@id="game-wrapper"]/div[6]/div[3]/div[9]'
            }

    def enterword(self, word):

        for letter in word:
            self.driver.find_element(by=By.XPATH, value=self.xpathdict[str(letter)]).click()

        self.driver.find_element(by=By.XPATH, value=self.xpathdict['enter']).click()

    def reapdata(self, roundnumber):

        self.l1c = ''
        self.l2c = ''
        self.l3c = ''
        self.l4c = ''
        self.l5c = ''

        self.lettercolors = [self.l1c, self.l2c, self.l3c, self.l4c, self.l5c]

        isright = 0
        time.sleep(4)

        for letter in range(5):
            element = self.driver.find_element(by=By.XPATH, value=f'//*[@id="game-wrapper"]/div[1]/div[{str(roundnumber)}]/div[{str(letter + 1)}]')
            html = element.get_attribute("class")
            #print(html)

            if 'letter-absent' in html:
                self.lettercolors[letter] = 'n'
            elif 'letter-present' in html:
                self.lettercolors[letter] = 'g'
            elif 'letter-elsewhere' in html:
                self.lettercolors[letter] = 'y'
            else:
                isright += 1
        if isright >= 5:
            print('YOU WON!')
            self.youwin = True