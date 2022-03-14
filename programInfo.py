from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

class WordleGet:

    def __init__(self):
        self.keyboardPath = {
            'q': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[1]/button[1]'),
            'w': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[1]/button[2]'),
            'e': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[1]/button[3]'),
            'r': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[1]/button[4]'),
            't': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[1]/button[5]'),
            'y': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[1]/button[6]'),
            'u': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[1]/button[7]'),
            'i': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[1]/button[8]'),
            'o': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[1]/button[9]'),
            'p': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[1]/button[10]'),
            'a': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[2]/button[1]'),
            's': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[2]/button[2]'),
            'd': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[2]/button[3]'),
            'f': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[2]/button[4]'),
            'g': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[2]/button[5]'),
            'h': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[2]/button[6]'),
            'j': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[2]/button[7]'),
            'k': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[2]/button[8]'),
            'l': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[2]/button[9]'),
            'enter': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[3]/button[1]'),
            'z': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[3]/button[2]'),
            'x': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[3]/button[3]'),
            'c': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[3]/button[4]'),
            'v': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[3]/button[5]'),
            'b': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[3]/button[6]'),
            'n': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[3]/button[7]'),
            'm': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[3]/button[8]'),
            'del': (By.CLASS_NAME, '/html/body/game-app//game-theme-manager/div/game-keyboard//div/div[3]/button[9]')
        }
        self.xButton = (By.XPATH, '/svg')

    def EnterWord(self, word, driver):
        driver.get('https://www.nytimes.com/games/wordle/index.html')

        for l in word:
            pyautogui.press(l)
        pyautogui.press('enter')