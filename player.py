from logic import WORDS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# install webdriver service manager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.wordleunlimited.com/")

game = driver.find_element(By.CLASS_NAME, 'Game')


# javascript for nytimes wordle
'''# get root element
game_root = driver.find_element(By.TAG_NAME, "game-app")
# use js script to access shadow elements
game_shadow = driver.execute_script(
    """
    return arguments[0]
    .shadowRoot
    .elementsFromPoint(0,0)
    ?.innerHTML
    """,
     game_root)'''

input(game)