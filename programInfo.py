from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui, time

class WordleGet:

    def __init__(self):
        None

    def EnterWord(self, word, driver):
        driver.get('https://www.nytimes.com/games/wordle/index.html')
        time.sleep(2)
        for l in word:
            pyautogui.press(l)
        pyautogui.press('enter')